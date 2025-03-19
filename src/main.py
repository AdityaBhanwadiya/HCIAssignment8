import openai
import os
from config import Config

# Set up OpenAI client for Azure
# Initialize the Azure OpenAI client with API key, version, and endpoint from the configuration
client = openai.AzureOpenAI(
    api_key=Config.AZURE_OPENAI_API_KEY,
    api_version=Config.AZURE_OPENAI_API_VERSION,
    azure_endpoint=Config.AZURE_OPENAI_ENDPOINT
)

# Function to generate a creative "Hello World" message
def generate_hello_world():
    try:
        # Send a request to the Azure OpenAI API to generate a response
        response = client.chat.completions.create(
            model=Config.AZURE_OPENAI_DEPLOYMENT_NAME,  # Specify the deployment name (model)
            messages=[
                # System message to set the assistant's behavior
                {"role": "system", "content": "You are a creative assistant."},
                # User message to request a unique "Hello World" message
                {"role": "user", "content": "Generate a unique 'Hello World' message in a fun way."}
            ],
            temperature=0.7  # Set the creativity level (higher = more creative)
        )

        # Extract and return the generated message from the response
        return response.choices[0].message.content 

    except Exception as e:
        # Handle exceptions and return the error message
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(generate_hello_world())
