[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance
  
**Section:** Interfaces

[Interfaces and Inheritance](index.html)

[Interfaces](createinterface.html)

Defining an Interface

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

[Summary of Inheritance](summaryinherit.html)

[Questions and Exercises](QandE/inherit-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Interfaces and Inheritance](index.html)

[« Previous](createinterface.html) • [Trail](../TOC.html) • [Next »](usinginterface.html)

# Defining an Interface

An interface declaration consists of modifiers, the keyword `interface`,
the interface name, a comma-separated list of parent interfaces (if any), and the interface body. For example:

```

public interface GroupedInterface extends Interface1,
                                        Interface2, Interface3 {

   // constant declarations
   double E = 2.718282;  // base of natural logarithms

   // method signatures
   void doSomething (int i, double x);
   int doSomethingElse(String s);

}

```

The `public` access specifier indicates that the interface can be used by any
class in any package. If you do not specify that the interface
is public, your interface will be accessible only to classes
defined in the same package as the interface.

An interface can extend other interfaces,
just as a class can extend or subclass another class. However,
whereas a class can extend only one other class, an interface
can extend any number of interfaces. The interface declaration includes
a comma-separated list of all the interfaces that it extends.

### The Interface Body

The interface body contains method declarations for all the
methods included in the interface. A method declaration within
an interface is followed by a semicolon, but no braces, because
an interface does not provide implementations for the methods
declared within it. All methods declared in an interface are implicitly
`public`, so the public modifier can be omitted.

An interface can contain constant declarations in addition to
method declarations. All constant values defined in an interface
are implicitly `public`, `static`, and `final`. Once again, these
modifiers can be omitted.

[« Previous](createinterface.html)
•
[Trail](../TOC.html)
•
[Next »](usinginterface.html)

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

**Previous page:** Interfaces
  
**Next page:** Implementing an Interface




A browser with JavaScript enabled is required for this page to operate properly.