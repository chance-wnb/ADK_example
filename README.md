# Simple Math Agent

A basic arithmetic agent built with Google Agent Development Kit (ADK) that can perform addition, subtraction, multiplication, and division operations.

## Features

- Addition of two numbers
- Subtraction of two numbers  
- Multiplication of two numbers
- Division of two numbers (with zero division protection)
- Friendly, encouraging responses
- Clear explanations of calculations

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
   # Edit .env with your credentials
   ```

5. **Authenticate with Google Cloud (if using Vertex AI):**
   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```

## Running the Agent

### CLI Mode
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
cd math_agent
adk run .
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
- **Main Agent**: `math_agent` - coordinates user requests and delegates to appropriate tools
- **Tools**: Four mathematical operation functions that return structured results
- **Model**: Uses Gemini 2.0 Flash for natural language understanding and response generation