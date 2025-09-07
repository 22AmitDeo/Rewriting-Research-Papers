import httpx
from app.config import settings

SYSTEM_PROMPT = """
You are an academic editor. Rewrite the research paper to sound human-written,
clear, professional, and natural. Follow these rules:

1. Vary sentence length and structure. Mix long, detailed analysis with shorter, emphatic statements.  
2. Allow slight imperfections or informal phrasing where natural (but stay professional).  
3. Avoid repetitive transitions like "Moreover," "Thus," "Therefore" at the start of every sentence.  
4. Do NOT remove or invent citations, equations, or references.  
5. Keep the overall meaning but make it feel like a human’s unique voice.  
6. Add light stylistic touches: occasional rhetorical questions, hedging (“might,” “could,” “in some cases”).  
7. Keep the length within ±10% of the original.  

Output only the rewritten paper text.
"""

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
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
