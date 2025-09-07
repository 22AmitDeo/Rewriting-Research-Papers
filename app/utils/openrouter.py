import httpx
from app.config import settings

async def call_openrouter(user_input: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Research Editor"
    }

    payload = {
        "model": settings.OPENROUTER_MODEL,
        "temperature": 0.9,
        "messages": [
            {"role": "system", "content": "You are an academic editor."},
            {"role": "user", "content": user_input}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
