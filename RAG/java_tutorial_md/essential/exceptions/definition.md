[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Exceptions

[Exceptions](index.html)

What Is an Exception?

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

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Exceptions](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](catchOrDeclare.html)

# What Is an Exception?

The term *exception* is shorthand for the phrase "exceptional event."

---

**Definition:**  An *exception* is an event, which occurs
during the execution of a program, that disrupts
the normal flow of the program's instructions.

---

When an error occurs within a method, the method creates an object
and hands it off to the runtime system. The object, called an
*exception object*, contains information about the error,
including its type and the state of the program when the
error occurred. Creating an exception object and handing it to
the runtime system is called *throwing an exception*.

After a method throws an exception, the runtime system attempts
to find something to handle it. The set of possible "somethings"
to handle the exception is the ordered list of methods that had
been called to get to the method where the error occurred. The
list of methods is known as the *call stack* (see
the next figure).

![The call stack showing three method calls, where the first method called has the exception handler.](../../figures/essential/exceptions-callstack.gif)

The call stack.

The runtime system searches the call stack for a method
that contains a block of code that can handle the
exception. This block of code is called an *exception
handler*. The search begins with the method in which
the error occurred and proceeds through the call stack
in the reverse order in which the methods were called.
When an appropriate handler is found, the runtime
system passes the exception to the handler. An exception
handler is considered appropriate if the type of the
exception object thrown matches the type that
can be handled by the handler.

The exception handler
chosen is said to *catch the exception*. If the
runtime system exhaustively searches all the methods on
the call stack without finding an appropriate exception
handler, as shown in
the next figure, the runtime system (and, consequently, the program) terminates.

![The call stack showing three method calls, where the first method called has the exception handler.](../../figures/essential/exceptions-errorOccurs.gif)

Searching the call stack for the exception handler.

Using exceptions to manage errors has some advantages over
traditional error-management techniques. You can learn more
in the
[Advantages of Exceptions](advantages.html) section.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](catchOrDeclare.html)

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

**Previous page:** Exceptions
  
**Next page:** The Catch or Specify Requirement




A browser with JavaScript enabled is required for this page to operate properly.