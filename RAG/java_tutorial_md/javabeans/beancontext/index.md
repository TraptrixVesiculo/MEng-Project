[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Using the BeanContext API

[Overview of the BeanContext API](overview.html)

[Bean Context #1: Containment Only](containment.html)

[Bean Context #2: Containment and Services](services.html)

[AWT Containers and the BeanContextProxy Interface](gui.html)

**Trail:** JavaBeans(TM)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)

[« Previous](../customization/index.html) • [Trail](../TOC.html) • [Next »](overview.html)

# Lesson: Using the BeanContext API

As stated in the specification, the purpose of the Extensible Runtime
Containment and Services Protocol is
*"to introduce the concept of a relationship between a Component
and its environment, or Container, wherein
a newly instantiated Component is provided with a reference to its Container or Embedding Context. The Container,
or Embedding Context not only establishes the hierarchy or logical structure, but it also acts as a service provider
that Components may interrogate in order to determine, and subsequently employ, the services provided by their
Context."*

## [Overview of the BeanContext API](../beancontext/overview.html)

This section introduces extensible mechanisms and represents inheritance
diagram of the BeanContext API.

## [Bean Context #1: Containment Only](../beancontext/containment.html)

This section teaches how to use the `BeanContextSupport` class
to provide the basic BeanContext functionality.

## [Bean Context #2: Containment and Services](../beancontext/services.html)

This section teaches how to use service capability defined by the
`BeanContextServices` interface.

## [AWT Containers and the BeanContextProxy Interface](../beancontext/gui.html)

This section describes how an AWT `Container`
can act as a `BeanContext`.

## Additional Resources

* The Extensible Runtime Containment and Services Protocol
  [Specification](http://java.sun.com/beans/glasgow/)* The `java.beans.beancontext`
    [API documentation](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/package-summary.html)

[« Previous](../customization/index.html)
•
[Trail](../TOC.html)
•
[Next »](overview.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Overview of the BeanContext API




A browser with JavaScript enabled is required for this page to operate properly.