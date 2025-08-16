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

[Controlling Access to Members of a Class](accesscontrol.html)

[Understanding Instance and Class Members](classvars.html)

Initializing Fields

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

[« Previous](classvars.html) • [Trail](../TOC.html) • [Next »](summaryclasses.html)

# Initializing Fields

As you have seen, you can often provide an initial value for a field in its declaration:

```

public class BedAndBreakfast {

    public static int capacity = 10;  //initialize to 10

    private boolean full = false;  //initialize to false
}

```

This works well when the initialization value is available and the initialization can be put on one line.
However, this form of initialization has limitations because of its simplicity.
If initialization requires some logic
(for example, error handling or a `for` loop to fill a complex array), simple assignment is inadequate.
Instance variables can be initialized in constructors, where error handling or other logic
can be used. To provide the same capability for class variables, the Java programming language includes
*static initialization blocks*.

---

**Note:** It is not necessary to declare fields at the beginning of the class definition, although this is the
most common practice. It is only necessary that they be declared and initialized before they are used.

---

### Static Initialization Blocks

A *static initialization block* is a normal block of code enclosed in braces,
`{ }`, and preceded by the `static` keyword. Here is an example:

```

static {

    // whatever code is needed for initialization goes here
}

```

A class can have any number of static initialization blocks, and they can
appear anywhere in the class body. The runtime system guarantees
that static initialization blocks are called in the order that they
appear in the source code.

There is an alternative to static blocks —you can write a private
static method:

```

class Whatever {
    public static varType myVar = initializeClassVariable();
	
    private static varType initializeClassVariable() {

        //initialization code goes here
    }
}

```

The advantage of private static methods is that they can be reused later
if you need to reinitialize the class variable.

### Initializing Instance Members

Normally, you would put code to initialize an instance variable in a constructor.
There are two alternatives to using a constructor to initialize instance variables: initializer blocks and final
methods.

Initializer blocks for instance variables look just like static initializer blocks, but without
the `static` keyword:

```

{

    // whatever code is needed for initialization goes here
}

```

The Java compiler copies initializer blocks into every constructor.
Therefore, this approach can be used to share a block of code between multiple constructors.

A *final method* cannot be overridden in a subclass. This is discussed in
the lesson on
interfaces and inheritance.
Here is an example of using a final
method for initializing an instance variable:

```

class Whatever {
    private varType myVar = initializeInstanceVariable();
	
    protected final varType initializeInstanceVariable() {

        //initialization code goes here
    }
}


```

This is especially useful if subclasses might want to reuse the
initialization method. The method is final because calling non-final
methods during instance initialization can cause problems.
Joshua Bloch describes this in more detail in
[Effective Java](http://java.sun.com/docs/books/effective).

[« Previous](classvars.html)
•
[Trail](../TOC.html)
•
[Next »](summaryclasses.html)

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

**Previous page:** Understanding Instance and Class Members
  
**Next page:** Summary of Creating and Using Classes and Objects




A browser with JavaScript enabled is required for this page to operate properly.