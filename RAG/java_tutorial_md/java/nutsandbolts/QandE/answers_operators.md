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

[« Previous](../QandE/questions_operators.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Operators

### Answers to Questions

> 1. Consider the following code snippet:
>
>    ```
>
>    arrayOfInts[j] > arrayOfInts[j+1]
>
>    ```
>
>    **Question:**
>    What operators does the code contain?
>      
>    **Answer:**
>    `>`, `+`  
>      
>    - Consider the following code snippet:
>
>      ```
>
>      int i = 10;
>      int n = i++%5;
>
>      ```
>
>      1. **Question:**
>         What are the values of `i` and `n`
>         after the code is executed?
>           
>         **Answer:** `i` is 11, and `n` is 0.  
>           
>         - **Question:**
>           What are the final values of `i` and `n`
>           if instead of using the postfix increment operator (`i++`),
>           you use the prefix version (`++i)`)?
>             
>           **Answer:** `i` is 11, and `n` is 1.
>
>      - **Question:** To invert the value of a `boolean`, which operator
>        would you use?  
>        **Answer:** The logical complement operator "!".
>
>        - **Question**: Which operator is used to compare two values, `=` or `==` ?  
>          **Answer:** The `==` operator is used for comparison, and `=` is used
>          for assignment.
>
>          - **Question:** Explain the following code sample: `result = someCondition ? value1 : value2;`
>              
>            **Answer:**
>            This code should be read as: "If `someCondition`
>            is `true`, assign the value of `value1` to `result`.
>            Otherwise, assign the value of `value2` to `result`."

### Exercises

> 1. Change the following program to use compound assignments:
>    > ```
>    >
>    > class ArithmeticDemo {
>    >
>    >      public static void main (String[] args){
>    >           
>    >           int result = 1 + 2; // result is now 3
>    >           System.out.println(result);
>    >
>    >           result = result - 1; // result is now 2
>    >           System.out.println(result);
>    >
>    >           result = result * 2; // result is now 4
>    >           System.out.println(result);
>    >
>    >           result = result / 2; // result is now 2
>    >           System.out.println(result);
>    >
>    >           result = result + 8; // result is now 10
>    >           result = result % 7; // result is now 3
>    >           System.out.println(result);
>    >
>    >      }
>    > }
>    >
>    >
>    > ```
>
>    Here is one solution:
>
>    ```
>
>    class ArithmeticDemo {
>
>         public static void main (String[] args){
>              int result = 3;
>              System.out.println(result);
>
>              result -= 1; // result is now 2
>              System.out.println(result);
>
>              result *= 2; // result is now 4
>              System.out.println(result);
>
>              result /= 2; // result is now 2
>              System.out.println(result);
>
>              result += 8; // result is now 10
>              result %= 7; // result is now 3
>              System.out.println(result);
>
>         }
>    }
>
>    ```
>
>    - In the following program, explain why the value "6" is printed twice in a row:
>      > ```
>      >
>      > class PrePostDemo {
>      >      public static void main(String[] args){
>      >           int i = 3;
>      > 	  i++;
>      > 	  System.out.println(i);	// "4"
>      > 	  ++i;			   
>      > 	  System.out.println(i);	// "5"
>      > 	  System.out.println(++i);	// "6"
>      > 	  System.out.println(i++);	// "6"
>      > 	  System.out.println(i);	// "7"
>      >      }
>      > }
>      >
>      > ```
>
>      The code `System.out.println(++i);` evaluates to 6, because the
>      prefix version of `++` evaluates to the incremented value. The next line, `System.out.println(i++);`
>      evaluates to the current value (6), then increments by one. So "7" doesn't get printed
>      until the next line.

[« Previous](../QandE/questions_operators.html)
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

**Previous page:** Questions and Exercises: Operators




A browser with JavaScript enabled is required for this page to operate properly.