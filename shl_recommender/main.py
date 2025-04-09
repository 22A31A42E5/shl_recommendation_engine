from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from search_engine import load_index, search

app = FastAPI()

# Enable CORS (important for frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input format for /recommend
class Query(BaseModel):
    query: str

# Load your data/index
index, df = load_index("final_tests.csv")

# SHL required: /recommend endpoint with POST
@app.post("/recommend")
def recommend(query: Query):
    results = search(query.query, index, df, top_k=10)
    return {"recommended_assessments": results}

# SHL required: /health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Optional: for UptimeRobot to ping without hitting POST-only endpoints
@app.get("/ping")
def ping():
    return {"status": "alive"}
