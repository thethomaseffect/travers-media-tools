#!/usr/bin/python

import re

#txt=' Duration: 00:02:17.30, start: 0.000000, bitrate: 4283 kb/s'
txt = "  Duration: 00:02:17.30, start: 0.000000, bitrate: 4283 kb/s"

duration_regex = '.*?Duration: (\\d+):(\\d+):(\\d+).*?'

rg = re.compile(duration_regex, re.IGNORECASE | re.DOTALL)
m = rg.search(txt)
if m:
    total_seconds = ((int(m.group(1)) * 3600) + (int(m.group(2)) * 60) + int(m.group(3)))
    print (total_seconds)
