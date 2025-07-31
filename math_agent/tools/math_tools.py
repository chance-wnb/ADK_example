# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Mathematical tools for the math agent."""

def add_numbers(a: float, b: float) -> dict:
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

def subtract_numbers(a: float, b: float) -> dict:
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

def multiply_numbers(a: float, b: float) -> dict:
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

def divide_numbers(a: float, b: float) -> dict:
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