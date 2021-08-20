# DayParts Calendar Overview

Rather than detailing the class itself, let's start with the initialization and usage syntaxes:

```py
default gt = DaypartsCalendar(
    ("20 Aug 2021", "Afternoon"), 
    (_("Morning"), 
     _("Afternoon"), 
     _("Evening"), 
     _("Night")), 
     ## [optional] 
     ## output = "{weekday} {day_part} (Day: {days_passed})"
    )
```
The first parameter is the start time and date.  
We can pass that as either a simple date string `"20 Aug 2021"` or as a tuple containing the named day part as well.  
The format for passing in the date is set as a class attribute called `date_input` and can be adjusted if needed.  
(for the `%char` naming conventions, see [The Python Datetime Format Page](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes))
