[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Arrays and Enumerated Types

[Arrays and Enumerated Types](index.html)

Arrays

[Identifying Array Types](arrayComponents.html)

[Creating New Arrays](arrayInstance.html)

[Getting and Setting Arrays and Their Components](arraySetGet.html)

[Troubleshooting](arrayTrouble.html)

[Enumerated Types](enum.html)

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

[Troubleshooting](enumTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](arrayComponents.html)

# Arrays

An *array* is an object of reference type which contains a fixed number
of components of the same type; the length of an array is immutable. Creating
an instance of an array requires knowledge of the length and component type.
Each component may be a primitive type (e.g. `byte`,
`int`, or `double`), a reference type
(e.g.
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html),
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html), or
[`java.nio.CharBuffer`](http://download.oracle.com/javase/7/docs/api/java/nio/CharBuffer.html)), or an array. Multi-dimensional arrays are really just arrays which contain
components of array type.

Arrays are implemented in the Java virtual machine. The only methods on
arrays are those inherited from
[`Object`](http://download.oracle.com/javase/7/docs/api/java/lang/Object.html). The length of an array is not part of its type; arrays have a
`length` field which is accessible via
[`java.lang.reflect.Array.getLength()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Array.html#getLength(java.lang.Object)).

Reflection provides methods for accessing array types and array component
types, creating new arrays, and retrieving and setting array component values.
The following sections include examples of common operations on arrays:

* [Identifying Array Types](arrayComponents.html) describes how to
  determine if a class member is a field of array type* [Creating New Arrays](arrayInstance.html) illustrates how to
    create new instances of arrays with simple and complex component types* [Getting and Setting Arrays and Their
      Components](arraySetGet.html) shows how to access fields of type array and individually
      access array elements* [Troubleshooting](arrayTrouble.html) covers common errors and
        programming misconceptions

All of these operations are supported via `static` methods in
[`java.lang.reflect.Array`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Array.html).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](arrayComponents.html)

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

**Previous page:** Arrays and Enumerated Types
  
**Next page:** Identifying Array Types




A browser with JavaScript enabled is required for this page to operate properly.