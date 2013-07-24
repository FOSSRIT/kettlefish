#!/usr/bin/python
# -*- coding: utf8 -*-

import argparse
import collections
import os
import re
import string


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


# These have to go first, or they will get overridden by later keys.
REMYSPEAK = collections.OrderedDict({
        "(ye )?new(e)?( )?biz": "new orders of business",
        "cycle on": "spend time on",
        "open loop": "unfinished task",
})
# Order-insensitive keys
REMYSPEAK.update({
        "what's good": "how are you",
        "kettle of fish": "matter",
        "cycle": "period of time",
        "cycles": "time available to spend on work",
        "loop": "task",
        "loops": "current tasks",
        "motherfucker": "fellow",
        "biz": "five",
        "hunny": "a hundred",
        "hundo": "a hundred",
        "step out": "smoke",
        "homeboy": "dude",
        "homegirl": "girl",
        "wat": "what",
        "chops": "skills",
        "foo": "skill",
        "step outside": "smoke",
        "fuck this": "education is important",
        "<buzzer>": "nope",
        "buzzer": "nope",
        "lolz": "*giggle*",
        "lolol": "haha",
        "lollerskates": "hilarious",
        "minute": "long time",
        "loadstone": "bad luck",
        "lodestone": "bad luck",
        "beverage": "alcohol",
        "beverages": "alcohol",
        "may or may not be": "is",
        'tomo': 'tomorrow',
        'def': 'definitely',
        "&": "leaves",
        "hosed": "destroyed",
        "EoB": "End of Business",
        "moar": "additional",
        "G/B/U": "Good/Bad/Ugly",
})

def translate_remyspeak(text):
    cap_map = [str.lower, str.capitalize, str.upper]
    # figure out casing of input
    if text[0] in string.lowercase:
        case = 0
    elif text[1] in string.lowercase:
        case = 1
    else:
        case = 2

    text = text.lower()
    for item in REMYSPEAK:
        text = re.sub(r'\b{}\b'.format(item), REMYSPEAK[item], text)

    return cap_map[case](text)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('text', nargs="+", help='Remyspeak to be translated.')
    p.add_argument('-n', '--nohead', action='store_true',
                   help='Don\'t print the ASCII Remy head.')
    p.add_argument('-s', '--speak', action='store_true',
                   help='Say it')
    args = p.parse_args()

    if not args.nohead:
        print REMY
    else:
        print "\n"

    result = translate_remyspeak(" ".join(args.text))
    print result
    print "\n"

    if args.speak:
        os.system("espeak %r" % result)
