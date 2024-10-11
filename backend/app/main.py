from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from backend.app.dependency import RoleChecker
from backend.app.routes.auth import auth_router

app = FastAPI()

app.include_router(router=auth_router)


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Drone Command Center!"}


@app.get("/protected_route")
async def protected_route(_: Annotated[bool, Depends(RoleChecker(allowed_roles=["Operator"]))]) -> dict:
    return {"message": "here is the protected route"}