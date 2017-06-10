FileDialog
==========
The FileDialog widget provides a dialog useful for selecting of files. These are commonly used when a user wants to open or save a file within the application.

===========
Constructor
===========
Construction of the FileDialog widget is made using::

  filedialog = QFileDialog()

=======
Methods
=======
The FileDialog can be opened using the method::

  filedialog.open()

To define whether the dialog is to be used for opening or saving files call::

  filedialog.setAcceptMode(mode)

The *mode* value should be set to one of:

* ``QFileDialog.AcceptOpen``
* ``QFileDialog.AcceptSave``

Text can be displayed in the FileDialog indicating the purpose with::

  filedialog.setLabelText(text)

A default suffix can be added for display if no other suffix is currently in use via::

  filedialog.setDefaultSuffix(suffix)

The *suffix* parameter should be a string and is commonly used to identify the type of file such as '.txt', '.odt', or '.png' for example.

Configuration of the displayed information within the FileDialog can be done with::

  filedialog.setViewMode(mode)

The *mode* in this case can be set to:

* ``QFileDialog.Detail`` - display an icon, name, and details for each item.
* ``QFileDialog.List`` - display icon and name only.

In some cases, the requirement will be that the dialog only display certain file types. The :doc:`dir` object can be set with::

  filedialog.setFilter(filter)

=======
Example
=======
Below is an example of a FileDialog:

.. literalinclude:: _examples/filedialog.py

Download: :download:`FileDialog <_examples/filedialog.py>`
