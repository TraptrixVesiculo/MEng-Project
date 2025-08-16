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

Chained Exceptions

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

[« Previous](throwing.html) • [Trail](../TOC.html) • [Next »](creating.html)

# Chained Exceptions

An application often responds to an exception by throwing another
exception. In effect, the first exception *causes* the
second exception. It can be very helpful to know when one exception
causes another. *Chained Exceptions* help the programmer do this.

The following are the methods and constructors in `Throwable` that support
chained exceptions.

```

Throwable getCause()
Throwable initCause(Throwable)
Throwable(String, Throwable)
Throwable(Throwable)

```

The `Throwable` argument to `initCause`
and the `Throwable` constructors is the exception
that caused the current exception. `getCause`
returns the exception that caused the current exception,
and `initCause` sets the current exception's cause.

The following example shows how to use a chained exception.

```

try {

} catch (IOException e) {
    throw new SampleException("Other IOException", e);
}

```

In this example, when an `IOException` is caught, a new
`SampleException` exception is created with the original
cause attached and the chain of exceptions is thrown up to the next
higher level exception handler.

### Accessing Stack Trace Information

Now let's suppose that the higher-level exception handler wants
to dump the stack trace in its own format.

---

**Definition:**  A *stack trace* provides information on the execution
history of the current thread and lists the names of the classes
and methods that were called at the point when the exception occurred. A stack trace is a useful debugging tool that you'll
normally take advantage of when an exception has been thrown.

---

The following code shows how to call the `getStackTrace` method on
the exception object.

```

catch (Exception cause) {
    StackTraceElement elements[] = cause.getStackTrace();
    for (int i = 0, n = elements.length; i < n; i++) {       
        System.err.println(elements[i].getFileName() + ":" 
                      + elements[i].getLineNumber() 
                      + ">> " 
                      + elements[i].getMethodName() + "()");
    }
}

```

### Logging API

The next code snippet logs where an exception occurred from within the `catch` block. However, rather than manually parsing the stack trace
and sending the output to `System.err()`, it sends the output
to a file using the logging facility in the
[`java.util.logging`](http://download.oracle.com/javase/7/docs/api/java/util/logging/package-summary.html) package.

```

try {
    Handler handler = new FileHandler("OutFile.log");
    Logger.getLogger("").addHandler(handler);
    
} catch (IOException e) {
    Logger logger = Logger.getLogger("package.name"); 
    StackTraceElement elements[] = e.getStackTrace();
    for (int i = 0, n = elements.length; i < n; i++) {
        logger.log(Level.WARNING, 
                   elements[i].getMethodName());
    }
}

```

[« Previous](throwing.html)
•
[Trail](../TOC.html)
•
[Next »](creating.html)

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

**Previous page:** How to Throw Exceptions
  
**Next page:** Creating Exception Classes




A browser with JavaScript enabled is required for this page to operate properly.