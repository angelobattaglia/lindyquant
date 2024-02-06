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

