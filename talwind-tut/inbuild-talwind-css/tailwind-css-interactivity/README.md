## Tailwind CSS Interactivity

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Interactivity utility provides classes like Tailwind CSS Appearance that control. This class is mostly used for cursors how it is interactive with another element.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Appearance | It is used for suppressing native form control styling, to reset any browser-specific styling. |
| Cursor | It specifies the mouse cursor to be displayed while pointing at an element. |
| Outline | It is used to control an element’s outline. |
| Pointer Events | It specify whether elements show to pointer events or not. | 
| Resize | It is used to resize the element according to user requirements. |
| Select | 	It specifies whether the text can be selected by the user or not. |

Below example will give you a brief idea about the Interactivity of Tailwind CSS:

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
	<b>Tailwind CSS Cursor Class</b> 
	<div id="main" class="p-2 justify-around ml-32 h-26 w-2/3 flex 
						items-stretch 
						bg-green-200 border-solid border-4 
						border-green-900 gap-4"> 
		<div class="cursor-auto bg-blue-600 
					w-full h-8 rounded-lg"> 
			Hover over 
		</div> 
		<div class="cursor-default bg-yellow-600 
					w-full h-8 rounded-lg"> 
			Hover over 
		</div> 
		<div class="cursor-pointer bg-purple-600 
					w-full h-8 rounded-lg"> 
			Hover over 
		</div> 
		<div class="cursor-wait bg-green-600 
					w-full h-8 rounded-lg"> 
			Hover over 
		</div> 
	</div> 
</body> 

</html> 
```