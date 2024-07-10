## Tailwind CSS Typography

Tailwind is a highly customizable, low-level CSS framework that gives you all of the buildings blocks that you need. Tailwind CSS Typography, In which all style, properties, and spacing are covered in this class. For ex. Font family has multiple fonts as backups, font size has set the font size of the text.

| Tailwind CSS Class | Description |
| ------------------ | ----------- |
| Font Family | It is used to specify the font of an element. |
| Font Size | It sets the font size of the text in an HTML document. |
| Font Smoothing | It controls the font smoothing of an element. | 
| Font Style | It is used to style the given particular text. |
| Font Weight | It sets the weight or thickness of the font. | 
| Font Variant Numeric | It controls the usage of alternate glyphs. |
| Letter Spacing | It sets the spacing behavior between text characters. |
| Line Height | It sets the amount of space used for lines, such as in the text. |
| List Style Type | It specifies the appearance of the list item marker. |
| Placeholder Color | It is used to color any placeholder text. | 
| Placeholder Opacity | It sets the opacity of any placeholder text. |
| Text Alignment | It specifies the horizontal alignment of text in an element. |
| Text Color | It is used to color any text. |
| Text Opacity | It sets the opacity of any text.|
| Text Decoration | It is used to “decorate” the content of the text. |
| Text Transform | It controls the capitalization of the text. |
| Vertical Alignment | It specifies the vertical alignment of the table-box or inline element. |
| Whitespace | It controls the text wrapping and white-spacing. | 
| Word Break | It specify how to break the word when the word reached at end of the line. |

Below example will give you a brief idea about the Typography of Tailwind CSS:

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
	<b>Tailwind CSS Font Variant Numeric Class</b> 
	<div class="bg-green-300 mx-24 h-full"> 
		<p class="lining-nums">lining-nums: 1234567890</p> 
		<p class="oldstyle-nums">oldstyle-nums: 1234567890</p> 
		<p class="proportional-nums">proportional-nums: 12121</p> 
		<p class="proportional-nums">proportional-nums: 90909</p> 
		<p class="tabular-nums">tabular-nums: 12121</p> 
		<p class="tabular-nums">tabular-nums: 90909</p> 
		<p class="diagonal-fractions"> 
			diagonal-fractions: 1/2 3/4 5/6 
		</p> 
	</div> 
</body> 

</html> 
```
