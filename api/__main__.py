from fastapi import FastAPI, APIRouter

from api.apps.banks.endpoints import router as bank_router
from api.apps.currencies.endpoints import router as currency_router


API_ROOT_URL = "/api/v1"
TITEL = "API по стягиванию курсов валют"
main_router = APIRouter(prefix=API_ROOT_URL)

def setup_router(app: FastAPI, main_router: APIRouter = main_router) -> None:
    main_router.include_router(bank_router)
    main_router.include_router(currency_router)
    app.include_router(main_router)

app = FastAPI(
    title=TITEL,
    version="0.0.1",
    docs_url=API_ROOT_URL + "/docs",
    redoc_url=API_ROOT_URL + "/redoc",
    )

setup_router(app)