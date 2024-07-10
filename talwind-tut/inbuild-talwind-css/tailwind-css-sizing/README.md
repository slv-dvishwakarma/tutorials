## Tailwind CSS Sizing

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Sizing that set the size of elements like setting element width, height, min-max width, and min-max height.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Width | It sets the width of the text, images. |
| Min-Width | It defines the minimum width of an element. |
| Max-Width | It defines the maximum width of an element. |
| Height | It sets the height of an element. |
| Min-Height | It sets the minimum height of an element. |
| Max-Height | It sets the maximum height of an element. |

Below example will give you a brief idea about the Sizing of Tailwind CSS:

```bash 
HTML

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
	<b>Tailwind CSS MIn-Width Class</b> 
	<div class="w-24 h-16 min-w-full md:min-w-0 
				bg-green-400 rounded-lg text-white"> 
	</div> 
</body> 

</html> 
```
