from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome: {name}"

# uvicorn main_3:app --reload
# http://127.0.0.1:8000/hello/Sam
