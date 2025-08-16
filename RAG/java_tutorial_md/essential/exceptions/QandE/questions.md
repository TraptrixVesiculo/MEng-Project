[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Exceptions

[Exceptions](../index.html)

[What Is an Exception?](../definition.html)

[The Catch or Specify Requirement](../catchOrDeclare.html)

[Catching and Handling Exceptions](../handling.html)

[The try Block](../try.html)

[The catch Blocks](../catch.html)

[The finally Block](../finally.html)

[The try-with-resources Statement](../tryResourceClose.html)

[Putting It All Together](../putItTogether.html)

[Specifying the Exceptions Thrown by a Method](../declaring.html)

[How to Throw Exceptions](../throwing.html)

[Chained Exceptions](../chained.html)

[Creating Exception Classes](../creating.html)

[Unchecked Exceptions — The Controversy](../runtime.html)

[Advantages of Exceptions](../advantages.html)

[Summary](../summary.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[Exceptions](../index.html)

[« Previous](../summary.html) • [Trail](../../TOC.html) • [Next »](../../io/index.html)

# Questions and Exercises

### Questions

> 1. Is the following code legal?
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
>    - What exception types can be caught by the following handler?
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
>      - Is there anything wrong with the following exception handler as written?
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
>        - Match each situation in the first list
>          with an item in the second list.
>          1. `int[] A;
>               
>             A[0] = 0;`- The JVM starts running your program,
>               but the JVM can't find the Java platform classes.
>               (The Java platform classes reside in
>               `classes.zip` or `rt.jar`.)- A program is reading a stream and reaches the `end of stream` marker.- Before closing the stream and after reaching the `end of stream` marker, a program tries to read the stream again.
>
>          1. \_\_error- \_\_checked exception- \_\_compile error- \_\_no exception

### Exercises

> 1. Add a `readList` method to
>    [`ListOfNumbers.java`](../examples/ListOfNumbers.java).
>    This method should read in `int` values from a file,
>    print each value,
>    and append them to the end of the vector.
>    You should catch all appropriate errors.
>    You will also need a text file containing numbers to read in.
>
>    - Modify the following `cat` method so that it will compile.
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

[Check your answers.](answers.html)

[« Previous](../summary.html)
•
[Trail](../../TOC.html)
•
[Next »](../../io/index.html)

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

**Previous page:** Summary
  
**Next page:** Basic I/O




A browser with JavaScript enabled is required for this page to operate properly.