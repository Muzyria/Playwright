from pydantic import BaseModel

class UserProfile(BaseModel):
    user_id: int
    username: str
    email: str | None = None
    age: int = 18
    is_active: bool = True


user_1 = {
    "user_id": 12345,
    "username": "Alex"
    }

user_2 = {
    "user_id": 12345,
    "username": "Alex",
    "email": "qwerty@qq.com",
    "age": 25,
    "is_active": True
    }

user = UserProfile(**user_1)
print(user.model_dump_json())

user = UserProfile(**user_2)
print(user.model_dump_json())
