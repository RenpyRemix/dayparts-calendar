
init python:

    import time, datetime

    class DaypartsCalendar(object):

        date_input = "%d %b %Y" ## 01 Jan 2021

        def __init__(self, dt="01 Jan 2018", parts=None, output=None):
            self.day_parts = parts or []
            if not self.day_parts:
                raise AttributeError, "GameTime expects a list of day parts"
            self.day_parts = tuple(list(self.day_parts))
            self.len_parts = len(self.day_parts)
            self._dt = self.parse_input(dt)
            self.start = self._dt 
            self.output = output or "{weekday} {day} {month} ({day_part})"

        def alter(self, **kwargs):
            if "sleep" in kwargs:
                # Always "sleep" until first day part (plus optional steps)
                self._dt += datetime.timedelta(
                    days = kwargs["sleep"],
                    hours = -self._dt.hour)
                # Set extra steps to zero if not passed
                kwargs['steps'] = kwargs.get('steps', 0)
            steps = kwargs.get("steps", 1)
            if steps:
                days, hours = divmod(self._dt.hour + steps, self.len_parts)
                hours -= self._dt.hour
                self._dt += datetime.timedelta(days=days, hours=hours)

        def __repr__(self):
            scope = {
                "day" : self.day,
                "weekday" : "%A",
                "month" : "%B",
                "days_passed" : self.days_passed,
                "day_part" : renpy.substitute(self.day_part)}
            return _strftime(
                self.output.format(**scope), 
                self._dt.timetuple())

        @property
        def day(self):
            return time.strftime("%d", self._dt.timetuple())

        @property
        def weekday(self):
            return time.strftime("%A", self._dt.timetuple())

        @property
        def month(self):
            return time.strftime("%B", self._dt.timetuple())

        @property
        def days_passed(self):
            return self._dt.toordinal() - self.start.toordinal() + 1

        @property
        def day_part(self):
            return self.day_parts[self._dt.hour]

        def parse_input(self, date_input):
            if not isinstance(date_input, (list, tuple)):
                date_input = [date_input, self.day_parts[0]]
            date = datetime.datetime.strptime(date_input[0], self.date_input)
            hour = self.day_parts.index(date_input[1])
            date += datetime.timedelta(hours=hour)
            return date

        def __eq__(self, other):
            ## For == we use current day part if not passed
            if not isinstance(other, (list, tuple)):
                other = [other, self.day_parts[self._dt.hour]]
            return self._dt == self.parse_input(other)

        def __ne__(self, other):
            return not self.__eq__(other)

        def __lt__(self, other):
            return self._dt < self.parse_input(other)

        def __gt__(self, other):
            ## For > we use final day part if not passed
            if not isinstance(other, (list, tuple)):
                other = [other, self.day_parts[-1]]
            return self._dt > self.parse_input(other)

        def __le__(self, other):
            return self.__lt__(other) or self.__eq__(other)

        def __ge__(self, other):
            return self.__gt__(other) or self.__eq__(other)




default gt = DaypartsCalendar(
    ("01 Jun 2008", "Noon"), 
    (_("Early Morning"), 
     _("Morning"), 
     _("Noon"),
     _("Afternoon"), 
     _("Evening"), 
     _("Night"), 
     _("Late Night")))

screen dayparts_calendar_viewdate():
    vbox:
        text "[gt]"
        ### Just testing translations
        # textbutton "English" action Language(None)
        # textbutton "French" action Language("french")


label dayparts_calendar_example:

    show screen dayparts_calendar_viewdate
    "Expecting: Sunday 01 June (Noon)"

    # No parameters = one steps forward
    $ gt.alter()
    "Expecting: Sunday 01 June (Afternoon)"

    # Using "sleep" keyword to sleep until next morning
    $ gt.alter(sleep=1)
    "Expecting: Monday 02 June (Early Morning)"

    # Using "steps" keyword to move a set number of steps
    $ gt.alter(steps=11)
    "Expecting: Tuesday 03 June (Evening)"

    # Both "sleep" and "steps"
    $ gt.alter(sleep=2, steps=2)
    "Expecting: Thursday 05 June (Noon)"

    # Test negative numbers
    $ gt.alter(sleep=-1, steps=-2)
    "Expecting: Tuesday 03 June (Night)"

    ## Testing versus --- Tuesday 03 June (Night)

    # Testing conditions : ==
    if gt == "03 Jun 2008":
        "Passed == with just date string"
    if gt == ("03 Jun 2008", "Night"):
        "Passed == with date tuple"
    if not gt == ("03 Jun 2008", "Noon"):
        "Correctly Failed == with date tuple"

    # Testing conditions : !=
    if gt != "09 Jun 2008":
        "Passed != with just date string"
    if gt != ("03 Jun 2008", "Evening"):
        "Passed != with date tuple"
    if not gt != ("03 Jun 2008", "Night"):
        "Correctly Failed != with date tuple"

    # Testing conditions : <
    if gt < "04 Jun 2008":
        "Passed < with just date string"
    if gt < ("03 Jun 2008", "Late Night"):
        "Passed < with date tuple"
    if not gt < "03 Jun 2008":
        "Correctly Failed < with just date string"

    # Testing conditions : >
    if gt > "02 Jun 2008":
        "Passed > with just date string"
    if gt > ("03 Jun 2008", "Evening"):
        "Passed > with date tuple"
    if not gt > "03 Jun 2008":
        "Correctly Failed > with just date string"

    # Testing conditions : <=
    if gt <= "03 Jun 2008":
        "Passed <= with just date string"
    if gt <= ("03 Jun 2008", "Late Night"):
        "Passed <= with date tuple"
    if not gt <= ("03 Jun 2008", "Evening"):
        "Correctly Failed <= with date tuple"

    # Testing conditions : >=
    if gt >= "03 Jun 2008":
        "Passed >= with just date string"
    if gt >= ("03 Jun 2008", "Evening"):
        "Passed >= with date tuple"
    if not gt >= ("03 Jun 2008", "Late Night"):
        "Correctly Failed >= with date tuple"

    # Testing conditions : pythonic x < obj < y
    if "02 Jun 2008" < gt < "04 Jun 2008":
        "Passed pythonic x < obj < y with just date string"
    if ("03 Jun 2008", "Night") >= gt > ("03 Jun 2008", "Evening"):
        "Passed pythonic x >= obj > y with date tuple"

    ## Note there is no simple >, <, >= etc tests for these
    if gt.weekday == "Tuesday":
        "Passed gt.weekday test"

    if gt.day_part == "Night":
        "Passed gt.day_part test"

    "Done"

    return
