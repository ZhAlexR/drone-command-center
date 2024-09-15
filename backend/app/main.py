from fastapi import FastAPI
from backend.app.routes.auth import auth_router

app = FastAPI()

app.include_router(router=auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Drone Command Center!"}
