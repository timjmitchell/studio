Source: https://music21.org/music21docs/moduleReference/moduleIpython21.html

# music21.ipython21

IPython/Jupyter extension to music21. In Jupyter Notebook call:

> %load\_ext music21.ipython21

and show will take place inside the browser.

Since at least music21 v5, however, when music21 is imported we set a timer
for two seconds to everything to settle and then load our extension (which
now just calls matplotlib inline)

## Functions

music21.ipython21.loadNoMagic()[[source]](../_modules/music21/ipython21.html#loadNoMagic)
:   Load the magic functions of load\_ipython\_extension when running Jupyter (was IPython)
    without needing to call a %magic function

    Safest is always ot call %load\_ext music21.ipython21 anyhow.
