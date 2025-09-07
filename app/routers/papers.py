from fastapi import APIRouter, Depends
from app.models.paper import PaperRequest, PaperResponse
from app.services.rewrite_service import rewrite_paper

router = APIRouter()

@router.post("/rewrite", response_model=PaperResponse)
async def rewrite_paper_endpoint(request: PaperRequest):
    rewritten = await rewrite_paper(request.paper)
    return PaperResponse(rewritten_paper=rewritten)
