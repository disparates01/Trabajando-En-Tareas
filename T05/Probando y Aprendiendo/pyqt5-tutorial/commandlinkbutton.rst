CommandLinkButton
=================
The CommandLinkButton provides an alternative to the :doc:`radiobutton`, but is displayed in the style of a :doc:`pushbutton` widget. It is modelled on the CommandLinkButton introduced by Windows Vista.

===========
Constructor
===========
The construction statement for the CommandLinkButton is::

  commandlinkbutton = QCommandLinkButton(text)

The *text* parameter specifies the text string to be displayed on the CommandLinkButton.

=======
Methods
=======
A description is set on the CommandLinkButton with::

  commandlinkbutton.setDescription(description)

=======
Example
=======
Below is an example of a CommandLinkButton:

.. literalinclude:: _examples/commandlinkbutton.py

Download: :download:`CommandLinkButton <_examples/commandlinkbutton.py>`
