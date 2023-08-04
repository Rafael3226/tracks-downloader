# models/database.py
from peewee import *

# Replace the database_name, username, password, and host with your actual PostgresSQL credentials
database_name = 'postgres'
username = 'postgres'
password = 'postgres'
host = 'localhost'

# Create a PostgresSQL database connection
db = PostgresqlDatabase(database_name,
                        user=username,
                        password=password,
                        host=host)


class Genre(Model):
    id = AutoField(unique=True)
    name = CharField(unique=True)
    path = CharField(unique=True)

    class Meta:
        database = db


class Track(Model):
    id = AutoField(unique=True)
    title = CharField()
    artist = CharField()
    genre = ForeignKeyField(Genre, backref='tracks')

    file_name = CharField(unique=True)
    file_path = CharField(unique=True)

    image_url = CharField()
    audio_url = CharField(unique=True)
    check_sum = CharField(unique=True)

    class Meta:
        database = db

