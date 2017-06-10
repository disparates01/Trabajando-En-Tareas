Frame
=====
The Frame container provides a grouping box with an associated title. Typically, widgets contained within the Frame are related to a particular function.

===========
Constructor
===========
The Frame is constructed using::

  frame = QFrame()

=======
Methods
=======
A layout widget can be added to the Frame container with::

  frame.setLayout(layout)

Typically the *layout* parameter will be a container widget such as :doc:`boxlayout`.

The line width of the Frame can be set in pixels using::

  frame.setLineWidth(width)

By default, the width of the line is ``1`` pixel.

The Frame can take on three appearances; plain, raised, or sunken. This is configurable via::

  frame.setFrameShadow(shadow)

The default appearance is plain. The *shadow* can be set however to one of the following:

* ``QFrame.Plain``
* ``QFrame.Raised``
* ``QFrame.Sunken``

The shape of the frame can be set via::

  frame.setFrameShape(shape)

The *shape* parameter should be set to one of the following:

* ``QFrame.NoFrame`` - draw no frame around the contents.
* ``QFrame.Box`` - draw a box around the contents.
* ``QFrame.Panel`` - draw a panel to make the content appear raised or sunken.
* ``QFrame.StyledPanel`` - draw a raised or sunken rectangular panel dependent on the interface style.
* ``QFrame.HLine`` - draw a horizontal line as a separator.
* ``QFrame.VLine`` - draw a vertical line as a separator.
* ``QFrame.WinPanel`` - draw a rectangular panel, raised or sunken, similar to those found in Windows 2000.

=======
Example
=======
Below is an example of a Frame:

.. literalinclude:: _examples/frame.py

Download: :download:`Frame <_examples/frame.py>`
