[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Language Basics](../index.html)

[« Previous](../QandE/questions_flow.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Control Flow Statements

### Answers to Questions

> 1. The most basic control flow statement supported by the Java programming language is the **if-then** statement.
>
>    - The **switch** statement allows for any number of possible execution paths.
>
>      - The **do-while** statement is similar to the `while` statement,
>        but evaluates its expression at the **bottom** of the loop.
>
>        - **Question:** How do you write an infinite loop using the `for` statement?
>
>          **Answer:**
>
>          ```
>
>          for ( ; ; ) {
>
>          }
>
>          ```
>
>          - **Question:** How do you write an infinite loop using the `while` statement?
>
>            **Answer:**
>
>            ```
>
>            while (true) {
>
>            }
>
>            ```

### Exercises

> 1. Consider the following code snippet.
>
>    ```
>
>    if (aNumber >= 0)
>        if (aNumber == 0) System.out.println("first string");
>    else System.out.println("second string");
>    System.out.println("third string");
>
>    ```
>
>    1. **Exercise:**
>       What output do you think the code will produce if `aNumber` is 3?
>
>       **Solution:**
>
>       ```
>
>       second string
>       third string
>
>       ```
>
>       - **Exercise:**
>         Write a test program containing the previous code snippet;
>         make `aNumber` 3.
>         What is the output of the program?
>         Is it what you predicted?
>         Explain why the output is what it is.
>         In other words, what is the control flow for the code snippet?
>
>         **Solution:**
>         [`NestedIf`](NestedIf.java)
>
>         ```
>
>         second string
>         third string
>
>         ```
>
>         3 is greater than or equal to 0,
>         so execution progresses to the second `if` statement. The
>         second `if` statement's test fails because 3 is not equal to 0.
>         Thus, the `else` clause
>         executes (since it's attached to the second `if` statement).
>         Thus, `second string` is displayed.
>         The final `println` is completely outside
>         of any `if` statement,
>         so it always gets executed,
>         and thus `third string` is always displayed.
>
>         - **Exercise:**
>           Using only spaces and line breaks, reformat the code snippet to make
>           the control flow easier to understand.
>
>           **Solution:**
>
>           ```
>
>           if (aNumber >= 0)
>               if (aNumber == 0)
>                   System.out.println("first string");
>               else
>                   System.out.println("second string");
>
>           System.out.println("third string");
>
>           ```
>
>           - **Exercise:**
>             Use braces `{` and `}`
>             to further clarify the code and reduce the
>             possibility of errors by future maintainers of the code.
>
>             **Solution:**
>
>             ```
>
>             if (aNumber >= 0) {
>                 if (aNumber == 0) {
>                     System.out.println("first string");
>                 } else {
>                     System.out.println("second string");
>                 }
>             }
>
>             System.out.println("third string");
>
>             ```

[« Previous](../QandE/questions_flow.html)
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

**Previous page:** Questions and Exercises: Control Flow Statements




A browser with JavaScript enabled is required for this page to operate properly.