FontDialog
==========
The FontDialog widget provides a widget for selecting a font, including the font type, the size, and features such as bold or italic styling. The dialog provides an area for previewing the selected font.

===========
Constructor
===========
Construction of the FontDialog is made using::

  fontdialog = QFontDialog(parent)

The *parent* argument supplied indicates the widget (i.e. window) which owns the FontDialog.

=======
Methods
=======
The FontDialog is opened using::

  fontdialog.open()

The current font can be set onto the FontDialog with::

  fontdialog.setCurrentFont(font)

Use of the *font* parameter requires a :doc:`font` object.

Retrieval of the font from the dialog is done via::

  fontdialog.currentFont()

Alternatively, the returned font from the dialog when the user presses the OK button is able to be fetched using::

  fontdialog.selectedFont()

Options customising the dialog state is done using::

  fontdialog.setOptions(options)

The *options* value can be set to one or more of the following constants:

* ``QFontDialog.NoButtons`` - do not show any OK or Cancel buttons.
* ``QFontDialog.DontUseNativeDialog`` - use Qt dialog rather than the native platform dialog.
* ``QFontDialog.ScalableFonts`` - show scalable fonts.
* ``QFontDialog.NonScalableFonts`` - show non-scalable fonts.
* ``QFontDialog.MonospacedFonts`` - show monospaced fonts.
* ``QFontDialog.ProportionalFonts`` - show proportional fonts.

Retrieval of the options from the dialog is done by calling::

  fontdialog.options()

=======
Example
=======
Below is an example of a FontDialog:

.. literalinclude:: _examples/fontdialog.py

Download: :download:`FontDialog <_examples/fontdialog.py>`
