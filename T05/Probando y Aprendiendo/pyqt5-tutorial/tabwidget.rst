TabWidget
=========
The TabWidget provides a container with multiple pages which are switchable via tabs. Each page can contain a single widget or other containers. The TabWidget is commonly found in multi-document applications such as web browsers or word processors.

===========
Constructor
===========
The TabWidget is constructed using::

  tabwidget = QTabWidget()

=======
Methods
=======
Tabs are added to the TabWidget via several methods::

  tabwidget.addTab(child, label)
  tabwidget.insertTab(index, child, label)

The ``.addTab()`` method adds each tab in the order the code is executed whereas the ``.insertTab()`` method allows an *index* value indicating the location to insert the tab, with the first position identified as ``0``. The *child* parameter is the name of the child object to be added to the tab. Finally, the *label* parameter is the text to be displayed on the tab itself.

Additionally, an icon can be added to each tab with::

  tabWidget.addTab(child, icon, label)
  tabWidget.insertTab(index, child, icon, label)

The *index*, *child*, and *label* arguments remain as above. The *icon* parameter should be set to an appropriate :doc:`icon` object.

Tabs are removed from the TabWidget via::

  tabWidget.removeTab(index)

The *index* value is the position of the tab within the TabWidget.

All the tabs currently held by the TabWidget can be removed with::

  tabWidget.clear()

The text displayed on each tab can be configured post-add with::

  tabWidget.setTabText(index, text)

The number of tabs contained can be counted using::

  tabWidget.count()

If the TabWidget contains less than two tabs, the tab bar can be configured to hide::

  tabWidget.tabBarAutoHide(autohide)

When *autohide* is set to ``True``, the tab bar will be hidden when there are fewer than two tabs being displayed.

In some cases, individual tabs should be removable. A close button can be added to each tab using::

  tabWidget.setTabsClosable(closable)

Each tab can be assigned a ToolTip and/or :doc:`whatsthis` to indicate the purpose of the tab with::

  tabWidget.setTabToolTip(index, text)
  tabWidget.setWhatsThis(index, text)

The *index* argument specifies which tab should receive the *text* parameter, with ``0`` specifying the first tab held by the TabWidget.

In some cases, individual tabs will need to be made inaccessible to the user. This is done by "greying-out" via::

  tabWidget.setTabEnabled(index, enabled)

When *enabled* is set to ``True``, the user will not be able to interact with it, though the content may still be available to view.

A check can be run on whether a tab is enabled with::

  tabWidget.isTabEnabled(index)

Tabs may also be required to be movable. This can be set via::

  tabWidget.setMovable(movable)

By default, tabs are not movable by the user, but when *movable* is set to ``True``, the user can drag-and-drop each tab into a new place.

The default appearance is to display all tabs at the top of the widget. This can be configured with::

  tabWidget.setTabPosition(position)

The *position* value should be set to one of:

* ``QTabWidget.North`` - draw tabs at top (default).
* ``QTabWidget.South`` - draw tabs at bottom.
* ``QTabWidget.East`` - draw tabs on left.
* ``QTabWidget.West`` - draw tabs on right.

=======
Example
=======
Below is an example of a TabWidget:

.. literalinclude:: _examples/tabwidget.py

Download: :download:`TabWidget <_examples/tabwidget.py>`
