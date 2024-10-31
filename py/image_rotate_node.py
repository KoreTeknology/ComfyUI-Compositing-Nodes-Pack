import numpy as np
import torch
from PIL import Image
from torch import Tensor
from math import sin, cos, radians

def tensor2pil(image: Tensor) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))


def pil2tensor(image: Image.Image) -> Tensor:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class ImageRotate:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "rotation": ("INT", {"default": 0, "min": 0, "max": 360, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "rotate"

    CATEGORY = "image/transform"

    def rotate(self, image, rotation):
        pil_image = tensor2pil(image)
        
        # Calculate new dimensions
        angle_rad = radians(rotation)
        #new_width = abs(pil_image.width * cos(angle_rad)) + abs(pil_image.height * sin(angle_rad))
        #new_height = abs(pil_image.height * cos(angle_rad)) + abs(pil_image.width * sin(angle_rad))

        # Rotate the image using PIL's rotate function
        angle = rotation  # Change this to the desired angle
        center_x = pil_image.width / 2
        center_y = pil_image.height / 2

        #converted_image = pil_image.convert("RGBA")
        rotated_image = pil_image.rotate(
            angle, resample=Image.NEAREST, center=(center_x, center_y), expand=False
        )
        
        # Crop the image to the new dimensions
        """ left = (rotated_image.width - new_width) / 2
        top = (rotated_image.height - new_height) / 2
        right = (rotated_image.width + new_width) / 2
        bottom = (rotated_image.height + new_height) / 2
        cropped_image = rotated_image.crop((left, top, right, bottom)) """
            
        # Convert the rotated image back to a tensor
        return (pil2tensor(rotated_image),)
    


NODE_CLASS_MAPPINGS = {
    "ImageRotate": ImageRotate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageRotate": "🌅Image Rotate",
}