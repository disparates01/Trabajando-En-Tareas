Menu
====
The Menu item provides the base layer for the menu items which are displayed on it. This can include single-click items, check and radio items, or additional menus.

===========
Constructor
===========
The Menu is constructed with the call::

  menu = QMenu()

.. note::

  When building a menubar for use in an application, the Menu item would not need to be manually constructed as it can be obtained from an existing menu action item.

=======
Methods
=======
Adding an item to the Menu with a simple text entry is done with::

  menu.addAction(text)

The *text* value should be set to the purpose of the action item. When called, it also returns the object for the item, allowing other :doc:`action` methods to be applied.

Another menu can be added to the Menu with::

  menu.addMenu()
  menu.insertMenu(action)

The ``.insertMenu()`` method takes an action parameter which determines the item on which the new menu should be inserted before.

The Menu can also contain sections which are useful for grouping items::

  menu.addSection(text)
  menu.insertSection(action, text)

The *text* parameter is set for the title of the section. If using the ``.insertSection()``, the *action* argument is also needed which indicates another item where the section should be inserted before.

To add a separator between items in the Menu use::

  menu.addSeparator()

All the items contained by the Menu can be cleared with the method::

  menu.clear()

The tearoff functionality allows menus to be floated in a window for easy access. This can be enabled on a menu with::

  menu.setTearOffEnabled(enabled)

A title should also be set when using the tearoff functionality, to ensure the floating window has an appropriate title::

  menu.setTitle(title)
