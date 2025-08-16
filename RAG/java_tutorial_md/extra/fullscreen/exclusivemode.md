[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Full-Screen Exclusive Mode API

[Full-Screen Exclusive Mode API](index.html)

Full-Screen Exclusive Mode

[Display Mode](displaymode.html)

[Passive vs. Active Rendering](rendering.html)

[Double Buffering and Page Flipping](doublebuf.html)

[`BufferStrategy` and `BufferCapabilities`](bufferstrategy.html)

[Examples](example.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Full-Screen Exclusive Mode API](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](displaymode.html)

# Full-Screen Exclusive Mode

Programmers who use Microsoft's DirectX API may already be familiar with
full-screen exclusive mode. Other programmers may be somewhat new
to the concept. In either case, full-screen exclusive mode is a powerful
feature of J2SETM
version 1.4 that allows the programmer to
suspend the windowing system so that drawing can be done directly to the
screen.

This is a slight paradigm shift from the usual kind of GUI program in
many ways. In traditional Java GUI programs, the AWT is responsible
for propagating *paint events* from the operating system, through
the *event dispatch thread*, and by calling AWT's Component.paint method
when appropriate. In full-screen exclusive applications, painting
is usually done actively by the program itself. Additionally, a traditional
GUI application is limited to the bit depth and size of the screen chosen
by the user. In a full-screen exclusive application, the program
can control the bit depth and size (*display mode*) of the screen.
Finally, many more advanced techniques, such as *page flipping* (discussed
below) and stereo buffering (utilizing systems which use a separate set of
frames for each eye) require, on some platforms, that an application first
be in full-screen exclusive mode.

#### Hardware-Accelerated Image Basics

To understand the full-screen exclusive mode API, you need to
understand some basic principles of hardware-accelerated images.
The
VolatileImage interface encapsulates a surface which may or
may not take advantage of hardware acceleration. Such surfaces may
lose their hardware acceleration or their memory at the behest of the operating
system (hence, the name 'volatile'). See the `VolatileImage` *Tutorial*
(coming soon) for more information on volatile images.

Full-screen exclusive mode is handled through a java.awt.GraphicsDevice
object. For a list of all available screen graphics devices (in single
or multi-monitor systems), you can call the method getScreenDevices
on the local java.awt.GraphicsEnvironment; for the default (primary)
screen (the only screen on a single-monitor system), you can call the method
getDefaultScreenDevice.

Once you have the graphics device, you can call one of the following methods:

public boolean isFullScreenSupported()
:   This method returns
    whether or not full-screen exclusive mode is available. On systems
    where full-screen exclusive mode is not available, it is probably better
    to run an application in windowed mode with a fixed size rather than setting
    a full-screen window.

public void setFullScreenWindow(Window w)
:   Given a window,
    this method enters full-screen exclusive mode using that window.
    If full-screen exclusive mode is not available, the window is positioned
    at (0,0) and resized to fit the screen. Use this method with a
    null
    parameter to exit full-screen exclusive mode.

### Programming Tips

> Here are some tips about programming using full-screen exclusive mode:
>
> * Check for isFullScreenSupported before entering full-screen
>   exclusive mode. If it isn't supported, performance may be degraded.
> * Entering and exiting full-screen mode is more robust when using a try...finally
>   clause. This is not only good coding practice, but it also prevents
>   your program from staying in full-screen exclusive mode longer than it
>   should:
>
> ```
>
> GraphicsDevice myDevice;
> Window myWindow;
>
> try {
>     myDevice.setFullScreenWindow(myWindow);
>     ...
> } finally {
>     myDevice.setFullScreenWindow(null);
> }
>
> ```
>
> * Most full-screen exclusive applications are better suited to use undecorated
>   windows. Turn off decorations in a frame or dialog using the setUndecorated
>   method.
> * Full-screen exclusive applications should not be resizable, since resizing
>   a full-screen application can cause unpredictable (or possibly dangerous)
>   behavior.
> * For security reasons, the user must grant fullScreenExclusive permission
>   when using full-screen exclusive mode in an applet.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](displaymode.html)

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

**Previous page:** Full-Screen Exclusive Mode API
  
**Next page:** Display Mode




A browser with JavaScript enabled is required for this page to operate properly.