from fastapi import APIRouter, Depends
from pydantic import BaseModel
import sqlalchemy
from src import database as db

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
)

@router.get("/{name}")
def post_deliver_barrels(name: str):
    """ """
    print(name)
        
    with db.engine.begin() as connection:
        results = connection.execute(sqlalchemy.text(f"SELECT greeting FROM characters WHERE name = {name}"))
