LCDNumber
=========
LCDNumber is a display widget typically used for showing numbers with an LCD screen-like (e.g. calculator, watch) appearance.

===========
Constructor
===========
The LCDNumber is constructed via the call::

  lcdnumber = QLCDNumber()

=======
Methods
=======
The contents to be displayed on the widget is set by::

  lcdnumber.display(number)
  lcdnumber.display(text)

The *number* argument can be set to an integer or float value. Alternatively, a *text* value can be displayed by passing a string.

Retrieval of the value from the LCDNumber is done using::

  lcdnumber.value()

LCDNumber supports a number of modes including decimal, hex, oct, and binary which are set via::

  lcdnumber.setMode(mode)

The *mode* should be set to one of:

* ``Bin``
* ``Oct``
* ``Dec`` (default)
* ``Hex``

Also provides are convenice functions to enable each of the supported modes above::

  lcdnumber.setBinMode()
  lcdnumber.setOctMode()
  lcdnumber.setDecMode()
  lcdnumber.setHexMode()

The display of the decimal point can be configured with the method::

  lcdnumber.setSmallDecimalPoint(small)

When *small* is set to ``True``, the point is drawn between the two numbers. When ``False``, the decimal point occupies a full digit position.

=======
Example
=======
Below is an example of a LCDNumber:

.. literalinclude:: _examples/lcdnumber.py

Download: :download:`LCDNumber <_examples/lcdnumber.py>`
