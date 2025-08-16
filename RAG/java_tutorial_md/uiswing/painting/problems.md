[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Performing Custom Painting

[Performing Custom Painting](index.html)

[Creating the Demo Application (Step 1)](step1.html)

[Creating the Demo Application (Step 2)](step2.html)

[Creating the Demo Application (Step 3)](step3.html)

[Refining the Design](refining.html)

[A Closer Look at the Paint Mechanism](closer.html)

[Summary](summary.html)

Solving Common Painting Problems

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Performing Custom Painting](index.html)

[« Previous](summary.html) • [Trail](../TOC.html) • [Next »](../QandE/questions-ch6.html)

# Solving Common Painting Problems

**Problem:**
I don't know where to put my painting code.

* Painting code belongs in the `paintComponent` method
  of any component descended from `JComponent`.

**Problem:**
The stuff I paint doesn't show up.

* Check whether your component is showing up at all.
  [Solving Common Component Problems](../components/problems.html) should help you with this.

  * Check whether `repaint` is invoked
    on your component
    whenever its appearance needs to be updated.

**Problem:**
My component's foreground shows up,
but its background is invisible.
The result is that
one or more components directly behind my component are
unexpectedly visible.

* Make sure your component is opaque.
  `JPanel`s, for example, are opaque by default
  in many but not all look and feels.
  To make components such as `JLabel`s
  and GTK+ `JPanel`s opaque,
  you must invoke `setOpaque(true)` on them.

  * If your custom component extends `JPanel`
    or a more specialized `JComponent` descendant,
    then you can paint the background by invoking
    `super.paintComponent`
    before painting the contents of your component.

    * You can paint
      the background yourself
      using this code at the top of a custom component's
      `paintComponent` method:

      ```

      g.setColor(getBackground());
      g.fillRect(0, 0, getWidth(), getHeight());
      g.setColor(getForeground());

      ```

**Problem:**
I used `setBackground`
to set my component's background color,
but it seemed to have no effect.

* Most likely, your component isn't painting its background,
  either because it's not opaque
  or your custom painting code doesn't paint the background.
  If you set the background color for a `JLabel`,
  for example,
  you must also invoke `setOpaque(true)`
  on the label to make the label's background be painted.

**Problem:**
I'm using the exact same code as a tutorial example,
but it doesn't work.
Why?

* Is the code executed in the exact same method as the tutorial example?
  For example, if the tutorial example has the code in the example's
  `paintComponent` method, then this method might be the
  only place where the code is guaranteed to work.

**Problem:**
How do I paint thick lines? patterns?

* The JavaTM 2D API
  provides extensive support for implementing line
  widths and styles, as well as patterns for use in filling and
  stroking shapes.
  See the
  [2D Graphics](../../2d/index.html) trail for more information on using the Java 2D API.

**Problem:**
The edges of a particular component look odd.

* Because components often update their borders
  to reflect component state,
  you generally should avoid invoking `setBorder`
  except on `JPanel`s
  and custom subclasses of `JComponent`.

  * Is the component painted by a look and feel
    such as GTK+ or Windows XP that uses UI-painted borders
    instead of `Border` objects?
    If so, don't invoke `setBorder` on the component.

    * Does the component have custom painting code?
      If so, does the painting code
      take the component's insets into account?

**Problem:**
Visual artifacts appear in my GUI.

* If you set the background color of a component,
  be sure the color has no transparency if the component is
  supposed to be opaque.

  * Use the `setOpaque` method
    to set component opacity if necessary.
    For example, the content pane must be opaque,
    but components with transparent backgrounds must not be opaque.

    * Make sure your custom component
      fills its painting area completely if it's opaque.

**Problem:**
The performance of my custom painting code is poor.

* If you can paint part of your component,
  use the `getClip` or
  `getClipBounds` method of `Graphics`
  to determine which area you need to paint.
  The less you paint, the faster it will be.

  * If only part of your component needs to be updated,
    make paint requests
    using a version of `repaint`
    that specifies the painting region.

    * For help on choosing efficient painting techniques,
      look for the string "performance" in the
      [Java 2D API home page](http://java.sun.com/products/java-media/2D/).

**Problem:**
The same transforms applied to
seemingly identical `Graphics` objects
sometimes have slightly different effects.

* Because the Swing painting code sets the transform
  (using the `Graphics` method `translate`)
  before invoking `paintComponent`,
  any transforms that you apply have a cumulative effect.
  This doesn't matter when doing a simple translation,
  but a more complex `AffineTransform`, for example,
  might have unexpected results.

If you don't see your problem in this list, see
[Solving Common Component Problems](../components/problems.html) and
[Solving Common Layout Problems](../layout/problems.html).

[« Previous](summary.html)
•
[Trail](../TOC.html)
•
[Next »](../QandE/questions-ch6.html)

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

**Previous page:** Summary
  
**Next page:** Questions and Exercises: Performing Custom Painting




A browser with JavaScript enabled is required for this page to operate properly.