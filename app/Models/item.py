from pydantic import BaseModel
from typing import List

class AddRequest(BaseModel):
    lists: List[List[int]]

class AddResponse(BaseModel):
    sums: List[int]
