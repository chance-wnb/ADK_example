# Simple Math Agent with OpenTelemetry Integration

A basic arithmetic agent built with Google Agent Development Kit (ADK) that can perform addition, subtraction, multiplication, and division operations. Now integrated with OpenTelemetry and Weave for comprehensive tracing and observability.

## Features

- Addition of two numbers
- Subtraction of two numbers  
- Multiplication of two numbers
- Division of two numbers (with zero division protection)
- Friendly, encouraging responses
- Clear explanations of calculations
- **OpenTelemetry integration with Weave for tracing and observability**
- **InMemoryRunner execution pattern for better performance**

## Setup

1. **Prerequisites:**
   - Python 3.9+ 
   - [uv](https://docs.astral.sh/uv/) (fast Python package manager)
   - Google Cloud Project with Vertex AI enabled OR Google AI Studio API key

2. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd math_agent
   ```

3. **Install dependencies:**
   ```bash
   # Install production dependencies
   uv sync
   
   # Or install with development dependencies
   uv sync --extra dev
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your credentials including:
   # - WANDB_API_KEY: Your W&B API key for OpenTelemetry tracing
   # - WANDB_PROJECT: Your W&B project ID (e.g., "username/project-name")
   # - Google Cloud or AI Studio credentials
   ```

5. **Authenticate with Google Cloud (if using Vertex AI):**
   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```

## Running the Agent

### New: Direct Python Execution with OTEL Integration
```bash
# Interactive mode
python main.py

# Single query mode
python main.py "What is 5 plus 3?"
```

### Traditional ADK CLI Mode
```bash
cd math_agent
uv run adk run .
```

### Web UI Mode
```bash
uv run adk web
```

### Alternative: Using uv shell
```bash
# Activate the uv environment
uv shell
# Then run normally
python main.py
```

## Development

### Code Quality
```bash
# Format code
uv run black .
uv run isort .

# Type checking
uv run mypy math_agent/

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=math_agent --cov-report=html
```

### Installing Development Dependencies
```bash
# Install all development tools
uv sync --extra dev

# Or install specific groups
uv sync --extra test
```

### Pre-commit Hooks (Optional)
```bash
# Install pre-commit hooks
uv run pre-commit install

# Run hooks manually
uv run pre-commit run --all-files
```

## Example Interactions

- "Add 5 and 3"
- "What is 10 minus 4?"
- "Multiply 6 by 7"
- "Divide 20 by 4"
- "What's 15 divided by 0?" (handles division by zero gracefully)

## Architecture

The agent consists of:
- **Main Agent**: `LlmAgent` (math_agent) - coordinates user requests and delegates to appropriate tools
- **Tools**: Four mathematical operation functions wrapped as `FunctionTool` instances
- **Runner**: `InMemoryRunner` for efficient execution
- **Model**: Uses Gemini 2.0 Flash for natural language understanding and response generation
- **Observability**: OpenTelemetry integration with Weave for comprehensive tracing
- **Configuration**: Environment-based configuration for W&B and Google Cloud credentials

## OpenTelemetry Integration

This implementation uses OpenTelemetry to trace agent interactions and send them to Weave for analysis:

- **Automatic Tracing**: All agent reasoning and tool calls are automatically traced
- **Weave Integration**: Traces are sent to W&B's Weave platform for visualization
- **Environment Configuration**: Uses `.env` file for W&B API key and project configuration
- **Batch Processing**: Uses `BatchSpanProcessor` for efficient trace export