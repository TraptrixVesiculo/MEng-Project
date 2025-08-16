[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects

[Classes and Objects](../index.html)

[Classes](../classes.html)

[Declaring Classes](../classdecl.html)

[Declaring Member Variables](../variables.html)

[Defining Methods](../methods.html)

[Providing Constructors for Your Classes](../constructors.html)

[Passing Information to a Method or a Constructor](../arguments.html)

[Objects](../objects.html)

[Creating Objects](../objectcreation.html)

[Using Objects](../usingobject.html)

[More on Classes](../more.html)

[Returning a Value from a Method](../returnvalue.html)

[Using the this Keyword](../thiskey.html)

[Controlling Access to Members of a Class](../accesscontrol.html)

[Understanding Instance and Class Members](../classvars.html)

[Initializing Fields](../initial.html)

[Summary of Creating and Using Classes and Objects](../summaryclasses.html)

Questions and Exercises

[Questions and Exercises](../QandE/objects-questions.html)

[Nested Classes](../nested.html)

[Inner Class Example](../innerclasses.html)

[Summary of Nested Classes](../summarynested.html)

[Questions and Exercises](../QandE/nested-questions.html)

[Enum Types](../enum.html)

[Questions and Exercises](../QandE/enum-questions.html)

[Annotations](../annotations.html)

[Questions and Exercises](../QandE/annotations-questions.html)

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Classes and Objects](../index.html)

[« Previous](../summaryclasses.html) • [Trail](../../TOC.html) • [Next »](../QandE/objects-questions.html)

# Questions and Exercises: Classes

### Questions

> 1. Consider the following class:
>
> ```
>
> public class IdentifyMyParts {
>     public static int x = 7; 
>     public int y = 3; 
> }
>
> ```
>
> > a. What are the class variables?
> >
> > b. What are the instance variables?
> >
> > c. What is the output from the following code:
> >
> > ```
> >
> > IdentifyMyParts a = new IdentifyMyParts();
> > IdentifyMyParts b = new IdentifyMyParts();
> > a.y = 5;
> > b.y = 6;
> > a.x = 1;
> > b.x = 2;
> > System.out.println("a.y = " + a.y);
> > System.out.println("b.y = " + b.y);
> > System.out.println("a.x = " + a.x);
> > System.out.println("b.x = " + b.x);
> > System.out.println("IdentifyMyParts.x = " + IdentifyMyParts.x);
> >
> > ```

### Exercises

> 1. Write a class whose instances represent a single playing card from
> a deck of cards. Playing cards have two distinguishing properties:
> rank and suit. Be sure to keep your solution as you will be asked to
> rewrite it in [Enum Types](enum-questions.html).
>
> ---
>
> **Hint:** You can use the `assert` statement to check your assignments. You write:
>
> ```
>
> assert (boolean expression to test); 
>
> ```
>
> If the boolean expression is false, you will get an error message. For example,
>
> ```
>
> assert toString(ACE) == "Ace";
>
> ```
>
> should return `true`, so there will be no error message.
>
> If you use the `assert` statement, you must run your program with the `ea` flag:
>
> ```
>
> java -ea YourProgram.class
>
> ```
>
> ---
>
> 2. Write a class whose instances represent a **full** deck of cards.
> You should also keep this solution.
>   
>
> 3. Write a small program to test your deck and card classes. The program can be as simple as creating a deck of cards and displaying its cards.

[Check your answers.](creating-answers.html)

[« Previous](../summaryclasses.html)
•
[Trail](../../TOC.html)
•
[Next »](../QandE/objects-questions.html)

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

**Previous page:** Summary of Creating and Using Classes and Objects
  
**Next page:** Questions and Exercises: Objects




A browser with JavaScript enabled is required for this page to operate properly.