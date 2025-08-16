[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Arrays and Enumerated Types

[Arrays](array.html)

[Identifying Array Types](arrayComponents.html)

[Creating New Arrays](arrayInstance.html)

[Getting and Setting Arrays and Their Components](arraySetGet.html)

[Troubleshooting](arrayTrouble.html)

[Enumerated Types](enum.html)

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

[Troubleshooting](enumTrouble.html)

**Trail:** The Reflection API

[Home Page](../../index.html)
>
[The Reflection API](../index.html)

[« Previous](../member/index.html) • [Trail](../TOC.html) • [Next »](array.html)

# Lesson: Arrays and Enumerated Types

From the Java virtual machine's perspective, arrays and enumerated
types (or enums) are just classes. Many of the methods in
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
may be used on them. Reflection provides a few specific APIs for arrays and
enums. This lesson uses a series of code samples to describe how to
distinguish each of these objects from other classes and operate on them.
Various errors are also be examined.

### Arrays

Arrays have a component type and a length (which is not part of the type).
Arrays may be maniuplated either in their entirety or component by component.
Reflection provides the
[`java.lang.reflect.Array`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Array.html)
class for the latter purpose.

* [Identifying Array Types](arrayComponents.html) describes how to
  determine if a class member is a field of array type* [Creating New Arrays](arrayInstance.html) illustrates how to
    create new instances of arrays with simple and complex component types* [Getting and Setting Arrays and Their
      Components](arraySetGet.html) shows how to access fields of type array and individually
      access array elements* [Troubleshooting](arrayTrouble.html) covers common errors and
        programming misconceptions

### Enumerated Types

Enums are treated very much like ordinary classes in reflection code.
[`Class.isEnum()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isEnum())
tells whether a
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
represents and `enum`.
[`Class.getEnumConstants()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getEnumConstants())
retrieves the enum constants defined in an enum.
[`java.lang.reflect.Field.isEnumConstant()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#isEnumConstant())
indicates whether a field is an enumerated type.

* [Examining Enums](enumMembers.html) illustrates how to retrieve
  an enum's constants and any other fields, constructors, and methods* [Getting and Setting Fields with Enum Types](enumSetGet.html) 
    shows how to set and get fields with an enum constant value* [Troubleshooting](enumTrouble.html) describes common errors
      associated with enums

[« Previous](../member/index.html)
•
[Trail](../TOC.html)
•
[Next »](array.html)

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
  
**Next page:** Arrays




A browser with JavaScript enabled is required for this page to operate properly.