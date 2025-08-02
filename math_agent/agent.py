from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from opentelemetry import trace

# Import the math tools
from .tools import add_numbers, subtract_numbers, multiply_numbers, divide_numbers


def after_model_callback(callback_context, llm_response):
    """
    Adds Wandb-specific attributes to the call_llm OpenTelemetry span.
    
    We use after_model_callback (not before_model_callback) because:
    - before_model_callback runs before the call_llm span is created, so attributes 
      would be added to the parent agent_run span instead
    - after_model_callback runs after the LLM response is received but while the 
      call_llm span is still active, allowing us to inject attributes into the 
      correct span that represents the actual LLM interaction
    """
    current_span = trace.get_current_span()
    current_span.set_attribute('wandb.thread_id', callback_context._invocation_context.session.id)
    current_span.set_attribute('wandb.is_turn', True)
    return None


# The main math agent using LlmAgent for InMemoryRunner compatibility
math_agent = LlmAgent(
    name="MathAgent",
    model="gemini-2.0-flash",
    instruction=(
        "You are a friendly math assistant. Help users with basic arithmetic operations "
        "like addition, subtraction, multiplication, and division. Always be encouraging "
        "and explain your calculations clearly. When a user asks for a math operation, "
        "use the appropriate tool to perform the calculation and provide a clear, "
        "friendly response with the result."
    ),
    tools=[add_numbers, subtract_numbers, multiply_numbers, divide_numbers],
    after_model_callback=after_model_callback,
)

# This is the required root_agent that ADK looks for
root_agent = math_agent