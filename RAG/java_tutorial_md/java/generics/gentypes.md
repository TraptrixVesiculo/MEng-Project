[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](generics.html)

Generic Types

[Generic Methods and Constructors](genmethods.html)

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

[« Previous](generics.html) • [Trail](../TOC.html) • [Next »](genmethods.html)

# Generic Types

Let's update our `Box` class to use generics. We'll first create a *generic type declaration* by
changing the code "`public class Box`" to "`public class Box<T>`"; this introduces one *type variable*, named `T`,
that can be used anywhere inside the class. This same technique can be applied to interfaces as well. There's nothing particularly complex about this concept. In fact, it's quite similar to what you already know about variables in general. Just think of `T` as a special kind of variable, whose "value" will be whatever type you pass in; this can be any class type, any interface type, or even another type variable. It just can't be any of the primitive data types.
In this context, we also say that
`T` is a *formal type parameter* of the `Box` class.

```

/**
 * Generic version of the Box class.
 */
public class Box<T> {

    private T t; // T stands for "Type"

    public void add(T t) {
        this.t = t;
    }

    public T get() {
        return t;
    }
}

```

As you can see, we've replaced all occurrences of `Object` with `T`.

Also note that a generic type may have multiple type parameters, but each parameter must be unique within its declaring class or interface. A declaration of `Box<T,T>`, for example, would generate an error on the second occurrence of `T`, but `Box<T,U>`, however, would be allowed.

To reference this generic class from within your own code,
you must perform a *generic type invocation*, which replaces `T` with some concrete value, such as `Integer`:

```

Box<Integer> integerBox;

```

You can think of a generic type invocation as being similar to an
ordinary method invocation, but instead of passing an argument to a method,
you're passing a *type argument* — `Integer`
in this case — to the `Box` class itself.

Like any other variable declaration, this code does not actually create a new `Box`
object. It simply declares that `integerBox` will hold a reference to a "`Box` of `Integer`", which is how
`Box<Integer>` is read.

An invocation of a generic type is generally known as a *parameterized type*.

To instantiate this class, use the `new` keyword, as usual, but
place `<Integer>` between the class name and the parenthesis:

```

integerBox = new Box<Integer>();

```

Or, you can put the entire statement on one line, such as:

```

Box<Integer> integerBox = new Box<Integer>();

```

Once `integerBox` is initialized, you're free to invoke its `get` method without providing a cast, as in
[`BoxDemo3`](examples/BoxDemo3.java):

```


public class BoxDemo3 {

    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<Integer>();
        integerBox.add(new Integer(10));
        Integer someInteger = integerBox.get(); // no cast!
        System.out.println(someInteger);
    }
}

```

Furthermore, if you try adding an incompatible type to the box,
such as `String`, compilation will fail, alerting you to
what previously would have been a runtime bug:

```

    BoxDemo3.java:5: add(java.lang.Integer) in Box<java.lang.Integer>
    cannot be applied to (java.lang.String)
        integerBox.add("10");
                  ^
    1 error

```

It's important to understand that type variables are
not actually types themselves.
In the above examples, you won't find `T.java`
or `T.class`
anywhere on the file system.
Furthermore, `T` is not a part of the `Box` class name.
In fact during compilation,
all generic information will be removed entirely, leaving only
`Box.class` on the file system. We'll discuss this later in the
section on
[Type Erasure](erasure.html)

## The Diamond Operator

Starting in Java SE 7, you can replace the type arguments required to invoke the constructor of a generic class with an empty set of type parameters (`<>`) as long as the compiler can determine, or infer, the type arguments from the context. This pair of angle brackets, `<>`, is informally called the *diamond operator*. For example, you can create an instance of `Box<Integer>` with the following statement:

```
Box<Integer> integerBox = new Box<>();
```

For more information about the diamond operator, see [Type Inference and Instantiation of Generic Classes](gentypeinference.html#type-inference-instantiation).

Note that using the diamond operator to infer the actual type parameters of the generic class being instantiated is different than inferring the actual type parameters of generic constructors (which is similar to generic methods and does not require the diamond operator). See [Type Inference and Generic Constructors of Generic and Non-Generic Classes](gentypeinference.html#type-inference-constructors) for more information.

## Type Parameter Naming Conventions

By convention, type parameter names are single, uppercase letters.
This stands in sharp contrast to the variable
[naming](../nutsandbolts/variables.html#naming) conventions that you already know about, and with good reason:
Without this
convention, it would be difficult to tell the difference between a type
variable and an ordinary class or interface name.

The most commonly used type parameter names are:

* E - Element (used extensively by the Java Collections Framework)* K - Key* N - Number* T - Type* V - Value* S,U,V etc. - 2nd, 3rd, 4th types

You'll see these names used throughout the Java SE API and the rest of this tutorial.

[« Previous](generics.html)
•
[Trail](../TOC.html)
•
[Next »](genmethods.html)

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

**Previous page:** Introduction
  
**Next page:** Generic Methods and Constructors




A browser with JavaScript enabled is required for this page to operate properly.