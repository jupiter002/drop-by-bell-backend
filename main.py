
from fastapi import FastAPI
import uvicorn

import pymysql
from sqlalchemy import create_engine
app = FastAPI()

db_connection_str = 'mysql+pymysql://dev:nangok_devs@34.127.105.242/memberInfo'
db_connection = create_engine(db_connection_str)
conn=db_connection.connect()



@app.get("/")
def root():
    return {"Hello": "World"}
