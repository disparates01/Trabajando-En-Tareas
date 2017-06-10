ScrollArea
==========
A ScrollArea widget provides a container for another widget to be placed, providing scrolling in both vertical and horizontal directions when the child is larger than the space allocated.

The ScrollArea automatically provides :doc:`scrollbar` objects and is preferred in most cases when scrolling must be provided.

===========
Constructor
===========
Construction of the ScrollArea is made using::

  scrollarea = QScrollArea()

=======
Methods
=======
Widgets are added to the ScrollArea container using::

  scrollarea.setWidget(widget)

The widget assigned to the ScrollArea can be retrieved with::

  scrollarea.widget()

The added widget can be positioned within the area via::

  scrollarea.setAlignment(alignment)

Set the *alignment* value to one of the following:

* ``Qt.AlignLeft``
* ``Qt.AlignRight``
* ``Qt.AlignTop``
* ``Qt.AlignBottom``
* ``Qt.AlignHCenter``
* ``Qt.AlignVCenter``

The child widget can be resized within the ScrollArea via::

  scrollarea.setWidgetResizable(resizable)

When *resizable* is set to ``True``, the ScrollArea automatically resizes the widget to try and avoid scroll bars and take advantage of extra space. If set to ``False``, the default widget size is honoured.

=======
Example
=======
Below is an example of a ScrollArea:

.. literalinclude:: _examples/scrollarea.py

Download: :download:`ScrollArea <_examples/scrollarea.py>`
