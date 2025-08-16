[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Language Basics

[Language Basics](../index.html)

[Variables](../variables.html)

[Primitive Data Types](../datatypes.html)

[Arrays](../arrays.html)

[Summary of Variables](../variablesummary.html)

[Questions and Exercises](../QandE/questions_variables.html)

[Operators](../operators.html)

[Assignment, Arithmetic, and Unary Operators](../op1.html)

[Equality, Relational, and Conditional Operators](../op2.html)

[Bitwise and Bit Shift Operators](../op3.html)

[Summary of Operators](../opsummary.html)

Questions and Exercises

[Expressions, Statements, and Blocks](../expressions.html)

[Questions and Exercises](../QandE/questions_expressions.html)

[Control Flow Statements](../flow.html)

[The if-then and if-then-else Statements](../if.html)

[The switch Statement](../switch.html)

[The while and do-while Statements](../while.html)

[The for Statement](../for.html)

[Branching Statements](../branch.html)

[Summary of Control Flow Statements](../flowsummary.html)

[Questions and Exercises](../QandE/questions_flow.html)

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Language Basics](../index.html)

[« Previous](../opsummary.html) • [Trail](../../TOC.html) • [Next »](../expressions.html)

# Questions and Exercises: Operators

### Questions

> 1. Consider the following code snippet.
>
>    ```
>
>    arrayOfInts[j] > arrayOfInts[j+1]
>
>    ```
>
>    Which operators does the code contain?
>
>    - Consider the following code snippet.
>
>      ```
>
>      int i = 10;
>      int n = i++%5;
>
>      ```
>
>      1. What are the values of `i` and `n`
>         after the code is executed?
>
>         - What are the final values of `i` and `n`
>           if instead of using the postfix increment operator (`i++`),
>           you use the prefix version (`++i)`)?
>
>      - To invert the value of a `boolean`, which operator
>        would you use?
>
>        - Which operator is used to compare two values, `=` or `==` ?
>
>          - Explain the following code sample: `result = someCondition ? value1 : value2;`

### Exercises

> 1. Change the following program to use compound assignments:
>
>    ```
>
>    class ArithmeticDemo {
>
>         public static void main (String[] args){
>              
>              int result = 1 + 2; // result is now 3
>              System.out.println(result);
>
>              result = result - 1; // result is now 2
>              System.out.println(result);
>
>              result = result * 2; // result is now 4
>              System.out.println(result);
>
>              result = result / 2; // result is now 2
>              System.out.println(result);
>
>              result = result + 8; // result is now 10
>              result = result % 7; // result is now 3
>              System.out.println(result);
>
>         }
>    }
>
>
>    ```
>
>    - In the following program, explain why the value "6" is printed twice in a row:
>
>      ```
>
>      class PrePostDemo {
>           public static void main(String[] args){
>                int i = 3;
>      	  i++;
>      	  System.out.println(i);	// "4"
>      	  ++i;			   
>      	  System.out.println(i);	// "5"
>      	  System.out.println(++i);	// "6"
>      	  System.out.println(i++);	// "6"
>      	  System.out.println(i);	// "7"
>           }
>      }
>
>      ```

[Check your answers](answers_operators.html)

[« Previous](../opsummary.html)
•
[Trail](../../TOC.html)
•
[Next »](../expressions.html)

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

**Previous page:** Summary of Operators
  
**Next page:** Expressions, Statements, and Blocks




A browser with JavaScript enabled is required for this page to operate properly.