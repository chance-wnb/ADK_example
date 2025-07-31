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

"""Simple math agent that can perform basic arithmetic operations."""

from google.adk.agents import Agent

# Import the math tools
from .tools import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

# The main math agent
math_agent = Agent(
    name="simple_math_agent",
    model="gemini-2.0-flash",
    description="A helpful agent that can perform basic arithmetic operations",
    instruction=(
        "You are a friendly math assistant. Help users with basic arithmetic operations "
        "like addition, subtraction, multiplication, and division. Always be encouraging "
        "and explain your calculations clearly. When a user asks for a math operation, "
        "use the appropriate tool to perform the calculation and provide a clear, "
        "friendly response with the result."
    ),
    tools=[add_numbers, subtract_numbers, multiply_numbers, divide_numbers],
)

# This is the required root_agent that ADK looks for
root_agent = math_agent