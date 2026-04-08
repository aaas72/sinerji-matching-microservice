from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from core.config import settings
import logging

logger = logging.getLogger(__name__)

# Lazy loading of the model to avoid slow startup if not used
_model = None

def get_model():
    global _model
    if _model is None:
        logger.info(f"Loading SentenceTransformer model: {settings.MODEL_NAME}")
        _model = SentenceTransformer(settings.MODEL_NAME)
    return _model

def get_embedding(text: str) -> np.ndarray:
    model = get_model()
    # Returns embedding as numpy array
    return model.encode(text)

def calculate_semantic_score(student_desc: str, job_desc: str) -> float:
    if not student_desc or not job_desc:
        return 0.0
        
    student_emb = get_embedding(student_desc)
    job_emb = get_embedding(job_desc)
    
    # Reshape for sklearn cosine_similarity
    student_emb = student_emb.reshape(1, -1)
    job_emb = job_emb.reshape(1, -1)
    
    # Calculate cosine similarity (-1 to 1) and normalize to 0-1
    sim = cosine_similarity(student_emb, job_emb)[0][0]
    
    # Cosine similarity can be negative, normalize to [0, 1] range
    normalized_score = (sim + 1) / 2
    return float(normalized_score)
