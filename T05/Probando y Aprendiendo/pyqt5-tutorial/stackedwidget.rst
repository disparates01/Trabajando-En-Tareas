StackedWidget
=============
The StackedWidget is a container which displays a single page at a time. A left-hand panel provides access to the pages which are then displayed to the right.

===========
Constructor
===========
Construction of the StackedWidget is done using::

  stackedwidget = QStackedWidget()

=======
Methods
=======
To add an item to the StackedWidget use::

  stackedwidget.addWidget(widget)
  stackedwidget.insertWidget(index, widget)

The *index* value should be set to the numerical position identifying where the widget should be inserted.

Removal of the widget from the StackedWidget is done using::

  stackedwidget.removeWidget(widget)

The index value or the widget currently visible widget within the StackedWidget is obtained via either::

  stackedwidget.currentIndex()
  stackedwidget.currentWidget()

The current page visible can be set by specifying the page index or widget::

  stackwidget.setCurrentIndex(index)
  stackwidget.setCurrentWidget(widget)

To retrieve the number of widgets held by the StackedWidget call::

  stackedwidget.count()

=======
Example
=======
Below is an example of a StackedWidget:

.. literalinclude:: _examples/stackedwidget.py

Download: :download:`StackedWidget <_examples/stackedwidget.py>`
