[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Object-Oriented Programming Concepts

[Object-Oriented Programming Concepts](index.html)

[What Is an Object?](object.html)

What Is a Class?

[What Is Inheritance?](inheritance.html)

[What Is an Interface?](interface.html)

[What Is a Package?](package.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Object-Oriented Programming Concepts](index.html)

[« Previous](object.html) • [Trail](../TOC.html) • [Next »](inheritance.html)

# What Is a Class?

In the real world, you'll often find many individual objects all of the same kind.
There may be thousands of other bicycles in existence, all of the same make and model. Each bicycle was built from the same set of blueprints and therefore contains the same components.
In object-oriented terms, we say that your bicycle is an
*instance* of the *class of objects* known as bicycles.
A *class* is the blueprint from which individual objects are created.

The following
[`Bicycle`](examples/Bicycle.java)
class is one possible implementation of a bicycle:

```


class Bicycle {

       int cadence = 0;
       int speed = 0;
       int gear = 1;

       void changeCadence(int newValue) {
            cadence = newValue;
       }

       void changeGear(int newValue) {
            gear = newValue;
       }

       void speedUp(int increment) {
            speed = speed + increment;   
       }

       void applyBrakes(int decrement) {
            speed = speed - decrement;
       }

       void printStates() {
            System.out.println("cadence:"+cadence+" speed:"+speed+" gear:"+gear);
       }
}

```

The syntax of the Java programming language will look new to you, but the design of this class is
based on the previous discussion of bicycle objects.
The fields `cadence`, `speed`, and `gear` represent the object's state,
and the methods (`changeCadence`, `changeGear`, `speedUp` etc.) define its interaction with the outside world.

You may have noticed that the `Bicycle` class does not contain a `main` method.
That's because it's not a complete application; it's just the blueprint for bicycles that might be *used* in an application.
The responsibility of creating and using new `Bicycle` objects belongs to some other class in your application.

Here's a
[`BicycleDemo`](examples/BicycleDemo.java)
class that creates two separate `Bicycle` objects and invokes their methods:

```


class BicycleDemo {
     public static void main(String[] args) {

          // Create two different Bicycle objects
          Bicycle bike1 = new Bicycle();
          Bicycle bike2 = new Bicycle();

          // Invoke methods on those objects
          bike1.changeCadence(50);
          bike1.speedUp(10);
          bike1.changeGear(2);
          bike1.printStates();

          bike2.changeCadence(50);
          bike2.speedUp(10);
          bike2.changeGear(2);
          bike2.changeCadence(40);
          bike2.speedUp(10);
          bike2.changeGear(3);
          bike2.printStates();
     }
}


```

The output of this test prints the ending pedal cadence, speed, and gear for the
two bicycles:

```

cadence:50 speed:10 gear:2
cadence:40 speed:20 gear:3

```

[« Previous](object.html)
•
[Trail](../TOC.html)
•
[Next »](inheritance.html)

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

**Previous page:** What Is an Object?
  
**Next page:** What Is Inheritance?




A browser with JavaScript enabled is required for this page to operate properly.