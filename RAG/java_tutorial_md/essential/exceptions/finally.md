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

[The try Block](try.html)

[The catch Blocks](catch.html)

The finally Block

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

[« Previous](catch.html) • [Trail](../TOC.html) • [Next »](tryResourceClose.html)

# The finally Block

The `finally` block *always* executes when the
`try` block exits. This ensures that the
`finally` block is executed even if an unexpected exception
occurs. But `finally` is useful for more than just
exception handling — it allows the programmer to avoid having
cleanup code accidentally bypassed by a `return`,
`continue`, or `break`. Putting cleanup code in
a `finally` block is always a good practice, even when no
exceptions are anticipated.

---

**Note:** If the JVM exits while the `try` or `catch`
code is being executed, then the `finally` block may not
execute. Likewise, if the thread executing the `try` or
`catch` code is interrupted or killed,
the `finally` block may not execute
even though the application as a whole continues.

---

The `try` block of the `writeList` method that
you've been working with here opens a `PrintWriter`. The
program should close that stream before exiting the `writeList`
method. This poses a somewhat complicated problem because
`writeList`'s `try` block can exit in one
of three ways.

1. The `new FileWriter` statement fails and throws an `IOException`.- The `vector.elementAt(i)` statement fails and throws
     an `ArrayIndexOutOfBoundsException`.- Everything succeeds and the `try` block exits normally.

The runtime system always executes the statements within the `finally`
block regardless of what happens within the `try` block.
So it's the perfect place to perform cleanup.

The following `finally` block for the `writeList` method
cleans up and then closes the `PrintWriter`.

```

finally {
    if (out != null) { 
        System.out.println("Closing PrintWriter");
        out.close(); 
    } else { 
        System.out.println("PrintWriter not open");
    } 
} 

```

In the `writeList` example, you could provide for
cleanup without the intervention of a `finally` block. For
example, you could put the code to close the `PrintWriter`
at the end of the `try` block and again within the exception handler
for `ArrayIndexOutOfBoundsException`, as follows.

```

try {
    
    out.close();       //Don't do this; it duplicates code. 
    
} catch (FileNotFoundException e) {
    out.close();       //Don't do this; it duplicates code.
    System.err.println("Caught: FileNotFoundException: " 
                      + e.getMessage());
    throw new RuntimeException(e);
    
} catch (IOException e) {
    System.err.println("Caught IOException: " 
                      + e.getMessage());
}

```

However, this duplicates code, thus making the code difficult to
read and error-prone should you modify it later. For example, if you
add code that can throw a new type
of exception to the `try` block, you have to remember to close the `PrintWriter`
within the new exception handler.

---

**Important:** The `finally` block is a key tool for preventing resource
leaks. When closing a file or otherwise recovering resources, place
the code in a `finally` block to ensure that resource is
*always* recovered.

If you are using Java SE 7 or later,
consider using the `try-`with-resources statement
in these situations, which automatically releases system resources
when no longer needed. The
[next section](tryResourceClose.html) has more information.

---

[« Previous](catch.html)
•
[Trail](../TOC.html)
•
[Next »](tryResourceClose.html)

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

**Previous page:** The catch Blocks
  
**Next page:** The try-with-resources Statement




A browser with JavaScript enabled is required for this page to operate properly.