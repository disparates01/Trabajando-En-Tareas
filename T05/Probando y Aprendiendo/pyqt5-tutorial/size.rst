Size
====
The Size object is used to contain the width and height values, amongst other parameters, for display on the interface.

===========
Constructor
===========
Construction of the Size object is made via::

  size = QSize()

=======
Methods
=======
Width and height values can be set with the methods::

  size.setWidth(width)
  size.setHeight(height)

The stored values can also be fetched by calling::

  size.width()
  size.height()

A reference width or height can also be obtained, which allows updating of the width and height values directly with::

  size.rWidth()
  size.rHeight()

The size values stored can be checked for zero or lower with the methods::

  size.isNull()
  size.isEmpty()

To check wheter a valid size is being stored, with a width and height greater than zero use::

  size.isValid()

Scaling of the Size object can be done with::

  size.scale(width, height, mode)

The *width* and *height* specify the scaled width and height values in pixels. The *mode* values set how to obey and original size and should be set to one of the constants:

* ``Qt.IgnoreAspectRatio`` - the aspect ratio is not preserved.
* ``Qt.KeepAspectRatio`` - preserve the aspect ratio making the content as large as possible for the pixel values defined.
* ``Qt.KeepAspectRatioByExpanding`` - resize preserving the aspect ratio to the largest pixel values defined.
