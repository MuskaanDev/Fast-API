from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()#instance, use this name only with uvivicorn

@app.get('/blog') #base url---------can't hardocde query parameters here
def index(limit=10,published=True, sort: Optional[str]=None): # default values if you dont want this can define the pydantic datatypes
    if published:# function doesnt matter the app decorator matters
     return {'data':f'{limit} published blogs from the list'}
    else:
        return{'data':f'{limit} blogs from the db'}
#fast api reads code line by line

@app.get('/blog/unpublished')
def unpub():
    return{'data':"all unpublished blogs"}


@app.get('/blog/{id}') #for dynamic routing use {}
def show(id: int):
    #to fetch the blog
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id: int,limit=10):# define thta id should only be of type integer
    return{'data':{'comments':[1,2,3]}}
    #to fetch the comments
    
    
    # request body
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]
    
@app.post('/blog')
def create_blog(blog: Blog):
    return{'data':f"Blog is created witht title as {blog.title}"}



