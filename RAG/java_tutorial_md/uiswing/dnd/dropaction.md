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

Choosing the Drop Action

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

[« Previous](dropmodedemo.html) • [Trail](../TOC.html) • [Next »](dropactiondemo.html)

# Choosing the Drop Action

Every drag source (Java based or otherwise) advertises the set of actions
it supports when exporting data. If it supports data being copied,
it advertises the `COPY` action; if it supports data being moved from it,
then it advertises the `MOVE` action, and so on.
For Swing components, the source actions are advertised through the
[`getSourceActions`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.html#getSourceActions(javax.swing.JComponent)) method.

When a drag is initiated, the user has some control over which of
the source actions is chosen for the transfer by way of keyboard
modifiers used in conjunction with the drag gesture — this is
called the *user action*.
For example,
the default (where no modifiers are used) generally indicates a move action,
holding the Control key indicates a copy action,
and holding both Shift and Control indicates a linking action.
The user action is available via the
[`getUserDropAction`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#getUserDropAction()) method.

The user action indicates a preference, but ultimately it is
the target that decides the drop action.
For example, consider a component that will only accept copied data.
And consider a drag source that supports both copy and move.
The `TransferHandler` for the copy-only target can be coded
to only accept data from the source using the
[`setDropAction`](http://download.oracle.com/javase/7/docs/api/javax/swing/TransferHandler.TransferSupport.html#setDropAction(int)) method, even if the user has indicated a preference for a move action.

This work happens in the `canImport` method, where the
target's `TransferHandler` decides whether to accept
the incoming data. An implementation that explicitly chooses
the `COPY` action, if it is supported by the source,
might look like this:

```

public boolean canImport(TransferHandler.TransferSupport support) {
    // for the demo, we will only support drops (not clipboard paste)
    if (!support.isDrop()) {
        return false;
    }

    // we only import Strings
    if (!support.isDataFlavorSupported(DataFlavor.stringFlavor)) {
        return false;
    }

    // check if the source actions (a bitwise-OR of supported actions)
    // contains the COPY action
    boolean copySupported = (COPY & support.getSourceDropActions()) == COPY;
    if (copySupported) {
        support.setDropAction(COPY);
        return true;
    }

    // COPY is not supported, so reject the transfer
    return false;
}

```

The code snippet displayed in bold shows where the source's supported
drop actions are queried.
If copy is supported, the `setDropAction` method is invoked
to ensure that only a copy action will take place and the method returns
true.

Next we will look at a demo that explicitly sets the drop action
using `setDropAction`.

[« Previous](dropmodedemo.html)
•
[Trail](../TOC.html)
•
[Next »](dropactiondemo.html)

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

**Previous page:** Demo - DropDemo
  
**Next page:** Demo - ChooseDropAction




A browser with JavaScript enabled is required for this page to operate properly.