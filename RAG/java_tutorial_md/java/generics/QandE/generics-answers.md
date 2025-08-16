[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Generics](../index.html)

[« Previous](../QandE/generics-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Generics

### Questions

> Question 1. Consider the following classes:
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
> > > Question 1a. AnimalHouse<Animal> house = new AnimalHouse<Cat>();
> > >
> > > ```
> > >
> > > > Answer 1a: 1. fails to compile
> > > > > `AnimalHouse<Cat>` and `AnimalHouse<Animal>` are not
> > > > > compatible types, even though `Cat` is a subtype of
> > > > > `Animal`.
> > >
> > > ```
> > >
> > > Question 1b. AnimalHouse<Cat> house = new AnimalHouse<Animal>();
> > >
> > > ```
> > >
> > > > Answer 1b: 1. fails to compile
> > > > > Same as 1a:
> > > > > `AnimalHouse<Cat>` and `AnimalHouse<Animal>` are not
> > > > > compatible types, even though `Cat` is a subtype of
> > > > > `Animal`.
> > >
> > > ```
> > >
> > > Question 1c. AnimalHouse<?> house = new AnimalHouse<Cat>();
> > >              house.setAnimal(new Cat());
> > >
> > > ```
> > >
> > > > Answer 1c: 1. fails to compile
> > > > > While the first line is acceptable — it is OK to define
> > > > > an instance of unknown type — the compiler doesn't know
> > > > > the type of animal stored in `house` so the
> > > > > `setAnimal` method cannot be used.
> > >
> > > ```
> > >
> > > Question 1d. AnimalHouse house = new AnimalHouse();
> > >              house.setAnimal(new Dog());
> > >
> > > ```
> > >
> > > > Answer 1d: 2. compiles with a warning
> > > > > The compiler doesn't know what type `house` contains.
> > > > > It will accept the code, but warn that there might be a problem when
> > > > > setting the animal to an instance of `Dog`.
> > > > >
> > > > > Using a generic type as a raw type might be a way to work around
> > > > > a particular compiler error, but you lose the
> > > > > type checking that generics provides, so *it is not recommended.*

### Exercises

> Exercise 1. Design a class that acts as a library for the following kinds
> of media: book, video, and newspaper. Provide one version of the class that
> uses
> generics and one that does not. Feel free to use any additional APIs for
> storing
> and retrieving the media.
>
> Answer 1:
>
> **Non-Generic Version**
>
> ```
>
> import java.util.List;
> import java.util.ArrayList;
>
> public class Library {
>     private List resources = new ArrayList();
>     public void addMedia(Media x) {
>         resources.add(x);
>     }
>     public Media retrieveLast() {
>         int size = resources.size();
>         if (size > 0) {
>             return (Media)resources.get(size - 1);
>         }
>         return null;
>     }
> }
>
> interface Media {
> }
>
> interface Book extends Media {
> }
>
> interface Video extends Media {
> }
>
> interface Newspaper extends Media {
> }
>
> ```
>
> **Generic Version**
>
> ```
>
> import java.util.List;
> import java.util.ArrayList;
>
> public class Library<E extends Media> {
>     private List<E> resources = new ArrayList<E>();
>     public void addMedia(E x) {
>         resources.add(x);
>     }
>     public E retrieveLast() {
>         int size = resources.size();
>         if (size > 0) {
>             return resources.get(size - 1);
>         }
>         return null;
>     }
> }
>
> ```

[« Previous](../QandE/generics-questions.html)
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

**Previous page:** Questions and Exercises: Generics




A browser with JavaScript enabled is required for this page to operate properly.