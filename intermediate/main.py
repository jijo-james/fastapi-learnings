from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional

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
    return {"data": "This is your latest post"}


@app.post("/posts")
def create_post(post: Post):
    print(post.rating)
    print(post.dict())
    return {"data": my_posts}
