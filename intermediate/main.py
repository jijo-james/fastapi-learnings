from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title post 1", "content": "content post 1", "id": 1},
    {"title": "favorate food", "content": "I like chicken", "id": 2},
]



@app.get("/")
async def root():
    return {"msg": "Welcome to my APIs"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(3, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post details":f"Here is post {id}"}

