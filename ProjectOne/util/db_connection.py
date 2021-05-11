import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            database='postgres',
            user='charles',
            password='passwordnotnothe',
            host='charles432postgres.cflalptztkhk.us-east-2.rds.amazonaws.com',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn

connection = create_connection()