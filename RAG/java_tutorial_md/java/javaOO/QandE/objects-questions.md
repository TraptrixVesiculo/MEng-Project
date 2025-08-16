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

Questions and Exercises

[Nested Classes](../nested.html)

[Inner Class Example](../innerclasses.html)

[Summary of Nested Classes](../summarynested.html)

[Questions and Exercises](../QandE/nested-questions.html)

[Enum Types](../enum.html)

[Questions and Exercises](../QandE/enum-questions.html)

[Annotations](../annotations.html)

[Questions and Exercises](../QandE/annotations-questions.html)

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Classes and Objects](../index.html)

[« Previous](../QandE/creating-questions.html) • [Trail](../../TOC.html) • [Next »](../nested.html)

# Questions and Exercises: Objects

### Questions

> 1. What's wrong with the following program?
>
>    ```
>
>    public class SomethingIsWrong {
>        public static void main(String[] args) {
>            Rectangle myRect;
>            myRect.width = 40;
>            myRect.height = 50;
>            System.out.println("myRect's area is " + myRect.area());
>        }
>    }
>
>    ```
>
>    - The following code creates one array and one
>      string object.
>      How many references to those objects exist after the code executes?
>      Is either object eligible for garbage collection?
>
>      ```
>
>      ...
>      String[] students = new String[10];
>      String studentName = "Peter Parker";
>      students[0] = studentName;
>      studentName = null;
>      ...
>
>      ```
>
>      - How does a program destroy an object that it creates?

### Exercises

> 1. Fix the program called `SomethingIsWrong` shown in Question 1.
>      
>    - Given the following class,
>      called
>      [`NumberHolder`](NumberHolder.java), write some code that creates an instance of the class,
>      initializes its two member variables,
>      and then displays the value of each member variable.
>
>      ```
>
>      public class NumberHolder {
>         public int anInt;
>         public float aFloat;
>      }
>
>      ```

[Check your answers.](objects-answers.html)

[« Previous](../QandE/creating-questions.html)
•
[Trail](../../TOC.html)
•
[Next »](../nested.html)

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
  
**Next page:** Nested Classes




A browser with JavaScript enabled is required for this page to operate properly.