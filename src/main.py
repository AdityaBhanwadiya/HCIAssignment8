import openai
import os
from config import Config

# Set up OpenAI client for Azure
client = openai.AzureOpenAI(
    api_key=Config.AZURE_OPENAI_API_KEY,
    api_version=Config.AZURE_OPENAI_API_VERSION,
    azure_endpoint=Config.AZURE_OPENAI_ENDPOINT
)

def generate_hello_world():
    try:
        response = client.chat.completions.create(
            model=Config.AZURE_OPENAI_DEPLOYMENT_NAME,  
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": "Generate a unique 'Hello World' message in a fun way."}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content 

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(generate_hello_world())
