# create connection syntax
# conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

import psycopg2
from posgresql.connection_config import *

def connect():
    """ Connect to the PostgreSQL database server """
    db_connection = None
    try:
        db_connection = psycopg2.connect(
            host=connection_host,
            port=connection_port,
            database=connection_database,
            user=connection_user,
            password=connection_password)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if db_connection is not None:
            print('Database connect successfully.')
            return db_connection
        else:
            print("Database connect error")
            exit()
            
