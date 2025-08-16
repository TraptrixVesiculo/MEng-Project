[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Essential Classes
  
**Lesson:** Exceptions

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[Exceptions](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises

### Questions

> 1. Question:
>    Is the following code legal?
>
>    ```
>
>    try {
>        
>    } finally {
>       
>    }
>
>    ```
>
>    Answer:
>    Yes, it's legal — and very useful
>    A `try` statement does not have to have
>    a `catch` block if it has
>    a `finally` block.
>    If the code in the `try` statement has multiple
>    exit points and no associated `catch` clauses,
>    the code in the `finally`
>    block is executed no matter how the `try` block is exited.
>    Thus it makes sense to provide a `finally` block
>    whenever there is code that *must always* be executed. This
>    include resource recovery code, such as the code to close I/O
>    streams.
>
>    - Question:
>      What exception types can be caught by the following handler?
>
>      ```
>
>      catch (Exception e) {
>           
>      }
>
>      ```
>
>      What is wrong with using this type of exception handler?
>
>      Answer:
>      This handler catches exceptions of type `Exception`;
>      therefore, it catches any exception.
>      This can be a poor implementation
>      because you are losing valuable information
>      about the type of exception being thrown
>      and making your code less efficient.
>      As a result, your program may be forced to determine the
>      type of exception before it can decide on the best recovery strategy.
>
>      - Question:
>        Is there anything wrong with this exception handler as written?
>        Will this code compile?
>
>        ```
>
>        try {
>
>        } catch (Exception e) {
>           
>        } catch (ArithmeticException a) {
>            
>        }
>
>        ```
>
>        Answer:
>        This first handler catches exceptions of type `Exception`;
>        therefore, it catches any exception,
>        including `ArithmeticException`.
>        The second handler could never be reached.
>        This code will not compile.
>
>        - Question: Match each situation in the first list
>          with an item in the second list.
>          1. `int[] A;
>               
>             A[0] = 0;`- The JVM starts running your program,
>               but the JVM can't find the Java platform classes.
>               (The Java platform classes reside in
>               `classes.zip` or `rt.jar`.)- A program is reading a stream and reaches the `end of stream` marker.- Before closing the stream and after reaching the `end of stream` marker, a program tries to read the stream again.
>
>          1. \_\_error- \_\_checked exception- \_\_compile error- \_\_no exception
>
>          Answer:
>          1. 3 (compile error). The array is not initialized and will not compile.- 1 (error).- 4 (no exception).
>                 When you read a stream, you expect there to
>                 be an end of stream marker. You should use
>                 exceptions to catch unexpected behavior in
>                 your program.- 2 (checked exception).

### Exercises

> 1. Exercise:
>    Add a `readList` method to
>    [`ListOfNumbers.java`](../examples/ListOfNumbers.java).
>    This method should read in `int` values from a file,
>    print each value,
>    and append them to the end of the vector.
>    You should catch all appropriate errors.
>    You will also need a text file containing numbers to read in.
>
>    Answer:
>    See `ListOfNumbers2.java.`
>
>    - Exercise:
>      Modify the following `cat` method so that it will compile:
>
>      ```
>
>      public static void cat(File file) {
>          RandomAccessFile input = null;
>          String line = null;
>
>          try {
>              input = new RandomAccessFile(file, "r");
>              while ((line = input.readLine()) != null) {
>                  System.out.println(line);
>              }
>              return;
>          } finally {
>              if (input != null) {
>                  input.close();
>              }
>          }
>      }
>
>      ```
>
>      Answer: The code to catch exceptions is shown in red:
>
>      ```
>
>      public static void cat(File file) {
>          RandomAccessFile input = null;
>          String line = null;
>
>          try {
>              input = new RandomAccessFile(file, "r");
>              while ((line = input.readLine()) != null) {
>                  System.out.println(line);
>              }
>              return;
>          } catch(FileNotFoundException fnf) {
>              System.err.format("File: %s not found%n", file);
>          } catch(IOException e) {
>              System.err.println(e.toString());
>          } finally {
>              if (input != null) {
>                  try {
>                      input.close();
>                  } catch(IOException io) {
>                  }
>              }
>          }
>      }
>
>      ```

[« Previous](../QandE/questions.html)
•
[TOC](../../TOC.html)


---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Questions and Exercises




A browser with JavaScript enabled is required for this page to operate properly.