Dial
====
The Dial widget provides a range object which takes the form of a control knob. Its design is similar to a volume knob on a music system, with the turning of the dial outputting different numbers within a defined range.

.. note::

  The Dial widget may change appearance based on the platform in use, however the functionality remains the same.

===========
Constructor
===========
The Dial widget is created by defining::

  dial = QDial()

=======
Methods
=======
The minimum and maximum values of the Dial are set by::

  dial.setMinimum(minimum)
  dial.setMaximum(maximum)

To set the value of the Dial programmatically, call::

  dial.setValue(value)

Retrieving the value set on the Dial is done using::

  dial.value()

The minimum and maximum values are also retrievable with the method::

  dial.minimum()
  dial.maximum()

By default, the Dial will wrap so that dragging from the highest number will reset the Dial back to the lowest. This can be configured with::

  dial.setWrapping(wrapping)

When *wrapping* is set to ``False``, the user will need to drag the Dial all the way back around from the highest to lowest point.

A notch target can be defined. This holds the number of pixels which the Dial attempts to place between notches, with a default of 3.7 pixels. This can be modified by the method::

  dial.setNotchTarget(target)

Notches can also be toggled visible or invisible with::

  dial.setNotchesVisible(visible)

=======
Example
=======
Below is an example of an Dial:

.. literalinclude:: _examples/dial.py

Download: :download:`Dial <_examples/dial.py>`
