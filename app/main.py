from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Prospect API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Prospect API is running!"
    }