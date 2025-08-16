[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Interfaces and Inheritance](../index.html)

[« Previous](../QandE/inherit-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Inheritance

### Questions

> Question 1: Consider the following two classes:
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
> > Question 1a: Which method overrides a method in the superclass?  
> >  Answer 1a: `methodTwo`
> >
> > Question 1b: Which method hides a method in the superclass?  
> >  Answer 1b: `methodFour`
> >
> > Question 1c: What do the other methods do?  
> >  Answer 1c: They cause compile-time errors.
>
> Question 2: Consider the
> [`Card`](../examples/Card.java),
> [`Deck`](../examples/Deck.java), and
> [`DisplayDeck`](../examples/DisplayDeck.java )
> classes you wrote in the previous exercise. What `Object`
> methods should each of these classes override?
>   
>  Answer 2:
> `Card` and `Deck` should override `equals`,
> `hashCode`, and `toString`.

### Exercises

> Exercise 1: Write the implementations
> for the methods that you answered in question 2.
>   
>  Answer 1:
> See
> [`Card2`](../examples/Card2.java ).

[« Previous](../QandE/inherit-questions.html)
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

**Previous page:** Questions and Exercises: Inheritance




A browser with JavaScript enabled is required for this page to operate properly.