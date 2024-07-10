## Semantic HTML

Semantic HTML is a way of writing HTML that emphasizes the meaning (or semantics) of the information contained within the web page rather than just the presentation. Using semantic elements makes the HTML more understandable and meaningful for both web browsers and developers, improving accessibility, search engine optimization (SEO), and maintainability of the code.

## Benefits of Semantic HTML

1. **Improved Accessibility:** Semantic HTML helps screen readers and other assistive technologies understand and navigate the content more effectively.

2. **Better SEO:** Search engines can better interpret and index your content, leading to improved search rankings.

3. **Enhanced Readability:** Code is easier to read and maintain for developers.

4. **Standardization:** Following semantic HTML practices ensures your code adheres to web standards.

## Common Semantic HTML Elements

1. `<header>`

    The `<header>` element represents introductory content or a set of navigational links. It typically contains headings, logos, and other introductory elements.

    ```bash
    <header>
    <h1>My Website</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    ```

2. `<nav>`

    The `<nav>` element is used to define a block of navigation links.

    ```bash
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    ```

3. `<main>`

    The `<main>` element represents the main content of the document. There should only be one `<main>` element per document.

    ```bash
    <main>
        <article>
            <h2>Main Article</h2>
            <p>This is the main content of the page.</p>
        </article>
    </main>
    ```

4. `<article>`

    The `<article>` element represents a self-contained piece of content that could be independently distributed or reused, such as a blog post or news article.

    ```bash
    <article>
        <h2>Article Title</h2>
        <p>This is an article.</p>
    </article>
    ```

5. `<section>`

    The `<section>` element defines a thematic grouping of content, typically with a heading.

    ```bash
    <section>
        <h2>Section Heading</h2>
        <p>This section contains related content.</p>
    </section>
    ```

6. `<aside>`

    The `<aside>` element represents content that is tangentially related to the main content, such as sidebars or pull quotes.

    ```bash
    <aside>
        <h3>Related Information</h3>
        <p>This is some related information.</p>
    </aside>
    ```

7. `<footer>`

    The `<footer>` element represents the footer of a section or the entire document. It typically contains information about the author, copyright, links to related documents, etc.

    ```bash
    <footer>
    <p>&copy; 2024 My Website</p>
        <nav>
            <ul>
                <li><a href="#privacy">Privacy Policy</a></li>
                <li><a href="#terms">Terms of Service</a></li>
            </ul>
        </nav>
    </footer>
    ```

### Example of a Webpage Using Semantic HTML

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semantic HTML Example</title>
</head>
<body>
    <header>
        <h1>My Website</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <article>
            <h2>Main Article Title</h2>
            <p>This is the main content of the page.</p>
        </article>

        <section>
            <h2>Related Section</h2>
            <p>This section contains related content.</p>
        </section>

        <aside>
            <h3>Related Information</h3>
            <p>This is some tangentially related information.</p>
        </aside>
    </main>

    <footer>
        <p>&copy; 2024 My Website</p>
        <nav>
            <ul>
                <li><a href="#privacy">Privacy Policy</a></li>
                <li><a href="#terms">Terms of Service</a></li>
            </ul>
        </nav>
    </footer>
</body>
</html>
```
