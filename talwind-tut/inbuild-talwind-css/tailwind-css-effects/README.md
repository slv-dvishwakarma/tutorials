## Tailwind CSS Effects

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Effects control the effects on elements. that provide classes to apply effects on elements like box-shadow, opacity/transparency.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Box Shadow | It controls the box-shadow of an element. |
| Opacity | It sets the opacity of any element.	|


Below example will give you a brief idea about the Effects of Tailwind CSS:


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
	<b>Tailwind CSS Box Shadow Class</b> 
	<div class="grid grid-flow-col text-center p-2"> 
		<div class="shadow-sm w-24 h-24 bg-green-200 
					rounded-lg">shadow-sm 
		</div> 
		<div class="shadow w-24 h-24 bg-green-200 
					rounded-lg">shadow 
		</div> 
		<div class="shadow-md w-24 h-24 bg-green-200 
					rounded-lg">shadow-md 
		</div> 
		<div class="shadow-lg w-24 h-24 bg-green-200 
					rounded-lg">shadow-lg 
		</div> 
		<div class="shadow-xl w-24 h-24 bg-green-200 
					rounded-lg">shadow-xl 
		</div> 
		<div class="shadow-2xl w-24 h-24 bg-green-200 
					rounded-lg">shadow-2xl 
		</div> 
	</div> 
</body> 

</html> 
```