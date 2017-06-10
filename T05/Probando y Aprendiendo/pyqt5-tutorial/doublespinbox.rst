DoubleSpinBox
=============
A DoubleSpinBox is much like a regular :doc:`spinbox`, however it is used to handle double type numbers. It supports numerical entry via the keyboard, or using the adjustment buttons built into the widget.

===========
Constructor
===========
The DoubleSpinBox widget is constructed with the call::

  doublespinbox = QDoubleSpinBox()

=======
Methods
=======
Setting a value on the DoubleSpinBox is done using::

  doublespinbox.setValue(value)

If the *value* paramter is out of the minimum and maximum boundaries, the value will be adjusted so that it fits between the minimum and maximum.

The value set in the DoubleSpinBox is retrievable via the use of::

  doublespinbox.value()

Minimum and maximum values are defined for the DoubleSpinBox using::

  doublespinbox.setMinimum(value)
  doublespinbox.setMaximum(value)

If both minimum and maximum values are required, the range can be defined in a single method::

  doublespinbox.setRange(minimum, maximum)

A prefix and suffix can be displayed within the DoubleSpinBox::

  doublespinbox.setPrefix(suffix)
  doublespinbox.setSuffix(suffix)

The *prefix* and *suffix* parameters should be set to a string. It is useful when displaying a unit associated with the value (e.g. "mph", "cm").

By default, the adjustment arrows change the displayed value by 1. The step can be changed with::

  doublespinbox.setSingleStep(value)

=======
Example
=======
Below is an example of a DoubleSpinBox:

.. literalinclude:: _examples/doublespinbox.py

Download: :download:`DoubleSpinBox <_examples/doublespinbox.py>`
