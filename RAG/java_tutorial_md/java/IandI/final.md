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

Writing Final Classes and Methods

[Abstract Methods and Classes](abstract.html)

[Summary of Inheritance](summaryinherit.html)

[Questions and Exercises](QandE/inherit-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Interfaces and Inheritance](index.html)

[« Previous](objectclass.html) • [Trail](../TOC.html) • [Next »](abstract.html)

# Writing Final Classes and Methods

You can declare some or all of a class's methods *final*.
You use the `final` keyword in a method
declaration to indicate that the method cannot be overridden
by subclasses. The `Object` class does this—a number
of its methods are `final`.

You might wish to make a method final if it has an implementation
that should not be changed and it is critical to the consistent
state of the object. For example, you might want to make the
`getFirstPlayer` method in this
`ChessAlgorithm` class final:

```

class ChessAlgorithm {
    enum ChessPlayer { WHITE, BLACK }
    ...
    final ChessPlayer getFirstPlayer() {
        return ChessPlayer.WHITE;
    }
    ...
}

```

Methods called from constructors should generally be declared final.
If a constructor calls a non-final method, a subclass may redefine
that method with surprising or undesirable results.

Note that you can also declare an entire class final — this
prevents the class from being subclassed. This is particularly
useful, for example, when creating an immutable class like the `String` class.

[« Previous](objectclass.html)
•
[Trail](../TOC.html)
•
[Next »](abstract.html)

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

**Previous page:** Object as a Superclass
  
**Next page:** Abstract Methods and Classes




A browser with JavaScript enabled is required for this page to operate properly.