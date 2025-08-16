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

[Methods](method.html)

[Obtaining Method Type Information](methodType.html)

[Retrieving and Parsing Method Modifiers](methodModifiers.html)

[Invoking Methods](methodInvocation.html)

[Troubleshooting](methodTrouble.html)

Constructors

[Finding Constructors](ctorLocation.html)

[Retrieving and Parsing Constructor Modifiers](ctorModifiers.html)

[Creating New Class Instances](ctorInstance.html)

[Troubleshooting](ctorTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](methodTrouble.html) • [Trail](../TOC.html) • [Next »](ctorLocation.html)

# Constructors

A *constructor* is used in the creation of an object that is an instance
of a class. Typically it performs operations required to initialize the class
before methods are invoked or fields are accessed. Constructors are never
inherited.

Similar to methods, reflection provides APIs to discover and retrieve the
constructors of a class and obtain declaration information such as the
modifiers, parameters, annotations, and thrown exceptions. New instances of
classes may also be created using a specified constructor. The key classes
used when working with constructors are
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
and
[`java.lang.reflect.Constructor`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html). Common operations involving constructors are covered in the following
sections:

* [Finding Constructors](ctorLocation.html) illustrates how to
  retrieve constructors with specific parameters* [Retrieving and Parsing Constructor
    Modifiers](ctorModifiers.html) shows how to obtain the modifiers of a constructor
    declaration and other information about the constructor* [Creating New Class Instances](ctorInstance.html) shows how to
      instantiate an instance of an object by invoking its constructor* [Troubleshooting](ctorTrouble.html) describes common errors
        which may be encountered while finding or invoking constructors

[« Previous](methodTrouble.html)
•
[Trail](../TOC.html)
•
[Next »](ctorLocation.html)

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
  
**Next page:** Finding Constructors




A browser with JavaScript enabled is required for this page to operate properly.