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

[« Previous](../QandE/creating-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Classes

### Questions

> Question 1:
> Consider the following class:
> > ```
> >
> > public class IdentifyMyParts {
> >     public static int x = 7;
> >     public int y = 3;
> > } 
> >
> > ```
>
> > Question 1a. What are the class variables?  
> > Answer 1a: x
> >
> > Question 1b. What are the instance variables?  
> > Answer 1b: y
> >
> > Question 1c. What is the output from the following
> > code:
> > > ```
> > >
> > > IdentifyMyParts a = new IdentifyMyParts(); 
> > > IdentifyMyParts b = new IdentifyMyParts(); 
> > > a.y = 5; 
> > > b.y = 6; 
> > > a.x = 1; 
> > > b.x = 2; 
> > > System.out.println("a.y = " + a.y); 
> > > System.out.println("b.y = " + b.y); 
> > > System.out.println("a.x = " + a.x); 
> > > System.out.println("b.x = " + b.x); 
> > > System.out.println("IdentifyMyParts.x = " + IdentifyMyParts.x);
> > >
> > > ```
> >
> > Answer 1c: Here is the output:
> > > ```
> > >
> > >  a.y = 5 
> > >  b.y = 6 
> > >  a.x = 2 
> > >  b.x = 2
> > >  IdentifyMyParts.x = 2
> > >
> > > ```
> > >
> > > Because `x` is defined as a `public static int`
> > > in the class `IdentifyMyParts`, every reference to
> > > `x` will have the value that was last assigned because
> > > `x` is a static variable (and therefore a class variable)
> > > shared across all instances of the class. That is, there is only
> > > one `x`: when the value of `x` changes in any
> > > instance it affects the value of `x` for all instances of
> > > `IdentifyMyParts`.
> > >
> > > This is covered in the Class Variables section of
> > > [Understanding Instance and Class Members](../classvars.html).
>
> ### Exercises
>
> > Exercise 1: Write a class whose
> > instances represent a single playing card from a deck of cards.
> > Playing cards have two distinguishing properties: rank and suit.
> > Be sure to keep your solution as you will be asked to rewrite it
> > in [Enum Types](enum-questions.html).
> >   
> >  Answer 1:
> >
> > [Card.java](../examples/Card.java)[![(in a .java source file)](../../../images/sourceIcon.gif)](../examples/Card.java)
> >
> > Exercise 2: Write a class whose instances
> > represents a **full** deck of cards. You should also keep this solution.
> >   
> >  Answer 2: See 
> > [Deck.java](../examples/Deck.java)
> > [![(in a .java source file)](../../../images/sourceIcon.gif)](../examples/Deck.java).
> >
> > Exercise 3: Write a small program to test your deck and card classes. The program can be as simple as creating a deck of cards and displaying its cards.   
> >  Answer 3: See
> > [DisplayDeck.java](../examples/DisplayDeck.java)
> > [![(in a .java source file)](../../../images/sourceIcon.gif)](../examples/DisplayDeck.java).

[« Previous](../QandE/creating-questions.html)
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

**Previous page:** Questions and Exercises: Classes




A browser with JavaScript enabled is required for this page to operate properly.