# DayParts Time Keeping

#### Note: All you really need is the file in [The game folder](game). Just one small script file. This can be dropped into a new or existing project and a label called to view an example (details in the .rpy file). 
#### Alternatively, just clone the lot as a zip from [The Repository Main Page](https://github.com/RenpyRemix/dayparts-calendar)

This time keeping system uses named parts of the day (such as Morning, Afternoon etc) and allows easy progress through them.

#### The main features are:
- Simple setup, just default an instance with start values and day part names.
- Easy to progress time, just call a method and optionally add parameters to control the steps moved or number of sleeps.
- In-built translation, even the weekday and month names (though remember to update both the /tl/lang/common.rpy as well as the translated day parts)
- In-built equality tests allowing code to check values versus needs.
 
Note though that the internal hours are not directly related to the day part names.  
If you name a day part "Afternoon", do not expect any "%H" output to also be in the afternoon.

#### This system is not built to also output hours or minutes of the day, just the named day part.

[![Support me on Patreon](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/bePatron?u=19978585)


### Further Reading:

The overview of the system is more fully explained in [DayParts Calendar Overview](explain_dayparts.md)

### Please note:

The way this approach works might not be suitable for complete beginners. It is a basic platform on which to build a system that might grow to include other features. As such it will likely require some knowledge of Ren'Py in order to extend it to your particular needs. 

Though I have tried to explain it as simply as possible, I will not be available to help extend it unless under a paid contract.
Basically, if you want it to do more, you are expected to know enough Ren'Py to handle that yourself (or consider paying someone)


