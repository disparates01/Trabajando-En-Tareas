TabBar
======
A TabBar provides the drawing of tabs, with common usage in tabbed dialogs. It is similar to the :doc:`tabwidget` which is a ready-made solution, whereas the TabBar provides more configuration for layout and style.

===========
Constructor
===========
The construction method for the TabBar is::

  tabbar = QTabBar()

=======
Methods
=======
A tab is added to the TabBar using one of four methods::

  tabbar.addTab(text)
  tabbar.addTab(icon, text)
  tabbar.insertTab(index, text)
  tabbar.insertTab(index, icon, text)

The *text* parameters passes the string to be displayed on the newly created tab. The *icon* argument specifies an :doc:`icon` object to be displayed alongside the text. The ``.insertTab()`` methods also take an *index* parameter which specifies where in the TabBar the new tab will be inserted.

Removal of tabs is done by the call::

  tabbar.removeTab(index)

The *index* value specifies the current position of the tab to be removed, with ``0`` used for the first tab.

If the user should be able to move tabs within the TabBar, call::

  tabbar.setMovable(movable)

A tab can be programatically moved via::

  tabbar.moveTab(from, to)

The *from* and *to* values indicate the position of the tab, from its current position to the new one.

In some circumstances such as a preferences dialog, some tabs may be made unavailable. This is done by::

  tabbar.setTabEnabled(index, enabled)

The *index* passes the position of the tab be made enabled or disabled. When *enabled* is set to ``False``, the tab will be greyed-out and inaccessible.

The icon and text on a tab can be defined after it has been added::

  tabbar.setTabText(index, text)
  tabbar.setTabIcon(index, icon)

Some applications such as web browsers require that tabs be closed. This is configurable via::

  tabbar.setTabsClosable(closable)

Then *closable* is set to ``True``, a close button is added to the tab.

A :doc:`tooltip` and :doc:`whatsthis` can be added with the methods::

  tabbar.setTabToolTip(index, tooltip)
  tabbar.setTabWhatsThis(index, whatsthis)

The *tooltip* and *whatsthis* parameters should be set to a string.

By default, the TabBar should always be visible. In may be preferential for the TabBar to be hidden when less than two tabs are visible::

  tabbar.setAutoHide(autohide)

Retrieval of the number of tabs currently held by the TabBar with::

  tabbar.count()

The active tab can be fetched and retrieved using the calls::

  tabbar.currentIndex()
  tabbar.setCurrentIndex(index)

=======
Example
=======
Below is an example of an TabBar:

.. literalinclude:: _examples/tabbar.py

Download: :download:`TabBar <_examples/tabbar.py>`
