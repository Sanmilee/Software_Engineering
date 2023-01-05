# Display "Hello: Welcome Lee"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello: Welcome Lee"

# uvicorn main_1:app --reload
# http://127.0.0.1:8000
