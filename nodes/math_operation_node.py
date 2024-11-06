class mathOperationNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 0.0}),
                "operation": (["add", "subtract", "multiply", "divide", "modulo", "power"],),
                "use_float": ("BOOLEAN", {"default": False, "label_on": "Float", "label_off": "Integer"}),
            },
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING")
    RETURN_NAMES = ("Integer", "Float", "Text")
    FUNCTION = "perform_operation"
    CATEGORY = "utils"

    def perform_operation(self, a, b, operation, use_float):
        if not use_float:
            a = int(a)
            b = int(b)

        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ValueError("Cannot divide by zero")
            result = a / b if use_float else a // b
        elif operation == "modulo":
            if b == 0:
                raise ValueError("Cannot perform modulo by zero")
            result = a % b
        elif operation == "power":
            result = a ** b

        # Return the result based on the use_float boolean
        if use_float:
            return (None, result, str(result))
        else:
            return (result, None, str(result))

NODE_CLASS_MAPPINGS = {"Math Operation": mathOperationNode,}
NODE_DISPLAY_NAME_MAPPINGS = {"Math Operation": "🛡️Math Operation",}


""" class mathFloatOperation:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "a": ("FLOAT", {"default": 0, "min": -999999999999.0, "max": 999999999999.0, "step": 0.01}),
                "b": ("FLOAT", {"default": 0, "min": -999999999999.0, "max": 999999999999.0, "step": 0.01}),
                "operation": (["add", "subtract", "multiply", "divide", "modulo", "power"],),
            },
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "float_math_operation"

    CATEGORY = "EasyUse/Logic/Math"

    def float_math_operation(self, a, b, operation):
        if operation == "add":
            return (a + b,)
        elif operation == "subtract":
            return (a - b,)
        elif operation == "multiply":
            return (a * b,)
        elif operation == "divide":
            return (a // b,)
        elif operation == "modulo":
            return (a % b,)
        elif operation == "power":
            return (a ** b,) """