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

[Passive vs. Active Rendering](rendering.html)

[Double Buffering and Page Flipping](doublebuf.html)

`BufferStrategy` and `BufferCapabilities`

[Examples](example.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Full-Screen Exclusive Mode API](index.html)

[« Previous](doublebuf.html) • [Trail](../TOC.html) • [Next »](example.html)

# `BufferStrategy` and `BufferCapabilities`

#### `BufferStrategy`

In Java 2 Standard Edition, you don't have to worry about video pointers
or video memory in order to take full advantage of either double-buffering
or page-flipping. The new class java.awt.image.BufferStrategy
has been added for the convenience of dealing with drawing to surfaces
and components in a general way, regardless of the number of buffers used
or the technique used to display them.

A buffer strategy gives you two all-purpose methods for drawing: getDrawGraphics
and show. When you want to start drawing, get a draw graphics
and use it. When you are finished drawing and want to present your
information to the screen, call show. These two methods
are designed to fit rather gracefully into a rendering loop:

```

BufferStrategy myStrategy;

while (!done) {
    Graphics g = myStrategy.getDrawGraphics();
    render(g);
    g.dispose();
    myStrategy.show();
}

```

Buffer strategies have also been set up to help you monitor VolatileImage
issues. When in full-screen exclusive mode, VolatileImage
issues are especially important because the windowing system can sometimes
take back the video memory it has given you. One important example
is when the user presses the ALT+TAB key combination in Windows--suddenly
your full-screen program is running in the background and your video memory
is lost. You can call the contentsLost method to find
out if this has happened. Similarly, when the windowing system returns
your memory to you, you can find out using the contentsRestored
method.

#### `BufferCapabilities`

As mentioned before, different operating systems, or even different
graphics cards on the same operating system, have different techniques
available at their disposal. These *capabilities* are exposed
for you so that you can pick the best technique for your application.

The class java.awt.BufferCapabilities encapsulates these capabilities.
Every buffer strategy is controlled by its buffer capabilities, so picking
the right ones for your application is very crucial. To find out
what capabilities are available, call the getBufferCapabilities
method from the GraphicsConfiguration objects available on your
graphics device.

The capabilities available in Java 2 Standard Edition version 1.4 are:

`isPageFlipping`
:   This capability returns whether or not hardware
    page-flipping is available on this graphics configuration.

`isFullScreenRequired`
:   This capability returns whether or not
    full-screen exclusive mode is required before hardware page-flipping should
    be attempted.

`isMultiBufferAvailable`
:   This capability returns whether or
    not multiple buffering (two or more back buffers plus the primary surface)
    in hardware is available.

`getFlipContents`
:   This capability returns a hint of the technique
    used to do hardware page-flipping. This is important because the
    contents of the back buffer after a show are different depending
    on the technique used. The value returned can be null (if isPageFlipping
    returns false) or one of the following values. Any value
    can be specified for a buffer strategy so long as the isPageFlipping method
    returns true, though performance will vary depending on the available capabilities.

`FlipContents.COPIED`
:   This value means that the contents of the
    back buffer are copied to the primary surface. A "flip" is probably
    performed as a hardware blt, which means that hardware double-buffering
    is probably done using blitting instead of true page-flipping. This
    should (in theory) be faster, or at least as fast, as blitting from a VolatileImage
    to the primary surface, though your mileage may vary. The contents
    of the back buffer are the same as the primary surface after a flip.

`FlipContents.BACKGROUND`
:   This value means that the contents of
    the back buffer have been cleared with the background color. Either
    a true page-flip or a blt has occurred.

`FlipContents.PRIOR`
:   This value means that the contents of the
    back buffer are now the contents of the old primary surface, and vice versa.
    Generally this value indicates that true page-flipping occurs, though this
    is not guaranteed and, once again, your mileage on this operation may vary.

`FlipContents.UNKNOWN`
:   This value means that the contents of the
    back buffer are undefined after a flip. You may have to experiment
    to find which technique works best for you (or you may not care), and you
    will definitely have to set up the contents of the back buffer yourself
    each time you draw.

To create a buffer strategy for a component, call the createBufferStrategy
method, supplying the number of buffers desired (this number includes
the primary surface).  If any particular buffering technique
is desired, supply an appropriate BufferCapabilities object.
Note that when you use this version of the method, you must catch an
AWTException
in the event that your choice is not available. Also note that these
methods are only available on Canvas and
Window.

Once a particular buffer strategy has been created for a component,
you can manipulate it using the getBufferStrategy method.
Note that this method is also only available for canvases and windows.

### Programming Tips

> Some tips about using buffer capabilities and buffer strategies:
>
> * Getting, using, and disposing a graphics object are more robust in a try...finally
>   clause:
>
> ```
>
> BufferStrategy myStrategy;
>
> while (!done) {
>     Graphics g;
>     try {
>         g = myStrategy.getDrawGraphics();
>         render(g);
>     } finally {
>         g.dispose();
>     }
>     myStrategy.show();
> }
>
> ```
>
> * Check the available capabilities before using a buffer strategy.
> * For best results, create your buffer strategy on a full-screen exclusive
>   window. Make sure you check the isFullScreenRequired and
>   isPageFlipping
>   capabilities before using page-flipping.
> * Don't make any assumptions about performance. Tweak your code as
>   necessary, but remember that different operating systems and graphics cards
>   have different capabilities. Profile your application!
> * You may want to subclass your component to override the createBufferStrategy
>   method. Use an algorithm for choosing a strategy that is best suited
>   to your application. The FlipBufferStrategy and  BltBufferStrategy
>   inner classes are protected and can be subclassed.
> * Don't forget that you may lose your drawing surfaces!  Be sure to
>   check contentsLost and contentsRestored before drawing.
>   All buffers that have been lost have to be redrawn when they are restored.
> * If you use a buffer strategy for double-buffering in a Swing application,
>   you probably want to turn off double-buffering for your Swing components,
>   since they will already be double-buffered. Video memory is somewhat
>   valuable and should only be used whenever absolutely necessary.
> * It may be end up being wasteful to use more than one back buffer.
>   Multi-buffering is only useful when the drawing time exceeds the time spent
>   to do a show. Profile your application!

[« Previous](doublebuf.html)
•
[Trail](../TOC.html)
•
[Next »](example.html)

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

**Previous page:** Double Buffering and Page Flipping
  
**Next page:** Examples




A browser with JavaScript enabled is required for this page to operate properly.