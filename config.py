import os

class Config:
    GITLAB_URL = os.environ.get("GITLAB_URL", "https://gitlab.example.com").rstrip("/")
    GITLAB_TOKEN = os.environ.get("GITLAB_TOKEN")
    
    # [NEW: Config block for Manual LLM execution]
    MANUAL_LLM_MODE = os.environ.get("MANUAL_LLM_MODE", "True").lower() == "true"
    PROMPT_EXPORT_DIR = os.environ.get("PROMPT_EXPORT_DIR", "./prompts_export")
    
    INTERNAL_LLM_API_BASE = os.environ.get("INTERNAL_LLM_API_BASE")
    INTERNAL_LLM_API_KEY = os.environ.get("INTERNAL_LLM_API_KEY")
    LLM_MODEL_NAME = os.environ.get("LLM_MODEL_NAME", "gpt-4o")
    
    DATABASE_PATH = os.environ.get("DATABASE_PATH", "casper_memory.sqlite")

    @classmethod
    def validate(cls):
        missing = []
        if not cls.GITLAB_TOKEN: missing.append("GITLAB_TOKEN")
        
        # [CHANGED: Only enforce LLM API keys if we are NOT in manual mode]
        if not cls.MANUAL_LLM_MODE:
            if not cls.INTERNAL_LLM_API_KEY: missing.append("INTERNAL_LLM_API_KEY")
            if not cls.INTERNAL_LLM_API_BASE: missing.append("INTERNAL_LLM_API_BASE")
            
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
