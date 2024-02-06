# Forms in HTML with flask


## If the current user is authenticated ..

I put the following in the base.html, as I wrap the button "+" to share a post on the 
social network, so that this one pops up only if the user is logged in:

```html
{% if current_user.is_authenticated %}

<!--Code that involves the button to post-->

{% endif %}
```

