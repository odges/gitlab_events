from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from route import router
import uvicorn

DEBUG = True
PROJECT_NAME = "gitlab-bot"
VERSION = "0.0.1"
import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()


def get_application() -> FastAPI:
    application = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        version=VERSION,
        openapi_url="/openapi.json",
    )

    @application.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
        logging.error(f"{request}: {exc_str}")
        content = {"status_code": 10422, "message": exc_str, "data": None}
        return JSONResponse(
            content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)
    return application


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Enter port")
    parser.add_argument("--port", type=int, default=8002, help="Enter port")
    args = parser.parse_args()
    app = get_application()

    uvicorn.run(
        app,
        host="0.0.0.0",
        loop="uvloop",
        debug=DEBUG,
        port=args.port,
    )
