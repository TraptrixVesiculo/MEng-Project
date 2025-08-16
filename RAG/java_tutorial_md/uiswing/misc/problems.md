[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Other Swing Features

[Using Other Swing Features](index.html)

[How to Integrate with the Desktop Class](desktop.html)

[How to Create Translucent and Shaped Windows](trans_shaped_windows.html)

[How to Decorate Components with JLayer](jlayer.html)

[How to Use Actions](action.html)

[How to Use Swing Timers](timer.html)

[How to Support Assistive Technologies](access.html)

[How to Use the Focus Subsystem](focus.html)

[How to Use Key Bindings](keybinding.html)

[How to Use Modality in Dialogs](modality.html)

[How to Print Tables](printtable.html)

[How to Print Text](printtext.html)

[How to Create a Splash Screen](splashscreen.html)

[How to Use the System Tray](systemtray.html)

Solving Common Problems Using Other Swing Features

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Other Swing Features](index.html)

[« Previous](systemtray.html) • [Trail](../TOC.html) • [Next »](../layout/index.html)

# Solving Common Problems Using Other Swing Features

**Problem:**
My application is not showing the look and feel I have requested
via `UIManager.setLookAndFeel`.
> You probably either set the look and feel to an invalid
> look and feel or set it after the UI manager loaded
> the default look and feel. If you are sure that the
> look and feel you specified is valid and setting the look
> and feel is the first thing your program does (at the top
> of its main method, for example), check whether you have
> a static field that references a Swing class. This
> reference can cause the default look and feel to be
> loaded if none has been specified. For more information,
> including how to set a look and feel after the GUI has
> been created, see the [look
> and feel](../lookandfeel/plaf.html) section.

**Problem:**
Why is not my component getting the focus?
> * Is it a custom component (for example, a direct subclass of
>   `JComponent`) that you created? If so,
>   you may need to give your component an input map
>   and mouse listener. See
>   [How to Make a Custom
>   Component Focusable](focus.html#focusable) for more information and a demo.
>
>   * Is the component inside of a `JWindow` object?
>     The focus system requires a `JWindow`'s owning
>     frame to be visible for any components in the `JWindow` object
>     to get the focus. By default, if you do not specify an owning
>     frame for a `JWindow` object, an invisible owning frame
>     is created for it. The solution is to either specify a visible
>     and focusable owning frame when creating the `JWindow` object or to use
>     `JDialog` or `JFrame` objects instead.

**Problem:**
Why cannot my dialog receive the event generated when the user
hits the Escape key?
This worked until I ported to release 1.4.
> If your dialog contains a text field,
> it may be consuming the event.
> (Prior to release 1.4.0, the text field did not get the focus.)
>
> * If you want to get the Escape event regardless of whether a component
>   consumes it, you should use a
>   [`KeyEventDispatcher`](http://download.oracle.com/javase/7/docs/api/java/awt/KeyEventDispatcher.html).
>
>   * If you want to get the Escape event only if a
>     component has not consumed it, then register a key
>     binding on any `JComponent` component in the
>     `JDialog` object, using the `WHEN_IN_FOCUSED_WINDOW`
>     input map. For more information, see the
>     [How to Use Key Bindings](../misc/keybinding.html) page.

**Problem:**
Why I cannot apply Swing components to a tray icon?
> Current implementation of the `TrayIcon` class
> supports the `PopupMenu` component, but not its
> Swing counterpart `JPopupMenu`. This limitation
> narrows capabilities to employ additional Swing features,
> for example, menu icons. See the Bug ID
> [6285881](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=6285881).
>
> * A new `JTrayIcon` class will be created to eliminate this inconvenience.
>   Until then, use AWT components to add a menu item, checkbox menu item, or submenu.
>
> If you do not find your problem in this section, consult
> [Solving Common Component Problems](../components/problems.html).

[« Previous](systemtray.html)
•
[Trail](../TOC.html)
•
[Next »](../layout/index.html)

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

**Previous page:** How to Use the System Tray
  
**Next page:** Laying Out Components Within a Container




A browser with JavaScript enabled is required for this page to operate properly.