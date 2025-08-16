[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects

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

[Controlling Access to Members of a Class](accesscontrol.html)

[Understanding Instance and Class Members](classvars.html)

[Initializing Fields](initial.html)

[Summary of Creating and Using Classes and Objects](summaryclasses.html)

[Questions and Exercises](QandE/creating-questions.html)

[Questions and Exercises](QandE/objects-questions.html)

Nested Classes

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

[« Previous](QandE/objects-questions.html) • [Trail](../TOC.html) • [Next »](innerclasses.html)

# Nested Classes

The Java programming language allows you to define a class within
another class. Such
a class is called a *nested class* and is illustrated here:

```

class OuterClass {
    ...
    class NestedClass {
        ...
    }
}

```

---

**Terminology:** Nested classes are divided into two categories: static and non-static. Nested classes that
are declared `static` are simply called *static nested classes*. Non-static nested classes are
called *inner classes*.

---

```

class OuterClass {
    ...
    static class StaticNestedClass {
        ...
    }
    class InnerClass {
        ...
    }
}

```

A nested class is a member of its enclosing class. Non-static nested classes (inner classes) have access to other members of
the enclosing class, even if they are declared private. Static nested classes do not have access to other members of
the enclosing class. As a member of the `OuterClass`,
a nested class can be declared `private`, `public`,
`protected`, or *package private*. (Recall that outer classes can only be declared
`public` or *package private*.)

### Why Use Nested Classes?

There are several compelling reasons for using nested classes, among them:

* It is a way of logically grouping classes that are only used in one place.
* It increases encapsulation.
* Nested classes can lead to more readable and maintainable code.

**Logical grouping of classes**—If a class is useful to only one other class,
then it is logical to embed it in that class and keep the two together. Nesting such "helper classes"
makes their package more streamlined.

**Increased encapsulation**—Consider two top-level classes, A and B, where B needs access to
members of A that would otherwise be declared `private`. By hiding class B within class
A, A's members can be declared private and B can access them. In addition, B itself can be hidden from the outside world.

**More readable, maintainable code**—Nesting small classes within top-level classes
places the code closer to where it is used.

### Static Nested Classes

As with class methods and variables, a static nested class is associated
with its outer class. And like static class methods, a static
nested class cannot refer directly to instance variables or
methods defined in its enclosing class — it can use
them only through an object reference.

---

**Note:** A static nested class interacts with the instance members of its outer class (and
other classes) just like any other top-level class. In effect, a static nested class is
behaviorally a top-level class that has been nested in another top-level class for packaging convenience.

---

Static nested classes are accessed using the enclosing class name:

```

OuterClass.StaticNestedClass

```

For example, to create an object for the static nested class, use this syntax:

```

OuterClass.StaticNestedClass nestedObject = new OuterClass.StaticNestedClass();

```

### Inner Classes

As with instance methods and variables, an inner class is
associated with an instance of its enclosing class and has
direct access to that object's
methods and fields. Also, because an inner class is associated with
an instance, it cannot define any static members itself.

Objects that are instances of an inner class exist *within* an instance of the outer class.
Consider the following classes:

```

class OuterClass {
    ...
    class InnerClass {
        ...
    }
}


```

An instance of `InnerClass`
can exist only within an instance of `OuterClass`
and has direct access to the
methods and fields of its enclosing instance.
The next figure illustrates this idea.

![An Instance of InnerClass Exists Within an Instance of OuterClass. ](../../figures/java/classes-inner.gif)

An Instance of InnerClass Exists Within an Instance of OuterClass

To instantiate an inner class, you must first instantiate the outer class.
Then, create the inner object within the outer object with this syntax:

```

OuterClass.InnerClass innerObject = outerObject.new InnerClass();

```

Additionally, there are two special kinds of inner classes:
local classes and anonymous classes (also called anonymous
inner classes). Both of these will be discussed briefly in the next section.

---

**Note:** If you want more information on the taxonomy of the different kinds of
classes in the Java programming language (which can be tricky to describe
concisely, clearly, and correctly),
you might want to read Joseph Darcy's blog:
[Nested, Inner, Member and Top-Level Classes](http://blogs.sun.com/darcy/entry/nested_inner_member_and_top).

---

[« Previous](QandE/objects-questions.html)
•
[Trail](../TOC.html)
•
[Next »](innerclasses.html)

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

**Previous page:** Questions and Exercises: Objects
  
**Next page:** Inner Class Example




A browser with JavaScript enabled is required for this page to operate properly.