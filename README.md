# font8X8
Language Agnostic 8x8 monochrome bitmap font for rendering

Adapted from: [dhepper/font8x8](https://github.com/dhepper/font8x8)
Copied hex codes from header file to text file.

LICENSE:
- ascii file: Public Domain
- converters: GPL v3

How-to for writing converters

1. Read file 'ascii'
2. seek to `ascii code * ((4 * 8) + 8)`
3. read `((4 * 8) + (1 * 8))` bytes
4. convert to binary
5. print array

Converts can also be used in unix-y way:
`convert.py A | sed 's/0/ /g`
