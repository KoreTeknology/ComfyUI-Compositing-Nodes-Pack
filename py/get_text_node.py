class GetText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True,"name":"DD"}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    # INPUT_NAMES = ("Input String",)

    RETURN_TYPES = ()
    FUNCTION = "get_text"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    # RESPECT THE MAIN CATEGORIES!!!
    CATEGORY = "utils"

    def get_text(self, text, unique_id=None, extra_pnginfo=None):
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "Get Text": GetText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Get Text": "🛡️Get Text",
}
