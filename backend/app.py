from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import logging
import numpy as npy
import pandas as pd

from models.google_search import google_search
from models.chatgpt import chatgpt_search
from models.mistral import prompt_mistral
from utils.scorer import load_model_vect, predict_complexity
from utils.energy_calc import update_overall, calculate_energy_out, get_overall_results
from utils.context_manager import ContextManager
from utils.algorithm import recommend_model_with_complexity_and_count

# Load environment variables
load_dotenv()

# Access environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MONGODB_URI = os.getenv('MONGODB_URI')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load model for complexity
try:
    loaded_model, loaded_vect = load_model_vect(
        model_name="./utils/scorer_rnd_forest_mdl.pkl",
        vect_name='./utils/tfidf_vectorizer.pkl'
    )
except FileNotFoundError as e:
    logger.error(f"Failed to load model or vectorizer: {e}")
    raise

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://azalea-ml.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate/")
async def run_calculations(request: Request):
    """
    Calculate and recommend a model based on query complexity.
    """
    try:
        data = await request.json()
        query_post = data["query"]
        complexity = predict_complexity(loaded_model, loaded_vect, query_post).item()
        return recommend_model_with_complexity_and_count(query_post, complexity)
    except Exception as e:
        logger.error(f"Error in run_calculations: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/")
async def process_query(request: Request):
    """
    Process a query using the specified model and update energy calculations.
    """
    try:
        data = await request.json()
        query_post = data["query"]
        model = data["model"]

        if model == "google":
            result = google_search(query_post)
        elif model == "chatgpt":
            result = chatgpt_search(query_post)
        elif model == "mistral":
            result = prompt_mistral(query_post)
        else:
            raise ValueError("Invalid model selected.")

        update_overall(model, calculate_energy_out(query_post))
        
        return {
            "query_result": result, 
            "dynamic_results": get_overall_results()
        }
    except Exception as e:
        logger.error(f"Error in process_query: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)