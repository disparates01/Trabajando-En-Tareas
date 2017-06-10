TimeEdit
========
The TimeEdit widget provides an editable box from which time value can be displayed and edited.

===========
Constructor
===========
The constructor for the TimeEdit is::

  timeedit = QTimeEdit()

=======
Methods
=======
The time is settable on the widget via::

  timeedit.setTime(time)

Time is also retrievable from the TimeEdit using::

  timeedit.time()

Minimum and maximum permissable time values can be set to define a range with the methods::

  timeedit.setMinimumTime(minimum)
  timeedit.setMaximumTime(maximum)

The *minimum* and *maximum* values should be set to an appropriate :doc:`time` object which contains the defined time values.

The ranges defined for minimum and maximum times are cleared with::

  timeedit.clearMinimumTime()
  timeedit.clearMaximumTime()

=======
Example
=======
Below is an example of a TimeEdit:

.. literalinclude:: _examples/timeedit.py

Download: :download:`TimeEdit <_examples/timeedit.py>`
