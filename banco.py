from datetime import datetime

from peewee import *

db = SqliteDatabase('pydb.db')

def create_table():
    with db:
        db.create_tables([Users,LastLogin])
        print('Tabelas criada')

class BaseModel(Model):

    class Meta:
        database = db
        


class Users(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class LastLogin(BaseModel):
    user = ForeignKeyField(Users)
    date = DateTimeField(default=datetime.now())
    remember = BooleanField()

if __name__ == '__main__':
    create_table()
