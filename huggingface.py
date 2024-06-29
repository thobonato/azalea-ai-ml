from transformers import pipeline

# Initialize the model
generator = pipeline('text-generation', model='meta-llama/Meta-Llama-3-8B-Instruct')

# Function to generate response
def generate_response(prompt, max_length=100):
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    return result[0]['generated_text']

# Example usage
prompt = "Explain quantum computing in simple terms:"
response = generate_response(prompt)
print(response)