from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Daniel Velasquez; Queen - good old fashioned lover boy"}