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
The format for passing in the date is set as a class attribute called `date_input` and can be adjusted if needed. Note though that you should not use %H or %M as the system does not use hours or minutes that way.  
(for the `%char` naming conventions, see [The Python Datetime Format Page](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes))

The second parameter is the tuple (or list) of day parts (starting from early and working to late).  
These should likely be wrapped in `_()` in order to mark them as translatable.  

The final (optional) parameter is the `output` and should contain a string with name `{}` format braces.
The available names are:
```py
    {day} ## Numeric day of month, 1 to 31
    {weekday} ## String long weekday, Sunday to Saturday
    {month} ## String short month, Jan to Dec
    {days_passed} ## Numeric count of days passed
    {day_part} ## String day part, as supplied in initialization
```
    

[![Support me on Patreon](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/bePatron?u=19978585)

[Return to Home Page](README.md)
