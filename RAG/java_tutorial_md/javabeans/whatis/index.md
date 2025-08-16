[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** JavaBeans(TM)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](../nb/index.html)

# Lesson: JavaBeans Concepts

The JavaBeans™ architecture is based on a component model which enables
developers to create software units called *components*.
Components are
self-contained, reusable software units that can be visually assembled into
composite components, applets, applications, and servlets using visual
application builder tools. JavaBean components are known as
*beans*.

A set of APIs describes a component model for a particular language. The
JavaBeans API
[`specification`](http://download.oracle.com/javase/7/docs/api/java/beans/package-summary.html
)describes the core detailed elaboration for the JavaBeans
component architecture.

Beans are dynamic in that they can be changed or customized. Through the design
mode of a builder tool you can use the Properties window of the bean to
customize the bean and then save (persist) your beans using visual
manipulation. You can select a bean from the toolbox, drop it into a form,
modify its appearance and behavior, define its interaction with other beans, and
combine it and other beans into an applet, application, or a new bean.

The following list briefly describes key bean concepts.

* Builder tools discover a bean's features (that is, its properties,
  methods, and events) by a process known as
  *introspection*.
  Beans support introspection in two ways:

  + By adhering to specific rules,
    known as *design patterns*, when
    naming bean features. The
    [`Introspector`](http://download.oracle.com/javase/7/docs/api/java/beans/Introspector.html
    )
    class examines beans for
    these design patterns to discover bean features.
    The `Introspector` class relies on the
    *core reflection* API. The trail
    [Getting Started](../../reflect
    /index.html
    ) is an excellent place to learn about reflection.
  + By explicitly providing property, method, and event information with
    a related *bean
    information* class. A bean information
    class implements the `BeanInfo`
    interface. A `BeanInfo` class
    explicitly lists those bean features that
    are to be exposed to application builder tools.* *Properties* are the appearance and behavior characteristics of a bean that can
    be changed at design time. Builder tools introspect on a bean to discover its
    properties and expose those properties for manipulation.
  * Beans expose properties so they can be customized
    at design time.
    *Customization* is supported in two ways: by using property editors, or by using
    more sophisticated bean customizers.
  * Beans use *events* to communicate with other beans. A bean that is to
    receive events (a listener bean) registers with the bean that fires the event (a
    source bean). Builder tools can examine a bean and determine which events that
    bean can fire (send) and which it can handle (receive).
  * *Persistence* enables beans to save and restore their state. After changing
    a bean's properties, you can save the state of the bean and restore that bean at
    a later time with the property changes intact. The JavaBeans architecture uses
    Java Object Serialization to support persistence.
  * A bean's *methods* are no different from Java methods, and can be called
    from other beans or a scripting environment. By default all public methods are
    exported.

Beans vary in functionality and purpose. You have probably met some of the
following beans in your programming practice:

* GUI (graphical user interface)
* Non-visual beans, such as a spelling checker
* Animation applet
* Spreadsheet application

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](../nb/index.html)

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

**Previous page:** Table of Contents
  
**Next page:** Using the NetBeans GUI Builder




A browser with JavaScript enabled is required for this page to operate properly.