# create connection syntax
# conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")



conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Abcd1234")