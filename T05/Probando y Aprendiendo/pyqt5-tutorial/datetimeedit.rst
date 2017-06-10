DateTimeEdit
============
The DateTimeEdit widget provides the functionality of both the :doc:`dateedit` and :doc:`timeedit` widgets in one, allowing both time and date information to be modified and displayed to the user.

===========
Constructor
===========
The construction of the DateTimeEdit is made via::

  datetimeedit = QDateTimeEdit()

=======
Methods
=======
The currently displayed Date, Time, and DateTime objects can be obtained from the DateTimeEdit by calling the methods::

  datetimeedit.date()
  datetimeedit.dateTime()
  datetimeedit.time()

Minimum and maximum dates and times can be defined which permit only a range to be accessed by::

  datetimeedit.setMinimumDate(date)
  datetimeedit.setMinimumDateTime(datetime)
  datetimeedit.setMinimumTime(time)
  datetimeedit.setMaximumDate(date)
  datetimeedit.setMaximumDateTime(datetime)
  datetimeedit.setMaximumTime(time)

The *date*, *time* and *datetime* parameters should be set to an appropriate object of the respective type :doc:`date`, :doc:`time`, and :doc:`datetime`.

Date, Time and DateTime ranges can be defined via a single method using::

  datetimeedit.setTimeRange(minimum, maximum)
  datetimeedit.setDateTimeRange(minimum, maximum)
  datetimeedit.setDateRange(minimum, maximum)

The minimum and maximum dates and times are retrieved via::

  datetimeedit.minimumDate()
  datetimeedit.minimumDateTime()
  datetimeedit.minimumTime()
  datetimeedit.maximumDate()
  datetimeedit.maximumDateTime()
  datetimeedit.maximumTime()

If required, the minimum and maximum defined objects from above can be cleared::

  datetimeedit.clearMinimumDate()
  datetimeedit.clearMinimumDateTime()
  datetimeedit.clearMinimumTime()
  datetimeedit.clearMaximumDate()
  datetimeedit.clearMaximumDateTime()
  datetimeedit.clearMaximumTime()

A :doc:`calendar` widget can be added to the DateTimeEdit using::

  datetimeedit.setCalendarWidget(widget)
