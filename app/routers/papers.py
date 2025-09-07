from fastapi import APIRouter, Body, Request
from fastapi.responses import JSONResponse
from app.services.rewrite_service import rewrite_paper

router = APIRouter()

@router.post("/rewrite")
async def rewrite(request: Request):
    """
    Accepts either:
      1. JSON: {"paper": "..."}
      2. Raw text/plain: "... full paper ..."
    """
    try:
        # Try to parse as JSON first
        data = await request.json()
        paper_text = data.get("paper")
    except Exception:
        # Fallback: treat it as raw text
        paper_text = await request.body()
        paper_text = paper_text.decode("utf-8")

    if not paper_text:
        return JSONResponse(status_code=400, content={"error": "No paper text provided."})

    rewritten = await rewrite_paper(paper_text)
    return {"rewritten_paper": rewritten}
