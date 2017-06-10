ProgressDialog
==============
The ProgressDialog is similar to the :doc:`progressbar`, with the ProgressBar portion of the widget placed in a dialog window. It is often used when the running process will require the user to wait, with the rest of the application being unavailable to use.

===========
Constructor
===========
Construction of the ProgressDialog is made using::

  progressdialog = QProgressDialog()

=======
Methods
=======
Setting the value of the progress completion is made using the method::

  progressdialog.setValue(value)

The value can also be retrieved with::

  progressdialog.value()

Minimum and maximum values are also required to be assigned to the ProgressDialog to define the range of values permitted::

  progressdialog.setMinimum(minimum)
  progressdialog.setMaximum(maximum)

The ability to automatically close the ProgressDialog is made using::

  progressdialog.setAutoClose(close)

A cancel button can be added to the ProgressDialog via::

  progressdialog.setCancelButton(button)

The *button* argument should be set to an appropriate :doc:`pushbutton`.

Checking whether a ProgressDialog was canceled by the user can be done using the call::

  progressdialog.wasCanceled()

If ``True`` is returned, the user canceled the running process.
