import uuid

class ContextManager:
    def __init__(self):
        self.contexts = {}

    def create_context(self):
        conversation_id = str(uuid.uuid4())
        self.contexts[conversation_id] = []
        return conversation_id

    def get_context(self, conversation_id):
        return self.contexts.get(conversation_id, [])

    def update_context(self, conversation_id, query, response):
        if conversation_id not in self.contexts:
            self.contexts[conversation_id] = []
        
        self.contexts[conversation_id].append({
            'query': query,
            'response': response
        })

        # Keep only last 5 interactions for simplicity
        self.contexts[conversation_id] = self.contexts[conversation_id][-5:]