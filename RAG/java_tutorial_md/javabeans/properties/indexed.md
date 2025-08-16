[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JavaBeans(TM)
  
**Lesson:** Properties

[Properties](index.html)

[Simple Properties](properties.html)

[Bound Properties](bound.html)

[Constrained Properties](constrained.html)

Indexed Properties

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Properties](index.html)

[« Previous](constrained.html) • [Trail](../TOC.html) • [Next »](../events/index.html)

# Indexed Properties

An indexed property is an array of properties or objects that supports a range of values and enables the accessor to specify
an element of a property to read or write.

*Indexed* properties are specified by the following methods:

```

	//Methods to access individual values
        public PropertyElement getPropertyName(int index)
	public void setPropertyName(int index, PropertyElement element)

```

and

```

	//Methods to access the entire indexed property array
        public PropertyElement[] getPropertyName()
	public void setPropertyName(PropertyElement element[])

```

Note that the distinction between the `get` and `set` methods for
indexed properties is subtle. The `get` method either has an
argument that is the array index of the property, or returns an array.
The `set` method either has two arguments,
namely an integer array index and the property element object that is being set,
or has the entire array as an argument.

## Creating an Indexed Property

To create an indexed property for your `MyBean` component, right-click the Bean
Patterns node and select Add|Indexed Property from the pop-up menu. Set up
Non-Index Options as shown in the following figure.

![Setting a Non-Indexed options for the property. ](../../figures/javabeans/new-indexed-properties.gif)

The code in the Source window will be changed automatically as follows:

```

import java.awt.Graphics;
import java.io.Serializable;
import javax.swing.JComponent;

/**
 * Bean with simple property 'title'.
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

    /**
     * Holds value of property lines.
     */
    private String[] lines;

    /**
     * Indexed getter for property lines.
     * @param index Index of the property.
     * @return Value of the property at index.
     */
    public String getLines(int index) {
        return this.lines[index];
    }

    /**
     * Getter for property lines.
     * @return Value of property lines.
     */
    public String[] getLines() {
        return this.lines;
    }

    /**
     * Indexed setter for property lines.
     * @param index Index of the property.
     * @param lines New value of the property at index.
     */
    public void setLines(int index, String lines) {
        this.lines[index] = lines;
    }

    /**
     * Setter for property lines.
     * @param lines New value of property lines.
     */
    public void setLines(String[] lines) {
        this.lines = lines;
    }
   }

```

Add the following code to the `MyBean.java` component to present the user with a
list of choices. You can provide and change these choices at design time. (Newly
added code is shown in bold.)

```

import java.awt.Graphics;
import java.io.Serializable;
import javax.swing.JComponent;

/**
 * Bean with a simple property "title"
 * and an indexed property "lines".
 */
public class MyBean
        extends JComponent
        implements Serializable
{
    private String title;
    private String[] lines = new String[10];

    public String getTitle()
    {
        return this.title;
    }

    public void setTitle( String title )
    {
        this.title = title;
    }

    public String[] getLines()
    {
        return this.lines.clone();
    }

    public String getLines( int index )
    {
        return this.lines[index];
    }

    public void setLines( String[] lines )
    {
        this.lines = lines;
    }

    public void setLines( int index, String line )
    {
        this.lines[index] = line;
    }

    protected void paintComponent( Graphics g )
    {
        g.setColor( getForeground() );

        int height = g.getFontMetrics().getHeight();
        paintString( g, this.title, height );

        if ( this.lines != null )
        {
            int step = height;
            for ( String line : this.lines )
                paintString( g, line, height += step );
        }
    }

    private void paintString( Graphics g, String str, int height )
    {
        if ( str != null )
            g.drawString( str, 0, height );
    }
}

```

The following figure represents the lines property in the Properties window.

![The indexed lines property is set to null. ](../../figures/javabeans/indexed-properties.png)

Notice that this property has a null value. To set up an alternative value,
press the "..." button. The form shown in the following figure enables you to
add ten items for the `lines` property list. First remove the default null items.
Then add custom items to the list by entering each item value into the Item
field and pressing the Add button each time.

![Creating a list of choices for the lines property. ](../../figures/javabeans/add-indexed-list.png)

[« Previous](constrained.html)
•
[Trail](../TOC.html)
•
[Next »](../events/index.html)

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

**Previous page:** Constrained Properties
  
**Next page:** Manipulating Events




A browser with JavaScript enabled is required for this page to operate properly.