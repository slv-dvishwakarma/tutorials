## HTML – ATTRIBUTES

We have seen few HTML tags and their usage like heading tags `<h1>`, `<h2>`, paragraph tag
`<p>` and other tags. We used them so far in their simplest form, but most of the HTML tags
can also have attributes, which are extra bits of information.

An attribute is used to define the characteristics of an HTML element and is placed inside the element's opening tag. All attributes are made up of two parts: a `name` and a `value`:

 - The name is the property you want to set. For example, the paragraph `<p>` element in the example carries an attribute whose name is align, which you can use to indicate
the alignment of paragraph on the page.

- The `value` is what you want the value of the property to be set and always put within
quotations. The below example shows three possible values of align attribute: `left`,
`center` and `right`.

## Example

```bash
<!DOCTYPE html>
<html>
<head>
<title>Align Attribute Example</title>
</head>
<body>
    <p align="left">This is left aligned</p>
    <p align="center">This is center aligned</p>
    <p align="right">This is right aligned</p>
</body>
</html>
```

## Core Attributes

The four core attributes that can be used on the majority of HTML elements (although not all)
are:

- **Id**
- **Title**
- **Class**
- **Style**



1. **Id Attribute**

    The `id` attribute uniquely identifies an element within a document. It must be unique across the entire HTML document. For example:

    ```bash
    <div id="header">
        <h1>Welcome to our Website</h1>
    </div>
    ```

    Here, the `id="header"` allows you to specifically target this `div` element using CSS or JavaScript.


2. **Title Attribute**

     The `title` attribute provides extra information about an element, typically displayed as a tooltip when the mouse hovers over the element. For example:

     ```bash
     <img src="example.jpg" alt="Example Image" title="This is an example image">
     ```

     Hovering over the image would display a tooltip with the text "This is an example image".

3. **Class Attribute**

    The `class` attribute is used to define multiple elements that share the same styling or behavior. It allows elements to be styled using CSS or targeted by JavaScript based on shared characteristics. For example:

    ```bash
    <p class="important">This paragraph has important information.</p>
    <p class="important">Another important paragraph.</p>
    ```

    Here, both paragraphs have the `class="important"`, which can be styled uniformly or targeted for specific actions.

4. **Style Attribute**

    The `style` attribute allows inline CSS styling to be applied directly to an element. It is useful for making quick styling adjustments or for unique, one-off styles. For example:

    ```bash
    <div style="background-color: #f0f0f0; padding: 10px;">
        <p>This div has a light gray background and 10 pixels of padding.</p>
    </div>
    ```

    Here, the `style` attribute sets the background color and padding directly on the `div` element.


