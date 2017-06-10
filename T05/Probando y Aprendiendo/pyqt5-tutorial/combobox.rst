ComboBox
========
A ComboBox provides a dropdown menu attached to a button, providing a list of options of which one can be selected by the user.

===========
Constructor
===========
The ComboBox widget is created by defining::

  combobox = QComboBox()

=======
Methods
=======
Individual items are added to the ComboBox using the methods::

  combobox.addItem(text)
  combobox.insertItem(index, text)

The *text* value should be set to the string of text which is to be added to the ComboBox. The ``.insertItem()`` method also allows for an *index* value to be specified which indicates where the item will be inserted.

An alternative is to add multiple items with a single method::

  combobox.addItems(text, text, text...)
  combobox.insertItems(index, text, text, text...)

Separators can be inserted into a specific position within the ComboBox popup with::

  combobox.insertSeparator(index)

Removal of items is done with the method::

  combobox.removeItem(index)

The *index* defines the location of the item to be removed held within the ComboBox, with ``0`` pointing to the first item.

The currently selected index or text is retrievable with the following::

  combobox.currentIndex()
  combobox.currentText()

To retrieve the number of items held within the ComboBox use::

  combobox.count()

The number of items permitted, and the maximum visible within the ComboBox is set by::

  combobox.setMaxCount(maximum)
  combobox.setMaxVisibleItems(maximum)

The *maximum* value should be an integer value indicating the limit. If the number of items added is greater than the maximum amount, the extra items are truncated.

The ComboBox popup menu can be shown or hidden programmatically with::

  combobox.showPopup()
  combobox.hidePopup()

Auto-completion functionality with the :doc:`completer` object can be added to the ComboBox widget with::

  combobox.setCompleter(completer)

By default, duplicate items are not allowed in the ComboBox, however this can be toggled using::

  combobox.setDuplicatesEnabled(enable)

The ComboBox can display an integrated :doc:`lineedit` to allow the user to enter items which are not provided in the dropdown menu using::

  combobox.setEditable(editable)

A LineEdit manually constructed can be added ot the ComboBox via the method::

  combobox.setLineEdit(lineedit)

The LineEdit object can be obtained from the ComboBox by calling::

  combobox.lineEdit()

Control over whether a user-added item should appear in the ComboBox can be set with the method::

  combobox.setInsertPolicy(policy)

The *policy* parameter should be set to one of the following:

* ``QComboBox.NoInsert`` - the item will not be inserted into the ComboBox.
* ``QComboBox.InsertAtTop`` - item will be added as the first in the ComboBox.
* ``QComboBox.InsertAtCurrent`` - item will be replaced by the new string.
* ``QComboBox.InsertAtBottom`` - item will be added as the last in the ComboBox.
* ``QComboBox.InsertAfterCurrent``  insert after current item in the ComboBox.
* ``QComboBox.InsertBeforeCurrent`` - insert before the current item in the ComboBox.
* ``QComboBox.InsertAlphabetically`` - insert item in alphabetical ordering.

If the data is being held by a model, this can be attached to the ComboBox with::

  combobox.setModel(model)

The column number of the data within the model should also be specified::

  combobox.setModelColumn(column)

By default, the *column* value is automatically set to ``0`` to indicate the first column of data. If the data to be displayed is held in a different column, define the integer value for that column.

=======
Example
=======
Below is an example of an ComboBox:

.. literalinclude:: _examples/combobox.py

Download: :download:`ComboBox <_examples/combobox.py>`
