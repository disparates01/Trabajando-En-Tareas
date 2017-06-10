Dialog
======
A Dialog is effectively similar to a :doc:`window` in appearance. It is commonly used in very simple applications, or as a sub-window (e.g. preferences) of an application.

===========
Constructor
===========
The Dialog window is constructed with the call::

  dialog = QDialog()

=======
Methods
=======
In certain circumstances, it may be useful to prevent the user from interacting with any other windows apart from the dialog. This is called modal operation, and defaults to False. To set the Dialog as modal use::

  dialog.setModal(modal)

The modal state of the Dialog can be retrieved using::

  dialog.isModal()

To allow users to easily resize the Dialog, a :doc:`sizegrip` can be added::

  dialog.sizeGripEnabled(enabled)

When *enabled* is set as ``True``, the SizeGrip will be added.

The Dialog can be run with::

  dialog.open()

The result code of the Dialog will be fetched using::

  dialog.result()

The result code is returned when the Dialog is closed, providing a value to work with which specifies the user response. For example, if the user accepted or rejected a question, a response result will be returned which can then be handled.

A result can also be set::

  dialog.setResult(result)

The *result* parameter can be set to any integer number, however the following values are recommended:

* ``0`` - Rejected
* ``1`` - Accepted

=======
Example
=======
Below is an example of a Dialog:

.. literalinclude:: _examples/dialog.py

Download: :download:`Dialog <_examples/dialog.py>`
