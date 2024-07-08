# Note: it is important to add "render_template" to the imports
from flask import Flask, render_template
from flask import Flask, render_template, request
from flask import redirect, url_for, flash, abort

# Flask-Login is a Flask extension that provides a framework for handling user authentication
import flask_login
from flask_login import LoginManager
from flask_login import login_required
# Logs a user in. We should pass the actual user object to this method:
# returns True if the log in attempt succeeds, and False if it fails
from flask_login import login_user

# Security and Forms for the login
import werkzeug.security as ws
from forms import LoginForm

# Import the Image module from the PIL (Python Imaging Library) package. 
# Used to preprocess the images uploaded by the users. 
# Ensure 'Pillow' is installed before running the application by using
# the command 'pip install Pillow'
from PIL import Image

# Import the datetime library to handle the pubblication date of the posts
import datetime

## Import the dao modules and the models module
# importing get_all_posts() from post_dao.py, using it in home()
import post_dao
from post_dao import get_all_posts
from post_dao import add_post
# from post_dao import populate_posts_table
import models
import utenti_dao
import commenti_dao
from commenti_dao import add_comment
from commenti_dao import get_comments

PROFILE_IMG_HEIGHT = 130
POST_IMG_WIDTH = 300

# create the application
app = Flask(__name__)
    

app.config['SECRET_KEY'] = 'gematria'

# This is for login_manager 
login_manager = LoginManager()
login_manager.init_app(app)

# Routes and web pages
@app.route('/')
def home():
    posts = []
    users = []
    posts = post_dao.get_all_posts()
    users = utenti_dao.get_users()

    # I'll create a new dictionary to pass into the home.html to jinja templates
    posts_new = []
    for post in posts:
        for user in users:
            if post['id_utente'] == user['id']:
                # In this revised code, user['immagine_profilo'] directly accesses the value
                # of the immagine_profilo column in the user sqlite3.Row. If this value is
                # None or an empty string (which you can check with if user['immagine_profilo']),
                # the code falls back to a default image path. The same logic applies to post['immagine_post'].
                #
                # Directly access 'immagine_profilo' from user, set a default if it's None or empty
                post['immagine_profilo'] = user['immagine_profilo'] if user['immagine_profilo'] else 'path/to/default/profile/image.jpg'
                # Assume 'immagine_post' is always present in post; set a default if it's None or empty
                post['immagine_post'] = post['immagine_post'] if post['immagine_post'] else 'path/to/default/post/image.jpg'
                posts_new.append(post)
                break
                # # # The following two solutions are wrong
                # # Set default image if 'immagine_profilo' is missing or empty
                # post['immagine_profilo'] = user.get('immagine_profilo') or 'static/img/pic1.png'
                # # Set default image if 'immagine_post' is missing or empty
                # post['immagine_post'] = post.get('immagine_post') or 'static/img/pic1.png'
                # posts_new.append(post)
                # break
                # The following alternative does not work if there's no profile image given or image post given
                # post['immagine_profilo'] = user['immagine_profilo']
                # posts_new.append(post)
                # # if I find the user, I can break the loop
                # break

    return render_template('home.html', posts_new = posts_new, title='Home')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Dynamic routing
@app.route('/post/<int:post_id>')
def post(post_id):
    posts = []
    posts = get_all_posts()
    
    # Check if the provided post_id is within the valid range
    if post_id < 1 or post_id > len(posts):
        abort(404)  # Post not found, return a 404 error

    post = posts[post_id-1]

    # I also have to pass it the user to whom the post belongs, 
    # each post has a user_id field, so I use post_dao's get_user_by_id method ..
    usr = utenti_dao.get_user_by_id(post['id_utente'])

    # Comments for the post with post_id equal to the one passed in the URL
    comments = commenti_dao.get_comments(post_id)

    return render_template('post.html', post = post, usr = usr, comments = comments, title='Post')

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    post = request.form.to_dict()

    # I make some checks and analysis on the post dictionary

    # If the post is either empty, with a wrong date or with a date
    # corresponding to a day that has already passed, you get redirected to
    # the home page and an error message is logged
    if post['text'] == '':
        app.logger.error('Il post non può essere vuoto!')
        return redirect(url_for('home'))

    if post['date'] == '':
        app.logger.error('Devi selezionare una data')
        return redirect(url_for('home'))

    if datetime.datetime.strptime(post['date'], '%Y-%m-%d').date() < datetime.date.today():
        app.logger.error('Data errata')
        return redirect(url_for('home'))

    post_image = request.files['immagine_post']
    if post_image:

        # Open the user-provided image using the Image module
        img = Image.open(post_image)

        # Get the width and height of the image
        width, height = img.size

        # Calculate the new height while maintaining the aspect ratio based on the desired width
        new_height = height/width * POST_IMG_WIDTH

        # Define the size for thumbnail creation with the desired width and calculated height
        size = POST_IMG_WIDTH, new_height
        img.thumbnail(size, Image.Resampling.LANCZOS)

        # Extracting file extension from the image filename
        ext = post_image.filename.split('.')[-1]
        # Getting the current timestamp in seconds
        secondi = int(datetime.datetime.now().timestamp())       

        # Saving the image with a unique filename in the 'static' directory
        img.save('static/@' + flask_login.current_user.nickname.lower() + '-' + str(secondi) + '.' + ext)

        # Updating the 'immagine_post' field in the post dictionary with the image filename
        post['immagine_post'] = '@' + flask_login.current_user.nickname.lower() + '-' + str(secondi) + '.' + ext

    # flask_login.current_user.id is the id of the current user
    post['id_utente'] = int(flask_login.current_user.id)  
    post['nickname'] = str(flask_login.current_user.nickname)

    # After finishing making the checks, I put the "post" dictionary in the database
    success = post_dao.add_post(post)

    if success:
        app.logger.info('Post creato correttamente')
    else:
        app.logger.error('Errore nella creazione del post: riprova!')

    return redirect(url_for('home'))

# Defining the comment endpoint
@app.route('/comments/new', methods=['POST'])
@login_required
def new_comment():

    comment = request.form.to_dict()

    # If the comment is empty, you get redirected to the home page and an error message is logged
    if comment['testo'] == '':
        app.logger.error('Il commento non può essere vuoto!')
        return redirect(url_for('single_post', id=comment['id_post']))
    
    comment_image = request.files['immagine_commento']

    # comment_image = request.files['immagine_commento']
    if comment_image:
        # Open the user-provided image using the Image module
        img = Image.open(comment_image)

        # Get the width and height of the image
        width, height = img.size

        # Calculate the new height while maintaining the aspect ratio based on the desired width
        new_height = height/width * POST_IMG_WIDTH

        # Define the size for thumbnail creation with the desired width and calculated height
        size = POST_IMG_WIDTH, new_height
        img.thumbnail(size, Image.Resampling.LANCZOS)

        # Extracting file extension from the image filename
        ext = comment_image.filename.split('.')[-1]
        # Getting the current timestamp in seconds
        secondi = int(datetime.datetime.now().timestamp())       

        # Saving the image with a unique filename in the 'static' directory
        img.save('static/@comment-' + str(secondi) + '.' + ext)

        # Updating the 'immagine_commento' field in the comment dictionary with the image filename
        comment['immagine_commento'] = '@comment-' + str(secondi) + '.' + ext
    else:
        comment['immagine_commento'] = None

    comment['id_post'] = int(comment['id_post'])
    comment['id_utente'] = int(flask_login.current_user.id)

    # radioOptions is the name of the input field for the radio buttons in the comment form
    if comment['radioOptions'] == '0':
        comment['Valutazione'] = None
    else:
        comment['Valutazione'] = int(comment['radioOptions'])

    if 'isAnonymous' in comment and comment['isAnonymous'] == 'on':
        comment['id_utente'] = None
    else:
        comment['id_utente'] = int(comment['id_utente'])

    success = commenti_dao.add_comment(comment)

    if success:
        app.logger.info('Commento creato correttamente')
    else:
        app.logger.error('Errore nella creazione del commento: riprova!')
            
    # I pass the id of the post to which the comment belongs to the post page
    return redirect(url_for('post', post_id=comment['id_post']))

# Define the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup_function():

    # I take from the form the input datas and import them locally as a dictionary
    nuovo_utente_form = request.form.to_dict()

    # I try to retrieve the unique username of the nuovo_utente_form from the db ..
    user_in_db = utenti_dao.get_user_by_nickname(nuovo_utente_form.get('nickname'))

    # ... and I check weather it has already been registered ..
    if user_in_db:
        flash('There\'s already a user with these credentials', 'danger')
        return redirect(url_for('signup'))
    # .. and if it hasn't been registered ..
    else:
        img_profilo = ''
        usr_image = request.files['immagine_profilo']
        if usr_image:
            # Open the user-provided image using the Image module
            img = Image.open(usr_image)

            # Get the width and height of the image
            width, height = img.size

            # Calculate the new width while maintaining the aspect ratio
            new_width = PROFILE_IMG_HEIGHT * width / height

            # Define the size for thumbnail creation with the desired height and calculated width
            size = new_width, PROFILE_IMG_HEIGHT
            img.thumbnail(size, Image.Resampling.LANCZOS)

            # Calculate the coordinates for cropping the image to a square shape
            left = (new_width/2 - PROFILE_IMG_HEIGHT/2)
            top = 0
            right = (new_width/2 + PROFILE_IMG_HEIGHT/2)
            bottom = PROFILE_IMG_HEIGHT

            # Crop the image using the calculated coordinates to create a square image
            img = img.crop((left, top, right, bottom))

            # Extracting file extension from the image filename
            ext = usr_image.filename.split('.')[-1]

            # Saving the image with a unique filename in the 'static' directory
            img.save('static/' + nuovo_utente_form.get('nickname').lower() + '.' + ext)

            img_profilo = nuovo_utente_form.get('nickname').lower() + '.' + ext

        # I generate an hash for the password that has been inserted by the form input
        nuovo_utente_form['password'] = ws.generate_password_hash(nuovo_utente_form.get('password'))

        # Updating the 'immagine_profilo' field in the user dictionary with the image filename
        nuovo_utente_form['immagine_profilo'] = img_profilo

        # I add the user to the db using the method "add_user" from the utenti_dao.py
        success = utenti_dao.add_user(nuovo_utente_form)

        if success:
            flash('Utente creato correttamente', 'success')
            return redirect(url_for('home'))
        else:
            flash('Errore nella creazione del utente: riprova!', 'danger')
            return redirect(url_for('signup'))

@login_manager.user_loader
def load_user(user_id):
    db_user = utenti_dao.get_user_by_id(user_id)
    if db_user is not None:
        user = models.User(id=db_user['id'], 
                           nickname=db_user['nickname'],	
                           password=db_user['password'], 
                           immagine_profilo=db_user['immagine_profilo'])
    else:
        user = None
    return user

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():

    # Retrieving the informations from the form @ /login
    utente_form = request.form.to_dict()
    # Using the "get_user_by_nickname" method from utenti.dao, which
    # retrieves the user from the database with the given nickname passed
    # from the form in /login
    utente_db = utenti_dao.get_user_by_nickname(utente_form['nickname'])

    # If there's no utente_db in the database (meaning the user just doesn't exist into the db)
    # or if the password given as input in the form /login isn't equal to the one in the database
    if not utente_db or not ws.check_password_hash(utente_db['password'], utente_form['password']):
        flash('Credenziali non valide, riprova', 'danger')
        return redirect(url_for('home'))
    else:
    # if, instead, it exists, we create a new user instance using the "User model" defined in models.py
        # Create a new user instance called "new"
        new = models.User(id=utente_db['id'], 
                          nickname=utente_db['nickname'], 
                          password=utente_db['password'], 
                          immagine_profilo=utente_db['immagine_profilo'] )
        # We log in said user called "new"
        flask_login.login_user(new, True)
        flash('Bentornato ' + utente_db['nickname'] + '!', 'success')
        return redirect(url_for('home'))

# Log out route
@app.route("/logout")
@login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

# # define the 'about' page
# @app.route('/about')
# def about():
    # p_developers = [
        # {'id': 1234, 'name': 'Luigi De Russis', 'devimg': 'user.jpg',
            # 'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'First quote author'},
        # {'id': 5678, 'name': 'Alberto Monge Roffarello', 'devimg': 'user.jpg',
            # 'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'Second quote author'},
        # {'id': 9012, 'name': 'Juan Pablo Sáenz', 'devimg': 'user.jpg',
            # 'quote': 'A well-known quote, contained in a blockquote element', 'quoteAuthor': 'Third quote author'}
    # ]
    # return render_template('about.html', developers=p_developers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
