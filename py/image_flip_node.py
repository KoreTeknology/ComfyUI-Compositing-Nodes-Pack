import torch

class ImageFlip:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "axis": (["x", "y", "xy"],),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "flip"

    CATEGORY = "image/transform"

    def flip(self, image, axis):
        dim = ()
        if "y" in axis:
            dim += (1,)
        if "x" in axis:
            dim += (2,)
        image = torch.flip(image, dim)

        return(image,)

NODE_CLASS_MAPPINGS = {
    "ImageFlip": ImageFlip,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageFlip": "🌅Image Flip",
}