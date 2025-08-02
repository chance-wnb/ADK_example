import base64
import os
from typing import Optional

from dotenv import load_dotenv
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def setup_otel_tracing(
    wandb_base_url: str = "https://trace.wandb.ai",
    project_id: Optional[str] = None,
    wandb_api_key: Optional[str] = None,
) -> trace.Tracer:
    """Setup OpenTelemetry tracing with Weave integration.
    
    Args:
        wandb_base_url: Base URL for W&B tracing endpoint
        project_id: W&B project ID (e.g., "wandb/project-name")
        wandb_api_key: W&B API key for authentication
        
    Returns:
        Configured OpenTelemetry tracer
    """
    # Load environment variables
    load_dotenv()
    
    # Get configuration from environment if not provided
    if wandb_api_key is None:
        wandb_api_key = os.getenv("WANDB_API_KEY")
    
    if project_id is None:
        project_id = os.getenv("WANDB_PROJECT", "math-agent/default")
    
    if not wandb_api_key:
        raise ValueError(
            "WANDB_API_KEY must be provided either as parameter or environment variable"
        )
    
    # Setup OTLP exporter configuration
    otel_endpoint = f"{wandb_base_url}/otel/v1/traces"
    auth_header = base64.b64encode(f"api:{wandb_api_key}".encode()).decode()
    
    headers = {
        "Authorization": f"Basic {auth_header}",
        "project_id": project_id,
    }
    
    # Create tracer provider
    tracer_provider = trace_sdk.TracerProvider()
    
    # Create OTLP exporter
    exporter = OTLPSpanExporter(
        endpoint=otel_endpoint,
        headers=headers,
    )
    
    # Add batch span processor
    tracer_provider.add_span_processor(BatchSpanProcessor(exporter))
    
    # Set global tracer provider
    trace.set_tracer_provider(tracer_provider)
    
    # Return tracer for this module
    return trace.get_tracer(__name__)