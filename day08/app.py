from fastapi import FastAPI
from pydantic import BaseModel

from pubchem_logic import analyze_compounds


app = FastAPI()


class CompoundRequest(BaseModel):
    compounds: list[str]


@app.get("/")
def home():
    return {
        "message": "Welcome to the PubChem Compound Analyzer API"
    }


@app.post("/analyze")
def analyze(request: CompoundRequest):
    result = analyze_compounds(request.compounds)
    return result
