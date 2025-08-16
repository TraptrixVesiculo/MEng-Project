[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Graphical User Interfaces
  
**Lesson:** Swing Features

[Swing Features](index.html)

[A Visual Guide to Swing Components (Java Look and Feel)](components.html)

[A Visual Guide to Swing Components (Windows Look and Feel)](compWin.html)

[Pluggable Look and Feel](plaf.html)

Data Transfer

[Internationalization and Localization](i18n.html)

[Accessibility](access.html)

[Integrating with the Desktop](desktop.html)

[System Tray Icon Support](tray.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Graphical User Interfaces](../index.html)
>
[Swing Features](index.html)

[« Previous](plaf.html) • [Trail](../TOC.html) • [Next »](i18n.html)

# Data Transfer

The Swing toolkit supports the ability to
transfer data between components within the same Java application,
between different Java applications, and between Java and native
applications. Data can be transferred via a drag and drop gesture,
or via the clipboard using cut, copy, and paste.

#### Drag and Drop

Drag-and-drop support can be easily enabled for many of Swing's
components (sometimes with a single line of code). For example,
it's trivial to enable drag and drop and copy and paste support
for `JTable`, Swing's table component. All you need to
provide is the data representing the selection and how to get your
data from the clipboard — that's it!

#### Cut, Copy, and Paste

Most of the text-based components, such as editor pane and text field,
support cut/copy and paste out of the box.
Of course, menu items need to be created
and "wired up" to the appropriate actions. Other components, such
as list and tree, can support cut, copy, and paste with some minimal work.

[PasswordStore](http://download.oracle.com/javase/tutorialJWS/ui/PasswordStore.jnlp)
supports data transfer in a variety of ways:

* The text in both the list and the table view supports
  cut, copy, and paste.

  * The text fields in the Details Panel, the Filter
    text field, and the Notes text pane support cut/copy,
    paste, and drag and drop.

    * The Company icon region in the Details panel accepts a dropped
      image (jpg, png, gif, or tif).

[« Previous](plaf.html)
•
[Trail](../TOC.html)
•
[Next »](i18n.html)

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

**Previous page:** Pluggable Look and Feel
  
**Next page:** Internationalization and Localization




A browser with JavaScript enabled is required for this page to operate properly.