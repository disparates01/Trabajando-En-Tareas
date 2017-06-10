WhatsThis
=========
The "WhatsThis" class provides a description of the purpose of any widget. Although similar to a tooltip, the WhatsThis description is longer and more detailed, but generally they provide less information than a help window.

===========
Constructor
===========
The WhatsThis object is not constructed separately, but is able to be attached to most widgets or actions by the method::

  widget.setWhatsThis(text)

The *text* string should be defined to explain the purpose of the widget.

=======
Example
=======
Below is an example of a WhatsThis object:

.. literalinclude:: _examples/whatsthis.py

Download: :download:`WhatsThis <_examples/whatsthis.py>`
