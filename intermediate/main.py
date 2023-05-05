from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"msg": "Welcome to my APIs"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your latest post"}


@app.post("/createposts")
def create_post(post: Post):
    print(post.rating)
    print(post.dict())
    return {"data": "new post"}
