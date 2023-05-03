from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Welcome to my APIs"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your latest post"}


@app.post("/createposts")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message": "Successfully created a post"}
