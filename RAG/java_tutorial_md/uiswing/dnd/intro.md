[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer

[Drag and Drop and Data Transfer](index.html)

Introduction to DnD

[Default DnD Support](defaultsupport.html)

[Demo - BasicDnD](basicdemo.html)

[TransferHandler Class](transferhandler.html)

[Export Methods](export.html)

[Import Methods](import.html)

[TransferSupport Class](transfersupport.html)

[Setting the Drop Mode](dropmodes.html)

[Demo - DropDemo](dropmodedemo.html)

[Choosing the Drop Action](dropaction.html)

[Demo - ChooseDropAction](dropactiondemo.html)

[Showing the Drop Location](showdroploc.html)

[Location Sensitive Drop](locsensitivedrop.html)

[Demo - LocationSensitiveDemo](locsensitivedemo.html)

[Empty Table Drop](emptytable.html)

[Drop Location Rendering](droplocation.html)

[Top-Level Drop](toplevel.html)

[Adding Cut, Copy and Paste (CCP)](cutpaste.html)

[CCP in a Text Component](textpaste.html)

[CCP in a non-Text Component](listpaste.html)

[Using and Creating a DataFlavor](dataflavor.html)

[Putting it All Together - DnD and CCP](together.html)

[Further Information](info.html)

[Solving Common Data Transfer Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Drag and Drop and Data Transfer](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](defaultsupport.html)

# Introduction to DnD

If you are writing an application you will want to support the
ability to transfer information between components in your application.
But you will also want your application to play well with others —
this includes supporting the ability to transfer information
between your application and other Java applications, and between
your application and native applications.
The ability to transfer data takes two forms:

* Drag and drop (DnD) support.
  The following diagram illustrates dragging from a
  `JList` and dropping onto
  a `JTextField` component
  (the arrows show the path of the data):

  ![Drag and Drop Illustration](../../figures/uiswing/dnd/dndprocess.jpg)

  * Clipboard transfer through cut or copy and paste.
    The following diagrams show cutting (or copying) from a `JList`
    and pasting onto a `JTextField` component:

    ![Cut/Copy/Paste Illustration](../../figures/uiswing/dnd/clipboardtransfer.jpg)

### Drag and Drop — Behind the Scenes

> Let us say there is a user named Rollo, who is running a Java application.
> He wants to drag some text from a list and deposit it into a text field.
> (Note that the process is the same when dragging from a native
> application to a Java application.)
> In a nutshell, the drag and drop process works like this:
>
> > * Rollo has selected a row of text in the *source* component:
> >   the list. While holding the mouse button Rollo begins to drag the
> >   text — this initiates the *drag gesture*.
> >
> >   * When the drag begins, the list
> >     packages up the data for *export* and declares what
> >     *source actions* it supports,
> >     such as `COPY`, `MOVE`, or `LINK`.
> >
> >     * As Rollo drags the data, Swing continuously calculates the
> >       location and handles the rendering.
> >
> >       * If Rollo simultaneously holds the Shift and/or Control key during
> >         the drag,
> >         this *user action* is also part of the drag gesture.
> >         Typically, an ordinary drag requests the `MOVE` action.
> >         Holding the Control key while dragging requests the
> >         `COPY` action, and holding both Shift and Control
> >         requests the `LINK` action.
> >
> >         * Once Rollo drags the text over the bounds of a text field component,
> >           the *target* is continually polled to see if it will
> >           accept or reject the potential drop. As he drags,
> >           the target provides feedback by showing the *drop location*,
> >           perhaps an insertion cursor or a highlighted selection.
> >           In this case, the text field (the current target) allows both
> >           replacement of selected text and insertion of new text.
> >
> >           * When Rollo releases the mouse button, the text component inspects
> >             the declared source actions and any user action and then it
> >             chooses what it wants out of the available options.
> >             In this case, the text field chooses to insert the new text
> >             at the point of the drop.
> >
> >             * Finally, the text field *imports* the data.
>
> While this might seem like a daunting process, Swing handles most of
> the work for you. The framework is designed so that you plug in the
> details specific to your component, and the rest "just works".
>
> More on this in the next section.
>
> ---
>
> **Note:** We *do not recommend* that you create your own drag and drop support
> using the AWT classes. This implementation would require significant complex
> support internal to each component. Prior to release 1.4 when the dnd system
> was reworked, developers did occasionally create their own dnd support,
> but it does not work with sophisticated components,
> like tree and table, that have subtle selection and drop issues.
>
> ---

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](defaultsupport.html)

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

**Previous page:** Drag and Drop and Data Transfer
  
**Next page:** Default DnD Support




A browser with JavaScript enabled is required for this page to operate properly.