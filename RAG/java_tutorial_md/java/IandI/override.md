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

Overriding and Hiding Methods

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

[« Previous](subclasses.html) • [Trail](../TOC.html) • [Next »](polymorphism.html)

# Overriding and Hiding Methods

### Instance Methods

An instance method in a subclass with the same signature (name, plus the number
and the type of its parameters) and return type as an instance method in
the superclass *overrides* the superclass's method.

The ability of a subclass to override a
method allows a class to inherit from a superclass whose
behavior is "close enough" and then to modify behavior as
needed.
The overriding method has the same name, number and type
of parameters, and return type as the method it overrides. An overriding
method can also return a subtype of the type returned by the overridden
method. This is called a *covariant return type*.

When overriding a method, you might want to use
the `@Override` annotation that instructs the
compiler that you intend to override a method in the superclass.
If, for some reason, the compiler detects that the method does
not exist in one of the superclasses, it will generate an
error. For more information on `@Override`, see
[`Annotations`](../javaOO/annotations.html).

### Class Methods

If a subclass defines a class method with the same signature
as a class method in the superclass, the method in the
subclass *hides* the one in the superclass.

The distinction between hiding and overriding has important
implications. The version of the overridden
method that gets invoked is the one in the subclass. The version of the
hidden method that gets invoked depends on whether it is invoked from the superclass
or the subclass.
Let's look at an example that contains two classes. The first is `Animal`,
which contains one instance method and one class method:

```

public class Animal {
    public static void testClassMethod() {
        System.out.println("The class method in Animal.");
    }
    public void testInstanceMethod() {
        System.out.println("The instance method in Animal.");
    }
}

```

The second class, a subclass of `Animal`,
is called `Cat`:

```

public class Cat extends Animal {
    public static void testClassMethod() {
        System.out.println("The class method in Cat.");
    }
    public void testInstanceMethod() {
        System.out.println("The instance method in Cat.");
    }

    public static void main(String[] args) {
        Cat myCat = new Cat();
        Animal myAnimal = myCat;
        Animal.testClassMethod();
        myAnimal.testInstanceMethod();
    }
}

```

The `Cat` class overrides the instance method
in `Animal` and
hides the class method in `Animal`.
The `main` method in this
class creates an instance of `Cat` and calls
`testClassMethod()` on the class and `testInstanceMethod()`
on the instance.

The output from this program is as follows:

```

The class method in Animal.
The instance method in Cat.

```

As promised, the version of the hidden method that gets invoked is the
one in the superclass, and the version of the overridden
method that gets invoked is the one in the subclass.

### Modifiers

The access specifier for an
overriding method can allow more, but not less, access than
the overridden method. For example, a protected instance method in
the superclass can be made public, but not private, in the subclass.

You will get a compile-time error if you attempt to change an instance method in the superclass
to a class method in the subclass, and vice versa.

### Summary

The following table summarizes what happens when you define a method with the same
signature as a method in a superclass.

**Defining a Method with the Same Signature as a Superclass's Method**

|  | Superclass Instance Method | Superclass Static Method |
| Subclass Instance Method | Overrides | Generates a compile-time error |
| Subclass Static Method | Generates a compile-time error | Hides |

---

**Note:** In a subclass, you can overload the methods inherited from the superclass. Such overloaded
methods neither hide nor override the superclass methods—they are new methods, unique to the
subclass.

---

[« Previous](subclasses.html)
•
[Trail](../TOC.html)
•
[Next »](polymorphism.html)

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

**Previous page:** Inheritance
  
**Next page:** Polymorphism




A browser with JavaScript enabled is required for this page to operate properly.