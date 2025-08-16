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

[« Previous](../QandE/interfaces-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Interfaces

### Questions

> Question 1: 
> What methods would a class that implements the
> `java.lang.CharSequence` interface have to implement?
>   
> Answer 1:  `charAt`,
> `length`, `subSequence`, and `toString`.
>
> Question 2: 
> What is wrong with the following interface?
> > ```
> >
> > public interface SomethingIsWrong {
> >     void aMethod(int aValue) {
> >         System.out.println("Hi Mom");
> >     }
> > }
> >
> > ```
>
> Answer 2:  It has a method implementation in it.
> It should just have a declaration.
>
> Question 3: 
> Fix the interface in Question 2.
>   
> Answer 3: 
> > ```
> >
> > public interface SomethingIsWrong {
> >     void aMethod(int aValue);
> > }
> >
> > ```
>
> Question 4: 
> Is the following interface valid?
> > ```
> >
> > public interface Marker {
> > }
> >
> > ```
>
> Answer 4:  Yes. Methods are not required.
> Empty interfaces can be used as types and to mark classes without
> requiring any particular method implementations.
> For an example of a useful empty interface, see `java.io.Serializable.`

### Exercises

> Exercise 1: 
> Write a class that implements the `CharSequence`
> interface found in the `java.lang` package.
> Your implementation should return the string backwards.
> Select one of the sentences from this book to use as the data.
> Write a small `main` method to test your class;
> make sure to call all four methods.
>   
> Answer 1:  See
> [`CharSequenceDemo.java`](../examples/CharSequenceDemo.java)
>
> Exercise 2: 
> Suppose that you have written a time server, which periodically
> notifies its clients of the current date and time. Write an
> interface that the server could use to enforce a particular
> protocol on its clients.
>   
> Answer 2:  See
> [`TimeClient.java`](../examples/TimeClient.java)

[« Previous](../QandE/interfaces-questions.html)
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

**Previous page:** Questions and Exercises: Interfaces




A browser with JavaScript enabled is required for this page to operate properly.