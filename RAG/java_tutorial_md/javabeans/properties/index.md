[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Properties

[Simple Properties](properties.html)

[Bound Properties](bound.html)

[Constrained Properties](constrained.html)

[Indexed Properties](indexed.html)

**Trail:** JavaBeans(TM)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)

[« Previous](../writingbean/index.html) • [Trail](../TOC.html) • [Next »](properties.html)

# Lesson: Properties

In the following sections you will learn how to implement
bean properties. A bean *property* is a named attribute of a bean
that can affect its behavior or appearance. Examples of bean properties include color,
label, font, font size, and display size.

The JavaBeans™ specification defines the following types of bean properties:

* [Simple](properties.html) – A bean property with a single value whose changes are independent
  of changes in any other property.

  * [Indexed](indexed.html) – A bean property that supports a range of values instead of a
    single value.

    * [Bound](bound.html) – A bean property for which a change to the property results in a
      notification being sent to some other bean.

      * [Constrained](constrained.html) – A bean property for which a change to the property results
        in validation by another bean. The other bean may reject the change if it is not
        appropriate.

Bean properties can also be classified as follows:

* Writable – A bean property that can be changed
  + Standard+ Expert+ Preferred* Read Only – A bean property that cannot be changed.* Hidden – A bean property that can be changed. However, these
      properties are not disclosed with the `BeanInfo` class

BeanBuilder uses this schema to group and represent properties in the Properties
window.

[« Previous](../writingbean/index.html)
•
[Trail](../TOC.html)
•
[Next »](properties.html)

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
  
**Next page:** Simple Properties




A browser with JavaScript enabled is required for this page to operate properly.