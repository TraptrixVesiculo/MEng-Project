[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** JavaBeans(TM)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)

[« Previous](../introspection/index.html) • [Trail](../TOC.html) • [Next »](../beancontext/index.html)

# Lesson: Bean Customization

*Customization* provides a means for modifying the appearance and
behavior of a bean within an application builder so it meets your
specific needs. There are several levels of customization available for a
bean developer to allow other developers to get maximum
benefit from a bean's potential functionality.

---

The following links are useful for learning about property
editors and customizers:

* [`PropertyEditor`](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyEditor.html) interface
* [`PropertyEditorSupport`](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyEditorSupport.html) class
* [`PropertyEditorManager`](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyEditorManager.html) class
* [`Customizer`](http://download.oracle.com/javase/7/docs/api/java/beans/Customizer.html) interface
* [`BeanInfo`](http://download.oracle.com/javase/7/docs/api/java/beans/BeanInfo.html) interface

---

A bean's appearance and behavior can be customized at
design time within beans-compliant builder tools.
There are two ways to customize a bean:

* By using a *property editor*.
  Each bean property has its own property editor.
  The NetBeans GUI Builder usually displays a bean's property
  editors in the Properties window.
  The property editor that is associated with a particular
  property type edits that property type.
* By using *customizers*.
  Customizers give you complete GUI control over bean
  customization. Customizers are used where property
  editors are not practical or applicable.
  Unlike a property editor, which is associated with a property,
  a customizer is associated with a bean.

## Property Editors

A property editor is a tool for customizing a particular
property type. Property editors are activated in the Properties window. This window determines
a property's type, searches for a relevant
property editor, and displays the property's current
value in a relevant way.

Property editors must implement the `PropertyEditor`
interface, which provides methods to specify
how a property should be displayed in a property sheet. The following figure
represents the Properties window containing
`myBean1` properties:

![This figure represents myBean1 properties in the Property window](../../figures/javabeans/customization.gif)

You begin the process of editing these properties
by clicking the property entry.
Clicking most of these entries will bring up separate panels.
For example, to set up the `foreground` or `background`
use selection boxes with choices of colors, or press the "..." button
to work with a standard ColorEditor window. Clicking on the `toolTipText`
property opens
a StringEditor window.

The support class `PropertyEditorSupport`
provides a default implementation of the
`PropertyEditor` interface. By subclassing
your property editor from `PropertyEditorSupport`,
you can simply override the methods you need.

To display the current property value "sample" within
the Properties window, you need to override `isPaintable`
to return `true`. You then must override `paintValue`
to paint the current property value in a rectangle in the property sheet.
Here's how `ColorEditor` implements
`paintValue`:

```

public void paintValue(java.awt.Graphics gfx, java.awt.Rectangle box) {
    Color oldColor = gfx.getColor();
    gfx.setColor(Color.black);
    gfx.drawRect(box.x, box.y, box.width-3, box.height-3);
    gfx.setColor(color);
    gfx.fillRect(box.x+1, box.y+1, box.width-4, box.height-4);
    gfx.setColor(oldColor);
}

```

To support the custom property editor, override
two more methods. Override `supportsCustomEditor` to
return true, and then override `getCustomEditor` to
return a custom editor instance.
`ColorEditor.getCustomEditor` returns `this`.

In addition, the `PropertyEditorSupport`
class maintains a `PropertyChangeListener`
list, and fires property change event notifications
to those listeners when a bound property is changed.

## How Property Editors are Associated with Properties

Property editors are discovered and associated
with a given property in the following ways:

* Explicit association by way of a
  `BeanInfo` object.
  The editor of the title's property is set with the following
  line of code:

  ```

  pd.setPropertyEditorClass(TitleEditor.class);

  ```

  * Explicit registration by way of the
    `java.beans.PropertyEditorManager.registerEditor` method.
    This method takes two arguments: the bean class type, and
    the editor class to be associated with that type.

    * Name search. If a class has no explicitly associated property
      editor, then the `PropertyEditorManager`
      searchs for that class's property editor in the following ways:
      + Appending "Editor" to the fully qualified class name.
        For example, for the `my.package.ComplexNumber` class,
        the property editor manager would search for the
        `my.package.ComplexNumberEditor` class.+ Appending "Editor" to the class name and searching
          a class path.

## Customizers

You have learned that builder tools provide support for you to create your
own property editors. What other needs should visual builders meet for complex,
industrial-strength beans? Often it is undesirable to have all the properties of
a bean revealed on a single (sometimes huge) property sheet. What if one single
root choice about the type of the bean rendered half the properties irrelevant?
The JavaBeans specification provides for user-defined customizers, through which
you can define a higher level of customization for bean properties than is
available with property editors.

When you use a bean *Customizer*, you have complete control over how to
configure or edit a bean. A Customizer is an application that specifically
targets a bean's customization. Sometimes properties are insufficient for
representing a bean's configurable attributes. Customizers are used where
sophisticated instructions would be needed to change a bean, and where property
editors are too primitive to achieve bean customization.

All customizers must:

* Extend `java.awt.Component` or one of
  its subclasses.
* Implement the `java.beans.Customizer` interface
  This means implementing methods to register `PropertyChangeListener` objects, and
  firing property change events at those listeners when
  a change to the target bean has occurred.
* Implement a default constructor.
* Associate the customizer with its target class
  via `BeanInfo.getBeanDescriptor`.

[« Previous](../introspection/index.html)
•
[Trail](../TOC.html)
•
[Next »](../beancontext/index.html)

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
  
**Next page:** Using the BeanContext API




A browser with JavaScript enabled is required for this page to operate properly.