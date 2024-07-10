## Tailwind CSS Layout

Tailwind CSS is a utility-first CSS framework that allows you to build custom designs without having to write traditional CSS. 

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Container | It fix the max-width of an element to match the min-width of the breakpoint. |
|Box Sizing | It defines how the user should calculate the total width and height of an element.|
| Display | It defines how the components (div, hyperlink, heading, etc) are going to be placed on the web page. |
| Float | It defines the flow of content for controlling the wrapping of content around an element. |
| Clear | It is used to specify which side of floating elements are not allowed to float. | 
Object Fit | It specifies how an image or video should be resized to fit its content box. | 
| Object Position | It specifies how an image or video element is positioned with x/y coordinates.  | 
| Overflow | It tells whether to clip content or to add scroll bars. |
| overscroll Behavior | It sets the behavior of the browser when the boundary of a scrolling area is reached. | 
| Position | It is used for controlling how an element is positioned in the DOM. | 
| Top/Right/Bottom/Left | These classes are used to control the alignment of a positioned element. | 
| Visibility | It is used to specify whether an element is visible or not. |
| Z-index | It describes the z-index along the three-dimensional plane. |

Below example will give you a brief idea about the Layout of Tailwind CSS:

```bash
HTML

<!DOCTYPE html>
<html>

<head>
    <link href=
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" 
        rel="stylesheet">
</head>

<body class="text-center">
    <h1 class="text-green-600 text-5xl font-bold">
        GeeksforGeeks
    </h1>
    <b>Tailwind CSS float Class</b>
    <div class="mx-10">
        <img class="float-right p-2" src=
    "https://varni-education.vercel.app/_next/image?url=%2Fimages%2Fabout-us.jpg&w=1920&q=75">

        <p class="text-justify ">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        </p>
    </div>
</body>

</html>
```
