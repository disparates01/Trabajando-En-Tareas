TableWidget
===========
The TableWidget is a complex widget providing rows and columns of information in a grid-like format. It supports a variety of features such as row and column headers, multiple selections, and sorting functionality.

===========
Constructor
===========
The TableWidget is constructed using the call::

  tablewidget = QTableWidget()

=======
Methods
=======
The number of rows and columns to be displayed by the TableWidget must be declared with the methods::

  tablewidget.setRowCount(count)
  tablewidget.setColumnCount(count)

The number of rows and columns can be obtained from the TableWidget::

  tablewidget.rowCount()
  tablewidget.columnCount()

Hiding individual columns can be done with::

  tablewidget.setColumnHiden(column, hidden)

The *column* value indicates the positional column value, with the first column identified by ``0``. The *hidden* value when set to ``True`` will hide the column from view.

To configured whether the TableWidget grid lines are toggled on or off use::

  tablewidget.setShowGrid(show_grid)

When *show_grid* is set to ``True`` each cell will have a box around it to make identifying rows and columns easier.

The row and column headers are contained as separate objects which are obtained via::

  tablewidget.horizontalHeader()
  tablewidget.verticalHeader()

By default, the TableWidget allows multiple rows to be selected. This can be configured using::

  tablewidget.setSelectionMode(mode)

The *mode* parameter should be set to one of:

* ``QAbstractItemView.NoSelection``
* ``QAbstractItemView.SingleSelection``
* ``QAbstractItemView.ContiguousSelection``
* ``QAbstractItemView.ExtendedSelection``
* ``QAbstractItemView.MultiSelection``

Also default is the ability to edit the contents of a cell when selected. This is set with the method::

  tablewidget.setEditTriggers(triggers)

The *triggers* value can be set to one of the following:

* ``QAbstractItemView.NoEditTriggers`` - no editing possible.
* ``QAbstractItemView.CurrentChanged`` - start editing when the current item changes.
* ``QAbstractItemView.DoubleClicked`` - start editing when item is double-clicked.
* ``QAbstractItemView.SelectedClicked`` - start editing when clicking an already selected item.
* ``QAbstractItemView.EditKeyPressed`` - start editing when platform edit key is pressed.
* ``QAbstractItemView.AnyKeyPressed`` - start editing when any key is pressed.
* ``QAbstractItemView.AllEditTriggers`` - start editing when any of the above are activated.

=======
Example
=======
Below is an example of a TableWidget:

.. literalinclude:: _examples/tablewidget.py

Download: :download:`TableWidget <_examples/tablewidget.py>`
