import asyncio
import os
import sys
import warnings

from google.adk.runners import InMemoryRunner
from google.genai import types
from dotenv import load_dotenv

from math_agent.agent import math_agent
from math_agent.otel_config import setup_otel_tracing


# load api key from .env
load_dotenv()

# Filter out the non-text parts warning since we handle function calls properly
warnings.filterwarnings("ignore", message=".*non-text parts in the response.*")

async def run_math_agent_interactive():
    """Run the math agent in interactive mode with OTEL tracing."""
    # Setup OpenTelemetry tracing before creating the runner
    setup_otel_tracing(wandb_base_url=os.getenv("WANDB_BASE_URL"))
    
    print("🧮 Math Agent with OpenTelemetry Integration")
    print("=" * 50)
    print("Ask me to perform math operations like:")
    print("- Add 5 and 3")
    print("- What is 10 minus 4?")
    print("- Multiply 6 by 7")
    print("- Divide 20 by 4")
    print("\nType 'quit' or 'exit' to stop.")
    print("=" * 50)
    
    # Create InMemoryRunner with the math agent
    runner = InMemoryRunner(agent=math_agent, app_name="math_assistant")
    session_service = runner.session_service
    
    user_id = "chance"
    session_id = "math_agent_session"
    await session_service.create_session(
        app_name="math_assistant",
        user_id=user_id,
        session_id=session_id
    )
    
    while True:
        try:
            # Get user input
            user_input = input("\n🤔 You: ").strip()
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print("👋 Goodbye!")
                break
                
            if not user_input:
                continue
                
            print("🤖 Math Agent: ", end="", flush=True)
            
            # Run the agent with tracing
            response_parts = []
            async for event in runner.run_async(
                user_id=user_id,
                session_id=session_id,
                new_message=types.Content(
                    role="user", 
                    parts=[types.Part(text=user_input)]
                )
            ):
                if event.is_final_response() and event.content:
                    # Handle all parts in the response (text and function calls)
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            print(part.text.strip(), end="", flush=True)
                            response_parts.append(part.text.strip())
                        elif hasattr(part, 'function_response'):
                            # Handle function call results
                            result = part.function_response.response
                            if isinstance(result, dict) and 'message' in result:
                                print(result['message'], end="", flush=True)
                                response_parts.append(result['message'])
            
            print()  # New line after response
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")


async def run_math_agent_single(query: str):
    """Run the math agent for a single query with OTEL tracing."""
    # Setup OpenTelemetry tracing before creating the runner
    setup_otel_tracing(wandb_base_url=os.getenv("WANDB_BASE_URL"))
    
    print(f"🧮 Math Agent Query: {query}")
    print("=" * 50)
    
    # Create InMemoryRunner with the math agent
    runner = InMemoryRunner(agent=math_agent, app_name="math_assistant")
    session_service = runner.session_service
    
    user_id = "example_user"
    session_id = "example_session"
    await session_service.create_session(
        app_name="math_assistant",
        user_id=user_id,
        session_id=session_id
    )
    
    try:
        print("🤖 Math Agent: ", end="", flush=True)
        
        # Run the agent with tracing
        response_parts = []
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=types.Content(
                role="user", 
                parts=[types.Part(text=query)]
            )
        ):
            if event.is_final_response() and event.content:
                # Handle all parts in the response (text and function calls)
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        print(part.text.strip(), end="", flush=True)
                        response_parts.append(part.text.strip())
                    elif hasattr(part, 'function_response'):
                        # Handle function call results
                        result = part.function_response.response
                        if isinstance(result, dict) and 'message' in result:
                            print(result['message'], end="", flush=True)
                            response_parts.append(result['message'])
        
        print()  # New line after response
        return "".join(response_parts)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return None


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        # Single query mode
        query = " ".join(sys.argv[1:])
        asyncio.run(run_math_agent_single(query))
    else:
        # Interactive mode
        asyncio.run(run_math_agent_interactive())


if __name__ == "__main__":
    main()