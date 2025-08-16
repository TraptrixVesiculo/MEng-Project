[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../TOC.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Questions and Exercises: Performing Custom Painting

### Questions

> 1. What method defined by `JComponent` paints the
> inside of a component?
>
> 2. Which of the following code snippets paint a rectangle
> (filled or not) that is 100x100 pixels?
>
> > a. `g.fillRect(x, y, 100, 100)`  
> > b. `g.fillRect(x, y, 99, 99)`  
> > c. `g.drawRect(x, y, 100, 100)`  
> > d. b and c  
> > e. a and c
>
> 3. What code would you use to make a component perform the
> next painting operation using the background color at 50% transparency?

### Exercises

> 1. Using a standard border and custom component painting,
> implement a component that has a preferred size of 250x100, is
> opaque by default, has a 5-pixel black border, and paints an
> “X” (using 5-pixel-thick lines) in the foreground color,
> as shown in the following figure.
>
> > ![ComponentDisplayer-1.png](../../figures/uiswing/QandE/ComponentDisplayer-1.png)
>
> 2. Implement an icon that’s 10x10 pixels and paints a
> solid rectangle that fills the 10x10 area. If the icon’s
> component is enabled, the rectangle should be red; if disabled,
> gray. Make a copy of `ButtonDemo.java` that uses your
> custom `Icon` for the middle button, instead of displaying
> `middle.gif`. The following pictures show what the
> icon should look like.  
> > |  |  |
> > | --- | --- |
> > | SquareIcon-1.png | SquareIcon-2.png |
>
> 3. Implement a border that paints a red 15-pixel-tall stripe
> all the way across the top of its component. Test this border
> by substituting it for the border on the component you created
> in exercise 1. The result should look like the following figure.
> > ![ComponentDisplayer-2.png](../../figures/uiswing/QandE/ComponentDisplayer-2.png)

[Check your answers.](answers-ch6.html)

[« Previous](../TOC.html)
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

**Previous page:** Solving Common Painting Problems
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.