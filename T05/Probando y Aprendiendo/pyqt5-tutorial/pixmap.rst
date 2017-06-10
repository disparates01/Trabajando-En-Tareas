Pixmap
======
The Pixmap object represents an off-screen image that can be loaded for display, typically in an :doc:`image` or other widget.

===========
Constructor
===========
Construction of the Pixmap is made with::

  pixmap = QPixmap()

A width and height can also be defined at construction via::

  pixmap = QPixmap(width, height)

The *widgth* and *height* parameters take integer values for the size declaration.

A :doc:`size` object can also be passed to provide the width and height dimensions with::

  pixmap = QPixmap(size)

=======
Methods
=======
The specified width and height can be obtained via the methods::

  pixmap.width()
  pixmap.height()
  pixmap.size()

The ``.size()`` method returns both values as a tuple.

A Pixmap can be converted into an :doc:`image` object with the call::

  pixmap.toImage()

When a Pixmap is constructed without defined sizes, the Pixmap will be null. This can be checked with::

  pixmap.isNull()
