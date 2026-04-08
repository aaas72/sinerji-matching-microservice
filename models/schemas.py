from pydantic import BaseModel, Field
from typing import List, Optional

class Skill(BaseModel):
    name: str = Field(..., description="Name of the skill, e.g., 'React'")
    level: int = Field(..., description="Level of proficiency from 1 to 5", ge=1, le=5)

class StudentProfile(BaseModel):
    id: str
    location: str
    expected_budget: Optional[float] = None
    skills: List[Skill]
    languages: List[str]
    description: str = Field(..., description="Free text description of the student's background, projects, etc.")

class JobRequirement(BaseModel):
    id: str
    location: str
    max_budget: Optional[float] = None
    required_skills: List[Skill]
    required_languages: List[str]
    description: str = Field(..., description="Free text description of the job role and responsibilities")
    alpha: Optional[float] = Field(None, description="Custom weight for semantic score (0.0 to 1.0)", ge=0.0, le=1.0)

class MatchRequest(BaseModel):
    job: JobRequirement
    students: List[StudentProfile]

class MatchResult(BaseModel):
    student_id: str
    deterministic_score: float
    semantic_score: float
    final_score: float

class MatchResponse(BaseModel):
    job_id: str
    matches: List[MatchResult]
