# Comments

This code snippet appears to be a Python function using the Flask web framework. Let's break it down step by step:

1. `@app.route('/comments/new', methods=['POST'])`: This is a decorator that associates the function `new_comment()` 
with the specified URL route `/comments/new` and HTTP method `POST`. It means that this function will handle POST 
requests sent to the `/comments/new` endpoint of your Flask application.

2. `@login_required`: This is another decorator, presumably from Flask-Login extension, which ensures that the user must be logged in to access the `new_comment()` function. If the user is not logged in, Flask-Login will redirect them to the login page before executing the `new_comment()` function.

3. `def new_comment():`: This is the definition of the `new_comment()` function, which will handle the POST requests to create a new comment.

4. `comment = request.form.to_dict()`: This line retrieves the form data submitted with the POST request and converts it into a dictionary named `comment`.

5. The subsequent code validates and processes the comment data. It checks if the comment text is empty, and if an image is included in the request. If an image is present, it resizes and saves it with a unique filename in the `static` directory.

6. Various fields of the comment dictionary are modified or added, such as `id_post`, `id_utente` (user ID), and `Valutazione` (evaluation).

7. If the comment is marked as anonymous (`isAnonymous` field checked), the user ID is set to None.

8. The `comment` dictionary is passed to a function called `add_comment()` presumably defined in a `commenti_dao` module, which likely handles database operations related to comments. The success of adding the comment to the database is stored in the `success` variable.

9. Based on the success of adding the comment to the database, appropriate log messages are generated.

10. Finally, the function redirects the user to the page displaying the post associated with the newly added comment (`single_post` route), passing the ID of the post as a parameter.

In summary, this function handles the submission of a new comment via a form, processes the data, including any uploaded image, and adds the comment to the database. It also logs appropriate messages and redirects the user back to the post page after the comment is added.