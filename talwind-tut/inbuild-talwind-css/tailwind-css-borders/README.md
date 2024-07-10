## Tailwind CSS Borders

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Border utility settings the radius, width, color, opacity, etc., of element’s borders. all the properties covered as in this class form.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Border Radius | It is used to set the border-radius. |
| Border Width | It sets the border width of all four sides of an element. |
| Border Color | It is used to specify the border color of an element. |
| Border Opacity | It describes the transparency of the element. |
| Border Style | It is used for controlling the style of an element’s borders. |
| Divide Width | It creates division between elements as a border. |
| Divide Color | It is used to color any Divider. |
| Divide Opacity | It sets the opacity of any divide. |
| Divide Style | It sets the divide style of any divide. |
| Ring Width | it sets the ring width of buttons. |
| Ring Color | It is used to color any ring. |
| Ring Opacity | It sets the opacity of any ring. |
| Ring Offset Width | It is used to set the ring-offset width of buttons. |
| Ring Offset Color | It is used to color any ring-offset.|


Below example will give you a brief idea about the Borders of Tailwind CSS:

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
	<b>Tailwind CSS Ring Opacity Class</b> 
	<div class="mx-16 grid grid-cols-5 gap-2 p-2"> 
		<button class="ring-0 ring-green-600 bg-green-400 
					ring-opacity-25 w-full h-12 rounded-lg"> 
			Ring-0 
		</button> 
		<button class="ring-1 ring-green-600 bg-green-400 
					ring-opacity-25 w-full h-12 rounded-lg"> 
			Ring-1 
		</button> 
		<button class="ring-2 ring-green-600 bg-green-400 
					ring-opacity-25 w-full h-12 rounded-lg"> 
			Ring-2 
		</button> 
		<button class="ring-4 ring-green-600 bg-green-400 
					ring-opacity-25 w-full h-12 rounded-lg"> 
			Ring-4 
		</button> 
		<button class="ring-8 ring-green-600 bg-green-400 
					ring-opacity-25 w-full h-12 rounded-lg"> 
			Ring-8 
		</button> 

	</div> 
</body> 
</html> 
```
