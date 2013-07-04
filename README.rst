kettlefish
==========

Python script which takes a string of Remyspeak and translates to
human-readable format.

Usage
-----

Translate some Remyspeak::

    ./kettlefish.py wat

Translate Remyspeak with characters like ``'`` and ``?``::

    ./kettlefish.py "What kind of cycles do you have?"

Translate without displaying the ACSII Remy head::

    # Can use -n or --nohead option.
    ./kettlefish.py Fuck this. -n

Translate with text-to-speech via espeak::

    # Can use -s or --speak option.
    ./kettlefish.py wat -s

License
-------

AGPL / Garlands of Freedom

Contributors
------------

-   David Gay (oddshocks)

-   Ralph Bean (threebean)

-   Luke Macken (lmacken)

-   Nate Case (Qalthos)
