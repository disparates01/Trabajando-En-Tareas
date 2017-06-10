PlainTextEdit
=============
The PlainTextEdit widget is optimised to display plain text content.

If the application is to display formatted text, the :doc:`textedit` widget should be used.

===========
Constructor
===========
The PlainTextEdit widget is constructed by using::

  plaintextedit = QPlainTextEdit()

=======
Methods
=======
Text is inserted into the PlainTextEdit by either of the following methods::

  plaintextedit.appendPlainText(text)
  plaintextedit.insertPlainText(text)

The ``.appendPlainText()`` method adds the new text to the end of the current text block whereas the ``.insertPlainText()`` method adds the text at the cursor position.

By default, the text in the PlainTextEdit can be modified by the user. It can however be used as a read-only widget with::

  plaintextedit.setReadOnly(read_only)

When *read_only* is set to ``True``, the user will only be able to navigate through the text.

The read-only state of the widget can also be retrieved using::

  plaintextedit.isReadOnly()

Placeholder text can be placed into the PlainTextEdit with::

  plaintextedit.setPlaceholderText(text)

The *text* specified will only be shown in the widget when there is no text loaded.

The title of the document can be set via::

  plaintextedit.setDocumentTitle(title)

Retrieval of the title string is also done with::

  plaintextedit.documentTitle()

The text held by the PlainTextEdit can also be line wrapped if required::

  plaintextedit.setLineWrapMode(mode)

The *mode* value should be set to one of the following:

* ``QPlainTextEdit.NoWrap`` - do not wrap the text.
* ``QPlainTextEdit.WidgetWidth`` - wrap text at width of PlainTextEdit.

Word wrapping is also enabled separately::

  plaintextedit.setWordWrapMode(mode)

The *mode* value in this case should be set to:

* ``QTextOption.NoWrap`` - text is not wrapped.
* ``QTextOption.WordWrap`` - wrap text at end of words.
* ``QTextOption.ManualWrap`` - same as the ``NoWrap`` constant.
* ``QTextOption.WrapAnywhere`` - wrap text anywhere, even in the middle of a word if required.
* ``QTextOption.WrapAtWordBoundaryOrAnywhere`` - wrap at end of a word, or anywhere if there is no other option.

By default, any text entered into the PlainTextEdit will be inserted. Existing text can be overwritten instead via::

  plaintextedit.setOverwriteMode(overwrite)

Undo and redo support is enabled on a PlainTextEdit. This can be turned off if not required using::

  plaintextedit.setUndoRedoEnabled(enable)

=======
Example
=======
Below is an example of a PlainTextEdit:

.. literalinclude:: _examples/plaintextedit.py

Download: :download:`PlainTextEdit <_examples/plaintextedit.py>`
