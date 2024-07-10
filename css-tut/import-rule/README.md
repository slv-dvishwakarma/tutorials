## @import Rule

The `@import` rule is used to import one style sheet into another. It allows you to modularize your CSS and manage dependencies.

**Syntax:**

```bash
@import url("styles.css");
```

**Example:**

```bash
@import url("https://fonts.googleapis.com/css?family=Roboto");
body {
    font-family: 'Roboto', sans-serif;
}
```

## @charset Rule

The `@charset` rule specifies the character encoding for an external style sheet. It must appear at the very beginning of the style sheet if used.

**Syntax:**

```bash
@charset "UTF-8";
```

## @font-face Rule

The `@font-face` rule allows you to define custom fonts that can be used throughout your CSS. This is particularly useful for using non-standard fonts that are not available on all users' computers.

**Syntax:**

```bash
@font-face {
    font-family: 'CustomFont';
    src: url('customfont.woff2') format('woff2'),
         url('customfont.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
```

**Example:**

```bash

@font-face {
    font-family: 'Roboto';
    src: url('Roboto-Regular.woff2') format('woff2'),
         url('Roboto-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

body {
    font-family: 'Roboto', sans-serif;
}
```

## !important Rule

The `!important` rule is used to give a CSS property higher priority than normal. It overrides any other styles applied to that element, except styles applied directly to the element using inline styles.

**Example:**

```bash

<!DOCTYPE html>
<html>
<head>
    <style>
        p {
            color: blue !important; /* This color will override any other styles */
        }
    </style>
</head>
<body>

<p style="color: green;">This paragraph will be blue because of !important.</p>

</body>
</html>

```