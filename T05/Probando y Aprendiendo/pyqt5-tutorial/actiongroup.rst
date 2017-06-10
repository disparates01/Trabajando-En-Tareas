ActionGroup
===========
An ActionGroup provides a way to group :doc:`action` objects together, typically when they provide related functionality.

===========
Constructor
===========
The construction method for the ActionGroup is::

  actiongroup = QActionGroup()

=======
Methods
=======
Action objects can be added to the group via::

  actiongroup.addAction(action)

Alternatively, an Action object can be created automatically with::

  actiongroup.addAction(text)
  actiongroup.addAction(icon, text)

The *text* parameter is required by both methods, and is displayed by the Action. An *icon* can also be added which will be displayed on the Action alongside the text.

An added action object is removable from the group by::

  actiongroup.removeAction(action)

All the objects contained within the group can be enabled or disabled using::

  actiongroup.setEnabled(enabled)

An entire group can be made visible or invisible by calling::

  actiongroup.setVisible(visible)

In some circumstances, only one item held in the group will be checkable at a time. This can be configured with::

  actiongroup.setExclusive(exclusive)

The checked item can be fetched from the group with the method::

  actiongroup.checkedAction()
