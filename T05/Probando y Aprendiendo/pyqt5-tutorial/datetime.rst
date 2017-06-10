DateTime
========
The DateTime object provides the ability to store both date and time information.

.. note::

  The DateTime object can be replaced with the :doc:`time` object if only representation of time is required. The :doc:`date` object can also be used it only the date is to be handled.

===========
Constructor
===========
The constructor for the DateTime object is::

  datetime = QDateTime()

=======
Methods
=======
The date and time values stored by the DateTime object are retrieved using the method::

  datetime.date()
  datetime.time()

Values can be added or modified post-construction using::

  datetime.addDays(days)
  datetime.addMSecs(milliseconds)
  datetime.addMonths(months)
  datetime.addSecs(seconds)
  datetime.addYears(years)

To check whether the DateTime object is currently set to empty, call::

  datetime.isNull()

The amount of time to another DateTime object can be found using the function calls::

  datetime.daysTo(object)
  datetime.secsTo(object)
  datetime.msecsTo(object)

The object parameter specifies another DateTime object, allowing for a comparison between the two objects.

The date and time held by the DateTime object can be set using other Date and Time objects with::

  datetime.setDate(date)
  datetime.setTime(time)

The date and time information held by the DateTime can be swapped with another using::

  datetime.swap(datetime)
