[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Exceptions
  
**Section:** How to Throw Exceptions

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

Creating Exception Classes

[Unchecked Exceptions — The Controversy](runtime.html)

[Advantages of Exceptions](advantages.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Exceptions](index.html)

[« Previous](chained.html) • [Trail](../TOC.html) • [Next »](runtime.html)

# Creating Exception Classes

When faced with choosing the type of exception to throw,
you can either use one written by someone else — the Java
platform provides a lot of exception classes you
can use — or you can write one of your own. You should
write your own exception classes if you answer yes to
any of the following questions; otherwise, you can
probably use someone else's.

* Do you need an exception type that isn't represented by those in the Java platform?* Would it help users if they could differentiate your exceptions from those thrown by classes written by other vendors?* Does your code throw more than one related exception?* If you use someone else's exceptions, will users have access to those exceptions? A similar question is, should your package be independent and self-contained?

### An Example

Suppose you are writing a linked list class. The class
supports the following methods, among others:

* **`objectAt(int n)`** — Returns the object in the `n`th position in the list.
  Throws an exception if the argument is less than 0 or more
  than the number of objects currently in the list.
* **`firstObject()`** — Returns the first object in the list. Throws an exception
  if the list contains no objects.
* **`indexOf(Object o)`** — Searches the list for the specified `Object` and returns its
  position in the list. Throws an exception if the object passed into
  the method is not in the list.

The linked list class can throw multiple exceptions, and it would
be convenient to be able to catch all exceptions thrown by the
linked list with one exception handler. Also, if you plan to
distribute your linked list in a package, all related code
should be packaged together. Thus, the linked list should
provide its own set of exception classes.

The next figure illustrates one possible class hierarchy for
the exceptions thrown by the linked list.

![A possible class hierarchy for the exceptions thrown by a linked list.](../../figures/essential/exceptions-hierarchy.gif)

Example exception class hierarchy.

### Choosing a Superclass

> Any `Exception` subclass can be used as the parent
> class of `LinkedListException`. However, a quick
> perusal of those subclasses shows that they are inappropriate
> because they are either too specialized or completely unrelated
> to `LinkedListException`. Therefore, the parent
> class of `LinkedListException` should be `Exception`.
>
> Most applets and applications you write will throw objects
> that are `Exception`s. `Error`s are normally used
> for serious, hard errors in the system, such as those that prevent
> the JVM from running.
>
> ---
>
> **Note:** For readable code, it's good practice to append the string
> `Exception` to the names of all classes that inherit
> (directly or indirectly) from the `Exception` class.
>
> ---

[« Previous](chained.html)
•
[Trail](../TOC.html)
•
[Next »](runtime.html)

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

**Previous page:** Chained Exceptions
  
**Next page:** Unchecked Exceptions — The Controversy




A browser with JavaScript enabled is required for this page to operate properly.