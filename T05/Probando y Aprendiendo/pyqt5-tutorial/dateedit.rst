DateEdit
========
The DateEdit widget allows date information to be displayed and changed.

===========
Constructor
===========
Construction of the DateEdit is made using::

  dateedit = QDateEdit()

=======
Methods
=======
Date information can be set onto the widget using the method::

  dateedit.setDate(date)

The current date set on the DateEdit widget is fetched using::

  dateedit.date()

A range of permissible dates is defined on the DateEdit by calling::

  dateedit.setMinimumDate(date)
  dateedit.setMaximumdate(date)

In both methods, the *date* parameter should be an appropriate :doc:`date` object which defines the date to set.

If required, the minimum and maximum range can be cleared individually using::

  dateedit.clearMinimumDate()
  dateedit.clearMaximumDate()

=======
Example
=======
Below is an example of a DateEdit:

.. literalinclude:: _examples/dateedit.py

Download: :download:`DateEdit <_examples/dateedit.py>`
