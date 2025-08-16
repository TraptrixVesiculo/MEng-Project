[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components
  
**Section:** How to Use Various Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

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

How to Use Root Panes

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

[« Previous](progress.html) • [Trail](../TOC.html) • [Next »](scrollpane.html)

# How to Use Root Panes

In general, you don't directly create a
[`JRootPane`](http://download.oracle.com/javase/7/docs/api/javax/swing/JRootPane.html) object.
Instead, you get a `JRootPane`
(whether you want it or not!)
when you instantiate
[`JInternalFrame`](internalframe.html) or
one of the top-level Swing containers,
such as
[`JApplet`](applet.html),
[`JDialog`](dialog.html), and
[`JFrame`](frame.html).

[Using Top-Level Containers](toplevel.html)
tells you the basics of using root panes —
getting the content pane,
setting its layout manager, and
adding Swing components to it.
This section tells you more about root panes,
including the components that make up a root pane
and how you can use them.

![A root pane manages four other panes: a layered pane, a menu bar, a content pane, and a glass pane.](../../figures/uiswing/components/1layers.gif)

As the preceding figure shows, a root pane has four parts:

**The glass pane**: Hidden, by default. If you make the glass pane visible, then it's like a sheet of glass over all the other parts of the root pane. It's completely transparent unless you implement the glass pane's `paintComponent` method so that it does something, and it can intercept input events for the root pane. In the [next section](#glasspane), you'll see an example of using a glass pane. **The layered pane**: Serves to position its contents, which consist of the content pane and the optional menu bar. Can also hold other components in a specified Z order. For information, see [The Layered Pane](#layeredpane). **The content pane**: The container of the root pane's visible components, excluding the menu bar. For information on using the content pane, see [Using Top-Level Containers](toplevel.html). **The optional menu bar**: The home for the root pane's container's menus. If the container has a menu bar, you generally use the container's `setJMenuBar` method to put the menu bar in the appropriate place. For more information on using menus and menu bars, see [How to Use Menus](menu.html).

### The Glass Pane

> The glass pane is useful when you want
> to be able to catch events or paint
> over an area
> that already contains one or more components.
> For example,
> you can deactivate mouse events for a multi-component region
> by having the glass pane intercept the events.
> Or you can display an image over multiple components
> using the glass pane.
>
> Here's a picture of an application
> that demonstrates glass pane features.
> It contains a check box that lets you set
> whether the glass pane is "visible" —
> whether it can get events and
> paint itself onscreen.
> When the glass pane is visible,
> it blocks all input events from reaching
> the components in the content pane.
> It also paints a red dot in the place
> where it last detected a mouse-pressed event.
>
> ![A snapshot of GlassPaneDemo](../../figures/uiswing/components/GlassPaneDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run GlassPaneDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#GlassPaneDemo).
>
>    [![Launches the GlassPaneDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/GlassPaneDemo.jnlp)
>
>    - Click Button 1.
>        
>      The button's appearance changes to show that it's been clicked.- Click the check box so that the glass pane becomes "visible,"
>        and then click Button 1 again.
>          
>        The button does not act clicked
>        because the glass pane intercepts
>        all the mouse events.
>        The glass pane paints a red circle
>        where you release the mouse.- Click the check box again so that the glass pane is hidden.
>            
>          When the glass pane detects an event over the check box,
>          it forwards it to the check box.
>          Otherwise, the check box would not respond to clicks.
>
> ---
>
> The following code from
> [`GlassPaneDemo.java`](../examples/components/GlassPaneDemoProject/src/components/GlassPaneDemo.java) shows and hides the glass pane.
> This program happens to create its own glass pane.
> However, if a glass pane doesn't do any painting,
> the program might simply attach listeners to the default glass pane,
> as returned by `getGlassPane`.
>
> ```
>
> myGlassPane = new MyGlassPane(...);
> changeButton.addItemListener(myGlassPane);
> frame.setGlassPane(myGlassPane);
> ...
> class MyGlassPane extends JComponent
>                   implements ItemListener {
>     ...
>     //React to change button clicks.
>     public void itemStateChanged(ItemEvent e) {
>         setVisible(e.getStateChange() == ItemEvent.SELECTED);
>     }
> ...
> }
>
> ```
>
> The next code snippet
> implements the mouse-event handling for the glass pane.
> If a mouse event occurs over the check box,
> then the glass pane redispatches the event
> so that the check box receives it.
>
> ```
>
> ...//In the implementation of the glass pane's mouse listener:
> public void mouseMoved(MouseEvent e) {
>     redispatchMouseEvent(e, false);
> }
>
> .../* The mouseDragged, mouseClicked, mouseEntered,
>     * mouseExited, and mousePressed methods have the same
>     * implementation as mouseMoved. */...
>
> public void mouseReleased(MouseEvent e) {
>     redispatchMouseEvent(e, true);
> }
>
> private void redispatchMouseEvent(MouseEvent e,
>                                   boolean repaint) {
>     Point glassPanePoint = e.getPoint();
>     Container container = contentPane;
>     Point containerPoint = SwingUtilities.convertPoint(
>                                     glassPane,
>                                     glassPanePoint,
>                                     contentPane);
>
>     if (containerPoint.y < 0) { //we're not in the content pane
>         //Could have special code to handle mouse events over
>         //the menu bar or non-system window decorations, such as
>         //the ones provided by the Java look and feel.
>     } else {
>         //The mouse event is probably over the content pane.
>         //Find out exactly which component it's over.
>         Component component =
>             SwingUtilities.getDeepestComponentAt(
>                                     container,
>                                     containerPoint.x,
>                                     containerPoint.y);
>
>         if ((component != null)
>             && (component.equals(liveButton))) {
>             //Forward events over the check box.
>             Point componentPoint = SwingUtilities.convertPoint(
>                                         glassPane,
>                                         glassPanePoint,
>                                         component);
>             component.dispatchEvent(new MouseEvent(component,
>                                                  e.getID(),
>                                                  e.getWhen(),
>                                                  e.getModifiers(),
>                                                  componentPoint.x,
>                                                  componentPoint.y,
>                                                  e.getClickCount(),
>                                                  e.isPopupTrigger()));
>         }
>     }
>
>     //Update the glass pane if requested.
>     if (repaint) {
>         glassPane.setPoint(glassPanePoint);
>         glassPane.repaint();
>     }
> }
>
> ```
>
> Here is the code in `MyGlassPane`
> that implements the painting.
>
> ```
>
> protected void paintComponent(Graphics g) {
>     if (point != null) {
>         g.setColor(Color.red);
>         g.fillOval(point.x - 10, point.y - 10, 20, 20);
>     }
> }
>
> ```

### The Layered Pane

> A layered pane is
> a container with depth
> such that
> overlapping components can appear one on top of the other.
> General information about layered panes is in
> [How to Use Layered Panes](layeredpane.html).
> This section discusses the particulars of how
> root panes use layered panes.
>
> Each root pane places its menu bar and content pane
> in an instance of `JLayeredPane`.
> The Z ordering that the layered pane provides
> enables behavior such as
> displaying popup menus above other components.
>
> You can choose to put components in the root pane's layered pane.
> If you do, then you should be aware that certain depths
> are defined to be used for specific functions,
> and you should use the depths as intended.
> Otherwise, your components might not play well with the others.
> Here's a diagram that shows the functional layers
> and their relationship:
>
> ![Layers defined by JLayeredPane](../../figures/uiswing/components/layeredPaneLayers.gif)
>
> The table below describes the intended use for each layer
> and lists the `JLayeredPane` constant
> that corresponds to each layer:
>
> | Layer Name Value Description | | |
> | --- | --- | --- |
> | `FRAME_CONTENT_LAYER` `new Integer(-30000)` | The root pane adds the menu bar and content pane to its layered pane at this depth. | |
> | `DEFAULT_LAYER` `new Integer(0)` | If you don't specify a component's depth when adding it to a layered pane, the layered pane puts it at this depth. | |
> | `PALETTE_LAYER` `new Integer(100)` | This layer is useful for floating tool bars and palettes. | |
> | `MODAL_LAYER` `new Integer(200)` | Modal internal-frame dialogs would belong in this layer. | |
> | `POPUP_LAYER` `new Integer(300)` | Popups go in this layer because they need to appear above just about everything. | |
> | `DRAG_LAYER` `new Integer(400)` | Intended to be used when a component is being dragged. The component should return to its regular layer when dropped. | |
>
> Here is a picture of RootLayeredPaneDemo,
> which is a version of
> [LayeredPaneDemo](../examples/components/index.html#LayeredPaneDemo)
> that uses the root pane's layered pane,
> rather than creating a new layered pane.
>
> ![LayeredPaneDemo modified to use the root pane's layered pane](../../figures/uiswing/components/RootLayeredPaneDemo.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run RootLayeredPaneDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
>    Alternatively, to compile and run the example yourself,
>    consult the
>    [example index](../examples/components/index.html#RootLayeredPaneDemo).
>
>    [![Launches the RootLayeredPaneDemo](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/RootLayeredPaneDemo.jnlp)
>
>    - Move the cursor around in the window,
>      so that Duke moves on top of other components.
>        
>      Note that when the cursor is on top of non-label components —
>      whether it's
>      in the content pane or
>      in the Java-look-and-feel provided title bar
>      —
>      Duke's movement is temporarily stopped.
>      This is because mouse-motion events go to the component that's
>      deepest in the containment hierarchy
>      and is interested in mouse events.
>      The mouse-motion listener that moves Duke
>      is registered on the layered pane,
>      and most of the components in that pane
>      (with the exception of the labels)
>      happen to have mouse-motion listeners.
>      When the mouse moves over an interested component
>      in the layered pane,
>      the layered pane doesn't get the event
>      and the interested component does.- Making sure the Top Position in Layer check box is selected,
>        change Duke's layer to Yellow (-30000).
>          
>        As before, he appears on top of other components,
>        except for the Magenta (0) and Cyan (301) rectangles.- Keeping Duke in the Yellow layer,
>          click the check box to send Duke to the back of layer -30000.
>            
>          Duke disappears because the content pane
>          and all the components in it are now above him.- Change Duke's layer to Cyan (301), move Duke
>            down a bit so he's standing on the top edge of the Yellow rectangle,
>            and then press Space to bring up the
>            combo box's drop-down list.
>              
>            If the look and feel implements the drop-down list
>            as a lightweight popup,
>            Duke appears on top of the drop-down list.
>
> ---

### The Root Pane API

> The tables that follow list the API
> for using root panes, glass panes,
> and content panes.
> For more information on using content panes,
> go to [Using Top-Level Containers](toplevel.html).
> Here are the tables in this section:
>
> * [Using a Root Pane](#rootpaneapi)* [Setting or Getting the Root Pane's Contents](#contentapi)
>
> The API for using other parts of the root pane
> is described elsewhere:
>
> * [The Layered Pane API](layeredpane.html#api)* [The Menu API](menu.html#api)
>
> Using a Root Pane
>
> | Method | Purpose |
> | [JRootPane getRootPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getRootPane())   *(in `JApplet`, `JDialog`, `JFrame`, `JInternalFrame`, and `JWindow`)* | Get the root pane of the applet, dialog, frame, internal frame, or window. |
> | [static JRootPane getRootPane(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingUtilities.html#getRootPane(java.awt.Component))  *(in `SwingUtilities`)* | If the component contains a root pane, return that root pane. Otherwise, return the root pane (if any) that contains the component. |
> | [JRootPane getRootPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getRootPane())   *(in `JComponent`)* | Invoke the `SwingUtilities` `getRootPane` method for the `JComponent`. |
> | [void setDefaultButton(JButton)](http://download.oracle.com/javase/7/docs/api/javax/swing/JRootPane.html#setDefaultButton(javax.swing.JButton))   [JButton getDefaultButton()](http://download.oracle.com/javase/7/docs/api/javax/swing/JRootPane.html#getDefaultButton()) | Set or get which button (if any) is the default button in the root pane. A look-and-feel-specific action, such as pressing Enter, causes the button's action to be performed. |
>
> Setting or Getting the Root Pane's Contents
>   
> *The following methods are defined in
> `JApplet`,
> `JDialog`,
> `JFrame`,
> `JInternalFrame`,
> `JRootPane`, and
> `JWindow`,
> unless noted otherwise.*
>
> | Method | Purpose |
> | [void setGlassPane(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setGlassPane(java.awt.Component))   [Component getGlassPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getGlassPane()) | Set or get the glass pane. |
> | [void setLayeredPane(JLayeredPane)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setLayeredPane(javax.swing.JLayeredPane))   [Container getLayeredPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getLayeredPane()) | Set or get the layered pane. |
> | [void setContentPane(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setContentPane(java.awt.Container))   [Container getContentPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getContentPane()) | Set or get the content pane. |
> | [void setJMenuBar(JMenuBar)](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#setJMenuBar(javax.swing.JMenuBar))   [JMenuBar getJMenuBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JFrame.html#getJMenuBar())  *(not defined in `JWindow`)* | Set or get the menu bar. |

### Examples that Use Root Panes

> Every Swing program has a root pane,
> but few reference it directly.
> The examples in the following list
> illustrate how to use features of `JRootPane`
> or the glass pane.
> Also see these lists:
>
> * [Examples that Use Layered Panes](layeredpane.html#eg)* [Examples that Use Menus](menu.html#eg)* [Examples that Use Frames](frame.html#eg)
>       (for examples of using content panes)
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`GlassPaneDemo`](../examples/components/index.html#GlassPaneDemo) | This section | Uses a glass pane that paints a bit and redispatches events. |
> | [`RootLayeredPaneDemo`](../examples/components/index.html#RootLayeredPaneDemo) | This section | Adapts LayeredPaneDemo to use the root pane's layered pane. |
> | [`ListDialog`](../examples/components/index.html#ListDialog) | [How to Use Lists](list.html) | Sets the default button for a `JDialog`. |
> | [`FrameDemo2`](../examples/components/index.html#FrameDemo2) | [How to Make Frames](frame.html) | Sets the default button for a `JFrame`. |

[« Previous](progress.html)
•
[Trail](../TOC.html)
•
[Next »](scrollpane.html)

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

**Previous page:** How to Use Progress Bars
  
**Next page:** How to Use Scroll Panes




A browser with JavaScript enabled is required for this page to operate properly.