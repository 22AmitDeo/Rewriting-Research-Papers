import httpx
from app.config import settings
SYSTEM_PROMPT = """
You are an academic editor. Rewrite the research paper so it passes as
naturally human-written. Apply these rules carefully:

1. Do NOT write with flawless, robotic uniformity. Instead:
   - Mix long and short sentences.
   - Use occasional incomplete sentences or conversational fragments.
   - Ask rhetorical questions sparingly.
   - Use hedging words (might, could, arguably, in some cases).
2. Allow minor imperfections or slight redundancy — the goal is naturalness, not perfection.
3. Vary transitions. Avoid starting most paragraphs with “Moreover,” “Thus,” or “Therefore.”
4. Keep academic tone but let the text “breathe” with natural rhythm.
5. Preserve meaning, citations, equations, and references exactly as provided.
6. Keep the rewritten paper length within ±10% of the original.
7. Do NOT fabricate any information.
8. Output only the rewritten paper text.
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
