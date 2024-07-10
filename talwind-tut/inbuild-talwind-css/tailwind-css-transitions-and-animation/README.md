## Tailwind CSS Transitions and Animation

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Transitions utilities control the transition and animation of elements. it provides transition classes like transition Property, duration, timing function, delay to manage elements perfectly. 

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Transition Property | It specifies the name of the CSS property for which the transition effect will occur. |
| Transition Duration | It specifies the length of time to complete the transition effect. |
| Transition Timing Function | It specifies the time an animation uses to change from one set of CSS transitions to another. |
| Transition Delay | It specifies the length of time to start the transition effect. |


Below example will give you a brief idea about the Transitions and Animation of Tailwind CSS:


```bash
HTML

<!DOCTYPE html> 
<html> 
<head> 
	<link href= 
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
		rel="stylesheet"> 
</head> 

<body class="text-center mx-4 space-y-2"> 
	<h1 class="text-green-600 text-5xl font-bold"> 
		GeeksforGeeks 
	</h1> 
	<b>Tailwind CSS Transition Duration Class</b> 
	<div class="bg-green-200 m-8 grid grid-flow-col gap-4 p-5"> 
		<button class="transition duration-75 ease-in-out 
					bg-green-300 hover:bg-green-600 transform 
					hover:-translate-y-1 hover:scale-110 
					rounded-lg p-4 border border-green-900"> 
			Hover me 
		</button> 
		<button class="transition duration-100 ease-in-out 
					bg-green-300 hover:bg-green-600 transform 
					hover:-translate-y-1 hover:scale-110 
					rounded-lg p-4 border border-green-900"> 
			Hover me 
		</button> 
		<button class="transition duration-500 ease-in-out 
					bg-green-300 hover:bg-green-600 transform 
					hover:-translate-y-1 hover:scale-110 
					rounded-lg p-4 border border-green-900"> 
			Hover me 
		</button> 
		<button class="transition duration-1000 ease-in-out 
					bg-green-300 hover:bg-green-600 transform 
					hover:-translate-y-1 hover:scale-110 
					rounded-lg p-4 border border-green-900"> 
			Hover me 
		</button> 
	</div> 
</body> 

</html> 
```
