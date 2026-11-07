
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Call the LLM
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what RAG is in 3 simple sentences."
)

# Print the response
print(response.output_text)
