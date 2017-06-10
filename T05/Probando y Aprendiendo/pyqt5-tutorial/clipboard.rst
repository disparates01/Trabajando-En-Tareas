Clipboard
=========
The Clipboard object provides access to the system clipboard, allowing data to be copied and pasted between applications.

.. note::

  The Clipboard support differs across platforms, such as Windows not supporting primary selection unlike X11. Some features may behave differently or be entirely unsupported.

===========
Constructor
===========
Construction of the Clipboard object is made using::

  clipboard = QClipboard()

=======
Methods
=======
Data is set on the Clipboard using a number of calls depending on the data type::

  clipboard.setText(text, mode)
  clipboard.setImage(image, mode)
  clipboard.setPixmap(pixmap, mode)
  clipboard.setMimeData(mimedata, mode)

The *mode* parameter controls which part of the Clipboard is used, and should be set to:

* ``QClipboard.Clipboard`` - store and retrieve from the global clipboard.
* ``QClipboard.Selection`` - store and retrieve from the mouse selection (X11 and others).
* ``QClipboard.FindBuffer`` - store and retrieve from the Find buffer (OS X).

Data is also retrievable from the Clipboard with::

  clipboard.text(mode)
  clipboard.image(mode)
  clipboard.pixmap(mode)
  clipboard.mimeData(mode)

The contents of the Clipboard can be cleared via the method::

  clipboard.clear()
