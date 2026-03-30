import psycopg2
from config import db_config


def connect_db():
    conn = psycopg2.connect(**db_config)
    return conn