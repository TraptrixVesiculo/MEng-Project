[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Laying Out Components Within a Container

[Laying Out Components Within a Container](index.html)

[A Visual Guide to Layout Managers](visual.html)

[Using Layout Managers](using.html)

[How Layout Management Works](howLayoutWorks.html)

[How to Use Various Layout Managers](layoutlist.html)

[How to Use BorderLayout](border.html)

[How to Use BoxLayout](box.html)

How to Use CardLayout

[How to Use FlowLayout](flow.html)

[How to Use GridBagLayout](gridbag.html)

[How to Use GridLayout](grid.html)

[How to Use GroupLayout](group.html)

[A GroupLayout Example](groupExample.html)

[How to Use SpringLayout](spring.html)

[Creating a Custom Layout Manager](custom.html)

[Doing Without a Layout Manager (Absolute Positioning)](none.html)

[Solving Common Layout Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Laying Out Components Within a Container](index.html)

[« Previous](box.html) • [Trail](../TOC.html) • [Next »](flow.html)

# How to Use CardLayout

---

**Note:** This lesson covers writing layout code by hand, which can be challenging. If you are not interested in learning all the details of layout management, you might prefer to use the `GroupLayout` layout manager combined with a builder tool to lay out your GUI. One such builder tool is the
[NetBeans IDE](../learn/index.html). Otherwise, if you want to code by hand and do not want to use `GroupLayout`, then `GridBagLayout` is recommended as the next most flexible and powerful layout manager.

---

The following figure represents a snapshot of an application that uses the
[`CardLayout`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html) class to switch between two panels.

![A snapshot of CardLayoutDemo](../../figures/uiswing/layout/CardLayoutDemo.png)
![Another snapshot of CardLayoutDemo](../../figures/uiswing/layout/CardLayoutDemo-2.png)

Click the Launch button
to run CardLayoutDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/layout/index.html#CardLayoutDemo).

[![Launches the CardLayoutDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/CardLayoutDemo.jnlp)

The complete code of this demo is in the
[`CardLayoutDemo.java`](../examples/layout/CardLayoutDemoProject/src/layout/CardLayoutDemo.java) file.

The `CardLayout` class manages two or more components
(usually `JPanel` instances)
that share the same display space.
When using the `CardLayout` class,
let the user choose between the components by using a combo box.
The `CardLayoutDemo` application is an example to illustrate this feature.

Another way to accomplish the same task is to use a
[tabbed pane](../components/tabbedpane.html).
The following picture shows a tabbed pane version of the preceding example:

![A snapshot of TabDemo](../../figures/uiswing/layout/TabDemo.png)

Because a tabbed pane provides its own GUI,
using a tabbed pane is simpler than using the `CardLayout` class.
For example, implementing the preceding example
using a tabbed pane results in a program with
fewer lines of code.

Click the Launch button
to run TabDemo using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/layout/index.html#TabDemo).

[![Launches the TabDemo application](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/layout/ex6/TabDemo.jnlp)

The complete code of this demo is in the
[`TabDemo.java`](../examples/layout/TabDemoProject/src/layout/TabDemo.java) file.

Conceptually, each component that a `CardLayout` manages
is like a playing card or trading card in a stack,
where only the top card is visible at any time.
You can choose the card that is showing
in any of the following ways:

* By asking for either the first or last card,
  in the order it was added to the container* By flipping through the deck backwards or forwards* By specifying a card with a specific name

The `CardLayoutDemo` class uses the last scheme.

The following code snippet from the
[`CardLayoutDemo.java`](../examples/layout/CardLayoutDemoProject/src/layout/CardLayoutDemo.java) application creates the `CardLayout` object
and the components it manages.

```

//Where instance variables are declared:
JPanel cards;
final static String BUTTONPANEL = "Card with JButtons";
final static String TEXTPANEL = "Card with JTextField";

//Where the components controlled by the CardLayout are initialized:
//Create the "cards".
JPanel card1 = new JPanel();
...
JPanel card2 = new JPanel();
...

//Create the panel that contains the "cards".
cards = new JPanel(new CardLayout());
cards.add(card1, BUTTONPANEL);
cards.add(card2, TEXTPANEL);

```

To add a component to a
container that a `CardLayout` object manages,
specify a string that identifies the component being added.
For example, in this demo,
the first panel has the string `"Card with JButtons"`,
and the second panel has the string `"Card with JTextField"`.
In this demo those strings are also used in the combo box.

To choose which component a `CardLayout` object shows,
put additional code in your code example:

```

//Where the GUI is assembled:
//Put the JComboBox in a JPanel to get a nicer look.
JPanel comboBoxPane = new JPanel(); //use FlowLayout
String comboBoxItems[] = { BUTTONPANEL, TEXTPANEL };
JComboBox cb = new JComboBox(comboBoxItems);
cb.setEditable(false);
cb.addItemListener(this);
comboBoxPane.add(cb);
...
pane.add(comboBoxPane, BorderLayout.PAGE_START);
pane.add(cards, BorderLayout.CENTER);
...

//Method came from the ItemListener class implementation,
//contains functionality to process the combo box item selecting
public void itemStateChanged(ItemEvent evt) {
    CardLayout cl = (CardLayout)(cards.getLayout());
    cl.show(cards, (String)evt.getItem());
}

```

This example shows that
to use the `show` method of the `CardLayout`
class, you must set the currently visible component.
The first argument in the `show` method
is the container the `CardLayout` controls —
that is, the container of the components the `CardLayout` manages.
The second argument is the string
that identifies the component to show.
This string is the same string that was used when
adding the component to the container.

### The CardLayout API

> The following table lists the `CardLayout` class methods that are used to choose a component.
> For each method, the first argument is the container for which the `CardLayout` is the layout manager
> (the container of the cards the `CardLayout` controls).
>
> | Method | Purpose |
> | --- | --- |
> | [`first (Container parent)`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html#first(java.awt.Container)) | Flips to the first card of the container. |
> | [`next (Container parent)`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html#next(java.awt.Container)) | Flips to the next card of the container. If the currently visible card is the last one, this method flips to the first card in the layout. |
> | [`previous (Container parent)`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html#previous(java.awt.Container)) | Flips to the previous card of the container. If the currently visible card is the first one, this method flips to the last card in the layout. |
> | [`last (Container parent)`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html#last(java.awt.Container)) | Flips to the last card of the container. |
> | [`show (Container parent, String name)`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html#show(java.awt.Container,%20java.lang.String)) | Flips to the component that was added to this layout with the specified `name`, using the [`addLayoutComponent`](http://download.oracle.com/javase/7/docs/api/java/awt/CardLayout.html#addLayoutComponent(java.awt.Component,%20java.lang.Object)) method. |

### Examples that Use CardLayout

> Only one example in this
> trail
> uses `CardLayout`, and this is the
> [`CardLayoutDemo`](../examples/layout/index.html#CardLayoutDemo).
> Generally, our examples use
> [tabbed panes](../components/tabbedpane.html) instead of `CardLayout`,
> since a tabbed pane provides its own GUI.

[« Previous](box.html)
•
[Trail](../TOC.html)
•
[Next »](flow.html)

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

**Previous page:** How to Use BoxLayout
  
**Next page:** How to Use FlowLayout




A browser with JavaScript enabled is required for this page to operate properly.