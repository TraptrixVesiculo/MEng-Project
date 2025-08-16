[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Classes and Objects](../index.html)

[« Previous](../QandE/nested-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Nested Classes

### Questions

> Question 1: The
> program
> [`Problem.java`](Problem.java) doesn't compile. What do you need to do to make it compile? Why?  
> Answer 1:
> Delete `static` in front of the declaration of the `Inner`
> class. An static inner class does not have access to the instance fields of the outer class. See
> [`ProblemSolved.java`](ProblemSolved.java).
>
> Question 2: Use the
> Java API documentation for the
> [`Box`](http://download.oracle.com/javase/7/docs/api/javax/swing/Box.html) class (in the
> `javax.swing` package) to help you answer the following
> questions.
> > **a.**What static nested class does `Box` define?   
> > Answer 2a:
> > `Box.Filler`
> > **b.** What inner class does
> > `Box` define?
> >   
> > Answer 2b:
> > `Box.AccessibleBox`
> > **c.** What is the
> > superclass of `Box`’s inner class?  
> > Answer 2c:`[java.awt.]Container.AccessibleAWTContainer`
> > **d.** Which of `Box`’s nested
> > classes can you use from any class?  
> > Answer 2d:
> > `Box.Filler`
> > **e.** How do you create an
> > instance of `Box`’s `Filler`
> > class?  
> > Answer 2e: `new
> > Box.Filler(minDimension, prefDimension, maxDimension)`

### Exercises

> Exercise 1: Get the
> file
> [`Class1.java`](Class1.java).
> > a.
> > Compile and run `Class1`. What is the output?
> >   
> > Answer:
> >   
> > `InnerClass1: getString invoked.  
> > InnerClass1:
> > getAnotherString invoked.`

[« Previous](../QandE/nested-questions.html)
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

**Previous page:** Questions and Exercises: Nested Classes




A browser with JavaScript enabled is required for this page to operate properly.