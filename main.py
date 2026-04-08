from fastapi import FastAPI, HTTPException
from models.schemas import MatchRequest, MatchResponse, MatchResult
from services.deterministic import calculate_deterministic_score
from services.semantic import calculate_semantic_score
from core.config import settings
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Hybrid Matching Microservice for Sinerji"
)

@app.get("/")
def read_root():
    return {"message": "Sinerji Matching Microservice is running!"}

@app.post("/api/v1/match", response_model=MatchResponse)
def match_students_to_job(request: MatchRequest):
    job = request.job
    students = request.students
    
    alpha = job.alpha if job.alpha is not None else settings.DEFAULT_ALPHA
    
    results = []
    for student in students:
        # 1. Deterministic Score (Skills & Hard Limits)
        det_score = calculate_deterministic_score(student, job)
        
        # 2. Semantic Score (NLP understanding of descriptions)
        sem_score = calculate_semantic_score(student.description, job.description)
        
        # 3. Fusion
        final_score = (alpha * sem_score) + ((1 - alpha) * det_score)
        
        results.append(MatchResult(
            student_id=student.id,
            deterministic_score=round(det_score, 4),
            semantic_score=round(sem_score, 4),
            final_score=round(final_score, 4)
        ))
        
    # Sort results by final score descending
    results.sort(key=lambda x: x.final_score, reverse=True)
    
    return MatchResponse(
        job_id=job.id,
        matches=results
    )
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
