import numpy as np
import torch
from torch import Tensor
from PIL import Image, ImageEnhance, ImageFilter

def tensor2pil(image: Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image: Image.Image) -> Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
 
class ImageGreyscale:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "image_greyscale"

    CATEGORY = "image/postprocessing"

    def image_greyscale(self, image):
        pil_image = tensor2pil(image)
        greyscaled_image = pil_image.convert("L")
        return (pil2tensor(greyscaled_image),)

# REG
NODE_CLASS_MAPPINGS = {
    "Image Greyscale": ImageGreyscale,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Image Greyscale": "🌅Image Greyscale",
}