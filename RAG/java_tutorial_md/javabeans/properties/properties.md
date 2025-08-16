[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JavaBeans(TM)
  
**Lesson:** Properties

[Properties](index.html)

Simple Properties

[Bound Properties](bound.html)

[Constrained Properties](constrained.html)

[Indexed Properties](indexed.html)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Properties](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](bound.html)

# Simple Properties

To add simple properties to a bean, add appropriate `getXXX` and
`setXXX` methods (or `isXXX`
and `setXXX` methods for a boolean
property).

The names of these methods follow specific rules
called *design patterns*.
These design pattern-based method names allow builder tools such as the NetBeans GUI Builder, to provide the
following features:

* Discover a bean's properties* Determine the properties' read/write attributes* Determine the properties' types* Locate the appropriate property editor for each property type* Display the properties (usually in the Properties window)* Alter the properties (at design time)

## Adding a Title Property

In previous lessons you learned how to create a simple property by using the
[NetBeans GUI Builder](../nb/index.html).
The following procedure shows how to create a
simple property in detail:

1. Right-click on the Bean Patterns node in the `MyBean`
   class hierarchy.- Select Add|Property from the pop-up menu.- Fill out the New Property Pattern form as shown in the following figure
       and click OK.

       ![Creating a simple property with the title name. ](../../figures/javabeans/newsimple.png)

       - The following code is automatically generated:

         ```

         public class MyBean {
             
             /** Creates a new instance of MyBean */
             public MyBean() {
             }

             /**
              * Holds value of property title.
              */
             private String title;

             /**
              * Getter for property title.
              * @return Value of property title.
              */
             public String getTitle() {
                 return this.title;
             }

             /**
              * Setter for property title.
              * @param title New value of property title.
              */
             public void setTitle(String title) {
                 this.title = title;
             }
             
         }

         ```

         - Now make your bean visual by extending the `JComponent` class and
           implement the `Serializable` interface. Then, add the
           `paintComponent` method to represent your bean.

           ```

           import java.awt.Graphics;
           import java.io.Serializable;
           import javax.swing.JComponent;

           /**
            * Bean with a simple property "title".
            */
           public class MyBean
                   extends JComponent
                   implements Serializable
           {
               private String title;

               public String getTitle()
               {
                   return this.title;
               }

               public void setTitle( String title )
               {
                   this.title = title;
               }

               protected void paintComponent( Graphics g )
               {
                   g.setColor( getForeground() );

                   int height = g.getFontMetrics().getHeight();
                   if ( this.title != null )
                       g.drawString(this.title, 0, height );
                  }
              }

           ```

## Inspecting Properties

Select the MyBean component in the Other Components node in the Inspector
window. Now you can analyze the title property in the Properties window and
change it. To change the title property press the "..." button and enter any
string you wish.

The following figure represents the title property set to the "The title"
value.

![the title property was set to the title. ](../../figures/javabeans/simple-properties.png)

The NetBeans GUI Builder enables you to restrict the changing of a property
value. To restrict the changing of the title property, right-click the title
property in the Bean Patterns node of the MyBean project. Select Properties from
the pop-up menu and the Properties window appears. Choose one of the following
property access types from the Mode combo box:

* Read/Write
* Read only
* Write only

The Read only property has only the `get` method only,
while the Write only property has only the `set` method only.
The Read/Write type property has both of these methods.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](bound.html)

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

**Previous page:** Properties
  
**Next page:** Bound Properties




A browser with JavaScript enabled is required for this page to operate properly.