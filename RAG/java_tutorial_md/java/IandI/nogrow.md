[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Interfaces and Inheritance
  
**Section:** Interfaces

[Interfaces and Inheritance](index.html)

[Interfaces](createinterface.html)

[Defining an Interface](interfaceDef.html)

[Implementing an Interface](usinginterface.html)

[Using an Interface as a Type](interfaceAsType.html)

Rewriting Interfaces

[Summary of Interfaces](summary-interface.html)

[Questions and Exercises](QandE/interfaces-questions.html)

[Inheritance](subclasses.html)

[Overriding and Hiding Methods](override.html)

[Polymorphism](polymorphism.html)

[Hiding Fields](hidevariables.html)

[Using the Keyword super](super.html)

[Object as a Superclass](objectclass.html)

[Writing Final Classes and Methods](final.html)

[Abstract Methods and Classes](abstract.html)

[Summary of Inheritance](summaryinherit.html)

[Questions and Exercises](QandE/inherit-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Interfaces and Inheritance](index.html)

[« Previous](interfaceAsType.html) • [Trail](../TOC.html) • [Next »](summary-interface.html)

# Rewriting Interfaces

Consider an interface that you have developed called `DoIt`:

```

public interface DoIt {
   void doSomething(int i, double x);
   int doSomethingElse(String s);
}

```

Suppose that, at a later time, you want to add a third method to `DoIt`,
so that the interface now becomes:

```

public interface DoIt {

   void doSomething(int i, double x);
   int doSomethingElse(String s);
   boolean didItWork(int i, double x, String s);
   
}

```

If you make this change, all classes that implement
the old `DoIt` interface will break because
they don't implement the interface anymore. Programmers relying
on this interface will protest loudly.

Try to anticipate all uses for your interface and to specify
it completely from the beginning. Given that this is often impossible,
you may need to create more interfaces later. For example, you could
create a `DoItPlus` interface that extends `DoIt`:

```

public interface DoItPlus extends DoIt {

   boolean didItWork(int i, double x, String s);
   
}

```

Now users of your code can choose to continue to use the old interface
or to upgrade to the new interface.

[« Previous](interfaceAsType.html)
•
[Trail](../TOC.html)
•
[Next »](summary-interface.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Using an Interface as a Type
  
**Next page:** Summary of Interfaces




A browser with JavaScript enabled is required for this page to operate properly.