import uvicorn 
from fastapi import FastAPI

# Create the app object
app = FastAPI()

# Index route
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# Route with a single parameter
@app.get('/Welcome')
def get_name():
    return {'Hello, Welcome!'}

# Route with a variable parameter
@app.get("/{any_name}")
async def hello(any_name):
    return f"Welcome {any_name}!"

# Route with a single parameter
@app.get('/Welcome/{name}')
def get_name(name: str):
    return {f'Welcome {name}!'}



# Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn main_5:app --reload

# http://127.0.0.1:8000
# http://127.0.0.1:8000/Welcome
# http://127.0.0.1:8000/Jay
# http://127.0.0.1:8000/Welcome/Jay


