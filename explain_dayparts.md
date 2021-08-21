# DayParts Calendar Overview

Rather than detailing the class itself, let's start with the initialization and usage syntaxes:

## Initialization
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
These names reflect the `@property` methods within the class, which return un-translated values that are then translated within the `__repr__` method.  
Extending these to add your own should follow similar logic, perhaps using the `%char` values from [The Python Datetime Format Page](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) in a manner similar to `weekday`. Just remember to have the property methods return un-translated values if you want to run tests against them.

The format passed or set there is used within the str/repr of the class and translation is applied there (within the `__repr__` method)

## Displaying the information

The standard way to display information is to just call the `__repr__` method which is done when the class is read as a string.  
Within Ren'Py this is done simply by using string interpolation:  
```py
## Presuming the variable gt was used to initialize the GameTime object

screen viewdate():
    vbox:
        text "[gt]" ## Interpolation is advised
        text str(gt) ## Alternate for places where interpolation is not supported

label viewdate_label():
    e "It is [gt]"
```
You could add further methods to output in different ways, just remember to `renpy.substitute` the return if you need it translated.

## Altering the Date or Day Part within the game

Advancing the current date or day part is done by using the `alter` method of the instance and can be given parameters:
```py
    # With no keywords the day part just advances by one
    # Note: This can cycle round to first day part of the next day
    $ gt.alter()

    # Using "sleep" keyword to sleep until the first day part of the next day
    $ gt.alter(sleep=1)

    # Using "steps" keyword to move a set number of day part steps
    # This can also cause the day to change if those steps cycle through
    $ gt.alter(steps=11)

    # Both "sleep" and "steps" can be used together
    # Note: The sleep is done first so the steps then count from the first day part
    $ gt.alter(sleep=2, steps=2)

    # Negative numbers can be used if needed
    # This would move to first day part of the day before and then two more steps back
    $ gt.alter(sleep=-1, steps=-2)
```
You *could* add extra methods if wanted.

## Testing against the Current Game Date and Day Part

Through use of the dunder equality methods of the instance and include all the usual operands.
All comparisons are passed a Date string or a tuple containing Date string and Day Part string.
```py
    if gt == "03 Jun 2008":
        pass
    if gt == ("03 Jun 2008", "Night"):
        pass
```
The logic of the comparison is done slightly differently depending on what operand and value is used:

== "03 Jun 2008"
Comparison is evaluated against the current day part of the supplied date. Thus if the date matches the test is valid.

!= "03 Jun 2008"
Comparison is evaluated against the current day part of the supplied date and then toggled. Thus if the date matches the test is not valid.

> "02 Jun 2008"
>= "02 Jun 2008"
Comparison is done against the last day part of the supplied date.

Other comparisons where only the Date is supplied are done against the first day part of that date.

#### If you find an error in any conparison test, please let me know and I will check it.



[![Support me on Patreon](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/bePatron?u=19978585)

[Return to Home Page](README.md)
