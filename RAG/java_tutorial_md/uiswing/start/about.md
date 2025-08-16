[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Getting Started with Swing

[Getting Started with Swing](index.html)

About the JFC and Swing

[Compiling and Running Swing Programs](compile.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Getting Started with Swing](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](compile.html)

# About the JFC and Swing

JFC is short for Java Foundation Classes, which encompass a group of
features for building graphical user interfaces (GUIs) and adding rich
graphics functionality and interactivity to Java applications.
It is defined as containing the features shown in the table below.
> | **Features of the Java Foundation Classes** | |
> | **Feature** | **Description** |
> | Swing GUI Components | Includes everything from buttons to split panes to tables. Many components are capable of sorting, printing, and drag and drop, to name a few of the supported features. |
> | Pluggable Look-and-Feel Support | The look and feel of Swing applications is pluggable, allowing a choice of look and feel. For example, the same program can use either the Java or the Windows look and feel. Additionally, the Java platform supports the GTK+ look and feel, which makes hundreds of existing look and feels available to Swing programs. Many more look-and-feel packages are available from various sources. |
> | Accessibility API | Enables assistive technologies, such as screen readers and Braille displays, to get information from the user interface. |
> | Java 2D API | Enables developers to easily incorporate high-quality 2D graphics, text, and images in applications and applets. Java 2D includes extensive APIs for generating and sending high-quality output to printing devices. |
> | Internationalization | Allows developers to build applications that can interact with users worldwide in their own languages and cultural conventions. With the input method framework developers can build applications that accept text in languages that use thousands of different characters, such as Japanese, Chinese, or Korean. |

This trail concentrates on the Swing components.
We help you choose the appropriate components for your GUI,
tell you how to use them, and give you the background information you
need to use them effectively. We also discuss other JFC features as
they apply to Swing components.

### Which Swing Packages Should I Use?

> The Swing API is powerful, flexible — and immense.
> The Swing API has 18 public packages:
> > |  |  |  |
> > | --- | --- | --- |
> > | `javax.accessibility` | `javax.swing.plaf` | `javax.swing.text` |
> > | `javax.swing` | `javax.swing.plaf.basic` | `javax.swing.text.html` |
> > | `javax.swing.border` | `javax.swing.plaf.metal` | `javax.swing.text.html.parser` |
> > | `javax.swing.colorchooser` | `javax.swing.plaf.multi` | `javax.swing.text.rtf` |
> > | `javax.swing.event` | `javax.swing.plaf.synth` | `javax.swing.tree` |
> > | `javax.swing.filechooser` | `javax.swing.table` | `javax.swing.undo` |
>
> Fortunately, most programs use only a small subset of the API. This trail sorts out the API for you, giving you examples of common code and pointing you to methods and classes you're likely to need. Most of the code in this trail uses only one or two Swing packages:
>
> * `javax.swing`* `javax.swing.event` (not always required)

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](compile.html)

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

**Previous page:** Getting Started with Swing
  
**Next page:** Compiling and Running Swing Programs




A browser with JavaScript enabled is required for this page to operate properly.