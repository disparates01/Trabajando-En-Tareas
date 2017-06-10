Color
=====
The Color object provides a way for Qt to represent colours. It supports RGB, CMYK, and HSV values, and is used by the :doc:`colordialog` to represent colours being displayed.

===========
Constructor
===========
The constructor for the Color object is::

  color = QColor()

Once initialised, the Color object defaults to ``0, 0, 0`` RGB.

Alternatively, a colour can be defined on the object at constructed with::

  color = QColor(red, green, blue)

The *red*, *green*, and *blue* values should be an integer value between ``0`` and ``255``.

=======
Methods
=======
The colour values can be retrieved from the Color object with::

  color.red()
  color.blue()
  color.green()
  color.yellow()
  color.black()
  color.cyan()
  color.magenta()

The colour values are settable post-construction via::

  color.setRed(red)
  color.setBlue(blue)
  color.setGreen(green)
  color.setYellow(yellow)
  color.setBlack(black)
  color.setCyan(cyan)
  color.setMagenta(magenta)

Hue, saturation and value numbers can also be fetched from the Color object::

  color.hue()
  color.saturation()
  color.value()

HSV numbers are also set with the methods::

  color.setHue(hue)
  color.setSaturation(saturation)
  color.setValue(value)

The transparency of the colour is fetched if required via::

  color.alpha()

Alpha transparency is set using::

  color.setAlpha(alpha)
