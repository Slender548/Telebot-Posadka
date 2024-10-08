from aiogram import Router
from .start import router as start_router
from .echo import router as echo_router


def get_router() -> Router:
    router = Router()
    router.include_router(start_router)
    router.include_router(echo_router)
    return router