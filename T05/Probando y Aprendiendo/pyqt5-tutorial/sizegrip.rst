SizeGrip
========
The SizeGrip widget provides a way to resize a parent :doc:`window`. It commonly appears as a triangle in the bottom right corner of the window and allows the user to increase or decreate the window width and height.

===========
Constructor
===========
The SizeGrip is constructable with the call::

  sizegrip = QSizeGrip(parent)

The *parent* parameter should be set to the parent widget to be assigned the SizeGrip.

=======
Methods
=======
To configure the visibility of the SizeGrip use::

  sizegrip.setVisible(visible)

=======
Example
=======
Below is an example of a SizeGrip:

.. literalinclude:: _examples/sizegrip.py

Download: :download:`SizeGrip <_examples/sizegrip.py>`
