    



The following is an alternative to post.html.. to display the post page

```html
<div class="row">
        <!--I have to replace the '' with the image inserted by the user-->
        <div class="col-md-6">
            <img src="{{ url_for('static', filename = post.immagine_post ) }}" class="img-fluid rounded" alt="Post Image">
        </div>

        <div class="col-lg-8 col-md-6">
            <article class="card">
                <div class="card-body">
                    {{ post.text }}
                    <div style="background-color: yellow; color: black; padding: 10px;">

                        <!-- Debugging -->
                        {% if post.immagine_post %}
                            Debug: post.immagine_post = {{ post.immagine_post }}
                        {% else %}
                            Debug: post.immagine_post is not set
                        {% endif %}
                    </div>
                </div>
            </article>
        </div>
```