from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.exceptions import BadRequest
from models.google_search import google_search
from models.chatgpt import chatgpt_search
from models.mistral import prompt_mistral
from utils.scorer import calculate_score
from utils.context_manager import ContextManager
from database import save_conversation, get_conversation

# Load environment variables from .env file
load_dotenv()

# Access environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
MONGODB_URI = os.getenv('MONGODB_URI')
FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

# Initialize Flask app
app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
app.config['SECRET_KEY'] = FLASK_SECRET_KEY

# Initialize context manager
context_manager = ContextManager()

def validate_query(data):
    if not data or 'query' not in data or 'model' not in data:
        raise BadRequest("Missing required fields: 'query' and 'model'")
    if data['model'] not in ['google', 'chatgpt', 'mistral']:
        raise BadRequest("Invalid model selection")
    if len(data['query']) > 500:  # Example max length
        raise BadRequest("Query too long. Maximum 500 characters allowed.")

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(Exception)
def handle_general_exception(e):
    app.logger.error(f"Unexpected error: {str(e)}")
    return jsonify(error="An unexpected error occurred. Please try again later."), 500

@app.route('/api/query', methods=['POST'])
def process_query():
    try:
        data = request.json
        validate_query(data)
        
        query = data['query']
        selected_model = data['model']
        conversation_id = data.get('conversationId')

        # Retrieve or create conversation context
        if conversation_id:
            context = context_manager.get_context(conversation_id)
        else:
            context = []
            conversation_id = context_manager.create_context()

        # Process query with selected model
        if selected_model == 'google':
            result = google_search(query)
        elif selected_model == 'chatgpt':
            result = chatgpt_search(query, context)
        elif selected_model == 'mistral':
            result = prompt_mistral(query)
        else:
            return jsonify({'error': 'Invalid model selection'}), 400

        # Calculate score and eco-metrics
        score, eco_metrics = calculate_score(selected_model, query, len(context))

        # Update context
        context_manager.update_context(conversation_id, query, result)

        # Save to MongoDB
        save_conversation(conversation_id, query, result, selected_model)

        return jsonify({
            'result': result,
            'score': score,
            'ecoMetrics': eco_metrics,
            'conversationId': conversation_id
        })

    except BadRequest as e:
        return jsonify(error=str(e)), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {str(e)}")
        return jsonify(error="An unexpected error occurred. Please try again later."), 500

@app.route('/api/conversation/<conversation_id>', methods=['GET'])
def get_conversation_history(conversation_id):
    try:
        conversation = get_conversation(conversation_id)
        if conversation:
            return jsonify(conversation)
        else:
            return jsonify({'error': 'Conversation not found'}), 404
    except Exception as e:
        app.logger.error(f"Error retrieving conversation: {str(e)}")
        return jsonify(error="An error occurred while retrieving the conversation."), 500

# Serve React App
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
