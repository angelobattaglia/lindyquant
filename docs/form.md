# Forms in HTML with flask


## If the current user is authenticated ..

I put the following in the base.html, as I wrap the button "+" to share a post on the 
social network, so that this one pops up only if the user is logged in:

```html
{% if current_user.is_authenticated %}

<!--Code that involves the button to post-->

{% endif %}
```


## How the form actually passes the values to the @route

The dictionary post in the route is created by converting the form data into a dictionary using request.form.to_dict().
However, there are a few issues in the current implementation that might prevent the form data from
 being processed correctly by the route.


### Beware of..
- Field Names Mismatch: The form fields and the keys expected in the route handler do not match. For example, the form has a textarea with name="postContent" and an input field with name="postDate", but in the route, you are trying to access these values with post['text'] and post['date'] respectively. You should change these to match the form's name attributes, like post['postContent'] and post['postDate'].

- Image Field Name Mismatch: Similarly, the file input for the image has name="postImage", but in the route, you are trying to access it with request.files['immagine_post']. This should be changed to request.files['postImage'] to match the form