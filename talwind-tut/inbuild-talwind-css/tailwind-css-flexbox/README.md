## Tailwind CSS Flexbox

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. The CSS flexbox is a vital feature to develop the frontend, there are four directions available in CSS so in Tailwind CSS all the properties are covered as in class form. we had alternative Tailwind CSS Flex classes for fast development of front-end like Tailwind CSS Flex Direction, Flex wrap, Flex, etc..

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
|Flex Direction | It established the main axis of the flexible item. |
| Flex Wrap | It specifies whether flex items are forced into a single line or wrapped onto multiple lines. | 
| Flex | It is used to set the length of flexible items. | 
| Flex Grow | This class specifies how much the item will grow compared to other items inside that container. | 
| Flex Shrink | This class specifies how much the item will shrink compared to other items inside that container. |
| Order | It renders flex and grid items in a different order than they appear in the DOM. |


Below example will give you a brief idea about the Flexbox of Tailwind CSS:


```bash
HTML

<!DOCTYPE html> 
<html> 

<head> 
	<title>Tailwind flex-1 Class</title> 

	<link href= 
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
		rel="stylesheet"> 
</head> 

<body> 
	<h1 class="text-center text-green-600 text-5xl font-bold"> 
		GeeksforGeeks 
	</h1> 

	<p class="text-center font-bold">Tailwind CSS flex-1 Class</p> 


	<div id="main" class="bg-green-200 border-4 
						border-green-600 w-2/3 ml-32"> 
		<p class="ml-2">This is the effect of flex-1:</p> 


		<div class="flex m-2 text-white"> 
			<div class="bg-green-900 flex-1"> 
				Geeksforgeeks 
			</div> 
			<div class="bg-green-800 flex-1"> 
				Tailwind CSS 
			</div> 
		</div> 
		<p class="ml-2"> 
				This is the effect of flex-initial: 
		</p> 


		<div class="flex m-2 text-white"> 
			<div class="bg-green-900 flex-initial"> 
				Geeksforgeeks 
			</div> 
			<div class="bg-green-800 flex-initial"> 
				A Computer Science for Geeks 
			</div> 
		</div> 
		<p class="ml-2"> 
			This is the effect of flex-auto: 
		</p> 


		<div class="flex m-2 text-white"> 
			<div class="bg-green-900 flex-auto"> 
				CSS 
			</div> 
			<div class="bg-green-800 flex-auto"> 
				Cascading Style Sheet 
			</div> 
		</div> 
		<p class="ml-2"> 
				This is the effect of flex-none: 
		</p> 


		<div class="flex m-2 text-white"> 
			<div class="bg-green-900 flex-none"> 
				HTML 
			</div> 
			<div class="bg-green-800 flex-none"> 
				Hypertext Markup Language 
			</div> 
		</div> 
	</div> 
</body> 

</html> 
```