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

Implementing an Interface

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

[« Previous](interfaceDef.html) • [Trail](../TOC.html) • [Next »](interfaceAsType.html)

# Implementing an Interface

To declare a class that implements an interface, you
include an `implements`
clause in the class declaration. Your class can implement more
than one interface, so the `implements` keyword is followed
by a comma-separated list of the interfaces implemented by the
class.
By convention, the `implements`
clause follows the `extends` clause, if there is one.

### A Sample Interface, Relatable

Consider an interface that defines how to compare the size of objects.

```

public interface Relatable {
	
   // this (object calling isLargerThan) and
   // other must be instances of the same class
   // returns 1, 0, -1 if this is greater
   // than, equal to, or less than other
   public int isLargerThan(Relatable other);
}

```

If you want to be able to compare the size of similar objects, no matter what they are,
the class that instantiates them should implement `Relatable`.

Any class can implement `Relatable` if there is some way to
compare the relative "size" of objects instantiated from the class. For strings, it could be
number of characters; for books, it could be number of pages; for students, it could be weight;
and so forth. For planar geometric objects, area would be a good choice (see the
`RectanglePlus` class that follows), while volume would work for three-dimensional geometric objects.
All such classes can implement the `isLargerThan()` method.

If you know that a class implements `Relatable`, then you
know that you can compare the size of the objects instantiated from that class.

### Implementing the Relatable Interface

Here is the `Rectangle` class that was presented in the
[Creating Objects](../javaOO/objectcreation.html) section, rewritten to implement `Relatable`.

```

public class RectanglePlus implements Relatable {
    public int width = 0;
    public int height = 0;
    public Point origin;

    // four constructors
    public RectanglePlus() {
	origin = new Point(0, 0);
    }
    public RectanglePlus(Point p) {
	origin = p;
    }
    public RectanglePlus(int w, int h) {
	origin = new Point(0, 0);
	width = w;
	height = h;
    }
    public RectanglePlus(Point p, int w, int h) {
	origin = p;
	width = w;
	height = h;
    }

    // a method for moving the rectangle
    public void move(int x, int y) {
	origin.x = x;
	origin.y = y;
    }

    // a method for computing the area of the rectangle
    public int getArea() {
	return width * height;
    }
    
    // a method required to implement the Relatable interface
    public int isLargerThan(Relatable other) {
    	RectanglePlus otherRect = (RectanglePlus)other;
    	if (this.getArea() < otherRect.getArea())
    		return -1;
    	else if (this.getArea() > otherRect.getArea())
    		return 1;
    	else
    		return 0;    		
    }
}

```

Because `RectanglePlus` implements `Relatable`,
the size of any two `RectanglePlus` objects can be compared.

---

**Note:** The `isLargerThan` method, as defined in the
`Relatable` interface, takes an object of
type `Relatable`.
The line of code, shown in bold in the previous example,
casts `other` to a `RectanglePlus` instance.
Type casting tells the compiler what the object really is.
Invoking `getArea` directly on the `other`
instance (`other.getArea()`) would fail to compile
because the compiler does not understand that `other`
is actually an instance of `RectanglePlus`.

---

[« Previous](interfaceDef.html)
•
[Trail](../TOC.html)
•
[Next »](interfaceAsType.html)

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

**Previous page:** Defining an Interface
  
**Next page:** Using an Interface as a Type




A browser with JavaScript enabled is required for this page to operate properly.