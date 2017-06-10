SpacerItem
==========
A SpacerItem provides a blank space in a layout. In most cases, the SpacerItem is not required as both the :doc:`boxlayout` and :doc:`gridlayout` containers provide spacing declarations.

===========
Constructor
===========
The constructor for the SpacerItem is::

  spaceritem = QSpacerItem()

=======
Methods
=======
The size of the SpacerItem can be adjusted by calling::

  spaceritem.changeSize(width, height, hpolicy, vpolicy)

The *width* and *height* take integer values for the size in pixels. The *hpolicy* and *vpolicy* values take SizePolicy objects as arguments to define the behaviour:

* ``QSizePolicy.Fixed`` - the size hint is set, and the SpacerItem will not shrink or grow.
* ``QSizePolicy.Minimum`` - the size hint is minimal, but the SpacerItem may expand if allowed.
* ``QSizePolicy.Maximum`` - the size hint is maximal, but the SpacerItem may shrink if allowed.
* ``QSizePolicy.Preferred`` - the size hint size is preferred.
* ``QSizePolicy.Expanding`` - te size hint is the sensible size.
* ``QSizePolicy.MinimumExpanding`` - the size hint is the minimal, but the SpacerItem can make use of more space if possible.
* ``QSizePolicy.Ignored`` - the size hint is ignored and the SpacerItem takes as much space as possible.

=======
Example
=======
Below is an example of a SpacerItem:

.. literalinclude:: _examples/spaceritem.py

Download: :download:`SpacerItem <_examples/spaceritem.py>`
