from fastapi import APIRouter, Depends
from pydantic import BaseModel
import sqlalchemy
from src import database as db
from urllib.parse import unquote



router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)

@router.get("/{name}")
def say_hi(name: str):
    """ """
    print(name)

    with db.engine.begin() as connection:
        sql = f"SELECT greeting FROM characters WHERE character_name = '{unquote(name)}'"
        print(f"sql executed: {sql}")
        results = connection.execute(sqlalchemy.text(sql))
        for row in results:
            return {"message": row[0]}
    return {"message": "Character not found"}
