SpinBox
=======
The SpinBox widget provides a way to enter numerical data. Thw widget provides integrated adjustment buttons which allow the user to adjust the number by clicking the arrows, while also allowing adjustment by typing into a text entry.

A :doc:`doublespinbox` can be used if the value to be stored is a double type.

===========
Constructor
===========
The SpinBox is constructed with the call::

  spinbox = QSpinBox()

=======
Methods
=======
Setting a value on the SpinBox is done using::

  spinbox.setValue(value)

If the *value* paramter is out of the minimum and maximum boundaries, the value will be adjusted so that it fits between the minimum and maximum.

Retrieval of the value set in the SpinBox is fetched via::

  spinbox.value()

Minimum and maximum values are defined for the SpinBox using::

  spinbox.setMinimum(value)
  spinbox.setMaximum(value)

Alternatively, the range can be defined using a single call::

  spinbox.setRange(minimum, maximum)

If required, the minimum and maximum values permissible in the SpinBox are found by calling::

  spinbox.minimum()
  spinbox.maximum()

A prefix and suffix can be displayed within the SpinBox::

  spinbox.setPrefix(suffix)
  spinbox.setSuffix(suffix)

The *prefix* and *suffix* parameters should be set to a string. It is useful when displaying a unit associated with the value (e.g. "mph", "cm").

By default, the adjustment arrows change the displayed value by 1. The step can be changed with::

  spinbox.setSingleStep(value)

=======
Example
=======
Below is an example of a SpinBox:

.. literalinclude:: _examples/spinbox.py

Download: :download:`SpinBox <_examples/spinbox.py>`
