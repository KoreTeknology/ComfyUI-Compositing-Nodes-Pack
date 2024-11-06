import numpy as np
import torch
from torch import Tensor
from PIL import Image, ImageEnhance, ImageFilter

def tensor2pil(image: Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image: Image.Image) -> Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
 
class ImageDesaturate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "brightness": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step":0.1}),
                "contrast": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step":0.1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "image_greyscale"

    CATEGORY = "image/postprocessing"

    def image_greyscale(self, image, brightness, contrast):
        pil_image = tensor2pil(image)
        greyscaled_image = pil_image.convert("L")
        greyscaled_image = ImageEnhance.Brightness(greyscaled_image).enhance(brightness)
        greyscaled_image = ImageEnhance.Contrast(greyscaled_image).enhance(contrast)
        greyscaled_image = greyscaled_image.convert("RGB")
        return (pil2tensor(greyscaled_image),)

# REG
NODE_CLASS_MAPPINGS = {
    "ImageDesaturate": ImageDesaturate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageDesaturate": "➡️ Image Desaturate",
}