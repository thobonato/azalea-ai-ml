
# app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

# # Configure CORS
# CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# # Initialize context manager
# context_manager = ContextManager()

# @app.route('/api/query/', methods=['POST', 'OPTIONS'])
# def process_query():
#     app.logger.info(f"Received request: {request.method} {request.url}")
#     app.logger.info(f"Request headers: {request.headers}")
#     app.logger.info(f"Request data: {request.get_data()}")

#     if request.method == 'OPTIONS':
#         return _build_cors_preflight_response()
#     try:
#         data = request.json
#         app.logger.info(f"Processed JSON data: {data}")

#         query = data['query']
#         selected_model = data['model']
#         conversation_id = data.get('conversationId')

#         if conversation_id:
#             context = context_manager.get_context(conversation_id)
#         else:
#             context = []
#             conversation_id = context_manager.create_context()

#         # Handling different AI model requests
#         if selected_model == 'google':
#             result = google_search(query)
#         elif selected_model == 'chatgpt':
#             result = chatgpt_search(query, context)
#         elif selected_model == 'mistral':
#             result = prompt_mistral(query)
#         else:
#             return jsonify({'error': 'Invalid model selection'}), 400

#         response = jsonify({
#             "result": result,
#             "conversationId": conversation_id
#         })
#         return _corsify_actual_response(response)

#     except Exception as e:
#         app.logger.error(f"Unexpected error: {str(e)}", exc_info=True)
#         return _corsify_actual_response(jsonify(error="An unexpected error occurred. Please try again later.")), 500

# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
#     response.headers.add("Access-Control-Allow-Headers", "Content-Type")
#     response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# if __name__ == '__main__':
#     app.run(debug=True)



from werkzeug.exceptions import BadRequest
from models.google_search import google_search
from models.chatgpt import chatgpt_search
from models.mistral import prompt_mistral
from utils.context_manager import ContextManager
from database import save_conversation, get_conversation
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

# Access environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MONGODB_URI = os.getenv('MONGODB_URI')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query/")
async def process_query(request: Request):
    print("RECEIVED REQUESTTTTT!!!")

    data = await request.json()
    print("data:", data)

    # Google search
    if data["model"] == "google":
        result = google_search(data["query"])
    elif data["model"] == "mistral":
        result = prompt_mistral(data["query"])
    
    return {"result": {"result" : result,
                       "ecoMetrics" : {
                           "energyUsage" : 5,
                           "treesSaved" : 5,
                           "drivingAvoided" : 5
                       }
                       },
                "complexity" : 5
            }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)