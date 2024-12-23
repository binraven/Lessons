from fastapi import FastAPI, Path
from typing import Annotated, Dict

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def all_users() -> dict:
    return users


@app.delete("/user/{user_id}")
async def read_user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="123")]) -> str:
    try:
        users.pop(str(user_id))
        return f"The user id {user_id} was deleted"
    except Exception as e:
        return f"The user id {user_id} wasn't deleted (not found)"


@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age'", example="24")]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age'", example="24")],
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="123")]) -> str:
    for user in users.keys():
        if str(user) == str(user_id):
            users[user_id] = f"Имя: {username}, возраст: {age}"
            return f"The user id {user_id} is updated"
        else:
            return f"The user id {user_id} not updated (not found)"
