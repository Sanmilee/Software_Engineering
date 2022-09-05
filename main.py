### Display "Hello: Welcome Lee"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello: Welcome Lee"
