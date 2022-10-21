import posgresql.postgresql_connector as posgres_connector

if __name__ == '__main__':
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
    INSERT INTO tbatoolnewstype
            (createddate, createduser, lastmodifieddate, lastmodifieduser, "type", childtype, childtypenameinvn, typenameinvn)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
            """
    cur.execute(query,("2022-10-23", "test", "2022-10-23", "test", "TEST","INTERNAL_TRANSACTIONS","Giao dịch nội bộ","Thông tin công bố" ))
    db_connection.commit()
