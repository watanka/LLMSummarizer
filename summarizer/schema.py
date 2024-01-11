from pydantic import BaseModel, field_validator


class SummaryRequest(BaseModel):
    url: str
    api_key: str
