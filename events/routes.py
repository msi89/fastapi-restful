from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def get_events():
    events = []
    return {"result": events}
