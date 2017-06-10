FormLayout
==========
The FormLayout provides a class layout to handle input widgets and their associated labels. The children are laid out in two columns, with the label column handling the label and the right column providing space for the input widgets such as text entries or spin boxes.

===========
Constructor
===========
The construction call for the FormLayout is::

  formlayout = QFormLayout()

=======
Methods
=======
Rows can be added to the container using::

  formlayout.addRow(label, widget)
  formlayout.addRow(text, widget)
  formlayout.addRow(widget)

An alternative method of adding rows allows for the position of the new row being inserted to be defined::

  formlayout.insertRow(row, label, widget)
  formlayout.insertRow(row, text, widget)
  formlayout.insertRow(row, widget)

The *widget* parameter can be a widget or another container. The *label* should be set to the :doc:`label` which is to be shown. Alternatively, *text* can be defined which automatically creates the label.

The spacing provided vertically or horizontally, or both can be set via::

  formlayout.setVerticalSpacing(spacing)
  formlayout.setHorizontalSpacing(spacing)
  formlayout.setSpacing(spacing)

The handling of how the fields grow based on size is controlled via the method::

  formlayout.setFieldGrowthPolicy(policy)

The *policy* parameter can be set to one of the following:

* ``QFormLayout.FieldsStayAtSizeHint`` - the fields never grow beyond their size hint.
* ``QFormLayout.ExpandingFieldsGrow`` - when set to expand, the fields will grow to fill the available space.
* ``QFormLayout.AllNonFixedFieldsGrow`` - all fields will grow to fill the available space.

=======
Example
=======
Below is an example of a FormLayout:

.. literalinclude:: _examples/formlayout.py

Download: :download:`FormLayout <_examples/formlayout.py>`
