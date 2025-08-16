[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JavaBeans(TM)
  
**Lesson:** Using the BeanContext API

[Using the BeanContext API](index.html)

[Overview of the BeanContext API](overview.html)

[Bean Context #1: Containment Only](containment.html)

[Bean Context #2: Containment and Services](services.html)

AWT Containers and the BeanContextProxy Interface

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Using the BeanContext API](index.html)

[« Previous](services.html) • [Trail](../TOC.html) • [Next »](../end.html)

# AWT Containers and the BeanContextProxy Interface

Sometimes, it is desirable for an AWT Container to act as a
BeanContext. However, AWT Containers cannot implement the BeanContext interface directly, because of a method
name collision between Component and Collection. If some AWT Component needs to act as a BeanContext, it must internally
create a BeanContext instance and delegate work to it. Third parties, such as visual builder tools, can discover
this BeanContext instance if the Component implements the
BeanContextProxy interface.

## The BeanContextProxy Interface

[`public BeanContextChild getBeanContextProxy()`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextProxy.html#getBeanContextProxy()) - Gets the
BeanContextChild (or subinterface) associated with this object.

[« Previous](services.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Bean Context #2: Containment and Services
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.