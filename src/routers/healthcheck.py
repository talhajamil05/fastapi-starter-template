from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck")
async def get_healthcheck():
    return {"status": "Ok"}

