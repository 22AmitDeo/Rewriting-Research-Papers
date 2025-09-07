from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.services.rewrite_service import rewrite_paper

router = APIRouter()

# Pydantic model for Swagger docs
class PaperInput(BaseModel):
    paper: str

@router.post("/rewrite")
async def rewrite_endpoint(
    request: Request,
    paper_input: PaperInput = Body(None)  # Optional JSON body for docs
):
    # Case 1: JSON provided
    if paper_input is not None:
        paper_text = paper_input.paper
    else:
        # Case 2: Raw text/plain
        body_bytes = await request.body()
        paper_text = body_bytes.decode("utf-8")

    if not paper_text.strip():
        return JSONResponse({"error": "No paper text provided"}, status_code=400)

    rewritten = await rewrite_paper(paper_text)
    return {"rewritten_paper": rewritten}
