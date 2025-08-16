[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Full-Screen Exclusive Mode API

[Full-Screen Exclusive Mode API](index.html)

[Full-Screen Exclusive Mode](exclusivemode.html)

[Display Mode](displaymode.html)

Passive vs. Active Rendering

[Double Buffering and Page Flipping](doublebuf.html)

[`BufferStrategy` and `BufferCapabilities`](bufferstrategy.html)

[Examples](example.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Full-Screen Exclusive Mode API](index.html)

[« Previous](displaymode.html) • [Trail](../TOC.html) • [Next »](doublebuf.html)

# Passive vs. Active Rendering

As mentioned before, most full-screen applications usually function better
if they are at the helm during drawing. In traditional windowed GUI
applications, the question of when to paint is usually handled by the operating
system. When operating in a windowed environment, this makes perfect
sense. A windowed application does not know when the user is going
to move, resize, expose, or cover an application by another window until
it actually happens. In a Java GUI application, the operating system
delivers a *paint event* to the AWT, which figures out what needs
to be painted, creates a
java.awt.Graphics object with the
appropriate clipping region, then calls the paint method with
that Graphics object:

```

// Traditional GUI Application paint method:
// This can be called at any time, usually from the event dispatch thread
public void paint(Graphics g) {
    // Use g to draw my Component
}

```

This is sometimes referred to as *passive rendering*. As you
can imagine, such a system incurs a lot of overhead, much to the annoyance
of many performance-sensitive AWT and Swing programmers.

When in full-screen exclusive mode, you don't have to worry anymore
about the window being resized, moved, exposed, or occluded (unless you've
ignored my suggestion to turn off resizing). Instead, the application
window is drawn directly to the screen (*active rendering*).
This simplifies painting quite a bit, since you don't ever need to worry
about paint events. In fact, paint events delivered by the operating
system may even be delivered at inappropriate or unpredictable times when
in full-screen exclusive mode.

Instead of relying on the paint method in full-screen exclusive
mode, drawing code is usually more appropriately done in a *rendering
loop*:

```

public void myRenderingLoop() {
    while (!done) {
        Graphics myGraphics = getPaintGraphics();
        // Draw as appropriate using myGraphics
        myGraphics.dispose();
    }
}

```

Such a rendering loop can done from any thread, either its own helper thread
or as part of the main application thread.

### Programming Tips

> Some tips about using active rendering:
>
> * Don't put drawing code in the paint routine. You may never
>   know when that routine may get called! Instead, use another method
>   name, such as render(Graphics g), which can be called from the
>   paint
>   method when operating in windowed mode, or alternately called with its
>   own graphics from the rendering loop.
> * Use the setIgnoreRepaint method on your application window and
>   components to turn off all paint events dispatched from the operating system
>   completely, since these may be called during inappropriate times, or worse,
>   end up calling paint, which can lead to race conditions between
>   the AWT event thread and your rendering loop.
> * Separate your drawing code from your rendering loop, so that you can operate
>   fully under both full-screen exclusive and windowed modes.
> * Optimize your rendering so that you aren't drawing everything on the screen
>   at all times (unless you are using page-flipping or double-buffering, both
>   discussed below).
> * Do not rely on the update or repaint methods for
>   delivering paint events.
> * Do not use heavyweight components, since these will still incur the overhead
>   of involving the AWT and the platform's windowing system.
> * If you use lightweight components, such as Swing components, you may have
>   to fiddle with them a bit so that they draw using your Graphics,
>   and not directly as a result of calling the paint method.
>   Feel free to call Swing methods such as paintComponents, paintComponent,
>   paintBorder,
>   and paintChildren directly from your rendering loop.
> * Feel free to use passive rendering if you just want a simple full-screen
>   Swing or AWT application, but remember that paint events may be somewhat
>   unreliable or unnecessary while in full-screen exclusive mode. Additionally,
>   if you use passive rendering, you will not be able to use more advanced
>   techniques such as page-flipping. Finally, be very careful to avoid
>   deadlocks if you decide to use both active and passive rendering simultaneously--this
>   approach is not recommended.

[« Previous](displaymode.html)
•
[Trail](../TOC.html)
•
[Next »](doublebuf.html)

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

**Previous page:** Display Mode
  
**Next page:** Double Buffering and Page Flipping




A browser with JavaScript enabled is required for this page to operate properly.