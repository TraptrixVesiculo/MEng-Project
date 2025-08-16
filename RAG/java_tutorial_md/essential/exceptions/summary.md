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

[Unchecked Exceptions — The Controversy](runtime.html)

[Advantages of Exceptions](advantages.html)

Summary

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Exceptions](index.html)

[« Previous](advantages.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Summary

A program can use exceptions to indicate that an error occurred.
To throw an exception, use the `throw` statement
and provide it with an exception object — a descendant of
`Throwable` — to provide information about the specific
error that occurred. A method that throws an uncaught, checked
exception must include a `throws` clause in its declaration.

A program can catch exceptions by using a combination of the
`try`, `catch`, and `finally`
blocks.

* The `try` block identifies a block
  of code in which an exception can occur.* The `catch` block identifies a block of code, known
    as an exception handler, that can handle a particular type of
    exception.* The `finally` block identifies a block of code that
      is guaranteed to execute, and is the right place to close files,
      recover resources, and otherwise clean up after the code enclosed
      in the `try` block.

The `try` statement should contain at least one `catch` block or a `finally` block and may have multiple `catch` blocks.

The class of the exception object indicates the type of
exception thrown. The exception object can contain further
information about the error, including an error message.
With exception chaining, an exception
can point to the exception that caused it, which can
in turn point to the exception that caused *it*, and so on.

[« Previous](advantages.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** Advantages of Exceptions
  
**Next page:** Questions and Exercises




A browser with JavaScript enabled is required for this page to operate properly.