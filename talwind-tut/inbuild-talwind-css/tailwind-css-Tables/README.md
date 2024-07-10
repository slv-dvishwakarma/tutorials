## Tailwind CSS Tables

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Tables settings the table elements like table layouts, borders. 

That provides classes like Border Collapse, Table layout to easily maintain the tables.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Border Collapse | It sets the borders of the cell and tells whether these cells will share a common border or not. |
| Table Layout | It sets the display of the layout of the table. |

Below example will give you a brief idea about the Tables of Tailwind CSS:

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
	<b>Tailwind CSS Table Layout Class</b> 
	<div class="bg-green-200"> 
		<table class="table-auto border-separate border border-green-900"> 
		<thead> 
		<tr> 
			<th class="border border-green-600">Frameworks</th> 
			<th class="border border-green-600">About</th> 
		</tr> 
		</thead> 
		<tbody> 
		<tr> 
			<td class="border border-green-600">Tailwind CSS</td> 
			<td class="border border-green-600"> 
				Tailwind CSS is a highly customizable, 
				low-level CSS framework that gives you all 
				of the building blocks 
			</td> 
		</tr> 
		<tr> 
			<td class="border border-green-600">Bulma</td> 
			<td class="border border-green-600"> 
				Bulma CSS by @jgthms is just perfect. 
				Simple, easily customizable and doesn't 
				impose Javascript implementations. 
			</td> 
		</tr> 
		<tr> 
			<td class="border border-green-600">Bootstrap</td> 
			<td class="border border-green-600"> 
				Bootstrap is a free and open-source CSS 
				framework directed at responsive, mobile-first 
				front-end web development. 
			</td> 
		</tr> 
		</tbody> 
		</table> 
	</div> 
</body> 

</html> 
```