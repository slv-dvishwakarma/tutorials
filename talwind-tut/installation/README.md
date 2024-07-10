## Installation

1. **Tailwind CLI**

The simplest and fastest way to get up and running with Tailwind CSS from scratch is with the Tailwind CLI tool.

- **Install Tailwind CSS**

Install `tailwindcss` via npm, and create your `tailwind.config.js` file.

  ```bash
  Terminal

  npm install -D tailwindcss
  npx tailwindcss init
  ```

  - **Configure your template paths**

  Add the paths to all of your template files in your `tailwind.config.js` file.

  ```bash
tailwind.config.js

  /** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

- **Add the Tailwind directives to your CSS**

Add the `@tailwind` directives for each of Tailwind’s layers to your main CSS file.

```bash
src/input.css

@tailwind base;
@tailwind components;
@tailwind utilities;
```
- **Start the Tailwind CLI build process**

Run the CLI tool to scan your template files for classes and build your CSS.

```bash
Terminal

npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
```

- **Start using Tailwind in your HTML**

Add your compiled CSS file to the `<head>` and start using Tailwind’s utility classes to style your content.

```bash
src/index.html

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="./output.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

2. **Using PostCSS**

Installing Tailwind CSS as a PostCSS plugin is the most seamless way to integrate it with build tools like webpack, Rollup, Vite, and Parcel.

- **Install Tailwind CSS**

Install `tailwindcss` and its peer dependencies via npm, and create your `tailwind.config.js` file.

```bash
Terminal

npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

- **Add Tailwind to your PostCSS configuration**

Add `tailwindcss` and `autoprefixer` to your `postcss.config.js` file, or wherever PostCSS is configured in your project.

```bash 
postcss.config.js

module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  }
}
```

- **Configure your template paths**

Add the paths to all of your template files in your `tailwind.config.js` file.

```bash
tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
- **Add the Tailwind directives to your CSS**

Add the `@tailwind` directives for each of Tailwind’s layers to your main CSS file.

```bash
main.css

@tailwind base;
@tailwind components;
@tailwind utilities;
```


- **Start your build process**

Run your build process with `npm run dev` or whatever command is configured in your `package.json` file.

```bash
Terminal

npm run dev
```

- **Start using Tailwind in your HTML**

Make sure your compiled CSS is included in the `<head>` (your framework might handle this for you), then start using Tailwind’s utility classes to style your content.

```bash
index.html

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/dist/main.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

3. **Play CDN**

Use the Play CDN to try Tailwind right in the browser without any build step. The Play CDN is designed for development purposes only, and is not the best choice for production.

- **Add the Play CDN script to your HTML**

Add the Play CDN script tag to the `<head>` of your HTML file, and start using Tailwind’s utility classes to style your content.

```bash
index.html

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello world!
  </h1>
</body>
</html>
```

- **Try customizing your config**

Edit the `tailwind.config` object to [customize your configuration](https://tailwindcss.com/docs/configuration) with your own design tokens.

```bash
index.html

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            clifford: '#da373d',
          }
        }
      }
    }
  </script>
</head>
<body>
  <h1 class="text-3xl font-bold underline text-clifford">
    Hello world!
  </h1>
</body>
</html>
```

- **Try adding some custom CSS**

Use `type="text/tailwindcss"` to add custom CSS that supports all of Tailwind's CSS features.

```bash
index.html

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <style type="text/tailwindcss">
    @layer utilities {
      .content-auto {
        content-visibility: auto;
      }
    }
  </style>
</head>
<body>
  <div class="lg:content-auto">
    <!-- ... -->
  </div>
</body>
</html>
```

- **Try using a first-party plugin**

Enable first-party plugins, like forms and typography, using the `plugins` query parameter.

```bash
index.html

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp,container-queries"></script>
</head>
<body>
  <div class="prose">
    <!-- ... -->
  </div>
</body>
</html>
```
