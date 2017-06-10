Completer
=========
The Completer object is used to provide auto-completions when text is entered into some widgets such as the :doc:`lineedit` or :doc:`combobox`. When a user begins to type, the model content is matched and suggestions are provided.

===========
Constructor
===========
A Completer is constructed using::

  completer = QCompleter()

The data model may be added post-construction, however it can be defined at construction time by using::

  completer = QCompleter(model)

=======
Methods
=======
Data used by the Completer is held in a model, which is attached by calling::

  completer.setModel(model)

The model attached to the Completer can also be retrieved with::

  completer.model()

In some cases, the data model may contain multiple columns. By default, the completer uses the first column (0), however this can be changed by the method::

  completer.setCompletionColumn(column)

The completion method set on the Completer is set using::

  completer.setCompletionMode(mode)

The *mode* defined should be set to one of:

* ``QCompleter.PopupCompletion`` - completions are displayed in a dropdown menu.
* ``QCompleter.InlineCompletion`` - completions appear inline as selected text.
* ``QCompleter.UnfilterPopupCompletion`` - completions are displayed in a dropdown menu with the most likely suggestion indicated as current.

By default, seven items are displayed in the completion. An alternative value can be set using::

  completer.setMaxVisibleItems(maximum)

In some cases, it may be preferable to control whether the completion is sensitive or insensitive via::

  completer.setCaseSensitivity(sensitivity)

The *sensitivity* constant should be defined as one or:

* ``Qt.CaseInsensitive``
* ``Qt.CaseSensitive``

=======
Example
=======
Below is an example of a Completer:

.. literalinclude:: _examples/completer.py

Download: :download:`Completer <_examples/completer.py>`
