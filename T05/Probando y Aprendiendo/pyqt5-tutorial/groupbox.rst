GroupBox
========
The GroupBox provides a tidy way to group items, with the container featuring a title label and bordering frame.

It should be noted that the GroupBox can only contain one widget itself, with the intention of other containers such as a :doc:`boxlayout`.

===========
Constructor
===========
The constructor for a GroupBox is::

  groupbox = QGroupBox(title)

The *title* parameter should be set with the string of text to display.

=======
Methods
=======
The title applied to the GroupBox can be set using::

  groupbox.setTitle(title)

A widget is added to the GroupBox with::

  groupbox.setLayout(child)

The alignment of children within the GroupBox is settable via::

  groupbox.setAlignment(alignment)

By default, the alignment is set to the left-edge, however it can be customised with the *alignment* value being set to one of the following:

* ``Qt.AlignLeft``
* ``Qt.AlignRight``
* ``Qt.AlignHCenter``

The GroupBox can be made checkable if required. This permits all child :doc:`checkbox` or :doc:`radiobutton` widgets to be made sensitive or insenstive. This is set via::

  groupbox.setCheckable(checkable)

The checked state of the GroupBox can be obtained using::

  groupbox.isChecked()

Programatically setting the checked state of the GroupBox can be done using::

  groupbox.setChecked(checked)

When *checked* is set to ``True``, the GroupBox checkbox will contain a tick. Setting to ``False`` will removed the tick.

=======
Example
=======
Below is an example of a GroupBox:

.. literalinclude:: _examples/groupbox.py

Download: :download:`GroupBox <_examples/groupbox.py>`
