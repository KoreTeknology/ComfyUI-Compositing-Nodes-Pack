import numpy as np
import time
import torch
import torch.nn.functional as F
import torchvision.transforms as T
import io
import base64
import random
import math
import os
import re
import json
from PIL.PngImagePlugin import PngInfo
from PIL import ImageColor,ImageGrab, ImageDraw, ImageFont, Image, ImageSequence, ImageOps
from nodes import MAX_RESOLUTION

class ImageExtend:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "left_px": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "top_px": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "right_px": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "bottom_px": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "background_white": ("FLOAT", {"default": 0.00, "min": 0.00, "max": 1.00, "step": 0.00}),
            },
            "optional": {
                "mask": ("MASK",),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "expand_image"

    CATEGORY = "image/transform"

    def expand_image(self, image, left_px, top_px, right_px, bottom_px, background_white, mask=None):
        if mask is not None:
            if torch.allclose(mask, torch.zeros_like(mask)):
                    print("Warning: The incoming mask is fully black. Handling it as None.")
                    mask = None
        B, H, W, C = image.size()

        new_image = torch.ones(
            (B, H + top_px + bottom_px, W + left_px + right_px, C),
            dtype=torch.float32,
        ) * background_white

        new_image[:, top_px:top_px + H, left_px:left_px + W, :] = image

        if mask is None:
            new_mask = torch.ones(
                (B, H + top_px + bottom_px, W + left_px + right_px),
                dtype=torch.float32,
            )

            t = torch.zeros(
            (B, H, W),
            dtype=torch.float32
            )
        else:
            # If a mask is provided, pad it to fit the new image size
            mask = F.pad(mask, (left_px, right_px, top_px, bottom_px), mode='constant', value=0)
            mask = 1 - mask
            t = torch.zeros_like(mask)
        
        if mask is None:
            new_mask[:, top_px:top_px + H, left_px:left_px + W] = t
            return (new_image, new_mask,)
        else:
            return (new_image, mask,)

NODE_CLASS_MAPPINGS = {
    "ImageExtend": ImageExtend,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageExtend": "🌅Image Extend",
}