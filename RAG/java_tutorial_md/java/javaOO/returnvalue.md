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

Returning a Value from a Method

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

[« Previous](more.html) • [Trail](../TOC.html) • [Next »](thiskey.html)

# Returning a Value from a Method

A method returns to the code that invoked it when it

* completes all the statements in the method,
* reaches a `return` statement, or
* throws an exception (covered later),

whichever occurs first.

You declare a method's return type in its method declaration.
Within the body of the method, you use the `return`
statement to return the value.

Any method declared `void`
doesn't return a value. It does not need to contain a `return` statement, but it may do so.
In such a case, a `return` statement can be used to branch out of a control flow block and exit the method
and is simply used like this:

```

 return;
 
```

If you try to return a value from a method that is declared `void`, you will get a compiler error.

Any method that is not declared `void` must
contain a `return` statement with a corresponding
return value, like this:

```

 return returnValue;
 
```

The data type of the return value must match the method's declared return type;
you can't return an integer value from a method declared to return a boolean.

The `getArea()` method in the `Rectangle`
[`Rectangle`](examples/Rectangle.java) class that was discussed in the sections on objects returns an integer:

```

    // a method for computing the area of the rectangle
    public int getArea() {
	return width * height;
    }

```

This method returns the integer that the expression `width*height` evaluates to.

The `area` method returns a primitive type. A method
can also return a reference type. For example, in a program to manipulate
`Bicycle` objects, we might have a method like this:

```

public Bicycle seeWhosFastest(Bicycle myBike, Bicycle yourBike, Environment env) {
  Bicycle fastest;
  // code to calculate which bike is faster, given
  // each bike's gear and cadence and given 
  // the environment (terrain and wind)
  return fastest;
}

```

### Returning a Class or Interface

If this section confuses you, skip it
and return to it after you have finished the
lesson
on interfaces and inheritance.

When a method uses a class name as its return type, such as
`whosFastest` does, the class of the type of the returned
object must be either a subclass of, or the exact class of, the
return type. Suppose that you have a class hierarchy in which
`ImaginaryNumber` is a subclass of
`java.lang.Number`, which is in turn a subclass of
`Object`, as illustrated in
the following figure.

![The class hierarchy for ImaginaryNumber](../../figures/java/classes-hierarchy.gif)

The class hierarchy for ImaginaryNumber

Now suppose that you have a method declared to return a
`Number`:

```

public Number returnANumber() {
    ...
}

```

The `returnANumber` method can return an
`ImaginaryNumber` but not an `Object`.
`ImaginaryNumber` is a `Number` because
it's a subclass of `Number`. However, an `Object`
is not necessarily a `Number` — it could be a
`String` or another type.

You can override a method and define it to return
a subclass of the original method, like this:

```

public ImaginaryNumber returnANumber() {
    ...
}

```

This technique, called *covariant return type*, means that the
return type is allowed to vary in the same direction as the subclass.

---

**Note:** You also can use interface names as return types. In this case,
the object returned must implement the specified interface.

---

[« Previous](more.html)
•
[Trail](../TOC.html)
•
[Next »](thiskey.html)

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

**Previous page:** More on Classes
  
**Next page:** Using the this Keyword




A browser with JavaScript enabled is required for this page to operate properly.