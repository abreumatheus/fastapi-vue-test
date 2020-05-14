from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from app.core import config
from app.api.api import api_router


app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

# CORS
origins = []

if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(",")
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"]
    )


@app.get('/', include_in_schema=False)
def redirect_to_docs():
    response = RedirectResponse(url='/redoc')
    return response


app.include_router(api_router, prefix=config.API_PREFIX)
