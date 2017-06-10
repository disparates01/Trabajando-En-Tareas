TreeWidgetItem
==============
The TreeWidgetItem is used as an object within a :doc:`treewidget` to contain content which is displayed to the user.

===========
Constructor
===========
A TreeWidgetItem may not need to be constructed as add methods for the TreeWidget can automatically create them. However, construction of the TreeWidgetItem is made using the call::

  treewidgetitem = QTreeWidgetItem()

=======
Methods
=======
A TreeWidgetItem can display text by simply specifying the column and text string::

  treewidgetitem.setText(column, text)

The text stored by the TreeWidgetItem can be obtained using::

  treewidgetitem.text(column)

The *column* value specifies the column which holds the text string to be fetched.

Alternatively, it can be used for handling check states or numeric values via::

  treewidgetitem.setCheckState(column, state)
  treewidgetitem.setIcon(column, icon)
  treewidgetitem.setToolTip(column, tooltip)

The TreeWidgetItem is able to be hidden by setting::

  treewidgetitem.setHidden(hidden)

When the *hidden* parameter is set to ``True``, the item will not be visible to the user.

To check whether a TreeWidgetItem is hidden from view call::

  treewidgetitem.isHidden()

Cloning of a TreeWidgetItem may be done using the method::

  treewidgetitem.clone()

The associated TreeWidget can be obtained from the TreeWidgetItem if required by::

  treewidgetitem.treeWidget()

A child can be added or removed from the TreeWidgetItem. This provides sub-items of the parent TreeWidgetItem::

  treewidgetitem.addChild(treewidgetitem)
  treewidgetitem.removeChild(treewidgetitem)

The *treewidgetitem* parameter specifies another TreeWidgetItem object to be added or removed as the child.

By default, child rows are collapsed with the TreeWidget. An individual child can be expanded by calling::

  treewidgetitem.setExpanded(expand)

=======
Example
=======
An example of the TreeWidgetItem can be viewed with the TreeWidget example.
