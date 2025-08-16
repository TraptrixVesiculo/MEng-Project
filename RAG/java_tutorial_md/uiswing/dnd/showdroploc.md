[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Drag and Drop and Data Transfer

[Drag and Drop and Data Transfer](index.html)

[Introduction to DnD](intro.html)

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

Showing the Drop Location

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

[« Previous](dropactiondemo.html) • [Trail](../TOC.html) • [Next »](locsensitivedrop.html)

# Showing the Drop Location

Generally during a drag operation, a component gives visual feedback
when it can accept the data. It might highlight the drop location,
or it might show a caret or a horizontal line where the
insertion would occur.
Swing renders the drop location when the `canImport`
method for the component's `TransferHandler` returns true.

To control this programmatically, you can use the
[`setShowDropLocation`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#setShowDropLocation(boolean)) method.
Calling this method with `true` causes the visual feedback
for the drop location to always be displayed, even if the drop will not
be accepted. Calling this method with `false` prevents any
visual feedback, even if the drop will be accepted.
You always invoke this method from `canImport`.

The
[Demo - LocationSensitiveDemo](locsensitivedemo.html) page includes a combo box that enables you to choose to
always show the drop location, or never show the drop location, or
the default behavior. But first we will talk about
location sensitive drop.

[« Previous](dropactiondemo.html)
•
[Trail](../TOC.html)
•
[Next »](locsensitivedrop.html)

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

**Previous page:** Demo - ChooseDropAction
  
**Next page:** Location Sensitive Drop




A browser with JavaScript enabled is required for this page to operate properly.