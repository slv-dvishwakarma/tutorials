## CSS ─ PSEUDO ELEMENTS

CSS pseudo-elements allow you to style specific parts of an element's content or parts that do not exist in the DOM. They are indicated by double colons `(::)` and enable you to create effects that were traditionally achievable only with extra HTML markup or JavaScript. Here are some commonly used CSS pseudo-elements:

**Basic Pseudo-Elements**

1. **::before:** Inserts content before the selected element.

    ```bash
    p::before {
        content: "Before ";
        font-weight: bold;
    }
    ```

2. **::after:** Inserts content after the selected element.

    ```bash
    p::after {
        content: " After";
        font-style: italic;
    }
    ```

## Example of Usage

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Pseudo-Elements Example</title>
    <style>
        /* Style for the ::before pseudo-element */
        p::before {
            content: "Before: ";
            font-weight: bold;
        }

        /* Style for the ::after pseudo-element */
        p::after {
            content: " :After";
            font-style: italic;
        }
    </style>
</head>
<body>
    <p>This paragraph demonstrates the usage of CSS pseudo-elements.</p>
</body>
</html>
```

## Explanation

- **::before:** Adds "Before: " before each `<p>` element.

- **::after:** Adds "
" after each `<p>` element.

## Conclusion

CSS pseudo-elements provide a powerful way to enhance the presentation of your web pages by adding extra content or styling elements that are not part of the DOM. By using pseudo-elements effectively, you can achieve sophisticated design effects with minimal additional markup or scripting.