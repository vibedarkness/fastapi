from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return {'message':'bienvenue dans mon nouveau fastapi'}