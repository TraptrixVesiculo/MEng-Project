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

Using the this Keyword

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

[« Previous](returnvalue.html) • [Trail](../TOC.html) • [Next »](accesscontrol.html)

# Using the this Keyword

Within an instance method or a constructor, `this` is
a reference to the *current object* — the object whose
method or constructor is being called. You can refer to any member
of the current object from within an instance method or a constructor
by using `this`.

### Using `this` with a Field

The most common reason for using the `this` keyword is
because a field is shadowed by a method or
constructor parameter.

For example, the `Point` class was written like this

```

public class Point {
    public int x = 0;
    public int y = 0;
	
    //constructor
    public Point(int a, int b) {
	x = a;
	y = b;
    }
}

```

but it could have been written like this:

```

public class Point {
    public int x = 0;
    public int y = 0;
	
    //constructor
    public Point(int x, int y) {
	this.x = x;
	this.y = y;
    }
}

```

Each argument to the constructor shadows one of the object's fields —
inside the constructor **`x`** is a local copy of the constructor's
first argument. To refer to the
`Point` field **`x`**,
the constructor must use `this.x`.

### Using `this` with a Constructor

From within a constructor, you can also use the `this` keyword
to call another constructor in the same class. Doing so is called an
*explicit constructor invocation*. Here's another `Rectangle`
class, with a different implementation from the one in the
[Objects](../javaOO/objects.html) section.

```

public class Rectangle {
    private int x, y;
    private int width, height;
	
    public Rectangle() {
        this(0, 0, 0, 0);
    }
    public Rectangle(int width, int height) {
        this(0, 0, width, height);
    }
    public Rectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }
    ...
}

```

This class contains a set of constructors. Each constructor initializes
some or all of the rectangle's member variables. The constructors
provide a default value for any member variable whose initial value
is not provided by an argument. For example, the no-argument constructor
calls the four-argument constructor with four 0 values and the two-argument constructor
calls the four-argument constructor with two 0 values.
As before, the compiler determines which constructor to call, based
on the number and the type of arguments.

If present, the invocation of another constructor must be the first
line in the constructor.

[« Previous](returnvalue.html)
•
[Trail](../TOC.html)
•
[Next »](accesscontrol.html)

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

**Previous page:** Returning a Value from a Method
  
**Next page:** Controlling Access to Members of a Class




A browser with JavaScript enabled is required for this page to operate properly.