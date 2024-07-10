## Tailwind CSS Spacing

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Spacing utilities manage and control the elements of padding, element’s margin, and space between child elements.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Padding | It creates space around the element, inside any defined border. |
| Margin | It creates space around the element, outside any defined border. |
| Space Between | It is used for controlling the space between child elements. |

Below example will give you a brief idea about the Spacing of Tailwind CSS:

```bash
HTML

<!DOCTYPE html> 
<head> 
	<link href= 
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
		rel="stylesheet"> 
</head> 

<body class="text-center"> 
	<h1 class="text-green-600 text-5xl font-bold"> 
		GeeksforGeeks 
	</h1> 
	<b>Tailwind CSS Space Between Class</b> 
	<div class="mx-4 space-y-4"> 
		<div class="bg-green-400 h-16 rounded-lg 
					border-2 border-green-800 p-1">1</div> 
		<div class="bg-green-400 h-16 rounded-lg 
					border-2 border-green-800">2</div> 
		<div class="bg-green-400 h-16 rounded-lg 
					border-2 border-green-800">3</div> 
		<div class="bg-green-400 h-16 rounded-lg 
					border-2 border-green-800">4</div> 
	</div> 
</body> 

</html> 
```
