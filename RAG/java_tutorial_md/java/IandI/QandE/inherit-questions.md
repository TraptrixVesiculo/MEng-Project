[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance

[Interfaces and Inheritance](../index.html)

[Interfaces](../createinterface.html)

[Defining an Interface](../interfaceDef.html)

[Implementing an Interface](../usinginterface.html)

[Using an Interface as a Type](../interfaceAsType.html)

[Rewriting Interfaces](../nogrow.html)

[Summary of Interfaces](../summary-interface.html)

[Questions and Exercises](../QandE/interfaces-questions.html)

[Inheritance](../subclasses.html)

[Overriding and Hiding Methods](../override.html)

[Polymorphism](../polymorphism.html)

[Hiding Fields](../hidevariables.html)

[Using the Keyword super](../super.html)

[Object as a Superclass](../objectclass.html)

[Writing Final Classes and Methods](../final.html)

[Abstract Methods and Classes](../abstract.html)

[Summary of Inheritance](../summaryinherit.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Interfaces and Inheritance](../index.html)

[« Previous](../summaryinherit.html) • [Trail](../../TOC.html) • [Next »](../../data/index.html)

# Questions and Exercises: Inheritance

### Questions

> 1. Consider the following two classes:
>
> ```
>
> public class ClassA {
>     public void methodOne(int i) {
>     }
>     public void methodTwo(int i) {
>     }
>     public static void methodThree(int i) {
>     }
>     public static void methodFour(int i) {
>     }
> }
>
> public class ClassB extends ClassA {
>     public static void methodOne(int i) {
>     }
>     public void methodTwo(int i) {
>     }
>     public void methodThree(int i) {
>     }
>     public static void methodFour(int i) {
>     }
> }
>
> ```
>
> > a. Which method overrides a method in the superclass?  
> > b. Which method hides a method in the superclass?  
> > c. What do the other methods do?
>
>   
> 2. Consider the
> [`Card`](../examples/Card.java),
> [`Deck`](../examples/Deck.java), and
> [`DisplayDeck`](../examples/DisplayDeck.java )
> classes you wrote in
> [`Questions and Exercises: Classes`](../../javaOO/QandE/creating-questions.html )
> . What `Object`
> methods should each of these classes override?

### Exercises

> 1. Write the implementations for the methods that you answered in question 2.
>
> [Check your answers.](inherit-answers.html)

[« Previous](../summaryinherit.html)
•
[Trail](../../TOC.html)
•
[Next »](../../data/index.html)

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

**Previous page:** Summary of Inheritance
  
**Next page:** Numbers and Strings




A browser with JavaScript enabled is required for this page to operate properly.