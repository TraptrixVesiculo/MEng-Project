[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance
  
**Section:** Inheritance

[Interfaces and Inheritance](index.html)

[Interfaces](createinterface.html)

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

Using the Keyword super

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

[« Previous](hidevariables.html) • [Trail](../TOC.html) • [Next »](objectclass.html)

# Using the Keyword super

### Accessing Superclass Members

If your method overrides one of its superclass's methods,
you can invoke the overridden method through the use of the keyword
`super`. You can also use `super`
to refer to a hidden field (although hiding fields is discouraged). Consider this class,
`Superclass`:

```

public class Superclass {

    public void printMethod() {
        System.out.println("Printed in Superclass.");
    }
}

```

Here is a subclass, called `Subclass`, that
overrides `printMethod()`:

```

public class Subclass extends Superclass {

    public void printMethod() { //overrides printMethod in Superclass
        super.printMethod();
        System.out.println("Printed in Subclass");
    }
    public static void main(String[] args) {
    	
    Subclass s = new Subclass();
    s.printMethod();	
    }

}

```

Within `Subclass`, the simple name
`printMethod()` refers to the one declared in
`Subclass`, which overrides the one in
`Superclass`. So, to refer to `printMethod()` inherited
from `Superclass`,
`Subclass` must use a qualified name, using
`super` as shown. Compiling and executing `Subclass` prints
the following:

```

Printed in Superclass.
Printed in Subclass

```

### Subclass Constructors

The following example illustrates how to use the `super` keyword
to invoke a superclass's constructor. Recall from the
[`Bicycle`](subclasses.html) 
example that
`MountainBike` is a subclass of
`Bicycle`. Here is the `MountainBike` (subclass) constructor that
calls the superclass constructor and then adds initialization code of its own:

```

    public MountainBike(int startHeight, int startCadence, int startSpeed, int startGear) {
        super(startCadence, startSpeed, startGear);
        seatHeight = startHeight;
    }	

```

Invocation of a superclass constructor must be the first line in the subclass constructor.

The syntax for calling a superclass constructor is

```

super();  
--or--
super(parameter list);

```

With `super()`, the superclass no-argument constructor is called. With `super(parameter list)`,
the superclass constructor with a matching parameter list is called.

---

**Note:** If a constructor does not
explicitly invoke a superclass constructor, the Java compiler
automatically inserts a call to the no-argument constructor of the
superclass. If the super class does not have a no-argument constructor, you will get a
compile-time error. `Object` *does* have such a constructor, so if
`Object` is the only superclass, there is no problem.

---

If a subclass constructor invokes a constructor of its superclass, either explicitly or implicitly,
you might think that there will be a whole chain of constructors called, all the way
back to the constructor of `Object`. In fact, this is the case. It is called
*constructor chaining*, and you need to be aware of it when there is a long line of class descent.

[« Previous](hidevariables.html)
•
[Trail](../TOC.html)
•
[Next »](objectclass.html)

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

**Previous page:** Hiding Fields
  
**Next page:** Object as a Superclass




A browser with JavaScript enabled is required for this page to operate properly.