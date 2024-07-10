## CSS ─ MEASUREMENT UNITS

CSS provides various measurement units that define the size and positioning of elements on web pages. These units can be broadly categorized into two types: relative units and absolute units. Here's an overview of the most commonly used CSS measurement units:

## Relative Units
Relative units are based on the size of other elements on the page, making them adaptable to different screen sizes and devices.

1. **em:** Relative to the font-size of the -  element (1em equals the current font size of the element).

    - Example: font-size: 1.2em; (increases the font size to 120% of the parent element's font size).

2. **rem:** Relative to the font-size of the root element (html).

    - Example: font-size: 1.2rem; (increases the font size to 120% of the root element's font size).

3. **%:** Relative to the parent element's size.

    Example: width: 50%; (sets the width to 50% of the parent element's width).

4. **vw, vh:** Relative to the viewport width (1vw equals 1% of the viewport width) and viewport height.

    - Example: width: 50vw; (sets the width to 50% of the viewport width).

## Absolute Units
Absolute units are fixed and do not change based on the size of other elements or the viewport.

1. **px:** Pixels, relative to the screen pixel.

    - Example: font-size: 16px; (sets the font size to 16 pixels).

2. **cm, mm, in:** Centimeters, millimeters, and inches respectively, relative to physical lengths.

    - Example: width: 10cm; (sets the width to 10 centimeters).
pt, pc: Points (1/72 of an inch) and Picas (1/6 of an inch), typically used for print stylesheets.

## Examples of Usage

**Relative Units Example**

```bash
.container {
    font-size: 16px; /* Base font size */
}

.text {
    font-size: 1.2em; /* 1.2 times the font size of .container */
}

.section {
    width: 50%; /* 50% of the parent elements width */
}

.viewport {
    width: 80vw; /* 80% of the viewport width */
}
```

**Absolute Units Example**

```bash
.box {
    width: 200px; /* Fixed width of 200 pixels */
}

.print {
    font-size: 12pt; /* Font size of 12 points  for print styles */
}

.inches {
    width: 3in; /* Width of 3 inches */
}
```

## Conclusion

Understanding and correctly applying CSS measurement units is crucial for creating responsive and visually appealing web designs. By choosing the appropriate unit based on the context and requirements of your project, you can ensure consistency and adaptability across different devices and screen sizes.