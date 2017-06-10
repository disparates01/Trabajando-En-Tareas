Slider
======
A Slider provides a way to adjust a numerical value by moving a slide along a run to change the output value. It is commonly seen when adjusting the volume of a speaker, or the brightness of a screen.

===========
Constructor
===========
Slider widgets are constructed using::

  slider = QSlider(orientation)

By default, the Slider is oriented vertically with the slider object moving from top to bottom. The *orientation* parameter is optional, by can be set to ``Qt.Vertical`` or ``Qt.Horizontal``.

=======
Methods
=======
The orientation can also be changed after construction with::

  slider.setOrientation(orientation)

By default the slider ranges between 0 and 99. Custom minimum and maximum values can be defined::

  slider.setMinimum(value)
  slider.setMaximum(value)

If attempting to set a value on the slider which falls outside the minimum and maximum values, the value will be adjusted so that it falls in the range.

A value can be set onto the Slider using::

  slider.setValue(value)

The Slider emits a signal that the value has changed whenever the user stops sliding and releases the mouse. In some cases, the requirement may be to emit a changed signal whenever the Slider moves. This can be done with::

  slider.setTracking(tracking)

If *tracking* is set to ``True``, the Slider will call the associated update function repeatedly when moving.

Ticks can be added to the Slider scale at set positions to ease the user in viewing where on the scale the marker is. The method for this is::

  slider.setTickInterval(interval)

The *interval* value should be a number, which indicates the gap between each tick.

The position of the ticks can be configured via::

  slider.setTickPosition(position)

The *position* value should be set to one of:

* ``QSlider.NoTicks`` - do not draw tick marks.
* ``QSlider.TicksBothSides`` - draw ticks on both sides of the scale.
* ``QSlider.TicksAbove`` - draw ticks above the horizontal slider.
* ``QSlider.TicksBelow`` - draw ticks below the horizontal slider.
* ``QSlider.TicksLeft`` - draw ticks to the left of the vertical slider.
* ``QSlider.TicksRight`` - draw ticks to the right of the vertical slider.

=======
Example
=======
Below is an example of a Slider:

.. literalinclude:: _examples/slider.py

Download: :download:`Slider <_examples/slider.py>`
