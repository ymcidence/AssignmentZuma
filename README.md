# AssignmentZuma

This repo is for the assignment of playing magic card.

Note that:
- For the convenience of visualization, **4** legitimate colours are defined in `tools.COLOURS`. One may modify it to add more colours as long as they are supported by graphviz.
- `have_a_try.py` randomly generates a sequence of balls with random colours, and then feeds them to `tools.spell_magic`. One may handcraft the sequence with any length he likes.


## Pre-requests
- Python 3
- `pip install graphviz` (**for visualization only**)

## Where?
`tools.spell_magic` is the function for the expected input/output.

## Have a Try
Simply run 
```
python ./have_a_try.py
```
and you will probably find something from the console:
```
The input balls are coloured as:
['yellow', 'yellow', 'red', 'lightgrey', 'lightblue2', 'lightgrey', 'lightgrey', 'yellow', 'lightgrey', 'lightgrey', 'yellow', 'yellow', 'red', 'lightblue2', 'yellow', 'yellow', 'lightblue2', 'lightblue2', 'red', 'red']
Best cast: lightgrey ===> yellow
Max elimination length: 7
```
with the following two pictures before and after the magic card.

*before_magic_card*
![f1](pics/before.png)
*after_magic_card*
![f2](pics/after.png)

