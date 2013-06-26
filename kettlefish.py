#!/usr/bin/python
# -*- coding: utf8 -*-

# TODO: Maintain capitalization upon translation.

import argparse

REMY = """
        :oooooooooooo+        
     +hhmNNNNNNNNNNNNNhhy`    
  .--yNNNNNNNNNNNNNNNNNNm:--  
  oNNNNNyoooooooooooooNNNNNm` 
`ymNNNNN+            .mNNNNNh:
.mNNN+   .mNm`   oNN+   .mNNN+
.mNNN+   `+o+    :oo-   .mNNN+
.mNNNo```` .::::::: ````-mNNN+
  oNNNNNNm`oh++++om`oNNNNNNm` 
  oNNNNNo. oNNNNNNm``:NNNNNm` 
  ./NNm:.  oNNNNNNm` `:yNNs-  
    `+hhhhhmNNNNNNNhhhhhy.`   
           :oooooo+           
"""


REMYSPEAK = {
        "what's good": "how are you",
        "kettle of fish": "matter",
        "cycle": "period of time",
        "cycle on": "spend time on",
        "cycles": "time available to spend on work",
        "loop": "task",
        "open loop": "unfinished task",
        "loops": "current tasks",
        "motherfucker": "fellow",
        "homeboy": "dude",
        "wat": "what",
        "chops": "skills",
        "foo": "skill",
        "step outside": "smoke",
        "fuck this": "education is important",
        "<buzzer>": "nope",
        "buzzer": "nope",
        "minute": "long time",
        }

def translate_remyspeak(text):
    text = text.lower()
    for item in REMYSPEAK:
        text = text.replace(item, REMYSPEAK[item])
    return text.capitalize()

p = argparse.ArgumentParser()
p.add_argument('text', nargs="+", help='Remyspeak to be translated.')
p.add_argument('-n', '--nohead', action='store_true',
               help='Don\'t print the ASCII Remy head.')
args = p.parse_args()

if not args.nohead:
    print REMY
else:
    print "\n"

print translate_remyspeak(" ".join(args.text))
print "\n"
