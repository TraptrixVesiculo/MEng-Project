[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects
  
**Section:** More on Classes

[Classes and Objects](index.html)

[Classes](classes.html)

[Declaring Classes](classdecl.html)

[Declaring Member Variables](variables.html)

[Defining Methods](methods.html)

[Providing Constructors for Your Classes](constructors.html)

[Passing Information to a Method or a Constructor](arguments.html)

[Objects](objects.html)

[Creating Objects](objectcreation.html)

[Using Objects](usingobject.html)

[More on Classes](more.html)

[Returning a Value from a Method](returnvalue.html)

[Using the this Keyword](thiskey.html)

Controlling Access to Members of a Class

[Understanding Instance and Class Members](classvars.html)

[Initializing Fields](initial.html)

[Summary of Creating and Using Classes and Objects](summaryclasses.html)

[Questions and Exercises](QandE/creating-questions.html)

[Questions and Exercises](QandE/objects-questions.html)

[Nested Classes](nested.html)

[Inner Class Example](innerclasses.html)

[Summary of Nested Classes](summarynested.html)

[Questions and Exercises](QandE/nested-questions.html)

[Enum Types](enum.html)

[Questions and Exercises](QandE/enum-questions.html)

[Annotations](annotations.html)

[Questions and Exercises](QandE/annotations-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Classes and Objects](index.html)

[« Previous](thiskey.html) • [Trail](../TOC.html) • [Next »](classvars.html)

# Controlling Access to Members of a Class

Access level modifiers determine whether other classes can use a particular
field or invoke a particular method. There are two levels of access control:

* At the top level—`public`, or *package-private* (no explicit modifier).
* At the member level—`public`, `private`, `protected`,
  or *package-private* (no explicit modifier).

A class may be declared with the modifier `public`, in which case that class
is visible to all classes everywhere. If a class has no modifier (the default, also known
as *package-private*), it is visible only within its own package (packages are named groups of
related classes—you will learn about them in a later
lesson.)

At the member level, you can also use the `public` modifier or no modifier (*package-private*)
just as with top-level classes, and with the same meaning. For members, there are two additional
access modifiers: `private` and `protected`.
The `private` modifier specifies that the member can only be accessed in its own class.
The `protected` modifier specifies that the member can only
be accessed within its own package (as with *package-private*) and, in addition, by a subclass of its class in another package.

The following table shows the access to members permitted by each modifier.
> **Access Levels**
>
> | Modifier | Class | Package | Subclass | World |
> | `public` | Y | Y | Y | Y |
> | `protected` | Y | Y | Y | N |
> | *no modifier* | Y | Y | N | N |
> | `private` | Y | N | N | N |

The first data column indicates whether the class itself has access to
the member defined by the access level. As you can see, a class
always has access to its own members. The second column indicates
whether classes in the same package as the class (regardless of
their parentage) have access to the member.
The third column indicates whether subclasses of the class —
declared outside this package — have access to the member.
The fourth column indicates whether all classes have access to the member.

Access levels affect you in two ways. First, when you use
classes that come from another source, such as the classes in the
Java platform, access levels determine which members of those classes
your own classes can use. Second, when you write a class, you need to
decide what access level every member variable and every method in
your class should have.

Let's look at a collection of classes and see how access levels affect visibility.
The following figure shows the four classes in this example and how they are related.

![Classes and Packages of the Example Used to Illustrate Access Levels](../../figures/java/classes-access.gif)

Classes and Packages of the Example Used to Illustrate Access Levels

The following table shows where the members of the Alpha class are visible for each of the access modifiers
that can be applied to them.
> **Visibility**
>
> | Modifier | Alpha | Beta | Alphasub | Gamma |
> | `public` | Y | Y | Y | Y |
> | `protected` | Y | Y | Y | N |
> | *no modifier* | Y | Y | N | N |
> | `private` | Y | N | N | N |

---

**Tips on Choosing an Access Level:** If other programmers use your class, you want to ensure that errors
from misuse cannot happen. Access levels can help you do this.

* Use the most restrictive access level that makes sense for a
  particular member. Use `private` unless you have a good
  reason not to.* Avoid `public` fields except for constants.
    (Many of the examples in the
    tutorial
    use public fields.
    This may help to illustrate some points concisely, but is not
    recommended for production code.)
    Public fields tend to link you to a particular implementation
    and limit your flexibility in changing your code.

---

[« Previous](thiskey.html)
•
[Trail](../TOC.html)
•
[Next »](classvars.html)

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

**Previous page:** Using the this Keyword
  
**Next page:** Understanding Instance and Class Members




A browser with JavaScript enabled is required for this page to operate properly.