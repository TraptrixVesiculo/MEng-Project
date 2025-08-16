[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Arrays and Enumerated Types

[Arrays and Enumerated Types](index.html)

[Arrays](array.html)

[Identifying Array Types](arrayComponents.html)

[Creating New Arrays](arrayInstance.html)

[Getting and Setting Arrays and Their Components](arraySetGet.html)

[Troubleshooting](arrayTrouble.html)

Enumerated Types

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

[Troubleshooting](enumTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](arrayTrouble.html) • [Trail](../TOC.html) • [Next »](enumMembers.html)

# Enumerated Types

An *enum* is a language construct that is used to define type-safe
enumerations which can be used when a fixed set of named values is desired.
All enums implicitly extend
[`java.lang.Enum`](http://download.oracle.com/javase/7/docs/api/java/lang/Enum.html). Enums may contain one or more *enum constants*, which define unique
instances of the enum type. An enum declaration defines an *enum type*
which is very similar to a class in that it may have members such as fields,
methods, and constructors (with some restrictions).

Since enums are classes, reflection has no need to define an explicit
`java.lang.reflect.Enum` class. The only Reflection APIs that are
specific to enums are
[`Class.isEnum()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#isEnum()),
[`Class.getEnumConstants()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getEnumConstants()), and
[`java.lang.reflect.Field.isEnumConstant()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#isEnumConstant()). Most reflective operations involving enums are the same as any other class
or member. For example, enum constants are implemented as `public static
final` fields on the enum. The following sections show how to use
[`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html)
and
[`java.lang.reflect.Field`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html)
with enums.

* [Examining Enums](enumMembers.html) illustrates how to retrieve
  an enum's constants and any other fields, constructors, and methods* [Getting and Setting Fields with Enum Types](enumSetGet.html) 
    shows how to set and get fields with an enum constant value* [Troubleshooting](enumTrouble.html) describes common errors
      associated with enums

For an introduction to enums, see the
lesson.

[« Previous](arrayTrouble.html)
•
[Trail](../TOC.html)
•
[Next »](enumMembers.html)

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
  
**Next page:** Examining Enums




A browser with JavaScript enabled is required for this page to operate properly.