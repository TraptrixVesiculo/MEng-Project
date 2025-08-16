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

[Generic Methods and Constructors](genmethods.html)

[Type Inference](gentypeinference.html)

[Bounded Type Parameters](bounded.html)

[Subtyping](subtyping.html)

[Wildcards](wildcards.html)

Type Erasure

[Using Non-Reifiable Parameters with Varargs Methods](non-reifiable-varargs-type.html)

[Summary of Generics](summarygenerics.html)

[Questions and Exercises](QandE/generics-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Generics](index.html)

[« Previous](wildcards.html) • [Trail](../TOC.html) • [Next »](non-reifiable-varargs-type.html)

# Type Erasure

When a generic type is instantiated, the compiler translates
those types by a technique called *type erasure* —
a process where the compiler removes all information related to
type parameters and type arguments within a class or method.
Type erasure enables Java applications that use generics to
maintain binary compatibility with Java libraries and applications
that were created before generics.

For instance, `Box<String>`
is translated to type `Box`, which is called the
*raw type* — a raw type is a generic class or interface name without any type arguments.
This means that you can't find out what type
of `Object` a generic class is using at runtime.
The following operations are not possible:
> ```
>
> public class MyClass<E> {
>     public static void myMethod(Object item) {
>         if (item instanceof E) {  //Compiler error
>             ...
>         }
>         E item2 = new E();   //Compiler error
>         E[] iArray = new E[10]; //Compiler error
>         E obj = (E)new Object(); //Unchecked cast warning
>     }
> }
>
> ```

The operations shown in bold are meaningless at runtime because the
compiler removes all information about the actual type argument
(represented by the type parameter `E`) at compile time.

Type erasure exists so that new code may continue to interface with
legacy code. Using a raw type for any other reason is considered bad
programming practice and should be avoided whenever possible.

When mixing legacy code with generic code, you may encounter warning messages similar to the following:

```

Note: WarningDemo.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.

```

This can happen when using an older API that operates on raw types, as shown in the following
[`WarningDemo`](examples/WarningDemo.java)
program:

```


public class WarningDemo {
    public static void main(String[] args){
        Box<Integer> bi;
        bi = createBox();
    }

    static Box createBox(){
        return new Box();
    }
}

```

Recompiling with `-Xlint:unchecked` reveals
the following additional information:

```

WarningDemo.java:4: warning: [unchecked] unchecked conversion
found   : Box
required: Box<java.lang.Integer>
        bi = createBox();
                      ^
1 warning

```

[« Previous](wildcards.html)
•
[Trail](../TOC.html)
•
[Next »](non-reifiable-varargs-type.html)

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

**Previous page:** Wildcards
  
**Next page:** Using Non-Reifiable Parameters with Varargs Methods




A browser with JavaScript enabled is required for this page to operate properly.