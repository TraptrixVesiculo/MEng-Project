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

Constrained Properties

[Indexed Properties](indexed.html)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Properties](index.html)

[« Previous](bound.html) • [Trail](../TOC.html) • [Next »](indexed.html)

# Constrained Properties

A bean property is *constrained* if the
bean supports the
[`VetoableChangeListener`](http://download.oracle.com/javase/7/docs/api/java/beans/VetoableChangeListener.html)(in the API reference documentation) and
[`PropertyChangeEvent`](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyChangeEvent.html)(in the API reference documentation) classes, and if the set method for this property throws a
[`PropertyVetoException`](http://download.oracle.com/javase/7/docs/api/java/beans/PropertyVetoException.html)(in the API reference documentation).

Constrained properties are more complicated than bound properties because they
also support property change listeners which happen to be *vetoers*.

The following operations in the `setXXX` method for the
constrained property must be implemented in this order:

1. Save the old value in case the change is vetoed.
2. Notify listeners of the new proposed value, allowing them to veto the
   change.
3. If no listener vetoes the change (no exception is thrown), set the
   property to the new value.

The accessor methods for a constrained property are defined in the same way as
those for simple properties, with the addition that the
`setXXX` method throws a `PropertyVetoException`
exception. The syntax is as follows:

```

	public void setPropertyName(PropertyType pt)
	throws PropertyVetoException {code}

```

## Handling Vetoes

If a registered listener vetoes a proposed property change by throwing a
`PropertyVetoException` exception, the source bean with the constrained
property is responsible for the following actions:

* Catching exceptions.
* Reverting to the old value for the property.
* Issuing a new `VetoableChangeListener.vetoableChange` call to all listeners
  to report the reversion.

The `VetoableChangeListener` class throws a `PropertyVetoException`
and handles the `PropertyChangeEvent` event fired by the bean with the
constrained property.

The `VetoableChangeSupport` provides the following operations:

* Keeping track of `VetoableChangeListener` objects.
* Issuing the `vetoableChange` method on all registered listeners.
* Catching any vetoes (exceptions) thrown by listeners.
* Informing all listeners of a veto by calling `vetoableChange` again, but
  with the old property value as the proposed "new" value.

## Creating a Constrained Property

To create a constrained property, set
the appropriate option in the New Property Pattern form as shown on the
following figure.

![Setting a constrained option for the radius property. ](../../figures/javabeans/constrained-property.gif)

Note that the Multicast Source Event Pattern - vetoableChangeListener was added
to the Bean Patterns hierarchy.

You can also modify the existing code generated in the previous lesson to make
the `title` and `lines` properties constrained as follows (where newly added code is
shown in bold):

```

import java.io.Serializable;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.beans.PropertyVetoException;
import java.beans.VetoableChangeListener;
import java.beans.VetoableChangeSupport;
import java.awt.Graphics;
import javax.swing.JComponent;

/**
 * Bean with constrained properties.
 */
public class MyBean
        extends JComponent
        implements Serializable
{
    private String title;
    private String[] lines = new String[10];

    private final PropertyChangeSupport pcs = new PropertyChangeSupport( this );
    private final VetoableChangeSupport vcs = new VetoableChangeSupport( this );

    public String getTitle()
    {
        return this.title;
    }
/**
 * This method was modified to throw the PropertyVetoException
 * if some vetoable listeners reject the new title value
 */
    public void setTitle( String title )
            throws PropertyVetoException
    {
        String old = this.title;
        this.vcs.fireVetoableChange( "title", old, title );
        this.title = title;
        this.pcs.firePropertyChange( "title", old, title );
    }

    public String[] getLines()
    {
        return this.lines.clone();
    }

    public String getLines( int index )
    {
        return this.lines[index];
    }
/**
 * This method throws the PropertyVetoException
 * if some vetoable listeners reject the new lines value
 */
    public void setLines( String[] lines )
            throws PropertyVetoException
    {
        String[] old = this.lines;
        this.vcs.fireVetoableChange( "lines", old, lines );
        this.lines = lines;
        this.pcs.firePropertyChange( "lines", old, lines );
    }

    public void setLines( int index, String line )
            throws PropertyVetoException
    {
        String old = this.lines[index];
        this.vcs.fireVetoableChange( "lines", old, line );
        this.lines[index] = line;
        this.pcs.fireIndexedPropertyChange( "lines", index, old, line );
    }

    public void addPropertyChangeListener( PropertyChangeListener listener )
    {
        this.pcs.addPropertyChangeListener( listener );
    }

    public void removePropertyChangeListener( PropertyChangeListener listener )
    {
        this.pcs.removePropertyChangeListener( listener );
    }
/**
 * Registration of the VetoableChangeListener
 */
    public void addVetoableChangeListener( VetoableChangeListener listener )
    {
        this.vcs.addVetoableChangeListener( listener );
    }

    public void removeVetoableChangeListener( VetoableChangeListener listener )
    {
        this.vcs.removeVetoableChangeListener( listener );
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

[« Previous](bound.html)
•
[Trail](../TOC.html)
•
[Next »](indexed.html)

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

**Previous page:** Bound Properties
  
**Next page:** Indexed Properties




A browser with JavaScript enabled is required for this page to operate properly.