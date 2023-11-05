import os
import dotenv
from sqlalchemy import create_engine
from collections import defaultdict

def database_connection_url():
    dotenv.load_dotenv()

    return os.environ.get("POSTGRES_URI")

engine = create_engine(database_connection_url(), pool_pre_ping=True)
print("created database connection engine")

order_id = 0
orders = defaultdict(lambda: defaultdict(int))
