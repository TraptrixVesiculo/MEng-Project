[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance
  
**Section:** Interfaces

[Interfaces and Inheritance](index.html)

[Interfaces](createinterface.html)

[Defining an Interface](interfaceDef.html)

[Implementing an Interface](usinginterface.html)

Using an Interface as a Type

[Rewriting Interfaces](nogrow.html)

[Summary of Interfaces](summary-interface.html)

[Questions and Exercises](QandE/interfaces-questions.html)

[Inheritance](subclasses.html)

[Overriding and Hiding Methods](override.html)

[Polymorphism](polymorphism.html)

[Hiding Fields](hidevariables.html)

[Using the Keyword super](super.html)

[Object as a Superclass](objectclass.html)

[Writing Final Classes and Methods](final.html)

[Abstract Methods and Classes](abstract.html)

[Summary of Inheritance](summaryinherit.html)

[Questions and Exercises](QandE/inherit-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Interfaces and Inheritance](index.html)

[« Previous](usinginterface.html) • [Trail](../TOC.html) • [Next »](nogrow.html)

# Using an Interface as a Type

When you define a new interface, you are defining a new reference
data type. You can use interface names anywhere you can use any
other data type name. If you define a reference variable whose type
is an interface, any object you assign to it *must* be
an instance of a class that implements the interface.

As an example, here is a method for finding the largest object in a pair of
objects, for *any* objects that are instantiated from a class that
implements `Relatable`:

```

public Object findLargest(Object object1, Object object2) {
   Relatable obj1 = (Relatable)object1;
   Relatable obj2 = (Relatable)object2;
   if ( (obj1).isLargerThan(obj2) > 0)
      return object1;
   else 
      return object2;
}

```

By casting `object1` to a `Relatable` type, it can
invoke the `isLargerThan` method.

If you make a point of implementing `Relatable` in a wide variety
of classes, the objects instantiated from *any* of those classes can be compared with the
`findLargest()` method—provided that both objects are of the same class.
Similarly, they can all be compared with the following methods:

```

public Object findSmallest(Object object1, Object object2) {
   Relatable obj1 = (Relatable)object1;
   Relatable obj2 = (Relatable)object2;
   if ( (obj1).isLargerThan(obj2) < 0)
      return object1;
   else 
      return object2;
}

public boolean isEqual(Object object1, Object object2) {
   Relatable obj1 = (Relatable)object1;
   Relatable obj2 = (Relatable)object2;
   if ( (obj1).isLargerThan(obj2) == 0)
      return true;
   else 
      return false;
}

```

These methods work for any "relatable" objects, no matter what their class inheritance is.
When they implement `Relatable`,
they can be of both their own class (or superclass) type and a `Relatable` type. This gives them some of the advantages
of multiple inheritance, where they can have behavior from both a superclass and an interface.

[« Previous](usinginterface.html)
•
[Trail](../TOC.html)
•
[Next »](nogrow.html)

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

**Previous page:** Implementing an Interface
  
**Next page:** Rewriting Interfaces




A browser with JavaScript enabled is required for this page to operate properly.