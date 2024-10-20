from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/') # when the user loads the page, this is what they will get
async def root():
    return {'example': 'This is an example', 'data': 0}


@app.get('/random')
async def getRandom():
    num = random.randint(0,100)
    return {'number': num, 'limit': 100}

@app.get('/random/{limit}')
async def getRandom(limit: int):
    num = random.randint(0,limit)
    return {'number': num, 'limit': limit}
