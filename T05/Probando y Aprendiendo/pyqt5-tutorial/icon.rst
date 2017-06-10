Icon
====
THe Icon object represents an image typically used to represent an action. They are commonly used on menus or buttons in association with a specific task such as saving a document or finding a string of text.

===========
Constructor
===========
Construction of an empty Icon object is made by::

  icon = QIcon()

Alternative constructors which allow the data to be loaded immediately are::

  icon = QIcon(filename)
  icon = QIcon(pixmap)

The *filename* parameter specifies the location from which to load an image. The *pixmap* argument points to a :doc:`pixmap` object which will be loaded into the Icon object.

=======
Methods
=======
An Icon can be set with an image via the methods::

  icon.addFile(filename, size, mode, state)
  icon.addPixmap(pixmap, mode, state)

The *filename* parameter points to the file to be loaded with the ``.addFile()`` method. Alternatively, the ``.addPixmap()`` method allows a :doc:`pixmap` object to be loaded. A *size* object allows the icon size to be specified using a :doc:`size` object. The *mode* value indicates the state of the icon and should be set to:

* ``QIcon.Normal`` - display as the icon is available, and the user is not interacting with it.
* ``QIcon.Disabled`` - display when the functionality of the icon is not allowed.
* ``QIcon.Active`` - display when the functionality of the icon is available, and the user it interacting with it (e.g. on mouseover).
* ``QIcon.Selected`` - display when the icon is selected.

A *state* parameter can also be defined as to whether the Icon object is on or off with:

* ``QIcon.Off``
* ``QIcon.On``

An Icon can also be checked for emptiness using::

  icon.isNull()

Icons can also be swapped if required with::

  icon.swap(icon)

The *icon* parameter should be set to another Icon object with which the values should be switched.
