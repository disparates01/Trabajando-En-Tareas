ListWidgetItem
==============
The ListWidgetItem is used to provide an item for use within the :doc:`listwidget`. Each item holds several pieces of information and displays the items as per the information.

===========
Constructor
===========
In many cases, the ListWidgetItem will not need to be constructed manually as one is created for each item added to a ListWidget. If required however, it is constructed via::

  listwidgetitem = QListWidgetItem()

=======
Methods
=======
The textual string of the item can be set using::

  listwidgetitem.setText(text)

It can also be retrieved via::

  listwidgetitem.text()

The item can be hidden from the viewing widget with the call::

  listwidgetitem.setHidden(hidden)

When *hidden* is set to ``True``, the item will not be visible to the user.

To check whether an item is hidden from view call::

  listwidgetitem.isHidden()

An exact copy of the ListWidgetItem including all properties set can be made with::

  listwidgetitem.clone()

The ListWidget which contains the item can be fetched if required by::

  listwidgetitem.listWidget()

=======
Example
=======
An example of the ListWidgetItem can be viewed with the ListWidget example.
