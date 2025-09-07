from app.utils.openrouter import call_openrouter
from app.utils.humanizer import humanize_text

async def rewrite_paper(paper_text: str) -> str:
    rewritten = await call_openrouter(paper_text)
    # Use "strong" mode to really lower AI detection
    humanized = humanize_text(rewritten, strength="extreme")
    return humanized
