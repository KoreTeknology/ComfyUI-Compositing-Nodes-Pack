import numpy as np
import torch
from torch import Tensor
from PIL import Image, ImageEnhance, ImageChops

def tensor2pil(image: Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pil2tensor(image: Image.Image) -> Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class ImageDifference:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "image2": ("IMAGE",),
                #"factor": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0, "step":0.1})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_difference"
    OUTPUT_NODE = True

    CATEGORY = "image/postprocessing"

    def apply_difference(self, image, image2):
        pil_image1 = tensor2pil(image)
        pil_image2 = tensor2pil(image2)

        diff = ImageChops.difference(pil_image1, pil_image2)


        #pil_image = pil_image.convert("RGB")
        # pil_image = ImageEnhance.Contrast(pil_image).enhance(factor)
        # pil_image = pil_image.convert("RGB")

        return (pil2tensor(diff),)

NODE_CLASS_MAPPINGS = {
    "Image Difference": ImageDifference,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Image Difference": "🌅Image Difference",
}