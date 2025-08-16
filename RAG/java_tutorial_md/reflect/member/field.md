[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Members

[Members](index.html)

Fields

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

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Members](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](fieldTypes.html)

# Fields

A *field* is a class, interface, or enum with an associated value.
Methods in the
[`java.lang.reflect.Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html)
class can retrieve information about the field, such as its name, type,
modifiers, and annotations. (The section
[Examining Class Modifiers and Types](../class/classModifiers.html)
in the
[Classes](../class/index.html)
lesson describes how to retrieve annotations.) There are also methods
which enable dynamic access and modification of the value of the
field. These tasks are covered in the following sections:

* [Obtaining Field Types](fieldTypes.html) describes how to get
  the declared and generic types of a field* [Retrieving and Parsing Field Modifiers](fieldModifiers.html)
    shows how to get portions of the field declaration such as
    `public` or `transient`* [Getting and Setting Field Values](fieldValues.html) illustrates
      how to access field values* [Troubleshooting](fieldTrouble.html) describes some common
        coding errors which may cause confusion

When writing an application such as a class browser, it might be useful to
find out which fields belong to a particular class. A class's fields are
identified by invoking
[`Class.getFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getFields()). The
[`getFields()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getFields())
method returns an array
of
[`Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html)
objects containing one object per accessible public field.

A public field is accessible if it is a member of either:

* this class* a superclass of this class* an interface implemented by this class* an interface extended from an interface implemented by this class

A field may be a class (instance) field, such as
[`java.io.Reader.lock`](http://download.oracle.com/javase/7/docs/api/java/io/Reader.html#lock)
, a static field, such as
[`java.lang.Integer.MAX_VALUE`](http://download.oracle.com/javase/7/docs/api/java/lang/Integer.html#MAX_VALUE)
, or an enum constant, such as
[`java.lang.Thread.State.WAITING`](http://download.oracle.com/javase/7/docs/api/java/lang/Thread.State.html#WAITING).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](fieldTypes.html)

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

**Previous page:** Members
  
**Next page:** Obtaining Field Types




A browser with JavaScript enabled is required for this page to operate properly.