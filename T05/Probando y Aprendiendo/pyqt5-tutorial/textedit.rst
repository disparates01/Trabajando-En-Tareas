TextEdit
========
The TextEdit widget is a powerful text display widget, with the ability to display both plain text and formatted text. It can handle paragraphs, images, tables, and lists, with the rich text display ability powered by HTML markup.

Smaller amounts of text are probably best being displayed using the :doc:`label` widget, or alternatively, the :doc:`lineedit` widget if the user should be able to manipulate the text. Alternatively, if the application only handles plain text content, it is better to use :doc:`plaintextedit`.

===========
Constructor
===========
The TextEdit widget is constructed by using::

  textedit = QTextEdit()

=======
Methods
=======
Text content can be added using a number of methods::

  textedit.append(text)
  textedit.insertHtml(text)
  textedit.insertPlainText(text)
  textedit.setText(text)
  textedit.setHtml(text)
  textedit.setPlainText(text)

The ``append()`` method adds text to the position of the cursor. Alternatively, the ``insertHtml()`` and ``insertPlainText()`` allows text to be added either with rich text or plain text. The ``setText()``, ``setHtml()`` and ``setPlainText()`` methods replace the existing content of the TextEdit with the new text.

Content from the TextEdit can be retrieved with the calls::

  textedit.toHtml()
  textedit.toPlainText()

All text within the TextEdit can be cleared using::

  textedit.clear()

In some circumstances, the TextEdit may only accept or display plain text. This is set via::

  textedit.setAcceptRichText(rich_text)

To ensure that a user can not change text held in the TextEdit, call::

  textedit.setReadOnly(read_only)

The read-only state of the TextEdit is fetchable via::

  textedit.isReadOnly(read_only)

Placeholder text can be added to the TextEdit, which is displayed when no other text is added::

  textedit.setPlaceholderText(text)

By default, any text added to the TextEdit will be inserted. Existing content can instead be overwritten via::

  textedit.setOverwriteMode(overwrite)

TextEdit widgets automatically support undo and redo actions. These can be called with::

  textedit.undo()
  textedit.redo()

If undo/redo support is not required, this can be turned of using the method::

  textedit.setUndoRedoEnabled(enable)

Words within the TextEdit default to wrapping at the end of a word. This is configured by::

  textedit.setLineWrapMode(mode)

The *mode* should be set to one of:

* ``QTextEdit.NoWrap`` - do not wrap the text.
* ``QTextEdit.WidgetWidth`` - wrap text at width of TextEdit.

The mode in use when wrapping words can also be configured by the method::

  textedit.setWordWrapMode(mode)

The *mode* value in this case should be defined to one of:

* ``QTextOption.NoWrap`` - text is not wrapped.
* ``QTextOption.WordWrap`` - wrap text at end of words.
* ``QTextOption.ManualWrap`` - same as the ``NoWrap`` constant.
* ``QTextOption.WrapAnywhere`` - wrap text anywhere, even in the middle of a word if required.
* ``QTextOption.WrapAtWordBoundaryOrAnywhere`` - wrap at end of a word, or anywhere if there is no other option.

=======
Example
=======
Below is an example of a TextEdit:

.. literalinclude:: _examples/textedit.py

Download: :download:`TextEdit <_examples/textedit.py>`
