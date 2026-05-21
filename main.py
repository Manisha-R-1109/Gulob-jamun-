from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Content": "Manisha Gulob Jamun"}

@app.get("/products")
def products():
    return [
        {"id": 1, "name": "Gulab Jamun"},
        {"id": 2, "name": "Ice Cream"}
    ]
