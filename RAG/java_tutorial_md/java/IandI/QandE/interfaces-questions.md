[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance

[Interfaces and Inheritance](../index.html)

[Interfaces](../createinterface.html)

[Defining an Interface](../interfaceDef.html)

[Implementing an Interface](../usinginterface.html)

[Using an Interface as a Type](../interfaceAsType.html)

[Rewriting Interfaces](../nogrow.html)

[Summary of Interfaces](../summary-interface.html)

Questions and Exercises

[Inheritance](../subclasses.html)

[Overriding and Hiding Methods](../override.html)

[Polymorphism](../polymorphism.html)

[Hiding Fields](../hidevariables.html)

[Using the Keyword super](../super.html)

[Object as a Superclass](../objectclass.html)

[Writing Final Classes and Methods](../final.html)

[Abstract Methods and Classes](../abstract.html)

[Summary of Inheritance](../summaryinherit.html)

[Questions and Exercises](../QandE/inherit-questions.html)

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Interfaces and Inheritance](../index.html)

[« Previous](../summary-interface.html) • [Trail](../../TOC.html) • [Next »](../subclasses.html)

# Questions and Exercises: Interfaces

### Questions

1. What methods would a class that implements
   the `java.lang.CharSequence` interface have to implement?

   - What is wrong with the following interface?

     ```

     public interface SomethingIsWrong {
         void aMethod(int aValue){
             System.out.println("Hi Mom");
         }
     }

     ```

     - Fix the interface in question 2.

       - Is the following interface valid?

         ```

         public interface Marker {
         }

         ```

### Exercises

1. Write a class that implements the `CharSequence`
   interface found in the `java.lang` package.
   Your implementation should return the string backwards.
   Select one of the sentences from this book to use as the data.
   Write a small `main` method to test your class;
   make sure to call all four methods.

   - Suppose you have written a time server that periodically
     notifies its clients of the current date and time. Write an interface
     the server could use to enforce a particular protocol on
     its clients.

[Check your answers.](interfaces-answers.html)

[« Previous](../summary-interface.html)
•
[Trail](../../TOC.html)
•
[Next »](../subclasses.html)

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

**Previous page:** Summary of Interfaces
  
**Next page:** Inheritance




A browser with JavaScript enabled is required for this page to operate properly.