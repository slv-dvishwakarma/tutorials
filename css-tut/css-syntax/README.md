## CSS-SYNTAX

CSS syntax consists of a set of rules that define how HTML elements should be styled. Each CSS rule comprises a selector and a declaration block. The declaration block contains one or more declarations, each specifying a CSS property and its value.

- **Selector:** Indicates the HTML element to be styled.

- **Property:** A style attribute to be applied to the element (e.g., color, font-size).

- **Value:** Specifies the value of the property.

## Types of Selectors

1. **The Universal Selectors**

    Universal selectors are a powerful tool in CSS that allow you to apply styles to every element on a page. The universal selector is represented by an asterisk `(*)`. Here’s an overview of its usage and some examples:

    ```bash
    * {
        margin: 0;
        padding: 0;
    }
    ```

    In this example, all elements will have their margin and padding set to zero, which is a common practice in CSS resets to ensure consistency across different browsers.

    **Combining with Other Selectors**

    You can combine the universal selector with other selectors to apply styles more selectively. For instance:

    ```bash
    /* All elements inside a specific container */
    .container * {
        color: blue;
    }

    /* All direct child elements of a specific container */
    .container > * {
        color: red;
    }
    ```

2. **The Descendant Selectors**

    Descendant selectors in CSS allow you to apply styles to elements that are nested within other elements. This is done using a space between the selectors, which indicates a relationship where the second element is a descendant (child, grandchild, etc.) of the first element.

    ## Examples
    **Basic Example**

    Consider the following HTML structure:

    ```bash
    <div class="container">
        <p>This is a paragraph inside a container.</p>
        <div>
            <p>This is another paragraph inside a nested div.</p>
        </div>
    </div>
    ```

    You can use a descendant selector to style all `<p>` elements inside the `.container`:

    ```bash
    .container p {
        color: blue;
    }
    ```

    This will make both paragraphs blue, regardless of how deeply nested they are within the `.container`.

    **Multiple Levels of Nesting**

    Descendant selectors can target elements nested at any depth:

    ```bash
    HTML

    <div class="outer">
        <div class="inner">
            <span>Some text</span>
        </div>
    </div>
    ```

    ```bash
    CSS

    .outer .inner span {
        font-weight: bold;
    }
    ```

    This will make the text inside the `<span>` bold, as it is a descendant of both `.outer` and `.inner`.


3. **The Class Selectors**

    Class selectors in CSS are used to apply styles to elements with specific class attributes. They are denoted by a period `(.)` followed by the class name. Class selectors are very flexible and commonly used because an element can have multiple classes, and the same class can be applied to multiple elements.

    **Examples**

    **Basic Example**

    Consider the following HTML structure:

    ```bash
    HTML

    <div class="container">
        <p class="text">This is a paragraph.</p>
    </div>
    ```

    You can use a class selector to style the paragraph with the class text:

    ```bash
    CSS

    .text {
        color: blue;
        font-size: 16px;
    }
    ```

    This will apply the styles to the paragraph, making the text blue and setting the font size to 16 pixels.

    **Multiple Classes**

    An element can have multiple classes:

    ```bash
    <p class="text highlight">This is a highlighted paragraph.</p>
    ```

    You can define styles for each class:

    ```bash
    .text {
        color: blue;
    }

    .highlight {
        background-color: yellow;
    }
    ```

4. **The ID Selectors**

    ID selectors in CSS are used to apply styles to a single, unique element on a web page. An ID is defined using a hash symbol `(#)` followed by the ID name. IDs are intended to be unique within a document, meaning each ID should only be used once per page.

    **Examples**

    **Basic Example**

    Consider the following HTML structure:

    ```bash
    HTML

    <div id="header">
        <h1>Welcome to My Website</h1>
    </div>
    ```

    You can use an ID selector to style the `header` `div`:

    ```bash
    CSS

    #header {
        background-color: lightblue;
        padding: 20px;
        text-align: center;
    }
    ```

    This will apply the styles to the `header` div, making its background light blue, adding padding, and centering the text.


5. **The Child Selectors**

    Child selectors in CSS are used to apply styles to elements that are direct children of a specified parent element. They are denoted using a greater-than sign `(>)`. This selector is more specific than the descendant selector because it only targets elements that are immediate children of a parent element.

    **Examples**

    **Basic Example**

    Consider the following HTML structure:

    ```bash
    HTML

    <div class="container">
        <p>This is a paragraph inside the container.</p>
        <div>
            <p>This is a nested paragraph inside another div.</p>
        </div>
    </div>
    ```

    You can use a child selector to style only the paragraphs that are direct children of the `.container` div:

    ```bash
    .container > p {
        color: blue;
    }
    ```

    This will make only the first paragraph blue, as it is a direct child of the `.container` div. The nested paragraph will not be affected.


6. **The Attribute Selectors**

    Attribute selectors in CSS allow you to target elements based on their attributes and attribute values. They provide a flexible way to style elements without needing to add extra classes or IDs.

    **Examples**

    **Basic Example**

    Consider the following HTML structure:

    ```bash
    HTML

    <input type="text" placeholder="Enter your name">
    <input type="email" placeholder="Enter your email">
    <input type="password" placeholder="Enter your password">
    ```

    You can use attribute selectors to style inputs based on their `type` attribute:

    ```bash

    /* Style all input elements with a type attribute */
    input[type] {
        margin: 10px;
        padding: 5px;
    }

    /* Style input elements with a type attribute equal to 'email' */
    input[type="email"] {
        border: 2px solid blue;
    }

    /* Style input elements with a type attribute containing the word 'password' */
    input[type*="password"] {
        border: 2px solid red;
    }
    ```


7. **Multiple Style Rules**

    In CSS, you can apply multiple style rules to an element, either by listing multiple declarations within a single rule set or by using multiple selectors. This allows you to create complex and flexible styles for your web pages.

    **Examples**

    **Multiple Declarations**

    Consider the following HTML structure:

    ```bash
    HTML

    <h1>Main Title</h1>
    <h2>Sub Title</h2>
    <p class="intro">This is an introductory paragraph.</p>
    ```

    ```bash
    CSS

    h1, h2, .intro {
        color: blue;
        margin-bottom: 20px;
    }
    ```

8. **Grouping Selectors**

    Grouping selectors in CSS allows you to apply the same styles to multiple selectors without repeating the style definitions. This technique is efficient and helps keep your CSS code concise and organized.

    **Example**

    Consider the following HTML structure:

    ```bash
    HTML

    <h1>Main Title</h1>
    <h2>Sub Title</h2>
    <p>This is a paragraph.</p>
    ```

    You can apply the same styles to multiple selectors by grouping them:

    ```bash
    CSS

    h1, h2, p {
        color: blue;
        font-family: Arial, sans-serif;
        margin-bottom: 20px;
    }
    ```
