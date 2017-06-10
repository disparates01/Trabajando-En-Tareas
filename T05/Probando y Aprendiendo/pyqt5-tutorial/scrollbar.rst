ScrollBar
=========
A ScrollBar provides a way to move horizontally or vertically within a frame where the content is to large to fit. The ScrollBar typically includes a bar with arrows buttons to move the view. A bar is also provided within to drag-and-drop into a new position.

===========
Constructor
===========
The ScrollBar is constructed using the call::

  scrollbar = QScrollBar()

The orientation can also be defined at construction time via::

  scrollbar = QScrollBar(orientation)

The *orientation* parameter should be set to one of the following:

* ``Qt.Horizontal``
* ``Qt.Vertical``

=======
Example
=======
Below is an example of a ScrollBar:

.. literalinclude:: _examples/scrollbar.py

Download: :download:`ScrollBar <_examples/scrollbar.py>`
