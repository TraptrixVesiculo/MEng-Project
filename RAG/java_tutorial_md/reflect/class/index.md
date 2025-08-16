[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Classes

[Retrieving Class Objects](classNew.html)

[Examining Class Modifiers and Types](classModifiers.html)

[Discovering Class Members](classMembers.html)

[Troubleshooting](classTrouble.html)

**Trail:** The Reflection API

[Home Page](../../index.html)
>
[The Reflection API](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](classNew.html)

# Lesson: Classes

Every object is either a reference or primitive type. Reference types all
inherit from
[`java.lang.Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). Classes, enums, arrays, and interfaces are all reference types. There is a
fixed set of primitive types: `boolean`, `byte`,
`short`, `int`, `long`, `char`,
`float`, and `double`. Examples of reference types
include
[`java.lang.String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html), all of the wrapper classes for primitive types such as
[`java.lang.Double`](http://download.oracle.com/javase/7/docs/api/java/lang/Double.html), the interface
[`java.io.Serializable`](http://download.oracle.com/javase/7/docs/api/java/io/Serializable.html), and the enum
[`javax.swing.SortOrder`](http://download.oracle.com/javase/7/docs/api/javax/swing/SortOrder.html).

For every type of object, the Java virtual machine instantiates an
immutable instance of
[`java.lang.Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
which provides methods to examine the runtime properties of the object
including its members and type information.
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
also provides the ability to create new classes and objects. Most importantly,
it is the entry point for all of the Reflection APIs. This lesson covers the
most commonly used reflection operations involving classes:

* [Retrieving Class Objects](classNew.html) describes the ways to
  get a
  [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)* [Examining Class Modifiers and Types](classModifiers.html)
    shows how to access the class declaration information* [Discovering Class Members](classMembers.html) illustrates how
      to list the constructors, fields, methods, and nested classes in a class
      * [Troubleshooting](classTrouble.html) describes common errors
        encountered when using
        [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](classNew.html)

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

**Previous page:** Table of Contents
  
**Next page:** Retrieving Class Objects




A browser with JavaScript enabled is required for this page to operate properly.