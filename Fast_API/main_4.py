from fastapi import FastAPI

app = FastAPI()

food = {
    'indian': ['samosa', 'dosa'],
    'american': ['hot dog', 'apple pie'],
    'italian': ['ravioli', 'pizza']
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food.get(cuisine)

# uvicorn main_4:app --reload
# http://127.0.0.1:8000/get_items/italian

