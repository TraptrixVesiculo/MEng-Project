[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Object-Oriented Programming Concepts

[Object-Oriented Programming Concepts](index.html)

[What Is an Object?](object.html)

[What Is a Class?](class.html)

[What Is Inheritance?](inheritance.html)

What Is an Interface?

[What Is a Package?](package.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Object-Oriented Programming Concepts](index.html)

[« Previous](inheritance.html) • [Trail](../TOC.html) • [Next »](package.html)

# What Is an Interface?

As you've already learned, objects define their interaction with the outside world through the methods that they expose.
Methods form the object's *interface* with the outside world; the buttons on the front of your television set, for example, are the interface between you and the electrical wiring on the other
side of its plastic casing. You press the "power" button to turn the television on and off.

In its most common form, an interface is a group of related methods with empty bodies. A bicycle's behavior, if specified as an interface, might appear as follows:

```

interface Bicycle {

       void changeCadence(int newValue);   // wheel revolutions per minute

       void changeGear(int newValue);

       void speedUp(int increment);

       void applyBrakes(int decrement);
}

```

To implement this interface, the name of your class would change
(to a particular brand of bicycle, for example, such as `ACMEBicycle`),
and you'd use the `implements` keyword in the class declaration:

```

class ACMEBicycle implements Bicycle {

   // remainder of this class implemented as before

}

```

Implementing an interface allows a class to become more formal about the
behavior it promises to provide. Interfaces form a contract between the class and the outside world, and this contract is enforced at build time by the compiler. If your class claims to implement an interface, all methods defined by that interface must appear in its source code before the class will successfully compile.

---

**Note:** 
To actually compile the `ACMEBicycle` class, you'll need to add the `public` keyword to the beginning of the implemented interface methods. You'll learn the reasons for this later in the lessons on
[Classes and Objects](../javaOO/index.html)
and
[Interfaces and Inheritance](../IandI/index.html).

---

[« Previous](inheritance.html)
•
[Trail](../TOC.html)
•
[Next »](package.html)

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

**Previous page:** What Is Inheritance?
  
**Next page:** What Is a Package?




A browser with JavaScript enabled is required for this page to operate properly.