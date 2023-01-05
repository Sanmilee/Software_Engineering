# Display hello
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return "Welcome"

# uvicorn main_2:app --reload
# http://127.0.0.1:8000/hello
