CheckBox
========
A CheckBox provides a checked or unchecked state, indicated via a tick in a box. These are commonly used to indicate when a feature is enabled.

===========
Constructor
===========
Constructing the CheckBox is done with the following statement::

  checkbox = QCheckBox(text)

The *text* parameter is optional. When included, the CheckBox will be displayed with an associated textual label, typically indicating the purpose of the option.

=======
Methods
=======
The text associated with the CheckBox can be set after construction by calling::

  checkbox.setText(text)

Adjusting the CheckBox state programmatically is done with the method::

  checkbox.setChecked(checked)

When *checked* is set to ``True``, the CheckBox will contain a ticket in the box.

To get the state of the CheckBox, use::

  checkbox.isChecked()

A tick in the CheckBox will return ``True`` from the method, while ``False`` is returned when the CheckBox is unchecked.

By default, a CheckBox can be true or false. A third (tri-state) is possible, and is enabled using::

  checkbox.setTristate(tristate)

When *tristate* is set to ``True``, the CheckBox will display a line through the indicator box. The tri-state is commonly used to show a mismatch between other set options.

To check whether a CheckBox is enabled for tri-state, use the method::

  checkbox.isTristate()

The ``.ischecked()`` method can only be used for CheckBox widgets which do not use the tri-state setting. To obtain the state when tri-state is being used, call::

  checkbox.checkState()

A tri-state enabled CheckBox status can be set using the method::

  checkbox.setCheckState(state)

The state should be set to one of the following values:

* ``Qt.Unchecked`` - the item is not checked.
* ``Qt.PartiallyChecked`` the item is in a partial checked state.
* ``Qt.Checked`` - the item is checked.

=======
Example
=======
Below is an example of a CheckBox:

.. literalinclude:: _examples/checkbox.py

Download: :download:`CheckBox <_examples/checkbox.py>`
