Dir
===
The Dir object provides access to directories and their contents. It is used to manipulate paths, access information regardings those directories, and change the file system.

A Dir object can point to a path in absolute or relative form.

===========
Constructor
===========
The constructor for the Dir object is::

  dir = QDir(path)

If the *path* parameter is not specified, the Dir object sets the path to the current working directory. Alternatively, another path can be specified.

=======
Methods
=======
To return the current directory, use::

  dir.current()

An absolute or canonical paths to the directory can be fetched with::

  dir.absolutePath()
  dir.canonicalPath()

An absolute path can also be retrieved by specifying a path with::

  dir.absoluteFilePath(filename)

The name of a set directory can be pulled from the object by::

  dir.dirName()

The total number of directories and files within the specified directory is retrievable via::

  dir.count()

Moving up through the directory structure is possible with the method::

  dir.cdUp()

Alternatively, to change to a different directory call::

  dir.cd(dirname)

The ``cd()`` method returns ``True`` if the directory exists and the method called successfully, otherwise ``False`` is returned.

A check can be performed on a passed filename with::

  dir.exists(filename)

Removal of the defined file can be done via::

  dir.remove(filename)

The ``remove()`` method returns ``True`` if the file is successfully removed, otherwise ``False`` is returned.

The Dir object can also be used to rename a file by::

  dir.rename(oldname, newname)

Readability of the set file can be checked with::

  dir.isReadable()
