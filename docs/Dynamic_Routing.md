# Dyamic Routing

Dynamic Routing in Flask. One template page for multiple objects


Let's suppose we have the following directory structure
```md
|app/
|--- app.py
|--- templates/
|---|--- base.html
|---|--- home.html
|---|--- post.html
|
```

## In app.py

In app.py, we add the dynamic route, as define by the script
```python
@app.route('/post/<int:post_id>')
def post(post_id):
    # indexing in python starts from 0
    post = posts[post_id-1]
    return render_template('post.html', post = post, title='Post')
```

int is the type, and post_id is the name of the variable in the scope of the method "post"
```python
<int:post_id>
```

The "post_id" parameter is part of the URL pattern in the route definition.

Note how "post" the variable defined within the scope of the function gets passed by value into
the "render_template" function as a return parameter.

## In the templates

In post.html:

1. post.html is the end-point of the dynamic route just defined.
2. Note how "post", the value passed onto render_template, is a dictionary.
3. post.username represents the field "username" within the dictionary "post".