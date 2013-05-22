#!/usr/bin/python

import re

test_string = 'frame=  305 fps=101 q=31.0 size=    1441kB time=12.76 bitrate= 925.2kbits/s '

non_greedy_filler = '.*?'   # Non-greedy match on filler
frame_int = '(\\d+)'    # Integer Number 1
fps_int = '(\\d+)'    # Integer Number 2
q_float = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 1
size_int = '(\\d+)'    # Integer Number 3
time_float = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 2
bitrate_float = '([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'  # Float 3

rg = re.compile(
    non_greedy_filler + frame_int + non_greedy_filler + fps_int +
    non_greedy_filler + q_float + non_greedy_filler + size_int +
    non_greedy_filler + time_float + non_greedy_filler + bitrate_float,
    re.IGNORECASE | re.DOTALL)
print(rg)
m = rg.search(test_string)
if m:
    int1 = m.group(1)
    int2 = m.group(2)
    float1 = m.group(3)
    int3 = m.group(4)
    float2 = m.group(5)
    float3 = m.group(6)
    print "(" + int1 + ")" + "(" + int2 + ")" + "(" + float1 + ")" + "(" + \
          int3 + ")" + "(" + float2 + ")" + "(" + float3 + ")"
