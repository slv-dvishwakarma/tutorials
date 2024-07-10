## What is HTML Boilerplate

**An HTML boilerplate is a basic template that provides a starting point for creating an HTML document. It includes essential tags and structures needed for a standard web page. Here’s a typical HTML boilerplate with descriptions of each tag:**

```bash
HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

## Tag Descriptions:

1. `<!DOCTYPE html>`

    Declares the document type and version of HTML. This is necessary to ensure the browser renders the page in standards mode.

2. `<html lang="en">`

    The root element of an HTML document. The `lang` attribute specifies the language of the document (in this case, English).

3. `<head>`

    Contains meta-information about the document, such as its title, character set, and links to scripts and stylesheets.

4. `<meta charset="UTF-8">`

    Specifies the character encoding for the document, ensuring it displays characters correctly. `UTF-8` is a widely used encoding that supports many languages.

5. `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

    Sets the viewport to control how the webpage is displayed on different devices, especially mobile. It ensures the page scales properly across various screen sizes.

6. `<meta http-equiv="X-UA-Compatible" content="ie=edge">`

    Instructs Internet Explorer to use the latest rendering engine. It helps in maintaining compatibility and proper rendering in older versions of IE.

7. `<title>Document</title>`

    Sets the title of the webpage, which appears in the browser tab and is used by search engines. Replace "Document" with your desired page title.

8. `<body>`

    Contains the content of the HTML document, such as text, images, links, and other elements. This is where you add the visible parts of your webpage.

9. `<style>`

    Contains CSS styles to apply to the HTML document. It can be placed within the `<head>` element.

10. `<script>`

    Used to embed or reference JavaScript code within the document.

11. `<noscript>`

    Defines alternative content for users who have disabled scripts in their browser or have a browser that doesn’t support script.

By using this HTML boilerplate, you start with a well-structured and standard-compliant HTML document, ensuring compatibility and proper rendering across different browsers and devices.