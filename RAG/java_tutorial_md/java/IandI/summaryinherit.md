[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance
  
**Section:** Inheritance

[Interfaces and Inheritance](index.html)

[Interfaces](createinterface.html)

[Defining an Interface](interfaceDef.html)

[Implementing an Interface](usinginterface.html)

[Using an Interface as a Type](interfaceAsType.html)

[Rewriting Interfaces](nogrow.html)

[Summary of Interfaces](summary-interface.html)

[Questions and Exercises](QandE/interfaces-questions.html)

[Inheritance](subclasses.html)

[Overriding and Hiding Methods](override.html)

[Polymorphism](polymorphism.html)

[Hiding Fields](hidevariables.html)

[Using the Keyword super](super.html)

[Object as a Superclass](objectclass.html)

[Writing Final Classes and Methods](final.html)

[Abstract Methods and Classes](abstract.html)

Summary of Inheritance

[Questions and Exercises](QandE/inherit-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Interfaces and Inheritance](index.html)

[« Previous](abstract.html) • [Trail](../TOC.html) • [Next »](QandE/inherit-questions.html)

# Summary of Inheritance

Except for the `Object` class, a class has
exactly one direct superclass. A class inherits fields and methods from all its
superclasses, whether
direct or indirect. A subclass can override methods that
it inherits, or it can hide fields or methods that it inherits.
(Note that hiding fields is generally bad
programming practice.)

The table in
[Overriding and Hiding Methods](override.html) section shows the effect of declaring a method with the same signature
as a method in the superclass.

The `Object` class is the top of the class hierarchy.
All classes are descendants from this class and inherit methods
from it. Useful methods inherited from `Object`
include `toString()`, `equals()`,
`clone()`, and `getClass()`.

You can prevent a class from being subclassed by using the
`final` keyword in the class's declaration. Similarly,
you can prevent a method from being overridden by subclasses by
declaring it as a final method.

An abstract class can only be subclassed; it cannot be
instantiated. An abstract class can contain abstract
methods—methods that are declared but not implemented.
Subclasses then provide the implementations for the abstract methods.

[« Previous](abstract.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/inherit-questions.html)

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

**Previous page:** Abstract Methods and Classes
  
**Next page:** Questions and Exercises: Inheritance




A browser with JavaScript enabled is required for this page to operate properly.