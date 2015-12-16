# font8X8
Language Agnostic 8x8 monochrome bitmap font for rendering

Adapted from: [dhepper/font8x8](https://github.com/dhepper/font8x8).

Copied hex codes from header file to text file.

How to write converters
-----------------------
1. Read file 'ascii'
2. seek to `ascii code * ((4 * 8) + 8)`
3. read `((4 * 8) + (1 * 8))` bytes
4. convert to binary
5. print array

Converters can also be used in unix-y way:

```bash
$ convert.py A | sed 's/0/ /g
  11
 1111
11  11
11  11
111111
11  11
11  11
        
 ```
Credits
=======
These header files are directly derived from an assembler file fetched from:
http://dimensionalrift.homelinux.net/combuster/mos3/?p=viewsource&file=/modules/gfx/font8_8.asm

Original header:

; Summary: font8_8.asm

; 8x8 monochrome bitmap fonts for rendering

;
; Author:
;     Marcel Sondaar
;     International Business Machines (public domain VGA fonts)
;
; License:
;     Public Domain
;
LICENSE:
- ascii file: Public Domain
- converters: GPL v3
