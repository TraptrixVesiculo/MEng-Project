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

[Questions and Exercises](../QandE/numbers-questions.html)

[Characters](../characters.html)

[Strings](../strings.html)

[Converting Between Numbers and Strings](../converting.html)

[Manipulating Characters in a String](../manipstrings.html)

[Comparing Strings and Portions of Strings](../comparestrings.html)

[The StringBuilder Class](../buffers.html)

[Summary of Characters and Strings](../stringsummary.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Numbers and Strings](../index.html)

[« Previous](../stringsummary.html) • [Trail](../../TOC.html) • [Next »](../../generics/index.html)

# Questions and Exercises: Characters and Strings

### Questions

> 1. What is the initial capacity of the following string builder?
>
>    ```
>
>    StringBuilder sb = new StringBuilder("Able was I ere I saw Elba.");
>
>    ```
>
>      
>    - Consider the following string:
>
>      ```
>
>      String hannah = "Did Hannah see bees? Hannah did.";
>
>      ```
>
>      1. What is the value displayed by the expression `hannah.length()`?- What is the value returned by the method call `hannah.charAt(12)`?- Write an expression that refers to the letter `b` in the string
>             referred to by `hannah`.- How long is the string returned by the following expression?
>        What is the string?
>
>        ```
>
>        "Was it a car or a cat I saw?".substring(9, 12)
>
>        ```
>
>          
>        - In the following program,
>          called
>          [`ComputeResult`](ComputeResult.java), what is the value of `result` after each numbered line executes?
>
>          ```
>
>          public class ComputeResult {
>              public static void main(String[] args) {
>                  String original = "software";
>                  StringBuilder result = new StringBuilder("hi");
>                  int index = original.indexOf('a');
>
>          /*1*/   result.setCharAt(0, original.charAt(0));
>          /*2*/   result.setCharAt(1, original.charAt(original.length()-1));
>          /*3*/   result.insert(1, original.charAt(4));
>          /*4*/   result.append(original.substring(1,4));
>          /*5*/   result.insert(3, (original.substring(index, index+2) + " ")); 
>
>                  System.out.println(result);
>              }
>          }
>
>          ```

### Exercises

> 1. Show two ways to concatenate the following two strings
>    together to get the string `"Hi, mom."`:
>
>    ```
>
>    String hi = "Hi, ";
>    String mom = "mom.";
>
>    ```
>
>    - Write a program that computes your initials from your full name and
>      displays them.  
>      - An anagram is a word or a phrase made by transposing the letters of
>        another word or phrase; for example, "parliament" is an anagram of
>        "partial men," and "software" is an anagram of "swear oft." Write a
>        program that figures out whether one string is an anagram of another
>        string. The program should ignore white space and punctuation.

[Check your answers.](characters-answers.html)

[« Previous](../stringsummary.html)
•
[Trail](../../TOC.html)
•
[Next »](../../generics/index.html)

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

**Previous page:** Summary of Characters and Strings
  
**Next page:** Generics




A browser with JavaScript enabled is required for this page to operate properly.