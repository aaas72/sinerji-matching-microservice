# Sinerji Matching Microservice 🚀

Hybrid AI-Powered Matching Engine for the Sinerji Tech Talent Ecosystem.

## 🌟 Overview
This microservice acts as the intelligent core of the Sinerji platform. It solves the complex problem of matching junior tech talent (students) with companies/jobs by using a **Hybrid Dual-Track Engine**:

1. **Deterministic Track (Hard Rules & Exact Skills):** Fast filtering based on budgets, required languages, locations, and rigid skill matching (e.g., if a job strictly requires intermediate React, students without it are penalized).
2. **Semantic Track (Probabilistic AI):** Powered by `Sentence-Transformers (NLP)`, this track converts free-text project descriptions and complex skills into vector embeddings, then uses **Cosine Similarity** to "understand" that a student who built an app with `Next.js` and `Zod` is a great fit for a `React Developer` role, even if keywords don't match exactly.

**Final Score Formula:** 
`Final = (α * Semantic Score) + ((1 - α) * Deterministic Score)`
Where `α` (alpha) is a configurable weight defining how "flexible" or "strict" the AI should be for each specific job.

---

## 🏗️ Tech Stack
- **FastAPI**: Blazing fast Python web framework for building the REST API.
- **Sentence-Transformers**: Open-source NLP state-of-the-art models (`all-MiniLM-L6-v2`) for computing semantic embeddings.
- **Pydantic**: Robust data validation and JSON schema generation.
- **Scikit-Learn & NumPy**: For vectorized mathematical operations and Cosine Similarity computations.

---

## ⚙️ Installation & Usage

### 1. Requirements
Ensure you have Python 3.9+ installed.

### 2. Local Setup
```bash
# Clone the repository
git clone https://github.com/aaas72/sinerji-matching-microservice.git
cd sinerji-matching-microservice

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Server
```bash
uvicorn main:app --reload
```
The server will start at `http://localhost:8000`. 
Access the interactive Swagger API documentation at: `http://localhost:8000/docs`

---

## 🧪 Testing the Model
To see the magic of the Hybrid matching in action without using the API, run the provided local test script:
```bash
python test_matcher.py
```
This script simulates a matching scenario where one student spells their skills exactly correctly, one tries to charge too much, and one uses different linguistic terms (Semantic match).

---

## 🔌 Core API Endpoint

### `POST /api/v1/match`
Calculates match scores between a single job and a batch of students.

**Body Payload:**
```json
{
  "job": {
    "id": "job_01",
    "location": "Remote",
    "max_budget": 1000,
    "required_skills": [{"name": "React", "level": 4}],
    "required_languages": ["English"],
    "description": "Looking for frontend developer to build UIs",
    "alpha": 0.6
  },
  "students": [
    {
      "id": "stu_01",
      "location": "Remote",
      "expected_budget": 800,
      "skills": [{"name": "Next.js", "level": 4}],
      "languages": ["English"],
      "description": "I build interactive UIs with modern JS frameworks."
    }
  ]
}
```

---

## 🚀 Roadmap / Next Steps
- [ ] Integrate **Faiss** or **Pinecone** Vector Database for `O(1)` lightning-fast semantic retrieval for millions of students.
- [ ] Add domain-specific NLP fine-tuning for Sinerji's unique tech datasets.
- [ ] Dockerize the service.
