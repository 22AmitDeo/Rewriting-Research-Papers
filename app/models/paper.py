from pydantic import BaseModel

class PaperRequest(BaseModel):
    paper: str

class PaperResponse(BaseModel):
    rewritten_paper: str
