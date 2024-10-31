class NoteAdvanced:
    @classmethod
    def INPUT_TYPES(cls):
        # Define the input types for your node. In this case, we need a string input.
        return {
            "required": {
                "user_note": ("STRING", {"default": "Note", "multiline":True}),
                "user_comment": ("STRING", {"default": "Comment", "multiline":True}),
            }
        }

    RETURN_TYPES = ()
    OUTPUT_NODE = False
    FUNCTION = "note_advanced"
    CATEGORY = "utils"

    def note_advanced(self, user_note,user_comment):
        # This function will be called to process the user input string.
        return (user_note,user_comment,)

NODE_CLASS_MAPPINGS = {
    "NoteAdvanced": NoteAdvanced,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NoteAdvanced": "🛡️Note Advanced",
}