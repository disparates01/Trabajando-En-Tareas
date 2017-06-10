MessageBox
==========
The MessageBox widget is a subclass of the :doc:`dialog` object. It is tailored for displaying short messages to the user such as information or errors, but can also be used to ask simple questions.

===========
Constructor
===========
The MessageBox widget is constructed using::

  messagebox = QMessageBox()

=======
Methods
=======
The text on the MessageBox can be set with::

  messagebox.setText(text)

If a more detailed description of the message is required, such as a portion of a log file, this can be displayed using::

  messagebox.setInformativeText(text)

Detailed text is also permitted and is specified with::

  messagebox.setDetailedText(text)

Standard buttons are Qt provided buttons which can easily be added to the MessageBox without the user having to create each one manually. These can be set via::

  messagebox.setStandardButtons(buttons)

The standard buttons supported are:

* ``QMessageBox.Ok``
* ``QMessageBox.Open``
* ``QMessageBox.Save``
* ``QMessageBox.Cancel``
* ``QMessageBox.Close``
* ``QMessageBox.Discard``
* ``QMessageBox.Apply``
* ``QMessageBox.Reset``
* ``QMessageBox.RestoreDefaults``
* ``QMessageBox.Help``
* ``QMessageBox.SaveAll``
* ``QMessageBox.Yes``
* ``QMessageBox.YesToAll``
* ``QMessageBox.No``
* ``QMessageBox.NoToAll``
* ``QMessageBox.Abort``
* ``QMessageBox.Retry``
* ``QMessageBox.Ignore``

A user can add and remove extra buttons manually with::

  messagebox.addButton(button)
  messagebox.removeButton(button)

In both cases, the *button* object points to the button object (such as a :doc:`pushbutton`) to be added or removed.

An alternative to creating the buttons manually is to have the MessageBox construct them with the method::

  messagebox.addButton(text, role)

The *text* string specifies the text to be displayed on the button. The *role* defines the result of the user clicking the button, with the following values permitted:

* ``QMessageBox.InvalidRole``
* ``QMessageBox.AcceptRole``
* ``QMessageBox.RejectRole``
* ``QMessageBox.DestructiveRole``
* ``QMessageBox.ActionRole``
* ``QMessageBox.HelpRole``
* ``QMessageBox.YesRole``
* ``QMessageBox.NoRole``
* ``QMessageBox.ApplyRole``
* ``QMessageBox.ResetRole``

Once added, a default button and escape button can be defined by::

  messagebox.setDefaultButton(button)
  messagebox.setEscapeButton(button)

The default button is pre-highlighted when the MessageBox is shown, and is often the button which accepts a setting or ensures that the user does not lose data. An escape button is activated when the user presses :kbd:`Escape`, and would typically be a Close or Cancel button.

A :doc:`checkbox` can also be added to the MessageBox by calling::

  messagebox.setCheckBox(checkbox)

The *checkbox* parameter specifies a CheckBox widget to be added.

Icons can be added to the MessageBox to further indicate the purpose of the content::

  messagebox.setIcon(icon)

The *icon* parameter should be set to:

* ``QMessageBox.NoIcon``
* ``QMessageBox.Question``
* ``QMessageBox.Information``
* ``QMessageBox.Warning``
* ``QMessageBox.Critical``

Window modality can be set by setting the method::

  messagebox.setWindowModality(modality)

The *modality* should be set to one of the following:

* ``Qt.NonModal`` - do not block input on other windows.
* ``Qt.WindowModal`` - block input to parent windows.
* ``Qt.ApplicationModal`` - block input to all other windows.

The MessageBox can be run using the call::

  messagebox.open()

=======
Example
=======
Below is an example of a MessageBox:

.. literalinclude:: _examples/messagebox.py

Download: :download:`MessageBox <_examples/messagebox.py>`
