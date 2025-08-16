[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Object-Oriented Programming Concepts

[Object-Oriented Programming Concepts](index.html)

What Is an Object?

[What Is a Class?](class.html)

[What Is Inheritance?](inheritance.html)

[What Is an Interface?](interface.html)

[What Is a Package?](package.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Object-Oriented Programming Concepts](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](class.html)

# What Is an Object?

Objects are key to understanding
*object-oriented*
technology. Look around right now and you'll find many examples of real-world objects: your dog, your desk, your television set, your bicycle.

Real-world objects share two characteristics: They all have *state* and *behavior*. Dogs have state (name, color, breed, hungry) and behavior (barking, fetching, wagging tail).
Bicycles also have state (current gear, current pedal cadence, current speed)
and behavior (changing gear, changing pedal cadence, applying brakes).
Identifying the state and behavior for real-world objects is a great way to begin thinking in terms of object-oriented programming.

Take a minute right now to observe the real-world objects that are in your immediate area. For each object that you see, ask yourself two questions: "What possible states can this object be in?" and "What possible behavior can this object perform?". Make sure to write down your observations.
As you do, you'll notice that real-world objects vary in complexity; your desktop lamp may have only two possible states (on and off) and two possible behaviors (turn on, turn off), but your desktop radio might have additional states (on, off, current volume, current station) and behavior (turn on, turn off, increase volume, decrease volume, seek, scan, and tune). You may also notice that some objects, in turn, will also contain other objects. These real-world observations all translate into the world of object-oriented programming.

![A circle with an inner circle filled with items, surrounded by gray wedges representing methods that allow access to the inner circle.](../../figures/java/concepts-object.gif)

A software object.

Software objects are conceptually similar to real-world objects: they too consist of
state and related behavior. An object stores its state in
*fields*
(variables in some programming languages)
and exposes its behavior through
*methods*
(functions in some programming languages). Methods operate on an object's internal state and serve as the primary mechanism for object-to-object communication. Hiding internal state and requiring all interaction to be performed through an object's methods is known as
*data encapsulation*
— a fundamental principle of object-oriented programming.

Consider a bicycle, for example:

![A picture of an object, with bibycle methods and instance variables.](../../figures/java/concepts-bicycleObject.gif)

A bicycle modeled as a software object.

By attributing state (current speed, current pedal cadence, and current gear) and providing methods for changing that state, the object remains in control of how the outside world is allowed to use it. For example, if the bicycle only has 6 gears, a method
to change gears could reject any value that is less than 1 or greater than 6.

Bundling code into individual software objects provides a number of benefits, including:

1. Modularity: The source code for an object can be written and maintained independently of the source code for other objects. Once created, an object can be easily passed around inside the system.

   - Information-hiding: By interacting only with an object's methods, the details of its internal implementation remain hidden from the outside world.

     - Code re-use: If an object already exists (perhaps written by another software developer),
       you can use that object in your program. This allows specialists to implement/test/debug complex, task-specific objects, which you
       can then trust to run in your own code.

       - Pluggability and debugging ease: If a particular object turns out to be problematic, you can simply
         remove it from your application and plug in a different object as its replacement.
         This is analogous to fixing mechanical problems in the real world. If a bolt breaks, you replace *it*, not the entire machine.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](class.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Object-Oriented Programming Concepts
  
**Next page:** What Is a Class?




A browser with JavaScript enabled is required for this page to operate properly.