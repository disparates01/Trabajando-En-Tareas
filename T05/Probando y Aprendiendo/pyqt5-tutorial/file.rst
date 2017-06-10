File
====
The File object provides an interface for reading and writing files. It supports handling of both text and binary files.

===========
Constructor
===========
Construction of the File object is made using::

  file = QFile()

=======
Methods
=======
The file name which the File object points to is set with the call::

  file.setFileName(filename)

Retrieval of the file name is done using::

  file.fileName()

A file can be copied to a new location with::

  file.copy(filename)

The *filename* parameter specifies the position the copied file will be created in.

Links can also be created as well via::

  file.link(filename)

Renaming of the file name held by the File object is made by calling::

  file.rename(filename)

Deletion of the file handled by the method::

  file.remove()

Checking whether a file exists on the hard disk can be done with::

  file.exists()

The method returns to ``True`` if the set file name exists, otherwise ``False`` is returned.
