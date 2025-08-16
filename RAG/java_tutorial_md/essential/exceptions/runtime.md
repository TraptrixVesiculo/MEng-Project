[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Exceptions

[Exceptions](index.html)

[What Is an Exception?](definition.html)

[The Catch or Specify Requirement](catchOrDeclare.html)

[Catching and Handling Exceptions](handling.html)

[The try Block](try.html)

[The catch Blocks](catch.html)

[The finally Block](finally.html)

[The try-with-resources Statement](tryResourceClose.html)

[Putting It All Together](putItTogether.html)

[Specifying the Exceptions Thrown by a Method](declaring.html)

[How to Throw Exceptions](throwing.html)

[Chained Exceptions](chained.html)

[Creating Exception Classes](creating.html)

Unchecked Exceptions — The Controversy

[Advantages of Exceptions](advantages.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Exceptions](index.html)

[« Previous](creating.html) • [Trail](../TOC.html) • [Next »](advantages.html)

# Unchecked Exceptions — The Controversy

Because the Java programming language does not require methods
to catch or to specify unchecked exceptions
(`RuntimeException`, `Error`, and their
subclasses), programmers
may be tempted to write code that throws only unchecked exceptions
or to make all their exception subclasses inherit from
`RuntimeException`. Both of these shortcuts allow
programmers to write code without bothering with compiler errors
and without bothering to specify or to catch any exceptions.
Although this may seem convenient to the programmer, it sidesteps
the intent of the `catch` or `specify` requirement and can cause
problems for others using your classes.

Why did the designers decide to force a method to specify all
uncaught checked exceptions that can be thrown within its scope?
Any `Exception` that can be thrown by a method is part of the method's
public programming interface. Those who call a method must know about
the exceptions that a method can throw so that they can decide what to
do about them. These exceptions are as much a part of that
method's programming interface as its parameters and `return` value.

The next question might be: "If it's so good to document a
method's API, including the exceptions it can throw, why not
specify runtime exceptions too?" Runtime exceptions represent
problems that are the result of a programming problem, and as
such, the API client code cannot reasonably be expected to
recover from them or to handle them in any way. Such problems
include arithmetic exceptions, such as dividing by zero;
pointer exceptions, such as trying to access an object
through a null reference; and indexing exceptions, such as
attempting to access an array element through
an index that is too large or too small.

Runtime exceptions
can occur anywhere in a program, and in a typical one they can
be very numerous. Having to add runtime exceptions in every method declaration would reduce a program's clarity. Thus,
the compiler does not require that you catch or specify runtime exceptions (although you can).

One case where it is common practice to throw a `RuntimeException` is when the user calls a method incorrectly. For example, a method can check if one of its arguments is incorrectly `null`. If an argument is `null`, the method might throw a `NullPointerException`, which is an *unchecked* exception.

Generally speaking, do not throw a `RuntimeException` or create a subclass of `RuntimeException` simply because
you don't want to be bothered with specifying the exceptions
your methods can throw.

Here's the bottom line guideline: If a client can reasonably be expected
to recover from an exception, make it a checked exception. If a
client cannot do anything to recover from the exception, make
it an unchecked exception.

[« Previous](creating.html)
•
[Trail](../TOC.html)
•
[Next »](advantages.html)

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

**Previous page:** Creating Exception Classes
  
**Next page:** Advantages of Exceptions




A browser with JavaScript enabled is required for this page to operate properly.