from peewee import *

database = SqliteDatabase('app.db')


def create_tables():
    with database:
        database.create_tables([User, Relationship, Message])
