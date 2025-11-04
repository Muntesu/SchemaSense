"""
Configuration for AI failure analyzer.
Handles API keys and LLM settings.
"""

import os
from pathlib import Path
from typing import Optional


PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOCAL_KEY_FILE = PROJECT_ROOT / ".groq_api_key"


class AIConfig:
    """Configuration for AI failure analysis using Groq (Llama 3.1-8B-instant)."""
    
    # Groq API settings
    GROQ_API_KEY_ENV = "GROQ_API_KEY"  # Environment variable name
    GROQ_API_KEY_DEFAULT = None  # Do not hardcode secrets; rely on env or local file
    GROQ_MODEL = "llama-3.1-8b-instant"  # Fast model, good for structured analysis
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    
    # Analysis settings
    MAX_TOKENS = 800  # Increased for more detailed analysis with request context
    TEMPERATURE = 0.1  # Low for consistent, structured output
    
    @classmethod
    def get_api_key(cls) -> Optional[str]:
        """Get Groq API key from environment variable or default."""
        # First, try environment variable
        api_key = os.getenv(cls.GROQ_API_KEY_ENV)
        
        # Next, try local key file in project root (ignored by git)
        if not api_key and LOCAL_KEY_FILE.exists():
            api_key = LOCAL_KEY_FILE.read_text(encoding="utf-8").strip()
        
        # If not found, use default/hardcoded key if available
        if not api_key and cls.GROQ_API_KEY_DEFAULT:
            api_key = cls.GROQ_API_KEY_DEFAULT
        
        if not api_key:
            raise ValueError(
                f"Groq API key not found. Please set {cls.GROQ_API_KEY_ENV} environment variable\n"
                f"or set GROQ_API_KEY_DEFAULT in ai_config.py.\n"
                f"Get your free API key at: https://console.groq.com"
            )
        return api_key
    
    @classmethod
    def is_configured(cls) -> bool:
        """Check if API key is configured (env var or default)."""
        return (
            (cls.GROQ_API_KEY_ENV in os.environ and os.getenv(cls.GROQ_API_KEY_ENV) is not None)
            or LOCAL_KEY_FILE.exists()
            or cls.GROQ_API_KEY_DEFAULT is not None
        )

