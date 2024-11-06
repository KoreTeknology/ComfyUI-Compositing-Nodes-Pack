import torch

import os
import sys
import json
import hashlib
import traceback
import math
import time
import random
import logging

from PIL import Image, ImageOps, ImageSequence, ImageFile
from PIL.PngImagePlugin import PngInfo

import numpy as np
import importlib
import folder_paths
import node_helpers

class LoadImageNai:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":{
                    "image_target": ("IMAGE",),
                    "method": (
                        [   
                            'mkl',
                            'hm', 
                            'reinhard', 
                            'mvgd', 
                            'hm-mvgd-hm', 
                            'hm-mkl-hm',
                        ], {
                        "default": 'mkl'
                        }),
                    "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                    "image": (sorted(files), {"image_upload": True}),
                    },
                    "optional": {
                    "strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                    }
                }

    CATEGORY = "experimental/image"

    RETURN_TYPES = ("IMAGE", "MASK", "IMAGE", "STRING", "STRING")
    RETURN_NAMES = ("IMAGE", "MASK", "LAYER", "Image Path", "Image Size")
    FUNCTION = "load_image"

    def colormatch(self, image, image_target, method, strength=1.0):
        try:
            from color_matcher import ColorMatcher
        except:
            raise Exception("Can't import color-matcher, did you install requirements.txt? Manual install: pip install color-matcher")
        cm = ColorMatcher()
        image = image.cpu()
        image_target = image_target.cpu()
        batch_size = image_target.size(0)
        out = []
        images_target = image_target.squeeze()
        images_ref = image.squeeze()

        image_np = images_ref.numpy()
        images_target_np = images_target.numpy()

        if image.size(0) > 1 and image.size(0) != batch_size:
            raise ValueError("ColorMatch: Use either single reference image or a matching batch of reference images.")

        for i in range(batch_size):
            image_target_np = images_target_np if batch_size == 1 else images_target[i].numpy()
            image_np_i = image_np if image.size(0) == 1 else images_ref[i].numpy()
            try:
                image_result = cm.transfer(src=image_target_np, ref=image_np_i, method=method)
            except BaseException as e:
                print(f"Error occurred during transfer: {e}")
                break
            # Apply the strength multiplier
            image_result = image_target_np + strength * (image_result - image_target_np)
            out.append(torch.from_numpy(image_result))
            
        out = torch.stack(out, dim=0).to(torch.float32)
        out.clamp_(0, 1)
        return (out,)
    
    
    def load_image(self, image, image_target, method, strength=1.0):
        image_path = folder_paths.get_annotated_filepath(image)
        
        img = node_helpers.pillow(Image.open, image_path)
        
        output_images = []
        output_masks = []
        w, h = None, None

        excluded_formats = ['MPO']
        
        for i in ImageSequence.Iterator(img):
            i = node_helpers.pillow(ImageOps.exif_transpose, i)

            if i.mode == 'I':
                i = i.point(lambda i: i * (1 / 255))
            image = i.convert("RGB")

            if len(output_images) == 0:
                w = image.size[0]
                h = image.size[1]
            
            if image.size[0] != w or image.size[1] != h:
                continue
            
            image = np.array(image).astype(np.float32) / 255.0
            image = torch.from_numpy(image)[None,]
            if 'A' in i.getbands():
                mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
                mask = 1. - torch.from_numpy(mask)
            else:
                mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
            output_images.append(image)
            output_masks.append(mask.unsqueeze(0))

        if len(output_images) > 1 and img.format not in excluded_formats:
            output_image = torch.cat(output_images, dim=0)
            output_mask = torch.cat(output_masks, dim=0)
        else:
            output_image = output_images[0]
            output_mask = output_masks[0]

        print(str(image_path))
        string_size = str(w) + " x " + str(h)
        #output_matched = output_image.colormatch(image_target, output_image, method, strength)

        return (output_image, output_mask, image_target, str(image_path), string_size)

    @classmethod
    def IS_CHANGED(s, image):
        image_path = folder_paths.get_annotated_filepath(image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, image):
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)

        return True

NODE_CLASS_MAPPINGS = {
    "LoadImageNai": LoadImageNai
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageNai": "Load Image Node"
}
