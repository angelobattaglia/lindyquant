# Jinja

Jinja is a template engine used by Flask.

## How to use images in Jinja templating

To add images to Jinja templates in Flask, you can use the `url_for` function to generate the correct URL for the image file. Here's a basic example:

Assuming you have a Flask application structure like this:

```plaintext
/myapp
    /static
        /images
            example.jpg
    /templates
        index.html
    app.py
```

In this example, the image file `example.jpg` is stored in the `static/images` directory.

Now, let's create a simple Flask application (`app.py`):

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

```

And the corresponding Jinja template (`index.html`) in the `templates` directory:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Image Example</title>
</head>
<body>
    <h1>Image Example</h1>
    
    <!-- Using url_for to generate the image URL -->
    <img src="{{ url_for('static', filename='images/example.jpg') }}" alt="Example Image">

</body>
</html>
```

In this example:

- The `url_for('static', filename='images/example.jpg')` generates the correct URL for the image file. The `'static'` argument is the endpoint name for the static route, and the `'images/example.jpg'` is the relative path to the image file from the `static` directory.

- Make sure to use the `url_for` function within the `src` attribute of the `img` tag to correctly generate the URL.

- You can replace `'images/example.jpg'` with the actual path to your image file.

Remember that the `static` directory is a special directory in Flask where you should store your static assets like images, stylesheets, and JavaScript files. The `url_for('static', ...)` call ensures that the correct URL is generated, regardless of your application's deployment configuration.


### How to pass a dictionary from a route to a template in jinja

In Jinja templates, the ability to access a variable like `{{ post.nickname }}` from anywhere within the template depends on the context in which the template is rendered. When you render a template using a Flask view function, for example, you pass a context that contains the variables accessible in the template.

If you've passed the `post` object to the template context, you should be able to access `{{ post.nickname }}` from anywhere within that template. Here's a basic example of how you might pass the `post` object to a template in a Flask view function:

```python
from flask import render_template

@app.route('/some-route')
def some_view_function():
    post = posts_dao.get_post_from_database()  # Hypothetical function to fetch a post, located in the script post_dao.py
    return render_template('your_template.html', post=post)
```

In the template `your_template.html`, you can then access `{{ post.nickname }}`:

```html
<div>{{ post.nickname }}</div>
```

However, if you're working with template inheritance in Flask using the `{% extends %}` and `{% block %}` tags, you need to ensure that the `post` variable is accessible in the context of the templates that inherit from the base template. If `post` is defined in a base template or passed in the view function rendering the child template, it will be accessible in child templates as well.

For example, if `base.html` passes `post`, and `child.html` extends `base.html`, `child.html` can access `{{ post.nickname }}` as long as `post` is in the context:

**base.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Base Template</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

**child.html:**
```html
{% extends "base.html" %}

{% block content %}
    <!-- Accessing post.nickname here is possible if 'post' is in the context -->
    <div>{{ post.nickname }}</div>
{% endblock %}
```

If you find that `{{ post.nickname }}` is not accessible in some parts of your template, you should check the context being passed to your template and ensure that the `post` object is included in it.


Jinja templates: In Python, `None` is used to denote the absence of a value, but when you pass variables to a Jinja template, `None` is not converted to the string `"None"`. Instead, you should directly check if `comment.Valutazione` is `None` or not in your Jinja template, without using quotes around `None`.

Here's how you can do it:

```jinja
{% if comment.Valutazione is none %}
    Il commento è privo di valutazione
{% else %}
    Ecco la valutazione dell'utente: {{ comment.Valutazione }}
{% endif %}
```

In this snippet:

- `{% if comment.Valutazione is none %}` checks if `comment.Valutazione` is `None`. Note the absence of quotes around `none`. In Jinja, `none` is the equivalent of Python's `None`.
- If `comment.Valutazione` is `None`, it displays the message "Il commento è privo di valutazione".
- If `comment.Valutazione` has a value, it displays "Ecco la valutazione dell'utente:" followed by the value of `comment.Valutazione`.

This approach ensures that your template correctly handles cases where `comment.Valutazione` is `None`, displaying an appropriate message to indicate the absence of a rating.