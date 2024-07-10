## Tailwind CSS Grid

Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Grid describes the number of properties that allow to design of the grid structure of the grid and control the placement of the grid.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Grid Template Columns | It sets the number of columns and size of the columns of the grid. | 
| Grid Column Start / End | It controls the placement of grid items using Tailwind CSS. | 
| Grid Template Rows | It sets the number of rows and size of the rows of the grid. | 
| Grid Row Start / End | It controls the placement of grid items using Tailwind CSS. | 
| Grid Auto Flow | It specifies how auto-placed items get flowed into the grid items. | 
| Grid Auto Columns | It specifies the size for the columns of implicitly generated grid containers. | 
| Grid Auto Rows | It specifies the size for the rows of implicitly generated grid containers. |
| Gap | It sets the spacing also caller gutter between the rows and columns. |


Below example will give you a brief idea about the Grid of Tailwind CSS:

```bash
HTML

<!DOCTYPE html> 

<head> 
	<title>Tailwind grid-rows Class</title> 

	<link href= 
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
		rel="stylesheet"> 
</head> 

<body class="text-center"> 
	<h1 class="text-green-600 text-5xl font-bold"> 
		GeeksforGeeks 
	</h1> 

	<b>Tailwind CSS grid-rows Class</b> 

	<div id="main" class="grid grid-rows-3 grid-flow-col"> 
		<div class="bg-green-500 rounded-lg m-4 h-12">1</div> 
		<div class="bg-green-500 rounded-lg m-4 h-12">2</div> 
		<div class="bg-green-500 rounded-lg m-4 h-12">3</div> 
		<div class="bg-green-500 rounded-lg m-4 h-12">4</div> 
		<div class="bg-green-500 rounded-lg m-4 h-12">5</div> 
		<div class="bg-green-500 rounded-lg m-4 h-12">6</div> 
	</div> 
</body> 

</html> 
```
