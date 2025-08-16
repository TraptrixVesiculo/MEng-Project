[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](generics.html)

[Generic Types](gentypes.html)

Generic Methods and Constructors

[Type Inference](gentypeinference.html)

[Bounded Type Parameters](bounded.html)

[Subtyping](subtyping.html)

[Wildcards](wildcards.html)

[Type Erasure](erasure.html)

[Using Non-Reifiable Parameters with Varargs Methods](non-reifiable-varargs-type.html)

[Summary of Generics](summarygenerics.html)

[Questions and Exercises](QandE/generics-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Generics](index.html)

[« Previous](gentypes.html) • [Trail](../TOC.html) • [Next »](gentypeinference.html)

# Generic Methods and Constructors

Type parameters can also be declared within method and constructor signatures to create
*generic methods* and *generic constructors*.
This is similar to declaring a generic type, but the type parameter's scope is limited to the method or constructor in which it's declared.

```

/**
 * This version introduces a generic method.
 */
public class Box<T> {

    private T t;          

    public void add(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }

    public <U> void inspect(U u){
        System.out.println("T: " + t.getClass().getName());
        System.out.println("U: " + u.getClass().getName());
    }

    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<Integer>();
        integerBox.add(new Integer(10));
        integerBox.inspect("some text");
    }
}

```

Here we've added one generic method, named `inspect`, that defines one type parameter, named `U`.
This method accepts an object and prints its type to standard output. For comparison,
it also prints out the type of `T`.
For convenience, this class now also has a `main` method so that
it can be run as an application.

The output from this program is:

```

T: java.lang.Integer
U: java.lang.String

```

By passing in different types, the output will change accordingly.

A more realistic use of generic methods might be something like the following, which
defines a static method that stuffs references to a single item
into multiple boxes:

```

public static <U> void fillBoxes(U u, List<Box<U>> boxes) {
    for (Box<U> box : boxes) {
        box.add(u);
    }
}

```

To use this method, your code would look something like the following:

```

Crayon red = ...;
List<Box<Crayon>> crayonBoxes = ...;

```

The complete syntax for invoking this method is:

```

Box.<Crayon>fillBoxes(red, crayonBoxes);

```

Here we've explicitly provided the type to be used as `U`, but more often than not, this can be left out and the compiler will infer the type that's needed:

```

Box.fillBoxes(red, crayonBoxes); // compiler infers that U is Crayon

```

This feature, known as *type inference*,
allows you to invoke a generic method as you would an ordinary method,
without specifying a type between angle brackets.

[« Previous](gentypes.html)
•
[Trail](../TOC.html)
•
[Next »](gentypeinference.html)

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

**Previous page:** Generic Types
  
**Next page:** Type Inference




A browser with JavaScript enabled is required for this page to operate properly.