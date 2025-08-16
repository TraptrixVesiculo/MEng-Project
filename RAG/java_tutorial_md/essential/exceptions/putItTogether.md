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

[The finally Block](finally.html)

[The try-with-resources Statement](tryResourceClose.html)

Putting It All Together

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

[« Previous](tryResourceClose.html) • [Trail](../TOC.html) • [Next »](declaring.html)

# Putting It All Together

The previous sections described how to construct the `try`,
`catch`, and `finally` code blocks for
the `writeList` method in the `ListOfNumbers` class.
Now, let's walk through the code and investigate what can happen.

When all the components are put together, the `writeList`
method looks like the following.

```

public void writeList() {
    PrintWriter out = null;

    try {
        System.out.println("Entering try statement");
        out = new PrintWriter(
	                  new FileWriter("OutFile.txt"));
            for (int i = 0; i < SIZE; i++)
                out.println("Value at: " + i + " = " 
                             + vector.elementAt(i));
		  
    } catch (ArrayIndexOutOfBoundsException e) {
         System.err.println("Caught " 
                     + "ArrayIndexOutOfBoundsException: " 
                     +   e.getMessage());
				 
    } catch (IOException e) {
         System.err.println("Caught IOException: " 
                             +  e.getMessage());
				 
    } finally {
         if (out != null) {
             System.out.println("Closing PrintWriter");
             out.close();
		
         } 
         else {
             System.out.println("PrintWriter not open");
         }
     }
}

```

As mentioned previously, this method's `try` block
has three different exit possibilities; here are two of them.

1. Code in the `try` statement fails and throws an exception.
   This could be an `IOException` caused by the `new
   FileWriter` statement or an
   `ArrayIndexOutOfBoundsException` caused by a wrong index
   value in the `for` loop.- Everything succeeds and the `try` statement exits normally.

Let's look at what happens in the `writeList` method
during these two exit possibilities.

### Scenario 1: An Exception Occurs

> The statement that creates a `FileWriter` can fail
> for a number of reasons. For example, the constructor for the
> `FileWriter` throws an `IOException`
> if the program cannot create or write to the file indicated.
>
> When `FileWriter` throws an `IOException`,
> the runtime system immediately stops executing the `try` block; method calls being executed are not completed. The runtime system then starts searching at the top of the method call stack for an appropriate exception handler. In this example, when the `IOException` occurs, the `FileWriter` constructor is at the top of the call stack. However, the `FileWriter` constructor doesn't have an appropriate exception handler, so the runtime system checks the next method — the `writeList` method — in the method call stack. The `writeList`
> method has two exception handlers: one for `IOException`
> and one for `ArrayIndexOutOfBoundsException`.
>
> The runtime system checks `writeList`'s handlers in the order
> in which they appear after the `try` statement. The argument
> to the first exception handler is `ArrayIndexOutOfBoundsException`. This does not match the type of exception thrown, so the runtime system checks the next exception handler — `IOException`. This matches the type of exception that was thrown, so the runtime system ends its search for an appropriate exception handler. Now that the runtime has found an appropriate handler, the code in that `catch` block is executed.
>
> After the exception handler executes, the runtime system passes
> control to the `finally` block. Code in the `finally` block executes regardless of the exception caught above it. In this scenario, the `FileWriter` was never opened and doesn't need to be
> closed. After the `finally` block finishes executing,
> the program continues with the first statement after the `finally` block.
>
> Here's the complete output from the `ListOfNumbers` program that appears when an `IOException` is thrown.
>
> ```
>
> Entering try statement
> Caught IOException: OutFile.txt
> PrintWriter not open 
>
> ```
>
> The boldface code in the following listing shows the statements
> that get executed during this scenario:
>
> ```
>
> public void writeList() {
>    PrintWriter out = null;
>
>     try {
>         System.out.println("Entering try statement");
>         out = new PrintWriter(
>                    new FileWriter("OutFile.txt"));
>         for (int i = 0; i < SIZE; i++)
>             out.println("Value at: " + i 
> 		        + " = " + vector.elementAt(i));
> 			       
>     } catch (ArrayIndexOutOfBoundsException e) {
>           System.err.println("Caught " 
>                     + "ArrayIndexOutOfBoundsException: " 
>                     + e.getMessage());
> 				 
>     } catch (IOException e) {
>             System.err.println("Caught IOException: "  
>                                 +  e.getMessage());
> 				 
>     } finally {
>         if (out != null) {
>             System.out.println("Closing PrintWriter");
>             out.close();
>         } 
>      else {
>             System.out.println("PrintWriter not open");
>         }
>     }
> }
>
> ```

### Scenario 2: The try Block Exits Normally

> In this scenario, all the statements within the scope of the `try`
> block execute successfully and throw no exceptions. Execution falls off the
> end of the `try` block, and the runtime system passes control
> to the `finally` block. Because everything was successful, the
> `PrintWriter` is open when control reaches the `finally`
> block, which closes the `PrintWriter`. Again, after the
> `finally` block finishes executing, the program continues
> with the first statement after the `finally` block.
>
> Here is the output from the `ListOfNumbers` program when no exceptions are thrown.
>
> ```
>
> Entering try statement
> Closing PrintWriter
>
> ```
>
> The boldface code in the following sample shows the statements that
> get executed during this scenario.
>
> ```
>
> public void writeList() {
>     PrintWriter out = null;
>     try {
>         System.out.println("Entering try statement");
>         out = new PrintWriter(
>                   new FileWriter("OutFile.txt"));
>         for (int i = 0; i < SIZE; i++)
>             out.println("Value at: " + i + " = " 
>                          +  vector.elementAt(i));
> 		  
>     } catch (ArrayIndexOutOfBoundsException e) {
>          System.err.println("Caught " 
>                      + "ArrayIndexOutOfBoundsException: " 
>                      + e.getMessage());
> 				 
>     } catch (IOException e) {
>          System.err.println("Caught IOException: " 
>                             + e.getMessage());
> 				 
>     } finally {
>          if (out != null) {
>              System.out.println("Closing PrintWriter");
>              out.close();
>           } 
>           else {
>              System.out.println("PrintWriter not open");
>           }
>     }
> }
>
> ```

[« Previous](tryResourceClose.html)
•
[Trail](../TOC.html)
•
[Next »](declaring.html)

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

**Previous page:** The try-with-resources Statement
  
**Next page:** Specifying the Exceptions Thrown by a Method




A browser with JavaScript enabled is required for this page to operate properly.