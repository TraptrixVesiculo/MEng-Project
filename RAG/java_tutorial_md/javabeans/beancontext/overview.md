[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JavaBeans(TM)
  
**Lesson:** Using the BeanContext API

[Using the BeanContext API](index.html)

Overview of the BeanContext API

[Bean Context #1: Containment Only](containment.html)

[Bean Context #2: Containment and Services](services.html)

[AWT Containers and the BeanContextProxy Interface](gui.html)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Using the BeanContext API](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](containment.html)

# Overview of the BeanContext API

The Extensible Runtime Containment and Services Protocol supports
extensible mechanisms that:

* *Introduce an abstraction for the environment, or context, in which a JavaBean logically functions during
  its life-cycle, that is a hierarchy of JavaBeans** *Enable the dynamic addition of arbitrary services to a JavaBean's environment** *Provide a single service discovery mechanism through which JavaBeans may interrogate their environment in
      order both to ascertain the availability of particular services and to subsequently employ those services.** *Provide better support for JavaBeans that are also Applets.*

In English, this means that there now exists a standard mechanism
through which Java developers can logically group a set of related
JavaBeans into a "context" that the beans can become aware of and/or
interact with. This context, or "containing environment", is
known as the
`BeanContext`.

There are two distinct types of `BeanContext` included in this
protocol: one which supports membership only (interface
[`java.beans.beancontext.BeanContext`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContext.html)) and
one which supports membership and offers services
(interface
[`java.beans.beancontext.BeanContextServices`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServices.html)) to its JavaBeans nested within.

To orient yourself with the classes and interfaces of
`java.beans.beancontext`, take a minute to look over the following
hierarchy diagram. You will notice that the majority of the package
is defined as interfaces, which allow for multiple
inheritance.

## Inheritance Diagram of the BeanContext API

The classes and interfaces relevant to the `BeanContext`
API are listed in the following diagrams.
As you study the diagrams, take note of the
`BeanContext` and `BeanContextServices`
interfaces, and that
each has its own concrete implementation
that you can subclass or instantiate directly
(classes
[`java.beans.beancontext.BeanContextSupport`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html) and
[`java.beans.beancontext.BeanContextServicesSupport`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html) respectively). Also take note of the location of the
[`java.beans.beancontext.BeanContextChild`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextChild.html) interface. This is the interface that allows nested JavaBeans
to become aware of their enclosing `BeanContext`.

![Diagram showing the bean support classes](../../figures/javabeans/support.gif)

![Diagram showing the bean interfaces.](../../figures/javabeans/interfaces.gif)

![Diagram showing the bean event classes.](../../figures/javabeans/events.gif)

![Diagram showing the bean listener classes.](../../figures/javabeans/listeners.gif)

![Diagram showing the bean proxy interfaces.](../../figures/javabeans/proxy_interfaces.gif)

![Diagram showing the BeanInfo interfaces.](../../figures/javabeans/beaninfo.gif)

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](containment.html)

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

**Previous page:** Using the BeanContext API
  
**Next page:** Bean Context #1: Containment Only




A browser with JavaScript enabled is required for this page to operate properly.