from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project.middlewares import ServerTiming
from project.config import get_settings
from project.routes.api import api_router
from project.logging import config_logs

config = get_settings()


app = FastAPI(
    title=config.APP_NAME,
    openapi_url="/openapi.json",
    debug=config.DEBUG,
    on_startup=[],
    on_shutdown=[]
)

origins = [
    "https://*.siembro.mx",
    "https://*.siembro.com",
    "*"
]

# if config.LOCAL:
#     origins.append("*")


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    ServerTiming
)


@app.get("/healthcheck", status_code=200)
def healthcheck():
    return "OK"


app.include_router(api_router, prefix='/api/v1')

# config_logs()
