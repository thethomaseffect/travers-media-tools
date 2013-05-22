#!/usr/bin/python

import re

test_string = "frame=  305 fps=101 q=31.0 size=    1441kB time=12.76 bitrate= 925.2kbits/s "

time_elapsed = ".*?time=([+-]?\\d*\\.\\d+)(?![-+0-9\\.])"

rg = re.compile(time_elapsed, re.DOTALL)
m = rg.search(test_string)
if m:
    time = m.group(1)
    print time
