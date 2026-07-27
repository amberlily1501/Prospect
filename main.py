from fastapi import FastAPI

app = FastAPI(
    title="Prospect API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Prospect API is running!"
    }