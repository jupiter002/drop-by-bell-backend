
from fastapi import FastAPI
import uvicorn

import pymysql
from sqlalchemy import create_engine
app = FastAPI()

## 데이터베이스 연결
db_connection_str = 'mysql+pymysql://dev:nangok_devs@34.127.105.242/dropbybell'
db_connection = create_engine(db_connection_str)
conn=db_connection.connect()



@app.get("/")
def root():
    return {"Hello": "World"}
