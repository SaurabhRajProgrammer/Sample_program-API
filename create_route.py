from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home_route():
    return {
        "message":"create the home route"
    }
@app.get("/About")
def get_route():
    return {
        "message":"This is about page"
    }
@app.get("/Users")
def users():
    return {
        "users":["Saurabh","Nayra","Shubham","Mohit"]
    }