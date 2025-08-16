[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Members

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

[Constructors](ctor.html)

[Finding Constructors](ctorLocation.html)

[Retrieving and Parsing Constructor Modifiers](ctorModifiers.html)

[Creating New Class Instances](ctorInstance.html)

[Troubleshooting](ctorTrouble.html)

**Trail:** The Reflection API

[Home Page](../../index.html)
>
[The Reflection API](../index.html)

[« Previous](../class/index.html) • [Trail](../TOC.html) • [Next »](field.html)

# Lesson: Members

Reflection defines an interface
[`java.lang.reflect.Member`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Member.html)
which is implemented by
[`java.lang.reflect.Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html),
[`java.lang.reflect.Method`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html), and
[`java.lang.reflect.Constructor`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html)
. These objects will be discussed in this lesson. For each member, the lesson
will describe the associated APIs to retrieve declaration and type information,
any operations unique to the member (for example, setting the value of a field
or invoking a method), and commonly encountered errors. Each concept will be
illustrated with code samples and related output which approximate some
expected reflection uses.

---

**Note:** According to [*The
Java Language Specification, Third Edition*](http://java.sun.com/docs/books/jls/third_edition/html/j3TOC.html), the *members* of a
class are the inherited components of the class body including fields, methods,
nested classes, interfaces, and enumerated types. Since constructors are not
inherited, they are not members. This differs from the implementing classes of
[`java.lang.reflect.Member`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Member.html).

---

## Fields

Fields have a type and a value. The
[`java.lang.reflect.Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html)
class provides methods for accessing type information and setting and getting
values of a field on a given object.

* [Obtaining Field Types](fieldTypes.html) describes how to get
  the declared and generic types of a field* [Retrieving and Parsing Field Modifiers](fieldModifiers.html)
    shows how to get portions of the field declaration such as
    `public` or `transient`* [Getting and Setting Field Values](fieldValues.html) illustrates
      how to access field values* [Troubleshooting](fieldTrouble.html) describes some common
        coding errors which may cause confusion

## Methods

Methods have return values, parameters, and may throw exceptions. The
[`java.lang.reflect.Method`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html)
class provides methods for obtained the type information for the parameters and
return value. It may also be used to invoke methods on a given object.

* [Obtaining Method Type Information](methodType.html)
  shows how to enumerate methods declared in a class and obtains type
  information* [Retrieving and Parsing Method Modifiers](methodModifiers.html)
    describes how to access and decode modifiers and other information
    associated with the method* [Invoking Methods](methodInvocation.html) illustrates how to
      execute a method and obtain its return value* [Troubleshooting](methodTrouble.html) covers common errors
        encountered when finding or invoking methods

## Constructors

The Reflection APIs for constructors are defined in
[`java.lang.reflect.Constructor`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html)
and are similar to those for methods, with two major exceptions: first,
constructors have no return values; second, the invocation of a constructor
creates a new instance of an object for a given class.

* [Finding Constructors](ctorLocation.html) illustrates how to
  retrieve constructors with specific parameters* [Retrieving and Parsing Constructor
    Modifiers](ctorModifiers.html) shows how to obtain the modifiers of a constructor
    declaration and other information about the constructor* [Creating New Class Instances](ctorInstance.html) shows how to
      instantiate an instance of an object by invoking its constructor* [Troubleshooting](ctorTrouble.html) describes common errors
        which may be encountered while finding or invoking constructors

[« Previous](../class/index.html)
•
[Trail](../TOC.html)
•
[Next »](field.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Fields




A browser with JavaScript enabled is required for this page to operate properly.