# Python database connector

## Requirement
- python
- pip 

## Install virtual environment 

```
pip3 install virtualenv
virtualenv envs
source envs/bin/activate
```

## PostgreSQL connector
1. Install Postgress on computer here: https://www.postgresql.org/download/

2. Install psycopg2 
```
pip install psycopg2
```

3. Create `connection_config.py` file follow structure of `connection_config_example.py`

4. Import `connect` function in `posgresql_connector.py` file and excute query
```
import posgresql.postgresql_connector as posgres_connector

db_connection = posgres_connector.connect()

# create a cursor
cur = db_connection.cursor()
    
query = "SELECT * FROM tbatoolnewstype ORDER BY id DESC"
# fetch all
cur.execute(query)
records = cur.fetchall()
print(records)

# fetch one 
cur.execute(query)
records = cur.fetchone()
print(records)

# fetch many 
cur.execute(query)
records = cur.fetchmany(3)
print(len(records))
print(records)

# fetch with param 
query = "SELECT * FROM tbatoolnewstype WHERE id = %s ORDER BY id DESC"
cur.execute(query,("2"))
records = cur.fetchall()
print(records)

# insert data
query = """
INSERT INTO tbatoolnewstype(createddate, createduser, lastmodifieddate, lastmodifieduser, "type", childtype, childtypenameinvn, typenameinvn) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
        """
cur.execute(query,("2022-10-23", "test", "2022-10-23", "test", "TEST","INTERNAL_TRANSACTIONS","Giao dịch nội bộ","Thông tin công bố" ))
db_connection.commit()
```
