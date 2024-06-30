from dotenv import load_dotenv
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv()

def prompt_mistral(prompt: str) -> str:
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "open-mistral-7b"

    client = MistralClient(api_key=api_key)

    messages = [
        ChatMessage(role="user", content=prompt)
    ]

    # No streaming
    chat_response = client.chat(
        model=model,
        messages=messages,
    )

    return chat_response.choices[0].message.content

if __name__ == "__main__":
    print(prompt_mistral("What is the best French cheese?"))