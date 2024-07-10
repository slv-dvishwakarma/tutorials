## CSS ─ SCROLLBARS

Customizing scrollbars in CSS involves using the `::-webkit-scrollbar` pseudo-element along with its sub-properties to adjust the appearance and behavior of scrollbars in web pages. However, it's important to note that scrollbar customization is primarily supported by WebKit-based browsers (such as Chrome, Safari, and newer versions of Edge), and the level of customization may vary across browsers. Here’s an overview of how you can style scrollbars:


## Styling Scrollbars

To style scrollbars, you can use the following CSS properties under the `::-webkit-scrollbar` pseudo-element:

1. **width and height:** Define the width and height of the scrollbar track.

2. **background-color:** Sets the background color of the scrollbar track.

3. **border:** Applies a border around the scrollbar track.

4. **border-radius:** Rounds the corners of the scrollbar track.

5. **thumb** - Specifies styles for the even of sl also have even th so had even perhaps even even even even even even even even even even even even even even th whom asked So Had Want knows ? icon


Certainly! Here's an example demonstrating how to style scrollbars using CSS:

```bash

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Scrollbar Example</title>
    <style>
        /* Target the scrollbar track */
        ::-webkit-scrollbar {
            width: 10px; /* Width of the scrollbar */
        }

        /* Target the scrollbar thumb */
        ::-webkit-scrollbar-thumb {
            background-color: #888; /* Color of the thumb */
            border-radius: 5px; /* Rounded corners of the thumb */
        }

        /* Optional: Target the scrollbar track on hover */
        ::-webkit-scrollbar-track:hover {
            background-color: #f0f0f0; /* Change background color on hover */
        }

        /* Optional: Target the scrollbar thumb on hover */
        ::-webkit-scrollbar-thumb:hover {
            background-color: #555; /* Change thumb color on hover */
        }

        /* Optional: Target the scrollbar corner */
        ::-webkit-scrollbar-corner {
            background-color: #ccc; /* Color of the scrollbar corner */
        }

        /* Optional: Target the scrollbar track when it's in a "decrement" state (e.g., up arrow or left arrow pressed) */
        ::-webkit-scrollbar-track-piece:start {
            background-color: #ddd; /* Color of the track piece */
        }

        /* Optional: Target the scrollbar track when it's in an "increment" state (e.g., down arrow or right arrow pressed) */
        ::-webkit-scrollbar-track-piece:end {
            background-color: #ddd; /* Color of the track piece */
        }

        /* Optional: Target the scrollbar thumb when it's in a "decrement" state */
        ::-webkit-scrollbar-button:start {
            background-color: #aaa; /* Color of the button */
        }

        /* Optional: Target the scrollbar thumb when it's in an "increment" state */
        ::-webkit-scrollbar-button:end {
            background-color: #aaa; /* Color of the button */
        }

        /* Optional: Target the scrollbar grip (not supported in all browsers) */
        ::-webkit-scrollbar-thumb:vertical:active {
            background-color: #666; /* Color of the thumb when active (clicked) */
        }
    </style>
</head>
<body>
    <div style="height: 300px; overflow-y: scroll;">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus euismod nisi sit amet aliquet volutpat. Proin convallis orci ut orci viverra, vitae ultrices arcu maximus. Nullam eu rutrum velit. Mauris accumsan feugiat fringilla. Nullam ultricies metus vel venenatis placerat. Fusce tincidunt diam a eros rutrum, sed vehicula augue ultricies. Nam aliquam imperdiet ipsum, sit amet viverra magna scelerisque vel. Nulla ut aliquam est. Donec lobortis efficitur ipsum, id dignissim eros pretium ut. Suspendisse ac nulla vel metus faucibus hendrerit nec eget dui.</p>
        <p>Maecenas dapibus sapien quam, ac elementum eros vestibulum id. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed euismod, erat ac interdum blandit, ligula leo dictum dolor, vel sagittis felis nunc non ante. Praesent eu sollicitudin purus, sed convallis turpis. Aliquam fermentum sem id dolor vestibulum laoreet. Duis eget risus nec dolor varius fermentum. Ut nec risus ac tortor laoreet aliquam at sed leo. Nam ullamcorper enim et nunc tincidunt aliquet.</p>
        <p>Vivamus varius risus eu augue elementum, et convallis ligula malesuada. Vestibulum maximus eget enim nec scelerisque. In vitae orci sit amet orci molestie vestibulum. Fusce vitae arcu ac metus suscipit tempus. Nulla aliquet fermentum tellus sit amet ultrices. Aliquam placerat, nulla at convallis commodo, ligula lorem feugiat dui, sit amet ultricies turpis quam in risus. Maecenas maximus, nulla sit amet interdum egestas, libero velit tempus risus, a dictum leo magna a diam.</p>
    </div>
</body>
</html>
```