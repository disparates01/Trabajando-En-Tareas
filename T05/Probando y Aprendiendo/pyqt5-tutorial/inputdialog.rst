InputDialog
===========
The InputDialog is used to retrieve a single value from the user.

===========
Constructor
===========
The constructor for the InputDialog is::

  inputdialog = QInputDialog(parent)

A *parent* can be defined which associates the InputDialog with a parent window.

=======
Methods
=======
To run the InputDialog, call::

  inputdialog.open()

The OK and Cancel button text is set with the methods::

  inputdialog.setOkButtonText(text)
  inputdialog.setCancelButtonText(text)

Label text should also be provided to indicate to the user what the dialog purpose is::

  inputdialog.setLabelText(label)

The input method defines the data handling of the dialog::

  inputdialog.setInputMode(mode)

The *mode* value should be set to one of the following:

* ``QInputDialog.TextInput``
* ``QInputDialog.IntInput``
* ``QInputDialog.DoubleInput``

The text value is set on the dialog via::

  inputdialog.setTextValue(text)

Entered text is retrieved from the dialog with::

  inputdialog.textValue()

If the InputDialog is being used in int mode, the value is set with the method::

  inputdialog.setIntValue(value)

Retrieving the integer value is done by calling::

  inputdialog.intValue()

The minimum and maximum values can be defined using::

  inputdialog.setIntMinimum(minimum)
  inputdialog.setIntMaximum(maximum)
  inputdialog.setIntRange(minimum, maximum)

A step value determines the amount that the value is adjusted::

  inputdialog.setIntStep(step)

When used in double mode, the InputDialog value is set by::

  inputdialog.setDoubleValue(value)

The double value set on the dialog is retrieved via::

  inputdialog.doubleValue()

Double value minimum and maximum numbers are specified with::

  inputdialog.setDoubleMinimum(minimum)
  inputdialog.setDoubleMaximum(maximum)
  inputdialog.setDoubleRange(minimum, maximum)

The InputDialog can also be used for retrieval of items from a combobox by defining the items::

  inputdialog.setComboBoxItems(item, ...)

Multiple items can be specified to be added to the combobox.

If the combobox should also provide an entry to allow the user to enter text, use::

  inputdialog.setComboBoxEditable(editable)
