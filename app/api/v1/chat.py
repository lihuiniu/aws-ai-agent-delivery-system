
from fastapi import APIRouter, WebSocket
from app.services.openai_service import stream_chat_response

router = APIRouter()

@router.websocket("/stream")
async def stream_chat(ws: WebSocket):
    await ws.accept()
    prompt = await ws.receive_text()
    async for token in stream_chat_response(prompt):
        await ws.send_text(token)
