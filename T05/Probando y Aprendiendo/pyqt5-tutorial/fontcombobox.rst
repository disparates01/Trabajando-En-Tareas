FontComboBox
============
The FontComboBox widget provides a way for a user to select a font family from a dropdown list. It is often used within :doc:`toolbar` widgets in applications such as word processors to allow the user to change fonts.

===========
Constructor
===========
The constructor for the FontComboBox is::

  fontcombobox = QFontComboBox()

=======
Methods
=======
The font set on the FontComboBox is retrievable with::

  fontcombobox.currentFont()

A font can also be preset programmatically using::

  fontcombobox.setCurrentFont(font)

The *font* parameter should be set to a :doc:`font` object holding the related information.

By default, all fonts installed on the system are shown. These can be filtered using::

  fontcombobox.setFontFilters(filters)

The *filters* parameter should be set to one of:

* ``QFontComboBox.AllFonts`` - show all fonts.
* ``QFontComboBox.ScalableFonts`` - show scalable fonts.
* ``QFontComboBox.NonScalableFonts`` - show non-scalable fonts.
* ``QFontComboBox.MonospacedFonts`` - show monospaced fonts.
* ``QFontComboBox.ProportionalFonts`` - show proportional fonts.

=======
Example
=======
Below is an example of a FontComboBox:

.. literalinclude:: _examples/fontcombobox.py

Download: :download:`FontComboBox <_examples/fontcombobox.py>`
