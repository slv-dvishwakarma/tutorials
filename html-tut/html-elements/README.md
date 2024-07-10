## HTML – ELEMENTS

An **HTML element** is defined by a starting tag. If the element contains other content, it ends
with a closing tag, where the element name is preceded by a forward slash as shown below
with few tags:

| Start Tag | Content | End Tag |
| --------- | ------- | ------- |
| `<p>` | This is paragraph content. | `</p>` |
| `<h1>` | This is heading content. | `</h1>` |
| `<div>` | This is division content | `</div>` |
| `<br />` | line break | we can add closing tag with same start tag |

Some HTML elements do not need a closing tag, such as `<img />`, `<hr />`, and `<br />` elements. These are known as **void elements**.

## Nested HTML Elements

Nested HTML elements are elements that are placed inside other elements. This hierarchical structure allows for organizing content and defining relationships between different parts of a webpage. Here's an example with descriptions:

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>This is <i>italic</i> heading</h1>
    <p>This is <u>underlined</u> paragraph</p>
</body>
</html>
```

