ListWidget
==========
A ListWidget is a simple list widget which provides an easy way to display a number of items, of which one or more can be selected.

===========
Constructor
===========
Constructing the ListWidget is done by::

  listwidget = QListWidget()

=======
Methods
=======
Item can be added to the ListWidget via several different methods::

  listwidget.addItem(text)
  listwidget.addItem(item)
  listwidget.addItems(text, text, ...)
  listwidget.insertItem(row, text)
  listwidget.insertItem(row, item)
  listwidget.insertItems(row, text, text, ...)

The first method takes a string of text as the parameter and adds it to the list. The second method takes a :doc:`listwidgetitem` as a parameter to display. The final method takes several strings of text and adds each one as a single item to the ListWidget. The 'insert' methods work in the same way, with the additional integer value indicating the row at which the item is to be added.

Removal of items from the list is done by passing the :doc:`listwidgetitem` object in the method::

  listwidget.removeItemWidget(item)

If editing of items is permitted, the item to edit can be declared via::

  listwidget.editItem(item)

The number of items currently in the list can be retrieved with::

  listwidget.count()

To enable sorting of the items in the list call::

  listwidget.sortingEnabled(enabled)

The direction of the sort can also be configured by::

  listwidget.sortItems(order)

The *order* parameter should be set to one of:

* ``Qt.AscendingOrder``
* ``Qt.DescendingOrder``

Items in the list can be programatically selected via their row number with::

  listwidget.setCurrentRow(row)

The *row* value should be the number identifying the item in the list, with ``0`` indicating the first item should be selected.

The current row selected can also be retrieved::

  listwidget.currentRow()

Items can be selected based on their ListWidgetItem object via::

  listwidget.setCurrentItem(item)

Alternatively, the current item can be fetched when selected by the method::

  listwidget.currentItem()

=======
Example
=======
Below is an example of a ListWidget:

.. literalinclude:: _examples/listwidget.py

Download: :download:`ListWidget <_examples/listwidget.py>`
