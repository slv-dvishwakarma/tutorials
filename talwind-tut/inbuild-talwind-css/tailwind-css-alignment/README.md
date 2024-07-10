## Tailwind CSS Alignment

Tailwind CSS is basically a utility first CSS framework for rapid custom UI. Tailwind CSS Alignment controls how the flex and grid items are aligned along with the container for fast front-end development. suppose Tailwind CSS Justify Content controlling how flex and grid items are positioned along a container’s main axis and Justify items controlling how grid items are aligned along their inline axis.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Justify Content | It describe the alignment of the flexible box container. |
| Justify Items | It controls how grid items are aligned along their inline axis. | 
| Justify Self | It specifies the alignment of a content’s position along with the appropriate axis. | 
| Align Content | It specifies the alignment between the lines inside a flexible container. | 
| Align Items | It aligns the flex Items across the axis. |
| Align Self | It controls how an individual flex or grid item is positioned along its container’s cross axis. |
| Place Content | It controls how content is justified and aligned at the same time. | 
| Place Items | It controls how items are justified and aligned at the same time. |
| Place Self | It controls how an individual item is justified and aligned at the same time. |

Below example will give you a brief idea about the Backgrounds of Tailwind CSS:

```bash
HTML

<!DOCTYPE html> 
<html> 
	<head> 
		<link href= 
"https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"
			rel="stylesheet" /> 
	</head> 

	<body> 
		<div class="h-screen flex flex-col 
					items-center justify-center"> 
			<p class="text-green-700 text-xl mb-3"> 
			Welcome to GeeksforGeeks 
			</p> 


			<form> 
				<input aria-label="Enter your email address"
					type="text"
					placeholder="Email address"
					class="text-sm text-gray-base w-full 
							mr-3 py-5 px-4 h-2 border 
							border-gray-200 rounded mb-2" /> 
				<input aria-label="Enter your password"
					type="password"
					placeholder="Password"
					class="text-sm text-gray-base w-full mr-3 
							py-5 px-4 h-2 border border-gray-200 
							rounded mb-2" /> 

				<button type="submit"
						class="bg-green-400 w-full mt-4"> 
					Login 
				</button> 
			</form> 
		</div> 
	</body> 
</html> 
```
