Date
====
The Date object provides an interface for handling dates, and is used by some widgets such as the :doc:`calendar` to represent a date.

.. note::

  Alternatives to the Date object includes the :doc:`datetime`, allowing both times and dates to be stored and the :doc:`time` object which is used only for time values.

===========
Constructor
===========
Construction of a Date object is made using::

  date = QDate()

Alternatively, the year, month, and day, can be specified at construction time via::

  date = QDate(year, month, day)

=======
Methods
=======
A date can also be set post-construction of the object with::

  date.setDate(year, month, day)

To retrieve a date from the Date object call::

  date.getDate()

The number corresponding to each of the year, month, and day values can be fetched individually by::

  date.year()
  date.month()
  date.day()

The held year, month, and day values in the Date object can be incremented using the method::

  date.addYears(years)
  date.addMonths(months)
  date.addDays(days)

All the above functions return a new Date object with the new incremented date held.

The day of the week and day of the year values can be obtained using::

  date.dayOfWeek()
  date.dayOfYear()

Returning the number of days in the currently set month or year is done via::

  date.daysInMonth()
  date.daysInYear()

The number of days until a particular day is reached can be found by passing a Date object using::

  date.daysTo(date)

The validity of the current Date object can be checked with::

  date.isValid()

Alternatively, the Date object can be checked to see if it has been set or not by::

  date.isNull()

The day or month string can be obtained from the Date object using the methods::

  date.longDayName(day)
  date.longMonthName(month)
  date.shortDayName(day)
  date.shortMonthName(month)

The long form functions return "Monday" or "October", while the short form returns "Tue" or "Mar". The *day* or *month* parameter should be the number of the day or month to be returned.

To check whether a particular year is a leap year or not, use::

  date.isLeapYear(year)

A Date object can be compared to another Date via the methods::

  date.operator!=(date)
  date.operator==(date)
  date.operator>(date)
  date.operator<(date)
  date.operator>=(date)
  date.operator<=(date)
