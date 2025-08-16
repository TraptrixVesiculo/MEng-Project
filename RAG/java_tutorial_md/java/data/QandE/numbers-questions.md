[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings

[Numbers and Strings](../index.html)

[Numbers](../numbers.html)

[The Numbers Classes](../numberclasses.html)

[Formatting Numeric Print Output](../numberformat.html)

[Beyond Basic Arithmetic](../beyondmath.html)

[Summary of Numbers](../numbersummary.html)

Questions and Exercises

[Characters](../characters.html)

[Strings](../strings.html)

[Converting Between Numbers and Strings](../converting.html)

[Manipulating Characters in a String](../manipstrings.html)

[Comparing Strings and Portions of Strings](../comparestrings.html)

[The StringBuilder Class](../buffers.html)

[Summary of Characters and Strings](../stringsummary.html)

[Questions and Exercises](../QandE/characters-questions.html)

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Numbers and Strings](../index.html)

[« Previous](../numbersummary.html) • [Trail](../../TOC.html) • [Next »](../characters.html)

# Questions and Exercises: Numbers

### Questions

> 1. Use the API documentation to find the answers to the following questions:
> > a. What `Integer` method can you use to convert an `int` into a string that expresses the number in hexadecimal? For example, what method converts the integer 65 into the string "41"?
> >
> > b. What `Integer` method would you use to convert a string expressed in base 5 into the equivalent `int`? For example, how would you convert the string "230" into the integer value 65? Show the code you would use to accomplish this task.
> >
> > c. What Double method can you use to detect whether a floating-point number has the special value Not a Number (`NaN`)?
>
> 2. What is the value of the following expression, and why?
>
> ```
>
> Integer.valueOf(1).equals(Long.valueOf(1))
>
> ```

### Exercises

> 1. Change
> [`MaxVariablesDemo`](MaxVariablesDemo.java) to show minimum values instead of maximum values. You can delete all code related to the variables `aChar` and `aBoolean`. What is the output?
>
> 2. Create a program that reads an unspecified number of integer arguments from the command line and adds them together. For example, suppose that you enter the following:
>
> ```
>
> java Adder 1 3 2 10
>
> ```
>
> The program should display `16` and then exit.
> The program should display an error message if the user
> enters only one argument. You can base your program on
> [`ValueOfDemo`](../../data/examples/ValueOfDemo.java).
>
> 3. Create a program that is similar to the previous one but has the following differences:
>
> * Instead of reading integer arguments, it reads floating-point arguments.* It displays the sum of the arguments, using exactly two digits to the right of the decimal point.
>
> For example, suppose that you enter the following:
>
> ```
>
> java FPAdder 1 1e2 3.0 4.754
>
> ```
>
> The program would display `108.75`. Depending on your locale, the decimal point might be a comma (`,`) instead of a period (`.`).

[Check your answers.](numbers-answers.html)

[« Previous](../numbersummary.html)
•
[Trail](../../TOC.html)
•
[Next »](../characters.html)

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

**Previous page:** Summary of Numbers
  
**Next page:** Characters




A browser with JavaScript enabled is required for this page to operate properly.