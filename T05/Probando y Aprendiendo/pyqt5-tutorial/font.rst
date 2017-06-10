Font
====
The Font object is used to represent a font style, size, and properties that have been set. It is commonly used by the :doc:`fontcombobox` and :doc:`fontdialog` widgets.

===========
Constructor
===========
Construction of the Font object is made by::

  font = QFont()

The base options within the Font can be set at construction by calling::

  font = QFont(family, pointsize, weight, italic)

=======
Methods
=======
Font settings such as bold, italics, underlines, weight and more can be set using the following methods::

  font.setBold(bold)
  font.setCapitalization(capitalization)
  font.setItalic(italic)
  font.setKerning(kerning)
  font.setOverline(overline)
  font.setStretch(strecth)
  font.setStrikeOut(strikeout)
  font.setUnderline(underline)

Each of the parameters takes ``True`` or ``False`` to set the enabled/disabled state.

A font family can be defined with the call::

  font.setFamily(family)

Typically, the family argument will be a specific font name, or a generic such as 'sans' or 'sans-serif'.

The pixel and point sizes can be defined with::

  font.setPixelSize(size)
  font.setPointSize(size)

Font weight can be defined with an integer value via::

  font.setWeight(weight)

The *weight* of standard size is usually ``400``, with higher values making the font bolder, and lower values making it thinner.

Retrieval of the options set within the Font object can be made by::

  font.bold()
  font.capitalization()
  font.family()
  font.italic()
  font.kerning()
  font.overline()
  font.pixelSize()
  font.pointSize()
  font.stretch()
  font.strikeOut()
  font.underline()
