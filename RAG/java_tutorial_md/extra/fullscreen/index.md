[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Full-Screen Exclusive Mode API

[Full-Screen Exclusive Mode](exclusivemode.html)

[Display Mode](displaymode.html)

[Passive vs. Active Rendering](rendering.html)

[Double Buffering and Page Flipping](doublebuf.html)

[`BufferStrategy` and `BufferCapabilities`](bufferstrategy.html)

[Examples](example.html)

**Trail:** Bonus

[Home Page](../../index.html)
>
[Bonus](../index.html)

[« Previous](../generics/index.html) • [Trail](../TOC.html) • [Next »](exclusivemode.html)

# Lesson: Full-Screen Exclusive Mode API

### *by Michael Martak*

> Do you want to use high-performance graphics in the Java development
> environment? Have you always wanted to program a game, but
> your images wouldn't move fast enough? Has your slide show program
> not worked properly because you had no control over the user's
> display resolution? If you've been asking any of these questions,
> then the full-screen exclusive mode API, introduced in release 1.4,
> may be what you're looking for.
>
> **[Full-Screen Exclusive Mode](exclusivemode.html)**
> :   Full-screen exclusive mode is a powerful new feature that enables
>     you to suspend the windowing system so that drawing
>     can be done directly to the screen.
>
> **[Display Mode](displaymode.html)**
> :   This section describes how to choose and set the display mode. It
>     also discusses why you'd want to set the display mode in the first place.
>
> **[Passive vs. Active Rendering](rendering.html)**
> :   This section discusses the merits of passive and active rendering. For
>     example, painting while on the main event loop using the
>     `paint` method is passive, whereas rendering in your own
>     thread is active. Active rendering tips are also listed.
>
> **[Double Buffering and Page Flipping](doublebuf.html)**
> :   This section explains double buffering and introduces page-flipping, a
>     double buffering technique available in full-screen exclusive mode.
>
> **[`BufferStrategy` and `BufferCapabilities`](bufferstrategy.html)**
> :   This section covers `java.awt.image.BufferStrategy`, a class that
>     allows you to draw to surfaces and components without having to
>     know the number of buffers used or the technique used to display them.
>     This section also reviews `java.awt.BufferCapabilities`, a class
>     that can help you determine the capabilities of your graphics device.
>
> **[Examples](example.html)**
> :   This page lists several full-screen exclusive mode examples.

[« Previous](../generics/index.html)
•
[Trail](../TOC.html)
•
[Next »](exclusivemode.html)

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
  
**Next page:** Full-Screen Exclusive Mode




A browser with JavaScript enabled is required for this page to operate properly.