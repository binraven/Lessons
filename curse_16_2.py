from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def read_admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def read_user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="123")]) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def read_user_info(username: str = Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")
                         , age: int = Path(ge=18, le=120, description="Enter age'", example="24")) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
