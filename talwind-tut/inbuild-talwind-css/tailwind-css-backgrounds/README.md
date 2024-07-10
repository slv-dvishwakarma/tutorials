## Tailwind CSS Backgrounds

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Background, In which all the properties are covered in this class. it is controlling the background portion of the page like a background Image that can set one or more background images to element, background-clip, background color, background opacity, etc.,

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Background Image | It sets one or more background images to an element. |
| Background Clip | It defines how to extend background (color or image) within an element. |
| Background Color | It specifies the background color of an element. |
| Background Opacity | It describes the transparency of the element. |
| Background Position | It sets one or more background images to an element. | 
| Background Repeat | It repeats the background image both horizontally and vertically. |
| Background Size | It sets the size of the background image. |
| Gradient Color Stops | It is used to create variants styling of images. |

Below example will give you a brief idea about the Backgrounds of Tailwind CSS:

```bash
<!DOCTYPE html> 
<head> 
    <link href= 
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
          rel="stylesheet"> 
</head> 
  
<body class="text-center mx-4 space-y-2"> 
    <h1 class="text-green-600 text-5xl font-bold"> 
        GeeksforGeeks 
    </h1> 
    <b>Tailwind CSS 
    <span class="bg-clip-text text-lg text-transparent 
                bg-gradient-to-r 
                from-green-400 to-blue-500"> 
        Background Clip Class 
        </span> 
    </b> 
    <div class="mx-2 grid grid-cols-3 gap-2 bg-green-200 rounded-lg"> 
        <div class="bg-clip-border p-6 bg-green-600 border-dashed 
                    border-4 border-green-300"> 
        </div> 
        <div class="bg-clip-padding p-6 bg-green-600 border-dashed 
                    border-4 border-green-300"> 
              
        </div> 
        <div class="bg-clip-content p-6 bg-green-600 border-dashed 
                    border-4 border-green-300"> 
              
        </div> 
    </div> 
</body> 
  
</html> 
```
