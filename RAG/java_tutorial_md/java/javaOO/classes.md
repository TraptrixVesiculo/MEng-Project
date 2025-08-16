[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects

[Classes and Objects](index.html)

Classes

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](classdecl.html)

# Classes

The introduction to object-oriented concepts in
the lesson titled
[Object-oriented Programming Concepts](../../java/concepts/index.html) used a bicycle class as an example,
with racing bikes, mountain bikes, and tandem bikes as subclasses.
Here is sample code for a possible implementation of a `Bicycle` class, to give you an overview of a
class declaration. Subsequent sections of this
lesson
will back up and explain class declarations
step by step. For the moment, don't concern yourself with the details.

```

public class Bicycle {
	
    // the Bicycle class has three fields
    public int cadence;
    public int gear;
    public int speed;
	
    // the Bicycle class has one constructor
    public Bicycle(int startCadence, int startSpeed, int startGear) {
        gear = startGear;
        cadence = startCadence;
        speed = startSpeed;
    }
	
    // the Bicycle class has four methods
    public void setCadence(int newValue) {
        cadence = newValue;
    }
	
    public void setGear(int newValue) {
        gear = newValue;
    }
	
    public void applyBrake(int decrement) {
        speed -= decrement;
    }
	
    public void speedUp(int increment) {
        speed += increment;
    }
	
}

```

A class declaration for a `MountainBike` class that is a subclass of `Bicycle` might look like this:

```

public class MountainBike extends Bicycle {
	
    // the MountainBike subclass has one field
    public int seatHeight;

    // the MountainBike subclass has one constructor
    public MountainBike(int startHeight, int startCadence, int startSpeed, int startGear) {
        super(startCadence, startSpeed, startGear);
        seatHeight = startHeight;
    }	
	
    // the MountainBike subclass has one method
    public void setHeight(int newValue) {
        seatHeight = newValue;
    }	

}

```

`MountainBike` inherits all the fields and methods of `Bicycle` and adds the field `seatHeight` and a method to set it (mountain bikes have seats that can be moved up and down
as the terrain demands).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](classdecl.html)

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

**Previous page:** Classes and Objects
  
**Next page:** Declaring Classes




A browser with JavaScript enabled is required for this page to operate properly.