from models.schemas import StudentProfile, JobRequirement
import numpy as np

def calculate_deterministic_score(student: StudentProfile, job: JobRequirement) -> float:
    # 1. Hard filters (e.g., languages)
    # Convert languages to sets for easy comparison
    req_langs = set(l.lower() for l in job.required_languages)
    stu_langs = set(l.lower() for l in student.languages)
    
    if req_langs and not req_langs.issubset(stu_langs):
        return 0.0 # Strict language requirement not met
        
    # Budget Check
    if job.max_budget and student.expected_budget:
        if student.expected_budget > job.max_budget:
            return 0.0 # Budget exceeded
            
    # Location Check (can be expanded later for partial matching)
    if job.location.lower() != "remote" and student.location.lower() != job.location.lower():
        # Example of harsh location filtering if not remote
        return 0.0
        
    # 2. Skill scoring
    if not job.required_skills:
        return 1.0 # No specific hard skills requested
        
    job_skills_dict = {s.name.lower(): s.level for s in job.required_skills}
    student_skills_dict = {s.name.lower(): s.level for s in student.skills}
    
    scores = []
    for req_name, req_level in job_skills_dict.items():
        if req_name in student_skills_dict:
            # Calculate how close the student is to the required level
            stu_level = student_skills_dict[req_name]
            if stu_level >= req_level:
                scores.append(1.0)
            else:
                # Partial score based on the gap
                scores.append(stu_level / req_level) # e.g., 3/5 = 0.6
        else:
            scores.append(0.0)
            
    # Return average skill score
    return float(np.mean(scores))
