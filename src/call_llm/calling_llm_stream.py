import asyncio
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

class ChatService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        self.client = AsyncOpenAI(api_key=api_key)

    async def stream(self, prompt: str):
        stream = await self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            stream=True,
            stream_options={
                "include_usage": True
            }
        )

        async for chunk in stream:
            if chunk.choices:
                delta = chunk.choices[0].delta

                if delta.content:
                    yield{
                        "type": "content",
                        "content": delta.content
                    }

            if chunk.usage:
                yield {
                    "type": "usage",
                    "usage": {
                        "prompt_tokens": chunk.usage.prompt_tokens,
                        "completion_tokens": chunk.usage.completion_tokens,
                        "total_tokens": chunk.usage.total_tokens
                    }
                }



async def main():
    chat_service = ChatService()
    query= input("Query: ")
    async for event in chat_service.stream(query):
        if event["type"] == "content":
            print(event["content"], end="", flush=True)
        elif event["type"] == "usage":
            print(f"\n\nUsage: {event['usage']}")

if __name__ == "__main__":
    asyncio.run(main())