[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Graphical User Interfaces
  
**Lesson:** A Brief Introduction to the Swing Package

[A Brief Introduction to the Swing Package](index.html)

What is Swing?

[A Swing Demo](demo.html)

[Home Page](../../index.html)
>
[Graphical User Interfaces](../index.html)
>
[A Brief Introduction to the Swing Package](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](demo.html)

# What is Swing?

To create a Java program with a graphical user interface (GUI),
you'll want to learn about Swing.

The Swing toolkit includes a rich set of components for building
GUIs and adding interactivity to Java applications.
Swing includes all the components you would expect from a modern
toolkit: table controls, list controls, tree controls, buttons,
and labels.

Swing is far from a simple component toolkit, however.
It includes rich undo support, a highly customizable text package,
integrated internationalization and accessibility support.
To truly leverage the cross-platform capabilities of the Java
platform, Swing supports numerous look and feels, including the
ability to create your own look and feel. The ability to create
a custom look and feel is made easier with Synth, a look and
feel specifically designed to be customized. Swing wouldn't
be a component toolkit without the basic user interface primitives
such as drag and drop, event handling, customizable painting,
and window management.

Swing is part of the Java Foundation Classes (JFC). The JFC
also include other features important to a GUI program, such
as the ability to add rich graphics functionality and the ability
to create a program that can work in different languages
and by users with different input devices.

The following list shows some of the features that Swing
and the Java Foundation Classes provide.

:   **Swing GUI Components**

    > The Swing toolkit includes a rich array of components: from basic > components, such as buttons and check boxes, to rich and complex > components, such as tables and text. > Even deceptively simple components, such as text fields, offer > sophisticated functionality, such as formatted text input > or password field behavior. > There are file browsers and dialogs to suit most needs, > and if not, customization is possible. > If none of Swing's provided components are exactly what > you need, you can leverage the basic Swing component functionality > to create your own. : **Java 2D API** > To make your application stand out; convey information > visually; or add figures, images, or animation to your GUI, > you'll want to use the > Java 2DTM API. > Because Swing is built on the 2D package, it's trivial to > make use of 2D within Swing components. Adding images, drop > shadows, compositing — it's easy with Java 2D. : **Pluggable Look-and-Feel Support** > Any program that uses Swing components has a choice of look and feel. > The JFC classes shipped by Sun and Apple provide a look > and feel that matches that of the platform. > The Synth package allows you to create your own look and feel. > The GTK+ look and feel makes hundreds of existing look and feels > available to Swing programs. > > A program can specify > the look and feel of the platform it is running on, > or it can specify to always use the Java look and feel, > and without recompiling, it will just work. > Or, you can ignore the issue and let the UI manager sort it out. **Data Transfer**: > Data transfer, via cut, copy, paste, and drag and drop, is essential > to almost any application. Support for data transfer is built into > Swing and works between Swing components within an application, > between Java applications, > and between Java and native applications. **Internationalization**: > This feature allows developers to build applications > that can interact with users worldwide in their own languages and > cultural conventions. Applications can be created that accept input > in languages that use thousands of different characters, > such as Japanese, Chinese, or Korean. > > Swing's layout managers make it easy to honor a particular > orientation required by the UI. > For example, the UI will appear right to left in a locale where the text > flows right to left. > This support is automatic: You need only code the UI once and > then it will work for left to right and right to left, as well as > honor the appropriate size of components that change as you > localize the text. **Accessibility API**: > People with disabilities use special software — assistive > technologies — that mediates the user experience for them. > Such software needs to obtain a wealth of information about the > running application in order to represent it in alternate > media: for a screen reader to read the screen with synthetic > speech or render it via a Braille display, for a screen magnifier > to track the caret and keyboard focus, for on-screen keyboards > to present dynamic keyboards of the menu choices and toolbar items > and dialog controls, and for voice control systems to know what the user > can control with his or her voice. The accessibility API enables these > assistive technologies to get the information they need, and to > programmatically manipulate the elements that make up the graphical > user interface. **Undo Framework API**: > Swing's undo framework allows developers to provide support for undo and redo. > Undo support is built in to Swing's text component. For other components, > Swing supports an *unlimited* number of actions to undo and redo, and > is easily adapted to an application. For example, > you could easily enable undo to add and remove elements from a table. **Flexible Deployment Support**: > If you want your program to run within a browser window, > you can create it as an applet and run it using Java Plug-in, > which supports a variety of browsers, such as Internet Explorer, > Firefox, and Safari. > If you want to create a program that can be launched from a browser, > you can do this with Java Web Start. > Of course, > your application can also run outside of browser as a standard > desktop application. > > For more information on deploying an application, see the > [Deployment](index.html) trail in this tutorial. This trail provides an overview of Swing capabilities, beginning with a demo that showcases many of these features. When you are ready to begin coding, the [Creating a GUI With JFC/Swing](../../uiswing/index.html) trail provides the programming techniques to take advantage of these features. Next, a demo shows many of these features.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](demo.html)

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

**Previous page:** A Brief Introduction to the Swing Package
  
**Next page:** A Swing Demo




A browser with JavaScript enabled is required for this page to operate properly.