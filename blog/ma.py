from fastapi import FastAPI

from . import schemas

app=FastAPI()


@app.post('/blog')
def create(request:schemas.blog):
    return request
