[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Full-Screen Exclusive Mode API

[Full-Screen Exclusive Mode API](index.html)

[Full-Screen Exclusive Mode](exclusivemode.html)

Display Mode

[Passive vs. Active Rendering](rendering.html)

[Double Buffering and Page Flipping](doublebuf.html)

[`BufferStrategy` and `BufferCapabilities`](bufferstrategy.html)

[Examples](example.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Full-Screen Exclusive Mode API](index.html)

[« Previous](exclusivemode.html) • [Trail](../TOC.html) • [Next »](rendering.html)

# Display Mode

Once an application is in full-screen exclusive mode, it may be able to
take advantage of actively setting the *display mode*. A display
mode (java.awt.DisplayMode) is composed of the size (width and
height of the monitor, in pixels), bit depth (number of bits per pixel),
and refresh rate (how frequently the monitor updates itself). Some
operating systems allow you to use multiple bit depths at the same time,
in which case the special value BIT\_DEPTH\_MULTI is used for the
value of bit depth. Also, some operating systems may not have any
control over the refresh rate (or you may not care about the refresh rate
setting). In this case, the special value REFRESH\_RATE\_UNKNOWN
is used for the refresh rate value.

#### How to Set the Display Mode

To get the current display mode, simply call the getDisplayMode
method on your graphics device. To obtain a list of all possible
display modes, call the getDisplayModes method. Both
getDisplayMode
and getDisplayModes can be called at any time, regardless of
whether or not you are in full-screen exclusive mode.

Before attempting to change the display mode, you should first call
the isDisplayChangeSupported method. If this method
returns false, the operating system does not support changing
the display mode.

Changing the display mode can only be done when in full-screen exclusive
mode. To change the display mode, call the setDisplayMode
method with the desired display mode. A runtime exception will be thrown
if the display mode is not available, if display mode changes are not
supported, or if you are not running in full-screen exclusive mode.

#### Reasons for Changing the Display Mode

The main reason for setting the display mode is *performance*. An
application can run much more quickly if the images it chooses to display
share the same bit depth as the screen. Also, if you can count on
the display to be a particular size, it makes drawing to that display much
simpler, since you do not have to scale things down or up depending on
how the user has set the display.

### Programming Tips

> Here are some tips for choosing and setting the display mode:
>
> * Check the value returned by the isDisplayChangeSupported method
>   before attempting to change the display mode on a graphics device.
> * Make sure you are in full-screen exclusive mode before attempting to change
>   the display mode.
> * As with using full-screen mode, setting the display mode is more robust
>   when in a `try...finally` clause:
>
> ```
>
> GraphicsDevice myDevice;
> Window myWindow;
> DisplayMode newDisplayMode;
>
> DisplayMode oldDisplayMode = myDevice.getDisplayMode();
> try {
>     myDevice.setFullScreenWindow(myWindow);
>     myDevice.setDisplayMode(newDisplayMode);
>     ...
> } finally {
>     myDevice.setDisplayMode(oldDisplayMode);
>     myDevice.setFullScreenWindow(null);
> }
>
> ```
>
> * When choosing a display mode for your application, you may want to keep
>   a list of preferred display modes, then choose the best one from the list
>   of available display modes.
> * As a fallback, if the display mode you desire is not available, you may
>   want to simply run in windowed mode at a fixed size.

[« Previous](exclusivemode.html)
•
[Trail](../TOC.html)
•
[Next »](rendering.html)

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

**Previous page:** Full-Screen Exclusive Mode
  
**Next page:** Passive vs. Active Rendering




A browser with JavaScript enabled is required for this page to operate properly.