import asyncio
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

class ChatService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        self.client = AsyncOpenAI(api_key=api_key)

    async def ask(self, prompt: str)->str:
        response = await self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content


async def main():
    chat_service = ChatService()
    query= input("Query: ")
    response = await chat_service.ask(query)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())