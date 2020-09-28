from fastapi import APIRouter, Depends
from accounts.routes import router as accounts_router
from events.routes import router as events_router
from core.middlewares.auth import get_token_header


router = APIRouter()


''' accounts '''
router.include_router(
    accounts_router,
    prefix='/accounts',
    tags=['accounts'],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

''' events app '''
router.include_router(
    events_router,
    prefix='/events',
    tags=['events']
)
