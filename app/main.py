from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return("Hello")

@app.get("/users/{userid}")
def user_data(userid : int):
    return{
        "User id" : userid
    }