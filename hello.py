from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def greet():
    return {"message": "Hello User"}