## Tailwind CSS Filters

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Filters applies graphical effects like filters, blur, brightness, contrast, drop shadow, etc. to an element. These classes are mostly used on image content

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Filter | It sets the visual effect of an element.	|
| Blur | It is used to apply a blurred effect filter on the image. |
| Brightness | It sets the brightness of the image.	|
| Contrast | It sets the Contrast of the image.	|
| Drop Shadow | It applies a filter to the image to set the shadow of the image. |
| Grayscale | It applies a filter to the image to set the grayscale of the image. |
| Hue Rotate | It applies a filter to the image to set the hue rotation of the image. |
| Invert | It sets the invert version of the color of the image. |
| Saturate | It is used to super-saturate or desaturate the input image. |
| Sepia | It applies a filter to the image to convert an image into a sepia image. |
| Backdrop Filter | It enables the backdrop of any filter which is used by the filter. |
| Backdrop Blur | It is used to apply a blurred effect filter to an element. |
| Backdrop Brightness | It sets the brightness of the image. |
| Backdrop Grayscale | It applies a filter to the image to set the grayscale of the image. |
| Backdrop Hue Rotate | It applies a filter to the image to set the hue rotation of the image. | 
| Backdrop Invert | It applies a filter to the image to set the invert of the color of the image. |
| Backdrop Opacity | It applies a filter to the image to set the transparency of the image. |
| Backdrop Saturate | It is used to super-saturate or desaturates the input image. |
| Backdrop Sepia | It applies a filter to the image to convert an image into a sepia image. |

Below example will give you a brief idea about the Filters of Tailwind CSS:

```bash
HTML

<!DOCTYPE html> 
<html> 
<head> 
	<link href= 
"https://unpkg.com/tailwindcss@^2.1/dist/tailwind.min.css"
		rel="stylesheet"> 
</head> 

<body class="text-center mx-4 space-y-2"> 
	<h1 class="text-green-600 text-5xl font-bold"> 
		GeeksforGeeks 
	</h1> 
	<b>Tailwind CSS Filter Class</b> 
	<div class="grid grid-flow-col text-center p-4"> 
		<img class="rounded-lg filter brightness-50"
		src= 
"https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75"
			alt="image"> 
		<img class="rounded-lg filter invert"
			src= 
"https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75"
			alt="image"> 
		<img class="rounded-lg filter blur-lg"
			src= 
"https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75"
			alt="image"> 
		<img class="rounded-lg filter contrast-125"
			src= 
"https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75"
			alt="image"> 
		<img class="rounded-lg filter grayscale"
			src= 
"https://varni-education.vercel.app/_next/image?url=%2Fimage%2Fimages%2Flogo.png&w=1920&q=75"
			alt="image"> 
		
	</div> 
</body> 

</html> 
```