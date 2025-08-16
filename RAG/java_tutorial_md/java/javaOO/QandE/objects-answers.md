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

[« Previous](../QandE/objects-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Objects

### Questions

> Question 1:
> What's wrong with the following program?
>
> ```
>
> public class SomethingIsWrong {
>     public static void main(String[] args) {
>         Rectangle myRect;
>         myRect.width = 40;
>         myRect.height = 50;
>         System.out.println("myRect's area is " + myRect.area());
>     }
> }
>
> ```
>
> Answer 1:
> The code never creates a
> [`Rectangle`](Rectangle.java) object.
> With this simple program, the compiler generates an error.
> However, in a more realistic situation,
> `myRect` might be initialized to `null` in one place,
> say in a constructor,
> and used later.
> In that case, the program will compile just fine,
> but will generate a `NullPointerException` at runtime.
>
> Question 2:
> The following code creates one array and one
> string object.
> How many references to those objects exist after the code executes?
> Is either object eligible for garbage collection?
>
> ```
>
> ...
> String[] students = new String[10];
> String studentName = "Peter Parker";
> students[0] = studentName;
> studentName = null;
> ...
>
> ```
>
> Answer 2:
> There is one reference to the `students` array and that array
> has one reference to the string `Peter Parker`.
> Neither object is eligible for garbage collection.
>   
>
> Question 3:
> How does a program destroy an object that it creates?
>   
> Answer 3:
> A program does not explicitly destroy objects.
> A program can set all references to an object to `null`
> so that it becomes eligible for garbage collection.
> But the program does not actually destroy objects.

  

### Exercises

> Exercise 1:
> Fix the program called `SomethingIsWrong` shown in Question 1.
>   
> Answer 1: See
> [`SomethingIsRight`](SomethingIsRight.java)
>
> ```
>
>
> public class SomethingIsRight {
>     public static void main(String[] args) {
>         Rectangle myRect = new Rectangle();
>         myRect.width = 40;
>         myRect.height = 50;
>         System.out.println("myRect's area is " + myRect.area());
>     }
> }
>
> ```
>
>   
>
> Exercise 2:
> Given the following class,
> called
> [`NumberHolder`](NumberHolder.java), write some code that creates an instance of the class,
> initializes its two member variables,
> and then displays the value of each member variable.
>
> ```
>
>
> public class NumberHolder {
>     public int anInt;
>     public float aFloat;
> }
>
> ```
>
>   
> Answer 2: See
> [`NumberHolderDisplay`](NumberHolderDisplay.java)
>
> ```
>
>
> public class NumberHolderDisplay {
>     public static void main(String[] args) {
> 	NumberHolder aNumberHolder = new NumberHolder();
> 	aNumberHolder.anInt = 1;
> 	aNumberHolder.aFloat = 2.3f;
> 	System.out.println(aNumberHolder.anInt);
> 	System.out.println(aNumberHolder.aFloat);
>     }
> }
>
> ```

[« Previous](../QandE/objects-questions.html)
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

**Previous page:** Questions and Exercises: Objects




A browser with JavaScript enabled is required for this page to operate properly.