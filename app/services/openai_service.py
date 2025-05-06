
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

async def stream_chat_response(prompt: str):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    async for chunk in response:
        delta = chunk.choices[0].delta.get("content", "")
        if delta:
            yield delta
