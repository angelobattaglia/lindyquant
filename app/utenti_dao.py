import sqlite3

def get_user_by_id(id):
    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM utenti WHERE id = ?'
    cursor.execute(sql, (id,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_nickname(nickname):
    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT * FROM utenti WHERE nickname = ?'
    cursor.execute(sql, (nickname,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_users():
    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = 'SELECT id, nickname FROM utenti'
    cursor.execute(sql)
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def add_user(user):

    conn = sqlite3.connect('datas.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    success = False
    sql = 'INSERT INTO utenti(nickname,password,immagine_profilo) VALUES(?,?,?)'

    try:
        cursor.execute(
            sql, (user['nickname'], user['password'], user['immagine_profilo']))
        conn.commit()
        success = True
    except Exception as e:
        print('ERROR', str(e))
        # if something goes wrong: rollback
        conn.rollback()

    cursor.close()
    conn.close()

# def create_table_and_insert_data():
    # with sqlite3.connect('datas.db') as con:
        # cur = con.cursor()

        # # cur.execute('''
            # # CREATE TABLE IF NOT EXISTS posts (
                # # id INTEGER PRIMARY KEY,
                # # username TEXT NOT NULL,
                # # data DATE NOT NULL,
                # # text TEXT NOT NULL
            # # );
        # # ''')

        # # To avoid SQL injections: the values are supplied as a tuple (data), 
        # # and they are securely inserted into the query using placeholders (?)
        # data = (2, 'Luigi', '2023-12-08', 'Lorem ipsum')
        # cur.execute('''
            # INSERT INTO posts (id, username, data, text) 
            # VALUES (?, ?, ?, ?)
        # ''', data)

        # con.commit()

# # ------------------------------------------------
# # ------------------------------------------------
# # ------------------------------------------------
# # The utenti data structure
# utenti = [
    # {'id': 1, 'nickname': 'Luigi', 'password': 'pass1', 'immagine_profilo': 'img/pic1.png'},
    # {'id': 2, 'nickname': 'Alberto', 'password': 'pass2', 'immagine_profilo': 'img/pic2.png'},
    # {'id': 3, 'nickname': 'Juan', 'password': 'pass3', 'immagine_profilo': 'img/pic3.png'}
# ]

# def populate_utenti_table(utenti):
    # # Connect to the SQLite database
    # con = sqlite3.connect('datas.db')

    # # Create a cursor object
    # cur = con.cursor()

    # # Iterate over the posts list
    # for utente in utenti:
        # # Insert each dictionary into the database
        # cur.execute('''
            # INSERT INTO utenti (id, nickname, password, immagine_profilo)
            # VALUES (?, ?, ?, ?)
        # ''', (utente['id'], utente['nickname'], utente['password'], utente['immagine_profilo']))

    # # Commit the transaction
    # con.commit()

    # # Close the cursor and the connection
    # cur.close()
    # con.close()

# # Call the function
# populate_utenti_table(utenti)