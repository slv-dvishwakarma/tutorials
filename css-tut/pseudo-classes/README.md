## CSS ─ PSEUDO CLASSES

CSS pseudo-classes are keywords added to selectors that specify a special state of the selected elements. They allow you to style elements based on user interaction, document structure, or other conditions that cannot be represented by simple selectors alone. Here's an overview of some commonly used CSS pseudo-classes:

## Basic Pseudo-Classes

1. Applies styles when the user hovers over an element.

    ```bash
    a:hover {
        color: red;
        text-decoration: underline;
    }
    ```

2. Applies styles when an element is being activated (usually when the mouse button is pressed down).

    ```bash
    button:active {
        background-color: gray;
    }
    ```

3. Applies styles when an element gains focus (e.g., via keyboard navigation or clicking).

    ```bash
    input:focus {
        border: 2px solid blue;
    }
    ```

## Structural Pseudo-Classes

1. Selects the first child element of its parent.

    ```bash
    li:first-child {
        font-weight: bold;
    }
    ```

2. Selects the last child element of its parent.

    ```bash
    div > p:last-child {
        margin-bottom: 0;
    }
    ```

3. (n): Selects elements based on their position within a parent.

    ```bash
    tr:nth-child(even) {
        background-color: lightgray;
    }
    ```

## Form Pseudo-Classes

1. Applies styles to checked checkboxes or radio buttons.

    ```bash
    input[type="checkbox"]:checked {
        border-color: green;
    }
    ```

2. Applies styles to disabled form elements.

    ```bash
    input:disabled {
        opacity: 0.6;
    }
    ```

## Conclusion

CSS pseudo-classes provide powerful ways to style elements based on various conditions and interactions. By using pseudo-classes effectively, you can enhance user experience, improve accessibility, and create dynamic and interactive web designs. Understanding these pseudo-classes allows you to apply styles that respond to user actions and document structure in a precise and intuitive manner.