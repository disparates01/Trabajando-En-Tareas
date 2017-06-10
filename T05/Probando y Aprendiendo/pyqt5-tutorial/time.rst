Time
====
The Time object contains details pertaining data related to a clock, with it being able to store hours, minutes, seconds, and milliseconds.

.. note::

  The Time object does not know about timezone or daylight savings time. If these are required, use the :doc:`datetime` object instead.

===========
Constructor
===========
Construction of the Time object is made using::

  time = QTime()

To construct a Time object with the values already set use::

  time = QTime(hours, minutes, seconds, milliseconds)

=======
Methods
=======
The values on the Time can be set post-construction by using the method::

  time.setHMS(hours, minutes, seconds, milliseconds)

To retrieve the values set call::

  time.hour()
  time.minute()
  time.second()
  time.msec()

The number of seconds or milliseconds from the currently set time can be retrieved via::

  time.secsTo(time)
  time.msecsTo(time)

The *time* parameter should be another Time object with the values to query.

Seconds or milliseconds can be added to the existing Time to create a new time object using the functions::

  time.addSecs(seconds)
  time.addMSecs(milliseconds)

To check whether the current time is valid call::

  time.isValid()

The Time can also be checked to see whether any values have been set with::

  time.isNull()

A second Time object can be compared using the operators::

  time.operator==(time)
  time.operator!=(time)
  time.operator>(time)
  time.operator<(time)
  time.operator>=(time)
  time.operator<=(time)
