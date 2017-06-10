TreeWidget
==========
The TreeWidget is similar to a :doc:`listwidget`, however it allows data to be stored across multiple columns as well as rows.

===========
Constructor
===========
Construction of the TreeWidget with::

  treewidget = QTreeWidget()

=======
Methods
=======
The TreeWidget takes :doc:`treewidgetitem` objects to be added to the TreeWidget::

  treewidget.addTopLevelItem(item)
  treewidget.insertTopLevelItem(index, items)
  treewidget.addTopLevelItems(items)
  treewidget.insertTopLevelItems(index, items)

The ``.insertTopLevelItem()`` and ``.insertTopLevelItems()`` methods take an *index* which specifies the position of the rows to be added. The ``.addTopLevelItems()`` and ``.insertTopLevelItems`` take a list of values to be added while the other two functions provide for a single item to be added.

An item can be removed from the TreeWidget using::

  treewidget.removeItemWidget(item, index)

The *index* specifies the position of the item to be removed from the TreeWidget.

Column titles can be specified by calling::

  treewidget.setHeaderLabels(labels)

The *labels* parameter passes a list of title for each columns. If there are not enough labels for each column, then some columns will remain titleless.

Items within the view can be sorted with a call to::

  treewidget.sortItems(column, order)

The *column* value defines the column to be sorted by number, and the *order* sets the method which should be one of the following constants:

* ``Qt.AscendingOrder``
* ``Qt.DescendingOrder``

Setting of the current item can be done with the functions::

  treewidget.setCurrentItem(item)
  treewidget.setCurrentItem(item, column)

Both methods take a TreeWidgetItem as the *item*, with the second method also allowing a column value to be specified.

The current item in the TreeWidget can be fetched by using the method::

  treewidget.currentItem()

=======
Example
=======
Below is an example of a TreeWidget:

.. literalinclude:: _examples/treewidget.py

Download: :download:`TreeWidget <_examples/treewidget.py>`
