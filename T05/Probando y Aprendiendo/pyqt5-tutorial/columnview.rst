ColumnView
==========
A ColumnView widget is similar to a :doc:`listwidget`, but it typically contains data which has subitems. Each subitem is placed horizontally within a new ListWidget. This method of displaying information is sometimes called a cascading list.

===========
Constructor
===========
The constructor for the ColumnView is::

  columnview = QColumnView()

=======
Methods
=======
To configure whether display grips are visible, allowing each column to be resized, use::

  columnview.setResizeGripsVisible(visible)

The width of each column can be defined in pixels via::

  columnview.setColumnWidgets(widths)

The *widths* parameter should be set to a list of sizes; one for each column. If the list does not contain enough values for each column, the columns with no value specified will not be modified. If the list contains more values than columns, the extra values will be used for any columns added later.

The widths of each column is defined using::

  columnview.setColumnWidths(width)

The *width* parameter should be a passed list with a value for each column defining the width in pixels.

Returning the column widths from the ColumnView is done using the method::

  columnview.columnWidths()
