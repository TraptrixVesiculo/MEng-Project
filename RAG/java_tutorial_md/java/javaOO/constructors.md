[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects
  
**Section:** Classes

[Classes and Objects](index.html)

[Classes](classes.html)

[Declaring Classes](classdecl.html)

[Declaring Member Variables](variables.html)

[Defining Methods](methods.html)

Providing Constructors for Your Classes

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

[« Previous](methods.html) • [Trail](../TOC.html) • [Next »](arguments.html)

# Providing Constructors for Your Classes

A class contains constructors that are invoked to create objects from the class blueprint.
Constructor declarations look
like method declarations—except that they use the name of the class and have no return type.
For example, `Bicycle` has one constructor:

```

public Bicycle(int startCadence, int startSpeed, int startGear) {
	gear = startGear;
	cadence = startCadence;
	speed = startSpeed;
}

```

To create a new `Bicycle` object called `myBike`, a constructor is called by the `new` operator:

```

Bicycle myBike = new Bicycle(30, 0, 8);

```

`new Bicycle(30, 0, 8)` creates space in memory for the object and initializes
its fields.

Although `Bicycle` only has one constructor, it
could have others, including a no-argument constructor:

```

public Bicycle() {
	gear = 1;
	cadence = 10;
	speed = 0;
}

```

`Bicycle yourBike = new Bicycle();` invokes the no-argument constructor to create a new `Bicycle` object called `yourBike`.

Both constructors could have been declared in `Bicycle`
because they have different argument lists. As with methods, the Java
platform differentiates constructors on the basis of the number
of arguments in the list and their types. You cannot write two
constructors that have the same number and type of arguments for
the same class, because the platform would not be able to tell
them apart. Doing so causes a compile-time error.

You don't have to provide any constructors for your class,
but you must be careful when doing this. The compiler automatically provides a no-argument,
default constructor for any class without constructors.
This default constructor will call the no-argument constructor
of the superclass. In this situation, the compiler will complain if the superclass
doesn't have a no-argument constructor so you must verify that it does. If your class has no explicit
superclass, then it has an implicit superclass of `Object`, which *does* have a
no-argument constructor.

You can use a superclass constructor yourself. The `MountainBike` class at the beginning of this
lesson
did just that. This will be discussed later, in the
lesson
on interfaces and inheritance.

You can use access modifiers in a
constructor's declaration to control which
other classes can call the constructor.

---

**Note
:** If another class cannot call a `MyClass` constructor, it cannot directly create `MyClass` objects.

---

[« Previous](methods.html)
•
[Trail](../TOC.html)
•
[Next »](arguments.html)

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

**Previous page:** Defining Methods
  
**Next page:** Passing Information to a Method or a Constructor




A browser with JavaScript enabled is required for this page to operate properly.