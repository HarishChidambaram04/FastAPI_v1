from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# import uvicorn
app = FastAPI()



@app.get('/blog')
def create(limit,published:bool ,sort:Optional[str] = None):
  if published:
    return {'data':f'{limit} blogs from the list'}
  else:
    return {'data':f'{limit} blogs from the db'}


@app.get('/blog/{id}/comments')
def comments(id,limit=10):

  return{'data':{'1','2'}}

@app.get('/blog/unpublished')                    
def unpublished():
  return {'data': 'all unpublished blogs'}

class Blog(BaseModel):
  name:str
  password:str


@app.post('/blog')
def create_blog(blog:Blog):
  return {'data':f'Blog is created with title as {blog.title}'}


# Developer has to run different port we have to use it
# if __name__ == "__main__":
#   uvicorn.run(app,host="127.0.0.1",port=9000)