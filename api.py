from fastapi import FastAPI, Query

app = FastAPI(title="Лабораторная №6")


@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}


@app.get("/hello")
def hello_name(name: str = Query(..., min_length=1, max_length=80)):
    return {"message": f"Привет, {name}!"}
