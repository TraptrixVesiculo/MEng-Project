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

[Initializing Fields](initial.html)

Summary of Creating and Using Classes and Objects

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

[« Previous](initial.html) • [Trail](../TOC.html) • [Next »](QandE/creating-questions.html)

# Summary of Creating and Using Classes and Objects

A class declaration names the class and encloses the class body between braces.
The class name can be preceded by modifiers. The class body contains fields, methods, and
constructors for the class. A class uses fields
to contain state information and uses methods to implement behavior.
Constructors that
initialize a new instance of a class use the name of the class and look like methods
without a return type.

You control access to classes and members in the same way:
by using an access modifier such as
`public` in their declaration.

You specify a class variable or a class method by using
the `static` keyword in the member's declaration. A
member that is not declared as `static` is implicitly
an instance member. Class variables are shared by all instances of
a class and can be accessed through the class name as well as an instance reference. Instances of
a class get their own copy of each instance variable, which must be
accessed through an instance reference.

You create an object from a class by using the `new` operator and a constructor.
The new operator returns a reference to the object that was created. You can assign the reference
to a variable or use it directly.

Instance variables and methods that are
accessible to code outside of the class that they are declared in can be
referred to by using a qualified name. The qualified name of an instance
variable looks like this:

```

objectReference.variableName

```

The qualified name of a method looks like this:

```

objectReference.methodName(argumentList)

  or

objectReference.methodName()

```

The garbage collector automatically cleans up unused objects. An object is
unused if the program holds no more references to it. You can explicitly drop
a reference by setting the variable holding the reference to `null`.

[« Previous](initial.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/creating-questions.html)

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

**Previous page:** Initializing Fields
  
**Next page:** Questions and Exercises: Classes




A browser with JavaScript enabled is required for this page to operate properly.