# Note: it is important to add "render_template" to the imports
from flask import Flask, render_template
from flask import Flask, render_template, request
from forms import LoginForm
from flask import redirect, url_for, flash

# Import the Image module from the PIL (Python Imaging Library) package. 
# Used to preprocess the images uploaded by the users. 
# Ensure 'Pillow' is installed before running the application by using
# the command 'pip install Pillow'
from PIL import Image

# Import the datetime library to handle the pubblication date of the posts
import datetime

# importing get_all_posts() from post_dao.py, using it in home()
from post_dao import get_all_posts
from post_dao import add_post
# from post_dao import populate_posts_table

# import sqlite3
# import post_dao

PROFILE_IMG_HEIGHT = 130
POST_IMG_WIDTH = 300

# create the application
app = Flask(__name__)

# app.run(host='-11.0.0.0',port=12345)

# Routes and web pages
@app.route('/')
def home():
    posts = []
    posts = get_all_posts()
    return render_template('home.html', posts = posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Dynamic routing
@app.route('/post/<int:post_id>')
def post(post_id):
    posts = []
    posts = get_all_posts()
    post = posts[post_id-1]
    return render_template('post.html', post = post, title='Post')

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    post = request.form.to_dict()

    # If the post is either empty, with a wrong date or with a date
    # corresponding to a day that has already passed, you get redirected to
    # the home page and an error message is logged
    if post['testo'] == '':
        app.logger.error('Il post non può essere vuoto!')
        return redirect(url_for('home'))
    if post['data_pubblicazione'] == '':
        app.logger.error('Devi selezionare una data')
        return redirect(url_for('home'))
    if datetime.strptime(post['data_pubblicazione'], '%Y-%m-%d').date() < date.today():
        app.logger.error('Data errata')
        return redirect(url_for('home'))

    #
    #
    #
    comment_image = request.files['immagine_commento']
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
        secondi = int(datetime.now().timestamp())       

        # Saving the image with a unique filename in the 'static' directory
        img.save('static/@comment-' + str(secondi) + '.' + ext)

        # Updating the 'immagine_commento' field in the comment dictionary with the image filename
        comment['immagine_commento'] = '@comment-' + str(secondi) + '.' + ext
    else:
        comment['immagine_commento'] = None

    comment['id_post'] = int(comment['id_post'])
    comment['id_utente'] = int(current_user.id)
    comment['valutazione'] = int(comment['radioOptions'])

    if 'isAnonymous' in comment and comment['isAnonymous'] == 'on':
        comment['id_utente'] = None
    else:
        comment['id_utente'] = int(comment['id_utente'])
           
    success = commenti_dao.add_comment(comment)

    if success:
        app.logger.info('Commento creato correttamente')
    else:
        app.logger.error('Errore nella creazione del commento: riprova!')
            
    return redirect(url_for('single_post', id=comment['id_post']))

    ## if request.method == 'POST':
        ## # Access the data submitted in the form
        ## username = request.form.get('username')
        ## date = request.form.get('date')
        ## text = request.form.get('text')
        ## immagine_profilo = request.form.get('immagine_post')

        ## # Create a new post
        ## post = {'username': username, 'date': date, 'text': text, 'immagine_post': immagine_post}

        ## # Add the new post to the database
        ## add_post(post)

        ## # Redirect to the single post page
        ## return redirect(url_for('post', post_id=post['id']))

    ## # Render the form
    ## return render_template('new_post.html')

# Authentication
app.config['SECRET_KEY'] = 'gematria'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  # Query user from database
        if user and user.check_password(form.password.data):  # Verify password
            # User authentication successful, proceed with login
            login_user(user)  # Flask-Login function to log in the user
            return redirect(url_for('dashboard'))  # Redirect to a protected page, e.g., dashboard
        else:
            flash('Invalid username or password')  # Show error message

    return render_template('login.html', title='Login', form=form)
