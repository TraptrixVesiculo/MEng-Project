[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects

[Classes and Objects](index.html)

[Classes](classes.html)

[Declaring Classes](classdecl.html)

[Declaring Member Variables](variables.html)

[Defining Methods](methods.html)

[Providing Constructors for Your Classes](constructors.html)

[Passing Information to a Method or a Constructor](arguments.html)

Objects

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

[« Previous](arguments.html) • [Trail](../TOC.html) • [Next »](objectcreation.html)

# Objects

A typical Java program creates many objects, which as you know,
interact by invoking methods.
Through these object interactions, a program can carry out
various tasks, such as implementing a GUI,
running an animation, or sending and receiving information over a network. Once an
object has completed the work for which it was created, its resources are
recycled for use by other objects.

Here's a small program, called
[`CreateObjectDemo`](examples/CreateObjectDemo.java), that creates three objects:
one
[`Point`](examples/Point.java) object and two
[`Rectangle`](examples/Rectangle.java) objects. You will need all three source files to compile this program.

```


public class CreateObjectDemo {

    public static void main(String[] args) {
		
        //Declare and create a point object
        //and two rectangle objects.
        Point originOne = new Point(23, 94);
        Rectangle rectOne = new Rectangle(originOne, 100, 200);
        Rectangle rectTwo = new Rectangle(50, 100);
		
        //display rectOne's width, height, and area
        System.out.println("Width of rectOne: " +
                rectOne.width);
        System.out.println("Height of rectOne: " +
                rectOne.height);
        System.out.println("Area of rectOne: " + rectOne.getArea());
		
        //set rectTwo's position
        rectTwo.origin = originOne;
		
        //display rectTwo's position
        System.out.println("X Position of rectTwo: "
                + rectTwo.origin.x);
        System.out.println("Y Position of rectTwo: "
                + rectTwo.origin.y);
		
        //move rectTwo and display its new position
        rectTwo.move(40, 72);
        System.out.println("X Position of rectTwo: "
                + rectTwo.origin.x);
        System.out.println("Y Position of rectTwo: "
                + rectTwo.origin.y);
    }
}

```

This program creates, manipulates, and
displays information about various objects. Here's the output:

```

Width of rectOne: 100
Height of rectOne: 200
Area of rectOne: 20000
X Position of rectTwo: 23
Y Position of rectTwo: 94
X Position of rectTwo: 40
Y Position of rectTwo: 72

```

The following three sections use the above example to describe the life cycle
of an object within a program. From them, you will learn
how to write code that creates and uses objects in your own programs.
You will also learn
how the system cleans up after an object when its life has ended.

[« Previous](arguments.html)
•
[Trail](../TOC.html)
•
[Next »](objectcreation.html)

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

**Previous page:** Passing Information to a Method or a Constructor
  
**Next page:** Creating Objects




A browser with JavaScript enabled is required for this page to operate properly.