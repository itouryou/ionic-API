from pydantic import BaseModel

class CompanyRequest(BaseModel):
    id: str