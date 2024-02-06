## Bootstrap

Using Bootstrap 5.3.x (latest version as of yet)
- [Introduction - Official Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

**Using through the CDN
**Delete the old references to the local CSS

### Where to place the CDN link
Put the CDN link into the <head> tag

1. Add the "Viewport" tag as name
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

2. Then, we add javascript through "deferred script placement/loading", i. e. at the end of the .html entry point. Adding Javascript adds animations and components that could not be made without it using CSS alone.
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
```
just before the closing </body> tag.

### Modal: interactive pop-up


