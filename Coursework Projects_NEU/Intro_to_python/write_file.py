#!/usr/bin/env python
line_to_write = 'some text to write'
with open("out_file.txt", 'w') as out:
    out.write(line_to_write)
