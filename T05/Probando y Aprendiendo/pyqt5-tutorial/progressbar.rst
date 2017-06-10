ProgressBar
===========
A ProgressBar is used to show the completion state of a process. It is typically drawn using an empty box which fills as the job completes, coupled with a percentage value or textual description.

Use of a ProgressBar is recommended when a job may take some time, to ensure that the user is kept up-to-date on the state of the application.

===========
Constructor
===========
Construction of the ProgressBar is done with the call::

  progressbar = QProgressBar()

=======
Methods
=======
The minimum and maximum values held by the ProgressBar are defined with::

  progressbar.setMinimum(minimum)
  progressbar.setMaximum(maximum)

The minimum and maximum values can also be retrieved::

  progressbar.minimum()
  progressbar.maximum()

The current value state of the ProgressBar is retrievable via::

  progressbar.value()

Setting the value will typically be done by the application using::

  progressbar.setValue(value)

The *value* parameter should be set to an integer value.

Orienting the ProgressBar is done with::

  progressbar.setOrientation(orientation)

The *orientation* parameter should be set to one of:

* ``Qt.Horizontal``
* ``Qt.Vertical``

When the ProgressBar is horizontally oriented, the bar fills from left to right while the vertically oriented ProgressBar fills from top to bottom. This can be inverted via::

  progressbar.setInvertedAppearance(appearance)

The completion percentage value can be set visible or not by using::

  progressbar.setTextVisible(visible)

Changing the text displayed within the widget can be done with::

  progressbar.setFormat(format)

The *format* value takes a string of text. The following modifiers are used to display the appropriate dynamic information:

* ``%p`` - percentage completion
* ``%v`` - current value
* ``%m`` - total number of steps

If required, the text can be retrieved by calling::

  progressbar.format()

Reverting to the default text format of a percentage value can be done using::

  progressbar.resetFormat()

=======
Example
=======
Below is an example of a ProgressBar:

.. literalinclude:: _examples/progressbar.py

Download: :download:`ProgressBar <_examples/progressbar.py>`
