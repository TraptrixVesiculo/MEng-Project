[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Generics](../index.html)

[Introduction](../generics.html)

[Generic Types](../gentypes.html)

[Generic Methods and Constructors](../genmethods.html)

[Type Inference](../gentypeinference.html)

[Bounded Type Parameters](../bounded.html)

[Subtyping](../subtyping.html)

[Wildcards](../wildcards.html)

[Type Erasure](../erasure.html)

[Using Non-Reifiable Parameters with Varargs Methods](../non-reifiable-varargs-type.html)

[Summary of Generics](../summarygenerics.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Generics](../index.html)

[« Previous](../summarygenerics.html) • [Trail](../../TOC.html) • [Next »](../../package/index.html)

# Questions and Exercises: Generics

### Questions

> 1. Consider the following classes:
>
> ```
>
> public class AnimalHouse<E> {
>     private E animal;
>     public void setAnimal(E x) {
>         animal = x;
>     }
>     public E getAnimal() {
>         return animal;
>     }
> }
>
> public class Animal{
> }
>
> public class Cat extends Animal {
> }
>
> public class Dog extends Animal {
> }
>
> ```
>
> > For the following code snippets, identify whether the code:
> >
> > * fails to compile,* compiles with a warning,* generates an error at runtime, or* none of the above (compiles and runs without problem.)
> >
> > > ```
> > >
> > > a. AnimalHouse<Animal> house = new AnimalHouse<Cat>();
> > >
> > > ```
> > >
> > > ```
> > >
> > > b. AnimalHouse<Dog> house = new AnimalHouse<Animal>();
> > >
> > > ```
> > >
> > > ```
> > >
> > > c. AnimalHouse<?> house = new AnimalHouse<Cat>();
> > >    house.setAnimal(new Cat());
> > >
> > > ```
> > >
> > > ```
> > >
> > > d. AnimalHouse house = new AnimalHouse();
> > >    house.setAnimal(new Dog());
> > >
> > > ```

### Exercises

> 1. Design a class that acts as a library for the following kinds
>    of media: book, video, and newspaper. Provide one version of the class that uses generics and one that does not. Feel free to use any additional APIs for storing and retrieving the media.

[Check your answers.](generics-answers.html)

[« Previous](../summarygenerics.html)
•
[Trail](../../TOC.html)
•
[Next »](../../package/index.html)

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

**Previous page:** Summary of Generics
  
**Next page:** Packages




A browser with JavaScript enabled is required for this page to operate properly.