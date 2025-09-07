from app.utils.openrouter import call_openrouter
from app.utils.humanizer import humanize_text

async def rewrite_paper(paper_text: str) -> str:
    # Call OpenRouter to rewrite the paper
    rewritten = await call_openrouter(paper_text)
    # Apply humanizer post-processing
    humanized = humanize_text(rewritten)
    return humanized
