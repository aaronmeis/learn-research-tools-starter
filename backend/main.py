from fastapi import FastAPI

app = FastAPI(title="Research Tools Starter API")

@app.get("/")
async def root():
    return {"message": "Starter Template active"}
