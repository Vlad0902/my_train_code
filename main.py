
from pydantic import BaseModel
from fastapi import FastAPI


class User(BaseModel):
    id: int = None
    name: str = None
    age: int = None
    description: str = None


Dima = User.parse_obj({'id': 1, 'name': "Dima", 'age': 10, 'description': "good"})
Vlad = User.parse_obj({'id': 2, 'name': "Vlad", 'age': 10, 'description': "good"})
Kate = User.parse_obj({'id': 3, 'name': "Kate", 'age': 10, 'description': "good"})
Ira = User.parse_obj({'id': 4, 'name': "Ira", 'age': 10, 'description': "good"})
Alexey = User.parse_obj({'id': 5, 'name': "Alexey", 'age': 10, 'description': "good"})

users = {Dima.id: Dima.dict(),
        Vlad.id: Vlad.dict(),
        Kate.id: Kate.dict(),
        Ira.id: Ira.dict(),
        Alexey.id: Alexey.dict()}

#print(users)

user = {}


class UsersRepository:
    def __init__(self):
        self.user = user

    def create(self, id_user, data):
        self.user[id_user] = data
        return self.user

    def read(self, id_user):
        return self.user[id_user]

    def update(self, id_user, data):
        self.user.update([(id_user, data)])
        return self.user

    def delete(self, id_user):
        self.user.pop(id_user)
        return self.user


user_repo = UsersRepository()

#user_repo.create(1, {'id': 5, 'name': "Alexey", 'age': 10, 'description': "good"})
#user_repo.delete(1)
#print(user_repo.user)

app = FastAPI()


@app.get('/read')
def read(id_user):
    return user_repo.read(id_user)


@app.post('/create/{id_user}')
def read(id_user, data):
    return user_repo.create(id_user, data)


@app.delete('/delete/{id_user}')
def read(id_user):
    return user_repo.delete(id_user)
