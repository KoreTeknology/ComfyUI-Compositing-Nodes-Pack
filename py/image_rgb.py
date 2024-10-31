import numpy as np
import torch
from torch import Tensor
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

def tensor2pil(image: Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image: Image.Image) -> Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
 
class ImageRgb:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "r_value": ("INT", {"default": 255, "min": 1, "max": 255, "step":1}),
                "g_value": ("INT", {"default": 255, "min": 1, "max": 255, "step":1}),
                "b_value": ("INT", {"default": 255, "min": 1, "max": 255, "step":1}),
            },
        }

    RETURN_TYPES = ("IMAGE","IMAGE","IMAGE",)
    RETURN_NAMES = ("R","G","B")
    FUNCTION = "image_rgb"

    CATEGORY = "image/postprocessing"

    def image_rgb(self, image, ImageOps=ImageOps , ImageEnhance=ImageEnhance, ImageFilter=ImageFilter, r_value=255, g_value=255, b_value=255):
        pil_image = tensor2pil(image)
        greyscaled_image = pil_image.convert("L")
        red_img = ImageOps.colorize(greyscaled_image,(0, 0, 0), (r_value, 0, 0))
        green_img = ImageOps.colorize(greyscaled_image,(0, 0, 0), (0, g_value, 0))
        blue_img = ImageOps.colorize(greyscaled_image,(0, 0, 0), (0, 0, b_value))

        # blended_img = Image.blend(red_img, green_img, 0.5)
        # blended_img = Image.blend(blended_img, blue_img, 0.5)

        return (pil2tensor(red_img), pil2tensor(green_img), pil2tensor(blue_img))
    

# REG
NODE_CLASS_MAPPINGS = {
    "Image Rgb": ImageRgb,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Image Rgb": "🌅Image Rgb",
}