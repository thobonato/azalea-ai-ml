from werkzeug.exceptions import BadRequest
from models.google_search import google_search
from models.chatgpt import chatgpt_search
from models.mistral import prompt_mistral
from utils.scorer import load_model_vect, predict_complexity
from utils.energy_calc import update_overall, calculate_energy_out, get_overall_results
from utils.context_manager import ContextManager
from utils.algorithm import recommend_model_with_complexity_and_count
from database import save_conversation, get_conversation
from models.google_search import google_search
from models.chatgpt import chatgpt_search
from models.mistral import prompt_mistral
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import numpy as npy
import pandas as pd

# Access environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MONGODB_URI = os.getenv('MONGODB_URI')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# load model for complexity
loaded_model,loaded_vect = load_model_vect(model_name="./utils/scorer_rnd_forest_mdl.pkl",
                                           vect_name='./utils/tfidf_vectorizer.pkl')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/calculate/")
async def run_calculations(request: Request):

    # fetch data
    data = await request.json()
    query_post = data["query"]

    # fetch complexity (turn into int with .item())
    complexity = predict_complexity(loaded_model, loaded_vect, query_post).item()

    # get this info from the algo eventually
    return recommend_model_with_complexity_and_count(query_post, complexity)


@app.post("/query/")
async def process_query(request: Request):
    
    # fetch data
    data = await request.json()
    query_post = data["query"]


    # Google search
    if data["model"] == "google":
        result = google_search(query_post)
    elif data["model"] == "chatgpt":
        result = chatgpt_search(query_post)
    elif data["model"] == "mistral":
        result = prompt_mistral(query_post)
    else:
        result = "Invalid model selected."

    # use energy calc to update everything
    update_overall(data["model"], calculate_energy_out(query_post))
    
    return {"query_result" : result, 
            "dyanmic_results" : get_overall_results()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)