CSS provides various media types and features to control how styles are applied based on different output devices and media types. Here's an overview of each:

## CSS Media Types

1. **All Media `(all)`**: Applies to all devices.

2. **Print `(print)`**: Intended for paged material and print preview.

3. **Screen `(screen)`**: Intended primarily for color computer screens.

4. **Speech `(speech)`**: Intended for speech synthesizers.

## CSS Media Features

1. **Width and Height:** Control based on the width and height of the viewport.

    ```bash
    @media screen and (min-width: 768px) {
        /* Styles applied for screens wider than 768px */
    }
    ```

2. **Orientation:** Adjust based on the orientation of the viewport (landscape or portrait).

    ```bash
    @media screen and (orientation: landscape) {
        /* Styles applied for landscape orientation */
    }
    ```

3. **Resolution:** Specify styles based on the resolution of the output device.

    ```bash
    @media screen and (min-resolution: 300dpi) {
        /* Styles applied for devices with at least 300 dots per inch resolution */
    }
    ```


## Paged Media

Paged media refers to styles applied specifically to documents that are meant to be printed or viewed in print preview. CSS for paged media includes properties that control page breaks, margins, and other aspects of printed documents.

**Example:**

```bash
@media print {
    body {
        font-size: 12pt;
        line-height: 1.5;
    }
    
    h1 {
        page-break-before: always;
    }
}
```

## Aural Media

Aural media styles are intended for speech synthesizers and other audio devices. They include properties for controlling speech synthesis, volume, and pitch.

**Example:**

```bash
@media speech {
    h1 {
        voice-family: "Alex", sans-serif;
        speak: spell-out;
    }
    
    p {
        pause-before: 2s;
        pause-after: 3s;
    }
}
```

## Using Media Queries

Media queries allow you to apply different styles based on the media type and features supported by the device. They use the `@media` rule followed by the media type and any media features:

```bash
@media screen and (min-width: 768px) {
    /* Styles applied for screens wider than 768px */
}
```

## Conclusion

Understanding CSS media types and features allows you to create responsive and adaptable designs that cater to different devices and output formats. By using media queries effectively, you can optimize the user experience across a variety of devices, whether they are screens, printed documents, or speech synthesizers.
