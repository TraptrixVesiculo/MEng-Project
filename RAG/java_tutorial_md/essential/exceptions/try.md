[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Exceptions
  
**Section:** Catching and Handling Exceptions

[Exceptions](index.html)

[What Is an Exception?](definition.html)

[The Catch or Specify Requirement](catchOrDeclare.html)

[Catching and Handling Exceptions](handling.html)

The try Block

[The catch Blocks](catch.html)

[The finally Block](finally.html)

[The try-with-resources Statement](tryResourceClose.html)

[Putting It All Together](putItTogether.html)

[Specifying the Exceptions Thrown by a Method](declaring.html)

[How to Throw Exceptions](throwing.html)

[Chained Exceptions](chained.html)

[Creating Exception Classes](creating.html)

[Unchecked Exceptions — The Controversy](runtime.html)

[Advantages of Exceptions](advantages.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Exceptions](index.html)

[« Previous](handling.html) • [Trail](../TOC.html) • [Next »](catch.html)

# The try Block

The first step in constructing an exception handler is to enclose the
code that might throw an exception within a `try` block.
In general, a `try` block looks like the following:

```

try {
    code
}
catch and finally blocks . . .

```

The segment in the example labeled `code` contains one
or more legal lines of code that could throw an exception. (The `catch` and `finally` blocks are explained in the next two subsections.)

To construct an exception handler for the `writeList`
method from the `ListOfNumbers` class, enclose the exception-throwing
statements of the `writeList` method within a `try` block.
There is more than one way to do this. You can put each line of code that might
throw an exception within its own `try` block and provide separate
exception handlers for each. Or, you can put all the `writeList` code
within a single `try` block and associate multiple handlers with it.
The following listing uses one `try` block for the entire method
because the code in question is very short.

```

private List<Integer> list;
private static final int SIZE = 10;

PrintWriter out = null;

try {
    System.out.println("Entered try statement");
    out = new PrintWriter(new FileWriter("OutFile.txt"));
    for (int i = 0; i < SIZE; i++) {
        out.println("Value at: " + i + " = " + list.get(i));
    }
}
catch and finally statements . . .

```

If an exception occurs within the `try` block, that
exception is handled by an exception handler associated with it.
To associate an exception handler with a `try` block,
you must put a `catch` block after it; the next section,
[The catch Blocks](catch.html), shows you how.

[« Previous](handling.html)
•
[Trail](../TOC.html)
•
[Next »](catch.html)

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

**Previous page:** Catching and Handling Exceptions
  
**Next page:** The catch Blocks




A browser with JavaScript enabled is required for this page to operate properly.