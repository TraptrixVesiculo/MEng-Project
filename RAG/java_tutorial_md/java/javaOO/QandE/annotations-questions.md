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

[Questions and Exercises](../QandE/creating-questions.html)

[Questions and Exercises](../QandE/objects-questions.html)

[Nested Classes](../nested.html)

[Inner Class Example](../innerclasses.html)

[Summary of Nested Classes](../summarynested.html)

[Questions and Exercises](../QandE/nested-questions.html)

[Enum Types](../enum.html)

[Questions and Exercises](../QandE/enum-questions.html)

[Annotations](../annotations.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Classes and Objects](../index.html)

[« Previous](../annotations.html) • [Trail](../../TOC.html) • [Next »](../../IandI/index.html)

# Questions and Exercises: Annotations

### Questions

> 1. What is wrong with the following interface?
>
> ```
>
> public interface House {
>     @Deprecated
>     void open();
>     void openFrontDoor();
>     void openBackDoor();
> }
>
> ```
>
> 2. Consider this implementation of the `House` interface,
> shown in Question 1.
>
> ```
>
> public class MyHouse implements House {
>     public void open() {}
>     public void openFrontDoor() {}
>     public void openBackDoor() {}
> }
>
> ```
>
> If you compile this program, the compiler complains that `open`
> has been deprecated (in the interface). What can you do to get rid of that
> warning?

  

[Check your answers.](annotations-answers.html)

[« Previous](../annotations.html)
•
[Trail](../../TOC.html)
•
[Next »](../../IandI/index.html)

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

**Previous page:** Annotations
  
**Next page:** Interfaces and Inheritance




A browser with JavaScript enabled is required for this page to operate properly.