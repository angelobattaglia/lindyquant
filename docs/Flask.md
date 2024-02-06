# Flask


## Explanations of the functions used in the project

- url_for: when you use the url_for function to generate URLs, you provide the endpoint name, not the actual URL. This makes it easier to maintain your code because if you change the URL pattern for a specific functionality, you only need to update the endpoint name, and all the url_for calls will automatically generate the correct URLs linking together two templates, and routing
```python
{{ url_for('endpoint') }}
```

- render_template: needs to be imported into the project itself, self explicative, and it renders the templates in the /templates directory
```python
render_template('about.html', title='About Us', content='Learn more about LindyQuant!')
```
