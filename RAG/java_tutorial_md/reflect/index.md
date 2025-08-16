[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)

[Home Page](../index.html)

[« Previous](../index.html)
•
[Trail](./TOC.html)
•
[Next »](./class/index.html)

# Trail: The Reflection API

## Uses of Reflection

Reflection is commonly used by programs which require the ability to
examine or modify the runtime behavior of applications running in the Java
virtual machine. This is a relatively advanced feature and should be used only
by developers who have a strong grasp of the fundamentals of the language.
With that caveat in mind, reflection is a powerful technique and can enable
applications to perform operations which would otherwise be impossible.

**Extensibility Features**: An application may make use of external, user-defined classes by creating instances of extensibility objects using their fully-qualified names. **Class Browsers and Visual Development Environments**: A class browser needs to be able to enumerate the members of classes. Visual development environments can benefit from making use of type information available in reflection to aid the developer in writing correct code. **Debuggers and Test Tools**: Debuggers need to be able to examine private members on classes. Test harnesses can make use of reflection to systematically call a discoverable set APIs defined on a class, to insure a high level of code coverage in a test suite.

## Drawbacks of Reflection

Reflection is powerful, but should not be used indiscriminately. If it is
possible to perform an operation without using reflection, then it is
preferable to avoid using it. The following concerns should be kept in mind
when accessing code via reflection.

**Performance Overhead**: Because reflection involves types that are dynamically resolved, certain Java virtual machine optimizations can not be performed. Consequently, reflective operations have slower performance than their non-reflective counterparts, and should be avoided in sections of code which are called frequently in performance-sensitive applications. **Security Restrictions**: Reflection requires a runtime permission which may not be present when running under a security manager. This is in an important consideration for code which has to run in a restricted security context, such as in an Applet. **Exposure of Internals**: Since reflection allows code to perform operations that would be illegal in non-reflective code, such as accessing `private` fields and methods, the use of reflection can result in unexpected side-effects, which may render code dysfunctional and may destroy portability. Reflective code breaks abstractions and therefore may change behavior with upgrades of the platform.

## Trail Lessons

This trail covers common uses of reflection for accessing and manipulating
classes, fields, methods, and constructors. Each lesson contains code
examples, tips, and troubleshooting information.

[![trail icon](../images/reflectionsm.GIF) **Classes**](class/index.html): This lesson shows the various ways to obtain a [`Class`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html) object and use it to examine properties of a class, including its declaration and contents. [![trail icon](../images/reflectionsm.GIF) **Members**](member/index.html): This lesson describes how to use the Reflection APIs to find the fields, methods, and constructors of a class. Examples are provided for setting and getting field values, invoking methods, and creating new instances of objects using specific constructors. [![trail icon](../images/reflectionsm.GIF) **Arrays and Enumerated Types**](special/index.html): This lesson introduces two special types of classes: arrays, which are generated at runtime, and `enum` types, which define unique named object instances. Sample code shows how to retrieve the component type for an array and how to set and get fields with array or `enum` types.

---

**Note:** The examples in this trail are designed for experimenting with the Reflection
APIs. The handling of exceptions therefore is not the same as would be used in
production code. In particular, in production code it is not recommended to
dump stack traces that are visible to the user.

---

[« Previous](../index.html)
•
[TOC](./TOC.html)
•
[Next »](./class/index.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Beginning of Tutorial
  
**Next page:** Classes




A browser with JavaScript enabled is required for this page to operate properly.