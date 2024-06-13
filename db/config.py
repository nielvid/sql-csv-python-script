import os
from dotenv import load_dotenv
# import mysql.connector
from sqlalchemy import create_engine

load_dotenv()



db_username: str = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT",3306)  # default mysql port
db = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{db_username}:{db_password}@{host}/{db}"
# db_config = {
#     'user': db_username,
#     'password': db_password,
#     'host': host,
#     'database': db
# }

# Connect to the MySQL database
# connection = mysql.connector.connect(**db_config)

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)
# Establish connection
connection = engine.connect()

