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
from PIL import ImageGrab, ImageDraw, ImageFont, Image, ImageSequence, ImageOps
# from nodes import MAX_RESOLUTION

from nodes import MAX_RESOLUTION, SaveImage
from comfy_extras.nodes_mask import ImageCompositeMasked
from comfy.cli_args import args
from comfy.utils import ProgressBar, common_upscale
import folder_paths
import model_management

class ImageConcanate:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "image1": ("IMAGE",),
            "image2": ("IMAGE",),
            "direction": (
            [   'right',
                'down',
                'left',
                'up',
            ],
            {
            "default": 'right'
             }),
            "match_image_size": ("BOOLEAN", {"default": True}),
        }}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "concanate"
    CATEGORY = "KJNodes/image"
    DESCRIPTION = """
Concatenates the image2 to image1 in the specified direction.
"""

    def concanate(self, image1, image2, direction, match_image_size, first_image_shape=None):
        # Check if the batch sizes are different
        batch_size1 = image1.shape[0]
        batch_size2 = image2.shape[0]

        if batch_size1 != batch_size2:
            # Calculate the number of repetitions needed
            max_batch_size = max(batch_size1, batch_size2)
            repeats1 = max_batch_size // batch_size1
            repeats2 = max_batch_size // batch_size2
            
            # Repeat the images to match the largest batch size
            image1 = image1.repeat(repeats1, 1, 1, 1)
            image2 = image2.repeat(repeats2, 1, 1, 1)

        if match_image_size:
            # Use first_image_shape if provided; otherwise, default to image1's shape
            target_shape = first_image_shape if first_image_shape is not None else image1.shape

            original_height = image2.shape[1]
            original_width = image2.shape[2]
            original_aspect_ratio = original_width / original_height

            if direction in ['left', 'right']:
                # Match the height and adjust the width to preserve aspect ratio
                target_height = target_shape[1]  # B, H, W, C format
                target_width = int(target_height * original_aspect_ratio)
            elif direction in ['up', 'down']:
                # Match the width and adjust the height to preserve aspect ratio
                target_width = target_shape[2]  # B, H, W, C format
                target_height = int(target_width / original_aspect_ratio)
            
            # Adjust image2 to the expected format for common_upscale
            image2_for_upscale = image2.movedim(-1, 1)  # Move C to the second position (B, C, H, W)
            
            # Resize image2 to match the target size while preserving aspect ratio
            image2_resized = common_upscale(image2_for_upscale, target_width, target_height, "lanczos", "disabled")
            
            # Adjust image2 back to the original format (B, H, W, C) after resizing
            image2_resized = image2_resized.movedim(1, -1)
        else:
            image2_resized = image2

        # Ensure both images have the same number of channels
        channels_image1 = image1.shape[-1]
        channels_image2 = image2_resized.shape[-1]

        if channels_image1 != channels_image2:
            if channels_image1 < channels_image2:
                # Add alpha channel to image1 if image2 has it
                alpha_channel = torch.ones((*image1.shape[:-1], channels_image2 - channels_image1), device=image1.device)
                image1 = torch.cat((image1, alpha_channel), dim=-1)
            else:
                # Add alpha channel to image2 if image1 has it
                alpha_channel = torch.ones((*image2_resized.shape[:-1], channels_image1 - channels_image2), device=image2_resized.device)
                image2_resized = torch.cat((image2_resized, alpha_channel), dim=-1)


        # Concatenate based on the specified direction
        if direction == 'right':
            concatenated_image = torch.cat((image1, image2_resized), dim=2)  # Concatenate along width
        elif direction == 'down':
            concatenated_image = torch.cat((image1, image2_resized), dim=1)  # Concatenate along height
        elif direction == 'left':
            concatenated_image = torch.cat((image2_resized, image1), dim=2)  # Concatenate along width
        elif direction == 'up':
            concatenated_image = torch.cat((image2_resized, image1), dim=1)  # Concatenate along height
        return concatenated_image,

import torch  # Make sure you have PyTorch installed

class ImageConcatenate:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "inputcount": ("INT", {"default": 2, "min": 2, "max": 1000, "step": 1}),
                "image_1": ("IMAGE", ),
                "image_2": ("IMAGE", ),
                "direction": (
                [   'right',
                    'down',
                    'left',
                    'up',
                ],
            {
            "default": 'right'
             }),
            "match_image_size": ("BOOLEAN", {"default": False}),
            },
    }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    FUNCTION = "combine"
    CATEGORY = "image/transform"
    DESCRIPTION = """
Creates an image from multiple images.  
You can set how many inputs the node has,  
with the **inputcount** and clicking update.
"""

    def combine(self, inputcount, direction, match_image_size, **kwargs):
        image = kwargs["image_1"]
        first_image_shape = None
        if first_image_shape is None:
            first_image_shape = image.shape
        for c in range(1, inputcount):
            new_image = kwargs[f"image_{c + 1}"]
            image, = ImageConcanate.concanate(self, image, new_image, direction, match_image_size, first_image_shape=first_image_shape)
        first_image_shape = None
        return (image,)

NODE_CLASS_MAPPINGS = {
    "ImageConcatenate": ImageConcatenate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageConcatenate": "🌅Image Concatenate",
}