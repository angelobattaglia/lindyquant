# Login: flask-wtf

To add a login form to your Flask application, you can use Flask-WTF, which is a simple wrapper for WTForms. Here's how you can do it:

1. Install Flask-WTF by running `pip install flask-wtf` in your terminal.

2. Create a form class in a new Python file, `forms.py`:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
```

3. Import the `LoginForm` in your `app.py` file and create a new route for the login page:

```python
from flask import Flask, render_template, request
from forms import LoginForm

# ... rest of your code ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Add your login logic here
        pass
    return render_template('login.html', title='Login', form=form)
```

4. Create a new template `login.html` in your templates folder:


- This template utilizes Flask-WTF, a Flask extension that integrates WTForms for handling forms, to render and process the form securely and conveniently. WTF forms typically refer to "WTForms," which is a flexible forms validation and rendering library for Python web development. They provide built-in validation functions, which can be extended with custom validation rules if necessary. This helps in ensuring that the data collected through forms is clean and secure before being processed or stored in a database.

```html
{% extends "layout.html" %}

{% block content %}
  <h2>Login</h2>
  <form method="POST">
    {{ form.hidden_tag() }}
    <p>
      {{ form.username.label }}<br>
      {{ form.username(size=32) }}
    </p>
    <p>
      {{ form.password.label }}<br>
      {{ form.password(size=32) }}
    </p>
    <p>{{ form.submit() }}</p>
  </form>
{% endblock %}
```

It extends a base template (base.html) to inherit common structures or elements. The block content section is where unique content for this template is defined, in this case, a login form.

- {% extends "base.html" %}: Inherits from a base template, allowing this template to include common elements defined in base.html.
- {% block content %} and {% endblock %}: Defines a section where page-specific content is placed. Anything within these tags will replace the corresponding block in the base template.
- <h2>Login</h2>: Displays a heading with the text "Login".
- <form method="POST">: Defines a form that sends data to the server using the POST method.
- {{ form.hidden_tag() }}: Renders hidden form fields, including a Cross-Site Request Forgery (CSRF) protection token.
- {{ form.username.label }} and {{ form.password.label }}: Display the labels for the username and password fields.
- {{ form.username(size=32) }} and {{ form.password(size=32) }}: Render input fields for username and password, with a specified size.
- {{ form.submit() }}: Renders a submit button for the form.

Now, when you navigate to `/login` in your web browser, you should see a login form. When you submit the form, it will validate the input and if it's valid, it will execute the code in the `if form.validate_on_submit():` block. You can add your login logic there.


# Decorators in Python
Basics: A decorator in Python is essentially a function that takes another function as an argument, adds some kind of functionality, and returns another function without altering the source function's code. Decorators are denoted by the @ symbol and are placed above a function definition.