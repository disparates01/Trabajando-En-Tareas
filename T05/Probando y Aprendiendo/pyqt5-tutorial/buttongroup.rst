ButtonGroup
===========
A ButtonGroup is an invisible object used to group buttons. It is typically used with :doc:`radiobutton` widgets to prevent them interacting with other RadioButton's not intended to be in the same group.

===========
Constructor
===========
A ButtonGroup is constructed with the call::

  buttongroup = QButtonGroup()

=======
Methods
=======
A button is added to the group with the method::

  buttongroup.addButton(button, id)

The *button* parameter indicated the button to be added into the ButtonGroup. The *id* value can be left if not required, in which case it will be assigned a negative value. If it is specified, the value should be positive. The value allows a button to be identified within the grouping.

To remove a button from the group, use the call::

  buttongroup.removeButton(button)

A list of all the buttons associated with the ButtonGroup can be made via::

  buttongroup.buttons()

Using the id property when adding the buttons, a button object can be retrieved for a given id with::

  buttongroup.button(id)

On the reverse, an id for a given button can also be fetched::

  buttongroup.id(button)

If the id is to be specified after the button has been added to the ButtonGroup, call::

  buttongroup.setId(button, id)

To enforce that only one button in the group can be selected at a time, use::

  buttongroup.setExclusive(exclusive)

If the ButtonGroup contains buttons which can be in the checked state, the active button can be found with::

  buttongroup.checkedButton()

=======
Signals
=======
The available ButtonGroup signals are::

  buttonClicked(button)
  buttonClicked(id)
  buttonPressed(button)
  buttonPressed(id)
  buttonReleased(button)
  buttonReleased(id)
  buttonToggled(button, checked)
  buttonToggled(id, checked)

Either the *button* object or *id* value can be connected, which will be actioned when the signal is triggered. The ``buttonToggled()`` signal also indicates whether the state is set to ``True`` or ``False``.

=======
Example
=======
Below is an example of a ButtonGroup:

.. literalinclude:: _examples/buttongroup.py

Download: :download:`ButtonGroup <_examples/buttongroup.py>`
