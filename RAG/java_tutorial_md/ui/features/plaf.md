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

Pluggable Look and Feel

[Data Transfer](dnd.html)

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

[« Previous](compWin.html) • [Trail](../TOC.html) • [Next »](dnd.html)

# Pluggable Look and Feel

The Swing toolkit allows you to decide how to configure the particular
look and feel of your application. If you don't specify a look
and feel, the Swing UI manager figures out which one to use.
The options for setting a look and feel include:

* Leave it up to the Swing UI manager. If a particular look and
  feel is not specified by the program, Swing's UI manager checks
  whether the user has specified a preference. If that preference
  hasn't been specified or isn't available, the default look and
  feel is used. The default look and feel is determined
  by the supplier of the JRE. For the JRE that Sun provides,
  the Java look and feel (called Metal) is used.
  The Java look and feel works on all platforms.

  * Use the look and feel of the native platform.
    If the application is running on a Microsoft Windows XP machine,
    the Windows look and feel is used. On Mac OS platforms, the Aqua
    look and feel is used. On UNIX platforms, such as Solaris or Linux,
    either the GTK+ look and feel or the CDE/Motif look and feel is used,
    depending on the user's desktop choice.

    * Specify a particular look and feel. Swing ships with
      four look and feels: Java (also called Metal), Microsoft Windows,
      GTK+, and CDE/Motif. The GTK+ look and feel requires a theme, and
      there are many available for free on the Internet.

      * Create your own look and feel using the Synth package.

        * Use an externally provided look and feel.

As shown in the following figures,
PasswordStore offers a choice of three look and feels. The Alloy
look and feel has been provided courtesy of
[Incors](http://www.incors.com/).

![This is a picture of the PasswordStore demo in the Java look and feel.](../../figures/ui/ui-JavaPasswordStore.png)

Java look and feel

![This is a picture of the PasswordStore demo in the Windows look and feel.](../../figures/ui/ui-WindowsPasswordStore.png)

Windows look and feel

![This is a picture of the PasswordStore demo in the CDE/Motif look and feel.](../../figures/ui/ui-MotifPasswordStore.png)

CDE/Motif look and feel

![This is a picture of the PasswordStore demo in the Alloy default look and feel.](../../figures/ui/ui-AlloyPasswordStore.png)

Default Alloy look and feel

[« Previous](compWin.html)
•
[Trail](../TOC.html)
•
[Next »](dnd.html)

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

**Previous page:** A Visual Guide to Swing Components (Windows Look and Feel)
  
**Next page:** Data Transfer




A browser with JavaScript enabled is required for this page to operate properly.