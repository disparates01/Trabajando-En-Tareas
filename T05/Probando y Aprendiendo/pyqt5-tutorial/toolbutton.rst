ToolButton
==========
The ToolButton widget provides a button which can be added to a :doc:`toolbar` or :doc:`toolbox` container. They are used commonly for quick access to common functions such as saving a document, or finding a string of text.

===========
Constructor
===========
Construction of the ToolButton is made using::

  toolbutton = QToolButton()

=======
Methods
=======
Text can be added to the ToolButton by calling::

  toolbutton.setText(text)

An icon can also be added to the ToolButton with::

  toolbutton.setIcon(icon)

The *icon* parameter should be set to an appropriate :doc:`icon` object.

ToolButton widgets can also be made checkable. This allows them to be in either a pressed or unpressed state, and is useful for indicating a true or false state. The function can be set using::

  toolbutton.setCheckable(checkable)

When *checkable* is set to ``True``, the ToolButton will appear depressed when clicked.

The checked state of the ToolButton can then be retrieved by calling::

  toolbutton.isChecked(checked)

Progamatically, the ToolButton when made checkable can be pressed with::

  toolbutton.setDown(down)

A :doc:`menu` object can be added to the ToolButton to provide a dropdown menu::

  toolbutton.setMenu(menu)

If a menu is in use with the ToolButton, the way the menu pops up can be configured by::

  toolbutton.setPopupMode(mode)

The *mode* value should be set to one of:

* ``QToolButton.DelayPopup`` - the Menu is shown when the ToolButton is pressed and held for a set time.
* ``QToolButton.MenuButtonPopup`` - show an arrow next to the ToolButton, which displays the Menu object when clicked.
* ``QToolButton.InstantPopup`` - display the Menu immediately when the ToolButton item is clicked.

=======
Example
=======
An example of the ToolButton in use can be found in the ToolBar example.
