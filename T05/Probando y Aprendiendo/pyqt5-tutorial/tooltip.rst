ToolTip
=======
ToolTip widgets are attached to other widgets and appear when the user hovers over the widget, displaying hints about the purpose of the widget.

=======
Methods
=======
The ToolTip is made visible to the user using::

  tooltip.showText(text)

The *text* parameter specifies the string to be displayed within the Tooltip.

The font and palette colour can be set with the methods::

  tooltip.setFont(font)
  tooltip.setPalette(palette)

The *font* and *palette* parameters take a :doc:`font` and :doc:`palette` object as arguments to customise the appearance of the Tooltip content.

To check whether the Tooltip is currently visible call::

  tooltip.isVisible()

=======
Example
=======
Below is an example of a ToolTip:

.. literalinclude:: _examples/tooltip.py

Download: :download:`ToolTip <_examples/tooltip.py>`
