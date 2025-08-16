[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Members

[Members](index.html)

[Fields](field.html)

[Obtaining Field Types](fieldTypes.html)

[Retrieving and Parsing Field Modifiers](fieldModifiers.html)

[Getting and Setting Field Values](fieldValues.html)

[Troubleshooting](fieldTrouble.html)

Methods

[Obtaining Method Type Information](methodType.html)

[Retrieving and Parsing Method Modifiers](methodModifiers.html)

[Invoking Methods](methodInvocation.html)

[Troubleshooting](methodTrouble.html)

[Constructors](ctor.html)

[Finding Constructors](ctorLocation.html)

[Retrieving and Parsing Constructor Modifiers](ctorModifiers.html)

[Creating New Class Instances](ctorInstance.html)

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](fieldTrouble.html) • [Trail](../TOC.html) • [Next »](methodType.html)

# Methods

A *method* contains executable code which may be invoked. Methods are
inherited and in non-reflective code behaviors such as overloading, overriding,
and hiding are enforced by the compiler. In contrast, reflective code makes it
possible for method selection to be restricted to a specific class without
considering its superclasses. Superclass methods may be accessed but it is
possible to determine their declaring class; this is impossible to discover
programmatically without reflection and is the source of many subtle bugs.

The
[`java.lang.reflect.Method`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html)
class provides APIs to access information about a method's modifiers, return
type, parameters, annotations, and thrown exceptions. It also be used to
invoke methods. These topics are covered by the following sections:

* [Obtaining Method Type Information](methodType.html)
  shows how to enumerate methods declared in a class and obtains type
  information* [Retrieving and Parsing Method Modifiers](methodModifiers.html)
    describes how to access and decode modifiers and other information
    associated with the method* [Invoking Methods](methodInvocation.html) illustrates how to
      execute a method and obtain its return value* [Troubleshooting](methodTrouble.html) covers common errors
        encountered when finding or invoking methods

[« Previous](fieldTrouble.html)
•
[Trail](../TOC.html)
•
[Next »](methodType.html)

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

**Previous page:** Troubleshooting
  
**Next page:** Obtaining Method Type Information




A browser with JavaScript enabled is required for this page to operate properly.