[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Generics](index.html)

Introduction

[Generic Types](gentypes.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](gentypes.html)

# Introduction

In any nontrivial software project, bugs are simply a fact of life. Careful planning, programming, and testing can help reduce their pervasiveness, but
somehow, somewhere, they'll always find a way to creep
into your code. This becomes especially apparent as new features are introduced and your code base grows in size and complexity.

Fortunately, some bugs are easier to detect than others. Compile-time bugs, for example, tell you immediately that something is wrong;
you can use the compiler's error messages
to figure out what the problem is and fix it, right then and there. Runtime bugs, however, can be much more problematic; they don't always surface immediately, and when they do, it may be at a point in time that's far removed from the actual cause of the problem.

Generics add stability to your code by making more of your bugs detectable
at compile time.
Some programmers choose to learn generics by studying
the Java Collections Framework; after all, generics *are* heavily used by those classes.
However, since we haven't yet covered collections, this chapter
will focus primarily on simple "collections-like" examples that we'll design
from scratch.
This hands-on approach will teach you
the necessary syntax and terminology while
demonstrating the various kinds of problems that generics were designed to solve.

### A Simple Box Class

Let's begin by designing a nongeneric `Box` class that
operates on objects of any type.
It need only provide two methods: `add`, which adds an object to
the box, and `get`, which retrieves it:

```

    public class Box {

        private Object object;

        public void add(Object object) {
            this.object = object;
        }

        public Object get() {
            return object;
        }
    }

```

Since its methods accept or return `Object`, you're free to pass in
whatever you want, provided that it's not one of the
primitive types.
However, should you need
to restrict the contained type to something specific (like `Integer`), your only option
would be to specify the requirement in documentation (or in this case, a comment), which of course the compiler
knows nothing about:

```


public class BoxDemo1 {

    public static void main(String[] args) {

        // ONLY place Integer objects into this box!
        Box integerBox = new Box();

        integerBox.add(new Integer(10));
        Integer someInteger = (Integer)integerBox.get();
        System.out.println(someInteger);
    }
}

```

The
[`BoxDemo1`](examples/BoxDemo1.java)
program creates an `Integer` object, passes it to `add`, then assigns that same object to `someInteger`
by the return value of `get`. It then prints the object's value (10) to standard output.
We know that the cast from `Object` to `Integer`
is correct because
we've honored the "contract" specified in the comment.
But remember, the compiler knows nothing about this — it just trusts that our cast is correct. Furthermore, it will do nothing to prevent a careless programmer from passing in an object of the wrong type, such as `String`:

```


public class BoxDemo2 {

    public static void main(String[] args) {

        // ONLY place Integer objects into this box!
        Box integerBox = new Box();

        // Imagine this is one part of a large application
        // modified by one programmer. 
        integerBox.add("10"); // note how the type is now String

        // ... and this is another, perhaps written
        // by a different programmer
        Integer someInteger = (Integer)integerBox.get();
        System.out.println(someInteger);
    }
}

```

In
[`BoxDemo2`](examples/BoxDemo2.java)
we've stored the number 10 as a `String`, which could be the case when, say,
a GUI collects input from the user.
However, the existing cast from `Object` to `Integer` has mistakenly been overlooked. This is clearly a bug, but because
the code still compiles, you wouldn't know anything is wrong until runtime, when
the application crashes with
a `ClassCastException`:

```

    Exception in thread "main"
         java.lang.ClassCastException:  
            java.lang.String cannot be cast to java.lang.Integer
            at BoxDemo2.main(BoxDemo2.java:6)

```

If the `Box` class had been designed with generics in mind, this mistake would have been caught by the compiler, instead of crashing the application at runtime.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](gentypes.html)

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

**Previous page:** Generics
  
**Next page:** Generic Types




A browser with JavaScript enabled is required for this page to operate properly.