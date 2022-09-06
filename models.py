import db
from sqlalchemy import Column, Integer, String


class User():
    __tablename__ = 'users'
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, primary_key=True, nullable=False, unique=True)
    password = Column(String)

    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return f'User: {self.id_user}, {self.first_name}, {self.last_name}, {self.email}, {self.password}'

    def __repr__(self):
        return f'User: {self.id_user}, {self.first_name}, {self.last_name}, {self.email}, {self.password}'


class Task():
    __tablename__ = 'tasks'

    num = Column(String, primary_key=True, nullable=False, unique=True)
    title = Column(String, nullable=False)
    desc = Column(String)

    def __init__(self, num: str, title: str, desc: str):
        self.num = num
        self.title = title
        self.desc = desc

    def __str__(self):
        return f'Task: {self.title}, {self.desc}'

    def __repr__(self):
        return f'Task: {self.title}, {self.desc}'

