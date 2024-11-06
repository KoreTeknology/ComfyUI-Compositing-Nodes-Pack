class SetText:
    @classmethod
    def INPUT_TYPES(cls):
        # Define the input types for your node. In this case, we need a string input.
        return {
            "required": {
                "user_input": ("STRING", {"default": "My Text", "multiline":True})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Output String",)
    FUNCTION = "process_string"
    CATEGORY = "utils"

    def process_string(self, user_input):
        # This function will be called to process the user input string.
        return (user_input,)

NODE_CLASS_MAPPINGS = {
    "Set Text": SetText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Set Text": "🛡️Set Text",
}