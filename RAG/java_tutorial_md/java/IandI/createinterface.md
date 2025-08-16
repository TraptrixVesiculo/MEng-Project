[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance

[Interfaces and Inheritance](index.html)

Interfaces

[Defining an Interface](interfaceDef.html)

[Implementing an Interface](usinginterface.html)

[Using an Interface as a Type](interfaceAsType.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](interfaceDef.html)

# Interfaces

There are a number of situations in software engineering when it is
important for disparate groups of programmers to agree to a "contract"
that spells out how their software interacts. Each group should be able to write their code
without any knowledge of how the other group's code is written.
Generally speaking, *interfaces* are such contracts.

For example, imagine a futuristic society where
computer-controlled robotic cars transport passengers through city streets
without a human operator. Automobile manufacturers write software (Java, of course)
that operates the automobile—stop, start, accelerate, turn left, and so forth.
Another industrial group, electronic guidance instrument manufacturers,
make computer systems
that receive GPS (Global Positioning System) position data and wireless
transmission of traffic conditions and use that information to drive the car.

The auto manufacturers must publish an industry-standard interface
that spells out in detail what methods can be invoked to make the car move (any car,
from any manufacturer). The guidance manufacturers can then write software that invokes the methods
described in the interface to command
the car. Neither industrial group needs to know *how* the other group's software
is implemented. In fact, each group considers its software highly proprietary and reserves
the right to modify it at any time, as long as it continues to adhere to the published interface.

### Interfaces in Java

In the Java programming language, an *interface* is a reference type, similar to a class, that can contain *only*
constants, method signatures, and nested types. There are no method bodies. Interfaces cannot be instantiated—they
can only be *implemented* by classes or *extended* by other interfaces. Extension is discussed later in
this
lesson.

Defining an interface is similar to creating a new class:

```

public interface OperateCar {

   // constant declarations, if any

   // method signatures
   int turn(Direction direction,   // An enum with values RIGHT, LEFT
              double radius, double startSpeed, double endSpeed);
   int changeLanes(Direction direction, double startSpeed, double endSpeed);
   int signalTurn(Direction direction, boolean signalOn);
   int getRadarFront(double distanceToCar, double speedOfCar);
   int getRadarRear(double distanceToCar, double speedOfCar);
         ......
   // more method signatures
}

```

Note that the method signatures have no braces and are terminated with a semicolon.

To use an interface, you write a class that *implements* the interface.
When an instantiable class implements an interface, it
provides a method body for each of the methods declared in the
interface. For example,

```

public class OperateBMW760i implements OperateCar {

   // the OperateCar method signatures, with implementation --
   // for example:
   int signalTurn(Direction direction, boolean signalOn) {
      //code to turn BMW's LEFT turn indicator lights on
      //code to turn BMW's LEFT turn indicator lights off
      //code to turn BMW's RIGHT turn indicator lights on
      //code to turn BMW's RIGHT turn indicator lights off
   }

   // other members, as needed -- for example, helper classes
   // not visible to clients of the interface

}

```

In the robotic car example above, it is the automobile manufacturers who will implement
the interface. Chevrolet's implementation will be substantially different from that
of Toyota, of course, but both manufacturers will adhere to the same interface. The guidance
manufacturers, who are the clients of the interface,
will build systems that use GPS data on a car's location, digital street maps, and traffic data to
drive the car. In so doing, the guidance systems will invoke the interface methods: turn,
change lanes, brake, accelerate, and so forth.

### Interfaces as APIs

The robotic car example shows an interface being used as an industry standard *Application Programming Interface (API)*. APIs are also common in commercial software products. Typically, a company sells a software
package that contains complex methods that another company wants to use in its own software product.
An example would be a package of digital image processing methods that are sold to companies making end-user
graphics programs. The image processing company writes its classes to implement an interface, which it makes
public to its customers. The graphics company then invokes the image processing methods using the signatures and
return types defined in the interface. While the image processing company's API is made public (to its customers),
its implementation of the API is kept as a closely guarded secret—in fact, it may revise the implementation
at a later date as long as it continues to implement the original interface that its customers have relied on.

### Interfaces and Multiple Inheritance

Interfaces have another very important role in the Java programming language.
Interfaces are not part of the class hierarchy, although they work in combination with classes.
The Java programming language does not permit multiple inheritance (inheritance is discussed later in
this
lesson),
but interfaces provide an alternative.

In Java, a class can inherit
from only one class but it can implement more than one interface. Therefore, objects can have multiple types:
the type of their own class and the types of all the interfaces that they implement. This means that if a variable is
declared to be the type of an interface, its value can reference any object that is instantiated from any class that
implements the interface. This is discussed later in this
lesson,
in the section titled "Using an Interface as a Type."

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](interfaceDef.html)

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

**Previous page:** Interfaces and Inheritance
  
**Next page:** Defining an Interface




A browser with JavaScript enabled is required for this page to operate properly.