import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return {'message:' 'Wag1 G!'}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)