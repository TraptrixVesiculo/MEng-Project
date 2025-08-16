[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components

[Using Swing Components](index.html)

Using Top-Level Containers

[The JComponent Class](jcomponent.html)

[Using Text Components](text.html)

[Text Component Features](generaltext.html)

[The Text Component API](textapi.html)

[How to Use Various Components](componentlist.html)

[How to Make Applets](applet.html)

[How to Use Buttons, Check Boxes, and Radio Buttons](button.html)

[How to Use the ButtonGroup Component](buttongroup.html)

[How to Use Color Choosers](colorchooser.html)

[How to Use Combo Boxes](combobox.html)

[How to Make Dialogs](dialog.html)

[How to Use Editor Panes and Text Panes](editorpane.html)

[How to Use File Choosers](filechooser.html)

[How to Use Formatted Text Fields](formattedtextfield.html)

[How to Make Frames (Main Windows)](frame.html)

[How to Use Internal Frames](internalframe.html)

[How to Use Labels](label.html)

[How to Use Layered Panes](layeredpane.html)

[How to Use Lists](list.html)

[How to Use Menus](menu.html)

[How to Use Panels](panel.html)

[How to Use Password Fields](passwordfield.html)

[How to Use Progress Bars](progress.html)

[How to Use Root Panes](rootpane.html)

[How to Use Scroll Panes](scrollpane.html)

[How to Use Separators](separator.html)

[How to Use Sliders](slider.html)

[How to Use Spinners](spinner.html)

[How to Use Split Panes](splitpane.html)

[How to Use Tabbed Panes](tabbedpane.html)

[How to Use Tables](table.html)

[How to Use Text Areas](textarea.html)

[How to Use Text Fields](textfield.html)

[How to Use Tool Bars](toolbar.html)

[How to Use Tool Tips](tooltip.html)

[How to Use Trees](tree.html)

[How to Use HTML in Swing Components](html.html)

[How to Use Models](model.html)

[How to Use Icons](icon.html)

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](jcomponent.html)

# Using Top-Level Containers

As we mentioned before,
Swing provides three generally useful top-level container classes:
[`JFrame`](frame.html),
[`JDialog`](dialog.html), and
[`JApplet`](applet.html).
When using these classes,
you should keep these facts in mind:

* To appear onscreen,
  every GUI component must be part of
  a *containment hierarchy*.
  A containment hierarchy is a tree of components
  that has a top-level container as its root.
  We'll show you one in a bit.

  * Each GUI component can be contained only once.
    If a component is already in a container
    and you try to add it to another container,
    the component will be removed from the first container
    and then added to the second.

    * Each top-level container has a
      content pane that, generally speaking, contains
      (directly or indirectly)
      the visible components in that top-level container's GUI.

      * You can optionally add a menu bar to a
        top-level container. The menu bar
        is by convention positioned within the top-level container,
        but outside the content pane.
        Some look and feels,
        such as the Mac OS look and feel,
        give you the option of placing the menu bar
        in another place more appropriate for the look and feel,
        such as at the top of the screen.

---

**Note:** 
Although [`JInternalFrame`](internalframe.html)
mimics `JFrame`,
internal frames aren't actually top-level containers.

---
Here's a picture of a frame created by an application.
The frame contains a green menu bar (with no menus)
and, in the frame's content pane,
a large blank, yellow label.

|  |  |
| --- | --- |
| A simple application with a frame that contains a menu bar and a content pane. | A diagram of the frame's major parts |

You can find the entire source for this example in
[`TopLevelDemo.java`](../examples/components/TopLevelDemoProject/src/components/TopLevelDemo.java).
Although the example uses a `JFrame` in
a standalone application, the same concepts apply
to `JApplet`s and `JDialog`s.

Here's the containment hierarchy for this example's GUI:

![Containment hierarchy for the TopLeveDemo example's GUI.](../../figures/uiswing/components/3jframe.gif)

As the ellipses imply,
we left some details out of this diagram.
We reveal the missing details a bit later.
Here are the topics this section discusses:

* [Top-Level Containers and Containment Hierarchies](#general)* [Adding Components to the Content Pane](#contentpane)* [Adding a Menu Bar](#menubar)* [The Root Pane (a.k.a. The Missing Details)](#rootpane)

### Top-Level Containers and Containment Hierarchies
> Each program that uses Swing components has at least one
> top-level container.
> This top-level container is the root of a containment hierarchy —
> the hierarchy that contains all of the Swing components
> that appear inside the top-level container.
>
> As a rule, a standalone application with a Swing-based GUI
> has at least one containment
> hierarchy with a `JFrame` as its root.
> For example, if an application has one main window and two dialogs,
> then the application has three containment hierarchies,
> and thus three top-level containers.
> One containment hierarchy has a `JFrame`
> as its root,
> and each of the other two has a `JDialog` object
> as its root.
>
> A Swing-based applet has at least one containment hierarchy,
> exactly one of which is rooted by a `JApplet` object.
> For example, an applet that brings up a dialog
> has two containment hierarchies.
> The components in the browser window
> are in a containment hierarchy
> rooted by
> a `JApplet` object.
> The dialog has a containment hierarchy
> rooted by a `JDialog` object.

### Adding Components to the Content Pane
> Here's the code that the preceding example
> uses to get a frame's content pane and add the yellow
> label to it:
>
> ```
>
> frame.getContentPane().add(yellowLabel, BorderLayout.CENTER);
>
> ```
>
> As the code shows,
> you find the content pane of a top-level container
> by calling the `getContentPane` method.
> The default content pane is
> a simple intermediate container
> that inherits from `JComponent`,
> and that uses a `BorderLayout`
> as its layout manager.
>
> It's easy to customize the content pane —
> setting the layout manager
> or adding a border, for example.
> However, there is one tiny gotcha.
> The `getContentPane` method
> returns a `Container` object,
> not a `JComponent` object.
> This means that if you want
> to take advantage of the content pane's `JComponent` features,
> you need to either typecast the return value
> or create your own component to be the content pane.
> Our examples generally take the second approach,
> since it's a little cleaner.
> Another approach
> we sometimes take is to simply add a customized component
> to the content pane,
> covering the content pane completely.
>
> Note that the default layout manager for `JPanel`
> is `FlowLayout`;
> you'll probably want to change it.
>
> To make a component the content pane,
> use the top-level container's
> `setContentPane` method.
> For example:
>
> ```
>
> //Create a panel and add components to it.
> JPanel contentPane = new JPanel(new BorderLayout());
> contentPane.setBorder(someBorder);
> contentPane.add(someComponent, BorderLayout.CENTER);
> contentPane.add(anotherComponent, BorderLayout.PAGE_END);
>
>
> topLevelContainer.setContentPane(contentPane);
>
> ```
>
> ---
>
> **Note:** 
> As a convenience, the `add` method and its variants,
> `remove` and `setLayout` have been overridden
> to forward to the `contentPane` as necessary.
> This means you can write
>
> ```
> frame.add(child);
> ```
>
> and the child will be added to the `contentPane.`   
>   
> Note that only these three methods do this. This means that `getLayout()` will not return the layout set with `setLayout()`.
>
>
> ---

### Adding a Menu Bar
> In theory, all top-level containers can hold a menu bar.
> In practice, however, menu bars usually appear only in frames
> and applets.
> To add a menu bar to a top-level container, create a `JMenuBar` object,
> populate it with menus,
> and then call `setJMenuBar`.
> The `TopLevelDemo` adds a menu bar
> to its frame with this code:
>
> ```
>
> frame.setJMenuBar(greenMenuBar);
>
> ```
>
> For more information about implementing menus
> and menu bars, see
> [How to Use Menus](menu.html).

### The Root Pane
> Each top-level container relies on a reclusive intermediate container
> called the *root pane*.
> The root pane manages the content pane and the menu bar,
> along with a couple of other containers.
> You generally don't need to know about root panes
> to use Swing components.
> However, if you ever need to intercept mouse clicks
> or paint over multiple components,
> you should get acquainted with root panes.
>
> Here's a list of the components that a root pane provides
> to a frame (and to every other top-level container):
>
> ![A root pane manages four other panes: a layered pane, a menu bar, a content pane, and a glass pane.](../../figures/uiswing/../ui/ui-rootPane.gif)
>
> We've already told you about the content pane and the optional menu bar.
> The two other components that a root pane adds
> are a layered pane and a glass pane.
> The layered pane contains the menu bar and content pane,
> and enables Z-ordering of other components.
> The glass pane is often used to intercept input events
> occuring over the top-level container,
> and can also be used to paint over multiple components.
>
> For more details, see
> [How to Use Root Panes](rootpane.html).

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](jcomponent.html)

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

**Previous page:** Using Swing Components
  
**Next page:** The JComponent Class




A browser with JavaScript enabled is required for this page to operate properly.