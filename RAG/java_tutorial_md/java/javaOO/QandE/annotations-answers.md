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

[« Previous](../QandE/annotations-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Annotations

### Questions

> Question 1: What is wrong with the following interface:
>
> ```
>
> public interface House {
>     @Deprecated
>     public void open();
>     public void openFrontDoor();
>     public void openBackDoor();
> }
>
> ```
>
> Answer 1:The documentation should reflect why
> `open` is deprecated and what to use instead. For example:
>
> ```
>
> public interface House { 
>     /**
>      * @deprecated use of open is discouraged, use
>      * openFrontDoor or openBackDoor instead.
>      */
>     @Deprecated
>     public void open(); 
>     public void openFrontDoor();
>     public void openBackDoor();
> }
>
> ```
>
> Question 2: Consider this implementation of the
> `House` interface, shown in Question 1.
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
>
> Answer 2: You can deprecate the implementation of
> `open`:
>
> ```
>
> public class MyHouse implements House { 
>     //The documentation is inherited from the interface.
>     @Deprecated
>     public void open() {} 
>     public void openFrontDoor() {}
>     public void openBackDoor() {}
> }
>
> ```
>
> Alternatively, you can suppress the warning:
>
> ```
>
> public class MyHouse implements House { 
>     @SuppressWarnings("deprecation")
>     public void open() {} 
>     public void openFrontDoor() {}
>     public void openBackDoor() {}
> }
>
> ```

[« Previous](../QandE/annotations-questions.html)
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

**Previous page:** Questions and Exercises: Annotations




A browser with JavaScript enabled is required for this page to operate properly.