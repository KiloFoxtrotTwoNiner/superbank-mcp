import sqlite3

def connect():
    try:
        sqliteConnection = sqlite3.connect('bank.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print('Error occurred -', error)
        return None

def disconnect(sqliteConnection):
    try:
        if sqliteConnection:
            sqliteConnection.close()
    except sqlite3.Error as error:
        print('Error occurred -', error)

def execute(conn, query):
    conn.cursor().execute(query)
    conn.commit()
    conn.cursor().close()

def db_config():
    create_partner = """
    CREATE TABLE IF NOT EXISTS PARTNER(
        Partner_Id INTEGER PRIMARY KEY AUTOINCREMENT,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(45) NOT NULL,
        Email VARCHAR(255) NOT NULL
    );
    """
    create_account = """
    CREATE TABLE IF NOT EXISTS ACCOUNT(
        Account_Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Partner_Id INT NOT NULL,
        Balance REAL NOT NULL,
        Currency CHAR(3) NOT NULL,
        FOREIGN KEY(Partner_Id) REFERENCES PARTNER(Partner_Id)
    );
    """
    conn = connect()
    execute(conn, create_partner)
    execute(conn, create_account)
    disconnect(conn)

def get_partners():
    result = []
    query = """
    SELECT * FROM PARTNER;
    """

    # conn = connect()
    # execute(conn, query)
    # for row in conn.cursor().fetchall():
    #     result.append(row)
    # disconnect(conn)

    conn = connect()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        disconnect(conn)

    if len(result) == 0:
        return "Table is empty"
    else:
        return result 
    

def create_partner(first_name, last_name, email):
    result = []
    query = f"""
    INSERT INTO PARTNER (First_Name, Last_Name, Email) VALUES ('{first_name}', '{last_name}', '{email}');
    """ 
    conn = connect()
    execute(conn, query)
    disconnect(conn)

    return "Partner added successfully"