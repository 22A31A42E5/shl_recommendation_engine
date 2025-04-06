from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from search_engine import load_index, search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str

index, df = load_index("final_tests.csv")

@app.post("/recommend")
def recommend(query: Query):
    return search(query.query, index, df, top_k=10)