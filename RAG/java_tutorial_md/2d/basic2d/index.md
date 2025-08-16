[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** 2D Graphics

[Home Page](../../index.html)
>
[2D Graphics](../index.html)

[« Previous](../overview/index.html) • [Trail](../TOC.html) • [Next »](../geometry/index.html)

# Lesson: Getting Started with Graphics

The Java 2D™ API is powerful and complex. However, the vast
majority of uses for the Java 2D API utilize a small subset of its capabilities
encapsulated in the `java.awt.Graphics` class. This lesson covers the most common
needs of applications developers. Less common needs are described later
in the [Advanced topics in the Java 2D API](../advanced/index.html) lesson.

Most methods of the
[`Graphics`](http://download.oracle.com/javase/7/docs/api/java/awt/Graphics.html) class can be divided into two basic groups:

* Draw and fill methods, enabling you to render basic shapes, text, and images
* Attributes setting methods, which affect how that drawing and filling appears

Methods such as `setFont` and `setColor` define how draw and fill methods render.

This figure illustrates how these methods relate to graphic objects:

![This figure represents basic methods of the Graphics class ](../../figures/2d/graphicMethods.gif)

Drawing methods include:

* `drawString` – For drawing text

```

   g.drawString("Hello", 10, 10);

```

* `drawImage` – For drawing images

```

   g.drawImage(img, 
                    0, 0, width, height,
                    0, 0, imageWidth, imageHeight,
                    null);                    


```

* `drawLine`, `drawArc`, `drawRect`,
  `drawOval`, `drawPolygon` – For drawing geometric shapes

```

g2.draw(new Line2D.Double(0, 0, 30, 40));

```

Depending on your current need, you can choose one of several methods in the `Graphics`
class based on the following criteria:

* Whether you want to render the image at the specified location in its original size or
  scale it to fit inside the given rectangle
* Whether you prefer to fill the transparent areas of the image with color or keep
  them transparent

Fill methods apply to geometric shapes and include `fillArc`, `fillRect`,
`fillOval`, `fillPolygon`.

Whether you draw a line of text or an image, remember that
in 2D graphics every point is determined by its x and y [coordinates](../overview/coordinate.html). All of the draw and fill methods need this information which determines
where the text or image should be rendered.

For example, to draw a line, an application calls the following:

`java.awt.Graphics.drawLine(int x1, int y1, int x2, int y2)`

In this code *(x1, y1)* is the start point of the line, and
*(x2, y2)* is the end point of the line.

So the code to draw a horizontal line is as follows:

`Graphics.drawLine(20, 100, 120, 100);` 

The demo below accumulates all mentioned techniques.
Move the slider to display various weather
types.

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

The `WeatherWizard` demo uses the `JSlider` component
as well as various graphics capabilities to generate and display a specified weather type.
For more information about the `JSlider` class see the
[How to Use Sliders](../../uiswing/components/slider.html) section of the Swing Tutorial.

The `paint` method of the `WeatherPainter` class
implements graphics features. The following code draws an image determined by using
the `setupWeatherReport()` method.

```

        ...
        origComposite = g2.getComposite();
        if (alpha0 != null) g2.setComposite(alpha0);
        g2.drawImage(img0,
                0, 0, size.width, size.height,
                0, 0, img0.getWidth(null), img0.getHeight(null),
                null);
        if (img1 != null) {
            if (alpha1 != null) g2.setComposite(alpha1);
            g2.drawImage(img1,
                    0, 0, size.width, size.height,
                    0, 0, img1.getWidth(null), img1.getHeight(null),
                    null);
        } 
        ...

```

The `setFont` and `drawString` methods
render the temperature and the weather condition.

```

        ...
        // Freezing, Cold, Cool, Warm, Hot,
        // Blue, Green, Yellow, Orange, Red
        Font font = new Font("Serif", Font.PLAIN, 36);
        g.setFont(font);
        
        String tempString = feels + " " + temperature+"F";
        FontRenderContext frc = ((Graphics2D)g).getFontRenderContext();
        ...
        g.setColor(textColor);
        int xTextTemp = rX-(int)boundsTemp.getX();
        int yTextTemp = rY-(int)boundsTemp.getY();
        g.drawString(tempString, xTextTemp, yTextTemp);
        
        int xTextCond = rX-(int)boundsCond.getX();
        int yTextCond = rY-(int)boundsCond.getY() + (int)boundsTemp.getHeight();
        g.drawString(condStr, xTextCond, yTextCond);
	

```

The `fillRect` method allows you to draw a rectangle filled with the specified color.

```

        ...
        Rectangle2D boundsTemp = font.getStringBounds(tempString, frc);
        Rectangle2D boundsCond = font.getStringBounds(condStr, frc);
        int wText = Math.max((int)boundsTemp.getWidth(), (int)boundsCond.getWidth());
        int hText = (int)boundsTemp.getHeight() + (int)boundsCond.getHeight();
        int rX = (size.width-wText)/2;
        int rY = (size.height-hText)/2;
        
        g.setColor(Color.LIGHT_GRAY);
        g2.fillRect(rX, rY, wText, hText);
	...

```

Try to modify the `WeatherWizard` demo to alter the graphical content.
For example, use the `fillRoundRect` method instead of `fillRect` or apply
another font size in the `setFont` method.
Find the complete code for this applet in the
[`WeatherWizard.java`](examples/WeatherWizard.java) file. The demo also requires the following images:
[`weather-cloud.png`](examples/images/weather-cloud.png),
[`weather-rain.png`](examples/images/weather-rain.png),
[`weather-snow.png`](examples/images/weather-snow.png), and
[`weather-sun.png`](examples/images/weather-sun.png) located in the `images` directory.

[« Previous](../overview/index.html)
•
[Trail](../TOC.html)
•
[Next »](../geometry/index.html)

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
  
**Next page:** Working with Geometry




A browser with JavaScript enabled is required for this page to operate properly.