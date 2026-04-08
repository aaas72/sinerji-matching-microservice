import os

class Settings:
    PROJECT_NAME: str = "Sinerji Matching Microservice"
    VERSION: str = "1.0.0"
    
    # Default alpha weight for blending Deterministic (1-alpha) and Semantic (alpha) scores
    DEFAULT_ALPHA: float = 0.6
    
    # Model configuration
    MODEL_NAME: str = "all-MiniLM-L6-v2"

settings = Settings()
