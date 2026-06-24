from fastapi import FastAPI

app = FastAPI()

def mimensaje():
    return "este es un mensaje"


@app.get("/")
def read_root():
    return {"message": mimensaje()}