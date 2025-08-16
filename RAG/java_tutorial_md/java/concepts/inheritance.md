[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Object-Oriented Programming Concepts

[Object-Oriented Programming Concepts](index.html)

[What Is an Object?](object.html)

[What Is a Class?](class.html)

What Is Inheritance?

[What Is an Interface?](interface.html)

[What Is a Package?](package.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Object-Oriented Programming Concepts](index.html)

[« Previous](class.html) • [Trail](../TOC.html) • [Next »](interface.html)

# What Is Inheritance?

Different kinds of objects often have a certain amount in common with each other.
Mountain bikes, road bikes, and tandem bikes, for example, all share the characteristics of bicycles (current speed, current pedal cadence, current gear). Yet each also defines additional features that make them different: tandem bicycles have two seats and two sets of handlebars; road bikes have drop handlebars; some mountain bikes have an additional chain ring, giving them a lower gear ratio.

Object-oriented programming allows classes to *inherit* commonly used state and
behavior from other classes. In this example, `Bicycle` now becomes the *superclass* of
`MountainBike`, `RoadBike`, and `TandemBike`.
In the Java programming language, each class is allowed to have one direct superclass, and each
superclass has the potential for an unlimited number of *subclasses*:

![A diagram of classes in a hierarchy.](../../figures/java/concepts-bikeHeirarchy.gif)

A hierarchy of bicycle classes.

The syntax for creating a subclass is simple. At the beginning of your class declaration, use the `extends` keyword, followed by the name of the class to inherit from:

```

class MountainBike extends Bicycle {

     // new fields and methods defining a mountain bike would go here

}

```

This gives `MountainBike` all the same fields and methods as `Bicycle`, yet allows its code to focus exclusively on the features that make it unique. This makes code for your subclasses easy to read. However, you must take care to properly document the state and behavior that each superclass defines, since that code will not appear in the source file of each subclass.

[« Previous](class.html)
•
[Trail](../TOC.html)
•
[Next »](interface.html)

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

**Previous page:** What Is a Class?
  
**Next page:** What Is an Interface?




A browser with JavaScript enabled is required for this page to operate properly.