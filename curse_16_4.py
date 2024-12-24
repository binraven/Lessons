from fastapi import FastAPI, status, Body, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user: User,
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age'", example="24")]) -> str:
    if len(users) == 0:
        user.id = 1
        user.username = username
        user.age = age
        users.append(user)
        return f"User {user.id} is registered"
    else:
        user.id = users[-1].id + 1
        user.username = username
        user.age = age
        users.append(user)
        return f"User {user.id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age'", example="24")],
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="123")]) -> str:

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f"User ID {user.id} updated!"
    else:
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found")



@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="123")]) -> str:
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return f"User ID {user.id} deleted!"
    else:
        raise HTTPException(status_code=404, detail=f"User ID {user_id} not found")



