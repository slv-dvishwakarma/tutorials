## Tailwind CSS Transforms

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Transform utilities are used to control the transform behavior of any element. This class is used to transform the element like rotation, scaling, translating the element.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Transform | It controls the transform behavior of any element. |
| Transform Origin | It specifies the origin of the rotation of an element.	 |
| Scale | It is used to resize the element in the 2D plane.	|
| Rotate | 	It rotates an element based on the given angle as an argument. |
| Translate | It is used to translating elements with transform. |

Below example will give you a brief idea about the Transforms of Tailwind CSS:

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
	<b>Tailwind CSS Rotate Class</b> 
	<div class="bg-green-300 
				mx-16 
				p-4 
				justify-between 
				grid grid-flow-col"> 
	<div class="bg-no-repeat 
				w-16 h-16 transform rotate-0" 
		style= 
		"background-image:url( 
https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75)"> 
	</div> 
	<div class="bg-no-repeat 
				w-16 h-16 transform rotate-45" 
		style= 
		"background-image:url( 
https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75)"> 
	</div> 
	<div class="bg-no-repeat 
				w-16 h-16 transform rotate-90" 
		style="background-image:url( 
https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75)"> 
	</div> 
	<div class="bg-no-repeat 
				w-16 h-16 transform rotate-180" 
		style="background-image:url( 
https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75)"> 
	</div> 
	</div> 
</body> 
</html> 
```