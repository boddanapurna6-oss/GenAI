

import os
from dotenv import load_dotenv

from llm_client import GeminiProvider, OllamaProvider, LLMClient

load_dotenv(override=True)

provider_name = input("Choose provider (gemini/ollama): ").strip().lower()

if provider_name == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key or api_key == "YOUR_API_KEY_HERE":
        raise ValueError("Please add your real Gemini API key in .env")

    provider = GeminiProvider(api_key)

elif provider_name == "ollama":
    provider = OllamaProvider("llama3.2")

else:
    raise ValueError("Invalid provider selected")

client = LLMClient(provider)

prompt = input("Enter your question: ")

print("\nGenerating response...\n")

answer = client.generate(prompt)

print("\nLLM Response:")
print(answer)
