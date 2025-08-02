"""Mathematical tools for the math agent."""

from google.adk.tools import FunctionTool


def add_numbers_impl(a: float, b: float) -> dict:
    """Adds two numbers together."""
    try:
        result = a + b
        return {
            "status": "success",
            "result": result,
            "message": f"{a} + {b} = {result}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error adding numbers: {str(e)}"
        }

def subtract_numbers_impl(a: float, b: float) -> dict:
    """Subtracts the second number from the first number."""
    try:
        result = a - b
        return {
            "status": "success",
            "result": result,
            "message": f"{a} - {b} = {result}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error subtracting numbers: {str(e)}"
        }

def multiply_numbers_impl(a: float, b: float) -> dict:
    """Multiplies two numbers together."""
    try:
        result = a * b
        return {
            "status": "success",
            "result": result,
            "message": f"{a} × {b} = {result}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error multiplying numbers: {str(e)}"
        }

def divide_numbers_impl(a: float, b: float) -> dict:
    """Divides the first number by the second number."""
    try:
        if b == 0:
            return {
                "status": "error",
                "error_message": "Cannot divide by zero"
            }
        result = a / b
        return {
            "status": "success",
            "result": result,
            "message": f"{a} ÷ {b} = {result}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error dividing numbers: {str(e)}"
        }


# Create FunctionTool instances for ADK
add_numbers = FunctionTool(add_numbers_impl)
subtract_numbers = FunctionTool(subtract_numbers_impl)
multiply_numbers = FunctionTool(multiply_numbers_impl)
divide_numbers = FunctionTool(divide_numbers_impl)