from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hi")
async def greet():
    return {"message": "Hello User"}

@app.get("/hi/{who}")
async def greet(who: str):
    return {"message": "Hello {who}".format(who=who)}