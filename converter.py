#!/usr/bin/python
import sys

if len(sys.argv) < 2 or ord(sys.argv[1]) > 127:
    print 'usage: converter.py character'
    sys.exit(1)

f = open('./ascii')
charCode = ord(sys.argv[1])

f.seek(charCode * ((4 * 8) + 8))
#                  |______|  |_|
#                   4 char    whitespace

row = f.read((4 * 8) + (1 * 8))
matrix = row.split()
matrix = map(lambda x: bin(int(x, 16))[2:].zfill(8)[::-1], matrix)
print '\n'.join(matrix)
