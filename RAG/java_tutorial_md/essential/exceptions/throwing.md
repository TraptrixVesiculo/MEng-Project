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

How to Throw Exceptions

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

[« Previous](declaring.html) • [Trail](../TOC.html) • [Next »](chained.html)

# How to Throw Exceptions

Before you can catch an exception, some code somewhere must
throw one. Any code can throw an exception: your code, code
from a package written by someone else such as the packages
that come with the Java platform, or the Java runtime
environment. Regardless of what throws the exception, it's
always thrown with the `throw` statement.

As you have probably noticed, the Java platform provides
numerous exception classes. All the classes are descendants
of the
[`Throwable`](http://download.oracle.com/javase/7/docs/api/java/lang/Throwable.html) class, and all allow programs
to differentiate among the various types of exceptions that
can occur during the execution of a program.

You can also create your own exception classes to represent
problems that can occur within the classes you write.
In fact, if you are a package developer, you might have to
create your own set of exception classes to allow
users to differentiate an error that can occur in your
package from errors that occur in the Java platform or other packages.

You can also create *chained* exceptions. For more information, see the
[Chained Exceptions](../../essential/exceptions/chained.html) section.

### The throw Statement

> All methods use the `throw` statement to throw an exception. The `throw`
> statement requires a single argument: a throwable object. Throwable objects are
> instances of any subclass of the `Throwable` class. Here's an example
> of a `throw` statement.
>
> ```
>
> throw someThrowableObject;
>
> ```
>
> Let's look at the `throw` statement in context. The following
> `pop` method is taken from a class that implements a common stack object. The method removes the top element from the stack and
> returns the object.
>
> ```
>
> public Object pop() {
>     Object obj;
>
>     if (size == 0) {
>         throw new EmptyStackException();
>     }
>
>     obj = objectAt(size - 1);
>     setObjectAt(size - 1, null);
>     size--;
>     return obj;
> }
>
> ```
>
> The `pop` method checks to see whether any elements are on
> the stack. If the stack is empty (its size is equal to `0`),
> `pop` instantiates a new `EmptyStackException`
> object (a member of `java.util`) and throws it. The
> [Creating Exception Classes](../../essential/exceptions/creating.html)
> section in this chapter explains how to create your own
> exception classes. For now, all you need to remember is that you
> can throw only objects that inherit from the `java.lang.Throwable` class.
>
> Note that the declaration of the `pop` method does not
> contain a `throws` clause. `EmptyStackException`
> is not a checked exception, so `pop` is not required to
> state that it might occur.

### Throwable Class and Its Subclasses

> The objects that inherit from the `Throwable` class include direct descendants (objects that inherit
> directly from the `Throwable` class) and indirect
> descendants (objects that inherit from children
> or grandchildren of the `Throwable` class).
> The figure below illustrates the class hierarchy of the `Throwable` class
> and its most significant subclasses. As you can see,
> `Throwable` has two direct descendants:
> [`Error`](http://download.oracle.com/javase/7/docs/api/java/lang/Error.html) and
> [`Exception`](http://download.oracle.com/javase/7/docs/api/java/lang/Exception.html).
>
> ![The Throwable class and its most significant subclasses.](../../figures/essential/exceptions-throwable.gif)
>
> The Throwable class.

### Error Class

> When a dynamic linking failure or other hard failure in
> the Java virtual machine occurs, the virtual machine throws
> an `Error`.
> Simple programs typically do *not*
> catch or throw `Error`s.

### Exception Class

> Most programs throw and catch objects that derive from the `Exception` class. An `Exception`
> indicates that a problem occurred, but it is not a serious
> system problem. Most programs you write will throw and catch
> `Exception`s as opposed to `Error`s.
>
> The Java platform defines the many descendants of the `Exception` class. These descendants indicate various
> types of exceptions that can occur. For example,
> `IllegalAccessException` signals that a particular
> method could not be found, and `NegativeArraySizeException`
> indicates that a program attempted to create an array with a negative size.
>
> One `Exception` subclass,
> `RuntimeException`, is reserved for exceptions
> that indicate incorrect use of an API.
> An example of a runtime exception is
> `NullPointerException`, which occurs when a method tries to
> access a member of an object through a `null` reference.
> The section
> [Unchecked Exceptions — The Controversy](runtime.html) discusses why most applications shouldn't throw runtime exceptions
> or subclass `RuntimeException`.

[« Previous](declaring.html)
•
[Trail](../TOC.html)
•
[Next »](chained.html)

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

**Previous page:** Specifying the Exceptions Thrown by a Method
  
**Next page:** Chained Exceptions




A browser with JavaScript enabled is required for this page to operate properly.