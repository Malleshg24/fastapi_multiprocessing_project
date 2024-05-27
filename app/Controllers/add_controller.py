from fastapi import HTTPException
from app.models.item import AddRequest
from app.utils.addition import add_lists
from app.utils.logging_config import logger

def perform_addition(request: AddRequest):
    try:
        logger.info(f"Received request: {request}")
        result = add_lists(request.lists)
        logger.info(f"Computed result: {result}")
        return result
    except ValueError as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
