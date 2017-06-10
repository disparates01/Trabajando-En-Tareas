Image
=====
The Image widget provides a way to display images within a Qt application.

.. note::

  There are actually four classes which handle the loading of images. These are:

  * ``QImage`` - optimised for input/output.
  * ``QPixmap`` - designed for showing images on screen.
  * ``QBitmap`` - inherits from QPixmap with a depth of 1.
  * ``QPicture`` - paint device to record and replay QPainter commands.

===========
Constructor
===========
Construction of an empty Image widget is made using::

  image = QImage()

An Image with a specified size and format, but containing no data can also be made using::

  image = QImage(size, format)
  image = QImage(width, height, format)

The *size* parameter takes a :doc:`size` object. Alternatively, a *width* and *height* integer can be specified instead of the QSize object being used.

A file can be loaded from disk using the filename specification::

  image = QImage(filename)

=======
Methods
=======
Loading of a file from disk post-construction can be made with::

  image.load(filename)

The width and height of the Image can be obtained using the methods::

  image.width()
  image.height()

Alternatively, both sizes can be obtained with a single call::

  image.size()

A check can be made to see whether any data is loaded via::

  image.isNull()

If the method returns ``True``, no image data has been loaded.

A function is also available to check whether the image is grayscale::

  image.isGrayscale()

The function will return ``True`` if all colours are shades of gray.

Mirroring of images is also supported by the call::

  image.mirrored(horizontal, vertical)

Te *horizontal* and *vertical* can be set to ``True`` or ``False``. The image will be mirrored along the direction when set to ``True``.

Copying of the image object is supported by a call to::

  image.copy(x, y, width, height)

The *x*, *y*, *width* and *height* paramters are all optional. When the co-ordinates are specified, the image is copied from those positions. The width and height specifies the size of the copy.

=======
Example
=======
Below is an example of a Image:

.. literalinclude:: _examples/image.py

Download: :download:`Image <_examples/image.py>`
