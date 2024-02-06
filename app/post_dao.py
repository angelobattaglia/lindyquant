import sqlite3

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
# The posts data structure
a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
posts = [
    {'id': 1, 'username': 'Luigi', 'date': '1 Giorni fa', 'text': a, 'immagine_post': 'img/pic1.png', 'id_utente': 1},
    {'id': 2, 'username': 'Alberto', 'date': '2 Giorni fa', 'text': a, 'immagine_post': 'img/pic2.png', 'id_utente': 2},
    {'id': 3, 'username': 'Juan', 'date': '3 Giorni fa', 'text': a, 'immagine_post': 'img/pic3.png', 'id_utente': 3}
]

def populate_posts_table(posts):
    # Connect to the SQLite database
    con = sqlite3.connect('datas.db')

    # Create a cursor object
    cur = con.cursor()

    # Clear the posts table
    # Clear Table Before Inserting: 
    # If it's acceptable for your use case (such as during initial setup or testing),
    # you could clear the posts table before inserting new posts. 
    # This ensures there are no duplicate id values but also removes all existing data from the table.
    cur.execute('DELETE FROM posts')

    # Iterate over the posts list
    for post in posts:
        # Insert each dictionary into the database
        cur.execute('''
            INSERT INTO posts (id, username, date, text, immagine_post, id_utente)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (post['id'],  post['username'], post['date'], post['text'], post['immagine_post'], post['id_utente'] ))

    # Commit the transaction
    con.commit()

    # Close the cursor and the connection
    cur.close()
    con.close()

# Call the function
populate_posts_table(posts)

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
# Retrieving all the posts
def get_all_posts():
    # Connect to the SQLite database
    con = sqlite3.connect('datas.db')

    # Set the row factory to sqlite3.Row for dictionary-like row objects
    con.row_factory = sqlite3.Row  

    # Create a cursor object
    cur = con.cursor()

    # Execute a SELECT query
    cur.execute('SELECT * FROM posts')

    # Fetch all the rows as dictionary objects
    # Ensure that row_objects is defined and used within the same scope
    row_objects = cur.fetchall()
    posts = [dict(row) for row in row_objects]  # Convert each row object to a dictionary

    # Close the cursor and the connection
    cur.close()
    con.close()

    return posts

    # # This method fetches all rows of the query result set and returns
    # # a list of rows as dictionary-like objects (due to the earlier row_factory setting).
    # # Each row in the list represents a post, along with the associated user information.
    # posts = cur.fetchall()

# ------------------------------------------------
# ------------------------------------------------
# ------------------------------------------------
# Retrieving all the posts
# input: post, which is expected to be a dictionary containing the data for the new post.
def add_post(post):
    # Connect to the SQLite database
    con = sqlite3.connect('datas.db')
    # The following line configures the connection to return rows as dictionary-like objects. 
    # This allows accessing the columns of each row by names, 
    # making the code more readable and maintainable.
    con.row_factory = sqlite3.Row
    # Create a cursor object
    cur = con.cursor()

    if 'immagine_post' in post:
        sql = 'INSERT INTO posts(data_pubblicazione,testo,immagine_post,id_utente) VALUES(?,?,?,?)'
        cur.execute(sql, (post['data_pubblicazione'],
                             post['testo'], post['immagine_post'], post['id_utente']))
        ### Insert the new post into the database
        ##cur.execute('''
            ##INSERT INTO posts (username, date, text, profile_img)
            ##VALUES (?, ?, ?, ?)
        ##''', (post['username'], post['date'], post['text'], post['profile_img']))
        ### # Alternatively, you can use the following code to insert the new post:
        ### sql = 'SELECT posts.id, posts.data_pubblicazione, posts.testo, posts.immagine_post, utenti.nickname, utenti.immagine_profilo FROM posts LEFT JOIN utenti ON posts.id_utente = utenti.id ORDER BY data_pubblicazione DESC'
        ### cursor.execute(sql)
    else:
        sql = 'INSERT INTO posts(data_pubblicazione,testo,id_utente) VALUES(?,?,?)'
        cur.execute(sql, (post['data_pubblicazione'],
                             post['testo'], post['id_utente']))

    # This method is focused on verifying that the changes are committed to the database,
    # hence, it's a good practice to structure an if-then-else statement to handle the commit.
    try: 
        con.commit()
        success = True
    # In case of exception, the code rolls back the transaction to the last commit point.
    except Exception as e:
        print('ERROR', str(e))
        con.rollback()

    # Close the cursor and the connection
    cur.close()
    con.close()

    return success
