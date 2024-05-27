from fastapi import APIRouter
from app.models.item import AddRequest, AddResponse
from app.controllers.add_controller import perform_addition

router = APIRouter()

@router.post("/", response_model=AddResponse)
async def add_lists_endpoint(request: AddRequest):
    result = perform_addition(request)
    return AddResponse(sums=result)
