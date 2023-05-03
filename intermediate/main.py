from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Welcome to my APIs"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your latest post"}

