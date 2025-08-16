[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components

[Using Swing Components](index.html)

[Using Top-Level Containers](toplevel.html)

The JComponent Class

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

[« Previous](toplevel.html) • [Trail](../TOC.html) • [Next »](text.html)

# The JComponent Class

With the exception of top-level containers,
all Swing components whose names begin with "J"
descend from the
[`JComponent`](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html) class.
For example,
`JPanel`,
`JScrollPane`,
`JButton`, and
`JTable`
all inherit from `JComponent`.
However, `JFrame` and `JDialog` don't
because they implement top-level containers.

The `JComponent` class
extends the
[`Container`](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html) class,
which itself extends
[`Component`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html).
The `Component` class includes everything from
providing layout hints
to supporting painting and events.
The `Container` class has support
for adding components to the container and
laying them out.
This section's
[API tables](#api) summarize the most often used
methods of `Component` and `Container`,
as well as of `JComponent`.
### JComponent Features
> The `JComponent` class provides
> the following functionality to its descendants:
>
> * [Tool tips](#tooltips)* [Painting and borders](#borders)* [Application-wide pluggable look and feel](#plug)* [Custom properties](#properties)* [Support for layout](#layout)* [Support for accessibility](#access)* [Support for drag and drop](#dnd)* [Double buffering](#buffer)* [Key bindings](#keyboardAction)
>
> **Tool tips**: By specifying a string with the `setToolTipText` method, you can provide help to users of a component. When the cursor pauses over the component, the specified string is displayed in a small window that appears near the component. See [How to Use Tool Tips](tooltip.html) for more information. **Painting and borders**: The `setBorder` method allows you to specify the border that a component displays around its edges. To paint the inside of a component, override the `paintComponent` method. See [How to Use Borders](../components/border.html) and [Performing Custom Painting](../painting/index.html) for details. **Application-wide pluggable look and feel**: Behind the scenes, each `JComponent` object has a corresponding `ComponentUI` object that performs all the drawing, event handling, size determination, and so on for that `JComponent`. Exactly which `ComponentUI` object is used depends on the current look and feel, which you can set using the `UIManager.setLookAndFeel` method. See [How to Set the Look and Feel](../lookandfeel/plaf.html) for details. **Custom properties**: You can associate one or more properties (name/object pairs) with any `JComponent`. For example, a layout manager might use properties to associate a constraints object with each `JComponent` it manages. You put and get properties using the `putClientProperty` and `getClientProperty` methods. For general information about properties, see [Properties](../../essential/environment/properties.html). **Support for layout**: Although the `Component` class provides layout hint methods such as `getPreferredSize` and `getAlignmentX`, it doesn't provide any way to set these layout hints, short of creating a subclass and overriding the methods. To give you another way to set layout hints, the `JComponent` class adds setter methods — `setMinimumSize`, `setMaximumSize`, `setAlignmentX`, and `setAlignmentY`. See [Laying Out Components Within a Container](../layout/index.html) for more information. **Support for accessibility**: The `JComponent` class provides API and basic functionality to help assistive technologies such as screen readers get information from Swing components, For more information about accessibility, see [How to Support Assistive Technologies](../misc/access.html). **Support for drag and drop**: The `JComponent` class provides API to set a component's transfer handler, which is the basis for Swing's drag and drop support. See [Introduction to DnD](../dnd/intro.html) for details. **Double buffering**: Double buffering smooths on-screen painting. For details, see [Performing Custom Painting](../painting/index.html). **Key bindings**: This feature makes components react when the user presses a key on the keyboard. For example, in many look and feels when a button has the focus, typing the Space key is equivalent to a mouse click on the button. The look and feel automatically sets up the bindings between pressing and releasing the Space key and the resulting effects on the button. For more information about key bindings, see [How to Use Key Bindings](../misc/keybinding.html).

### The JComponent API
> The `JComponent` class provides many new methods
> and inherits many methods
> from `Component` and `Container`.
> The following tables summarize the methods
> we use the most.
>
> * [Customizing Component Appearance](#complookapi)* [Setting and Getting Component State](#stateapi)* [Handling Events](#eventapi)* [Painting Components](#custompaintingapi)* [Dealing with the Containment Hierarchy](#containmentapi)* [Laying Out Components](#layoutapi)* [Getting Size and Position Information](#sizeapi)* [Specifying Absolute Size and Position](#absoluteapi)
>
> **Customizing Component Appearance**
>
> | Method | Purpose || [void setBorder(Border)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setBorder(javax.swing.border.Border))   [Border getBorder()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getBorder()) | Set or get the border of the component. See [How to Use Borders](../components/border.html) for details. |
> | [void setForeground(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setForegroundColor(java.awt.Color))   [void setBackground(Color)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setBackground(java.awt.Color)) Set the foreground or background color for the component. The foreground is generally the color used to draw the text in a component. The background is (not surprisingly) the color of the background areas of the component, assuming that the component is opaque. | |
> | [Color getForeground()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getForeground())   [Color getBackground()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getBackground()) Get the foreground or background color for the component. | |
> | [void setOpaque(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setOpaque(boolean))   [boolean isOpaque()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#isOpaque()) | Set or get whether the component is opaque. An opaque component fills its background with its background color. |
> | [void setFont(Font)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setFont(java.awt.Font))   [Font getFont()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getFont()) Set or get the component's font. If a font has not been set for the component, the font of its parent is returned. | |
> | [void setCursor(Cursor)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setCursor(java.awt.Cursor))  [Cursor getCursor()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getCursor()) Set or get the cursor displayed over the component and all components it contains (except for children that have their own cursor set). Example: `aPanel.setCursor( Cursor.getPredefinedCursor( Cursor.WAIT_CURSOR));` | |
>
> **Setting and Getting Component State**
>
> | Method | Purpose || [void setComponentPopupMenu(JPopupMenu)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setComponentPopupMenu(javax.swing.JPopupMenu)) Sets the `JPopupMenu` for this `JComponent`. The UI is responsible for registering bindings and adding the necessary listeners such that the `JPopupMenu` will be shown at the appropriate time. When the `JPopupMenu` is shown depends upon the look and feel: some may show it on a mouse event, some may enable a key binding.   If `popup` is null, and `getInheritsPopupMenu` returns `true`, then `getComponentPopupMenu` will be delegated to the parent. This provides for a way to make all child components inherit the `popupmenu` of the parent. | |
> | [void setTransferHandler(TransferHandler)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setTransferHandler(javax.swing.TransferHandler))   [TransferHandler getTransferHandler()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getTransferHandler()) | Set or remove the `transferHandler` property. The `TransferHandler` supports exchanging data via cut, copy, or paste to/from a clipboard as well a drag and drop. See [Introduction to DnD](../dnd/intro.html) for more details. |
> | [void setToolTipText(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setToolTipText(java.lang.String)) Set the text to display in a tool tip. See [How to Use Tool Tips](tooltip.html) for more information. | |
> | [void setName(String)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setName(java.lang.String))   [String getName()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getName()) Set or get the name of the component. This can be useful when you need to associate text with a component that does not display text. | |
> | [boolean isShowing()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#isShowing()) Determine whether the component is showing on screen. This means that the component must be visible, and it must be in a container that is visible and showing. | |
> | [void setEnabled(boolean)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setEnabled(boolean))   [boolean isEnabled()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#isEnabled()) | Set or get whether the component is enabled. An enabled component can respond to user input and generate events. |
> | [void setVisible(boolean)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setVisible(boolean))   [boolean isVisible()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#isVisible()) | Set or get whether the component is visible. Components are initially visible, with the exception of top-level components. |
>
> **Handling Events**
>   
> (see
> [Writing Event Listeners](../events/index.html) for details)
>
> | Method | Purpose || [void addHierarchyListener(hierarchyListener l)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addHierarchyListener(java.awt.event.HierarchyListener))   [void removeHierarchyListener(hierarchyListener l)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#removeHierarchyListener(java.awt.event.HierarchyListener)) | Adds or removes the specified hierarchy listener to receive hierarchy changed events from this component when the hierarchy to which this container belongs changes. If listener l is null, no exception is thrown and no action is performed. |
> | [void addMouseListener(MouseListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addMouseListener(java.awt.event.MouseListener))   [void removeMouseListener(MouseListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#removeMouseListener(java.awt.event.MouseListener)) | Add or remove a [mouse listener](../events/mouselistener.html) to or from the component. Mouse listeners are notified when the user uses the mouse to interact with the listened-to component. |
> | [void addMouseMotionListener(MouseMotionListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addMouseMotionListener(java.awt.event.MouseMotionListener))   [void removeMouseMotionListener(MouseMotionListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#removeMouseMotionListener(java.awt.event.MouseMotionListener)) | Add or remove a [mouse motion listener](../events/mousemotionlistener.html) to or from the component. Mouse motion listeners are notified when the user moves the mouse within the listened-to component's bounds. |
> | [void addKeyListener(KeyListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addKeyListener(java.awt.event.KeyListener))   [void removeKeyListener(KeyListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#removeKeyListener(java.awt.event.KeyListener)) Add or remove a [key listener](../events/keylistener.html) to or from the component. Key listeners are notified when the user types at the keyboard and the listened-to component has the keyboard focus. | |
> | [void addComponentListener(ComponentListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#addComponentListener(java.awt.event.ComponentListener))   [void removeComponentListener(ComponentListener)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#removeComponentListener(java.awt.event.ComponentListener)) Add or remove a [component listener](../events/componentlistener.html) to or from the component. Component listeners are notified when the listened-to component is hidden, shown, moved, or resized. | |
> | [boolean contains(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#contains(int, int))   [boolean contains(Point)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#contains(java.awt.Point)) | Determine whether the specified point is within the component. The argument should be specified in terms of the component's coordinate system. The two `int` arguments specify *x* and *y* coordinates, respectively. |
> | [Component getComponentAt(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentAt(int, int))  [Component getComponentAt(Point)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentAt(java.awt.Point)) | Return the component that contains the specified *x, y* position. The top-most child component is returned in the case where components overlap. This is determined by finding the component closest to the index 0 that claims to contain the given point via `Component.contains()`. |
> | [Component setComponentZOrder(component comp, int index)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentZOrder(java.awt.Component, int)) | Moves the specified component to the specified z-order index in the container.    If the component is a child of some other container, it is removed from that container before being added to this container. The important difference between this method and  `java.awt.Container.add(Component, int)` is that this method doesn't call `removeNotify` on the component while removing it from its previous container unless necessary and when allowed by the underlying native windowing system. This way, if the component has the keyboard focus, it maintains the focus when moved to the new position.   **Note:**  The z-order determines the order that components are painted. The component with the highest z-order paints first and the component with the lowest z-order paints last. Where components overlap, the component with the lower z-order paints over the component with the higher z-order. |
> | [Component getComponentZOrder(component comp)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentZOrder(comp)) | Returns the z-order index of the component inside the container. The higher a component is in the z-order hierarchy, the lower its index. The component with the lowest z-order index is painted last, above all other child components. |
>
> **Painting Components**
>   
> (see
> [Performing Custom Painting](../painting/index.html) for details)
>
> | Method | Purpose || [void repaint()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#repaint())   [void repaint(int, int, int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#repaint(int, int, int, int)) | Request that all or part of the component be repainted. The four `int` arguments specify the bounds (*x*, *y*, width, height, in that order) of the rectangle to be painted. |
> | [void repaint(Rectangle)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#repaint(java.awt.Rectangle)) | Request that the specified area within the component be repainted. |
> | [void revalidate()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#revalidate()) | Request that the component and its affected containers be laid out again. You should not generally need to invoke this method unless you explicitly change a component's size/alignment hints after it's visible or change a containment hierarchy after it is visible. Always invoke `repaint` after `revalidate`. || [void paintComponent(Graphics)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#paintComponent(java.awt.Graphics)) | Paint the component. Override this method to implement painting for custom components. |
>
> **Dealing with the Containment Hierarchy**
>   
> (see
> [Using Top-Level Containers](toplevel.html) for more information)
>
> | Method | Purpose || [Component add(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component))   [Component add(Component, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, int))   [void add(Component, Object)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#add(java.awt.Component, java.lang.Object)) | Add the specified component to this container. The one-argument version of this method adds the component to the end of the container. When present, the `int` argument indicates the new component's position within the container. When present, the `Object` argument provides layout constraints to the current layout manager. |
> | [void remove(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#remove(int))   [void remove(Component)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#remove(java.awt.Component))   [void removeAll()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#removeAll()) | Remove one of or all of the components from this container. When present, the `int` argument indicates the position within the container of the component to remove. |
> | [JRootPane getRootPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getRootPane()) | Get the root pane that contains the component. |
> | [Container getTopLevelAncestor()](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#getTopLevelAncestor()) | Get the topmost container for the component — a `Window`, `Applet`, or null if the component has not been added to any container. |
> | [Container getParent()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getParent()) | Get the component's immediate container. |
> | [int getComponentCount()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentCount()) | Get the number of components in this container. |
> | [Component getComponent(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponent(int))   [Component[] getComponents()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponents()) | Get the one of or all of the components in this container. The `int` argument indicates the position of the component to get. |
> | [Component getComponentZOrder(int)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponentZOrder(int))   [Component[] getComponentZOrder()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getComponents()) | Returns the z-order index of the component inside the container. The higher a component is in the z-order hierarchy, the lower its index. The component with the lowest z-order index is painted last, above all other child components. |
>
> **Laying Out Components**
>   
> (see
> [Laying Out Components Within a Container](../layout/index.html) for more information)
>
> | Method | Purpose || [void setPreferredSize(Dimension)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setPreferredSize(java.awt.Dimension))   [void setMaximumSize(Dimension)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setMaximumSize(java.awt.Dimension))   [void setMinimumSize(Dimension)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setMinimumSize(java.awt.Dimension)) | Set the component's preferred, maximum, or minimum size, measured in pixels. The preferred size indicates the best size for the component. The component should be no larger than its maximum size and no smaller than its minimum size. Be aware that these are hints only and might be ignored by certain layout managers. |
> | [Dimension getPreferredSize()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getPreferredSize())   [Dimension getMaximumSize()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getMaximumSize())   [Dimension getMinimumSize()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getMinimumSize()) | Get the preferred, maximum, or minimum size of the component, measured in pixels. Many JComponent classes have setter and getter methods. For those non-`JComponent` subclasses, which do not have the corresponding setter methods, you can set a component's preferred, maximum, or minimum size by creating a subclass and overriding these methods. |
> | [void setAlignmentX(float)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setAlignmentX(float))   [void setAlignmentY(float)](http://download.oracle.com/javase/7/docs/api/javax/swing/JComponent.html#setAlignmentY(float)) | Set the alignment along the *x-* or *y-* axis. These values indicate how the component would like to be aligned relative to other components. The value should be a number between 0 and 1 where 0 represents alignment along the origin, 1 is aligned the furthest away from the origin, and 0.5 is centered, and so on. Be aware that these are hints only and might be ignored by certain layout managers. |
> | [float getAlignmentX()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getAlignmentX())   [float getAlignmentY()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getAlignmentY()) | Get the alignment of the component along the *x-* or *y-* axis. For non-`JComponent` subclasses, which do not have the corresponding setter methods, you can set a component's alignment by creating a subclass and overriding these methods. |
> | [void setLayout(LayoutManager)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setLayout(java.awt.LayoutManager))   [LayoutManager getLayout()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getLayout()) | Set or get the component's layout manager. The layout manager is responsible for sizing and positioning the components within a container. |
> | [void applyComponentOrientation(ComponentOrientation)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#applyComponentOrientation(java.awt.ComponentOrientation)) [void setComponentOrientation(ComponentOrientation)](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#setComponentOrientation(java.awt.ComponentOrientation)) | Set the `ComponentOrientation` property of this container and all the components contained within it. See [Setting the Container's Orientation](../layout/using.html#orientation) for more information. |
>
> **Getting Size and Position Information**
>
> | Method | Purpose || [int getWidth()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getWidth())   [int getHeight()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getHeight()) | Get the current width or height of the component measured in pixels. |
> | [Dimension getSize()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getSize())   [Dimension getSize(Dimension)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getSize(java.awt.Dimension)) | Get the component's current size measured in pixels. When using the one-argument version of this method, the caller is responsible for creating the `Dimension` instance in which the result is returned. |
> | [int getX()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getX())   [int getY()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getY()) | Get the current *x* or y coordinate of the component's origin relative to the parent's upper left corner measured in pixels. |
> | [Rectangle getBounds()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getBounds())   [Rectangle getBounds(Rectangle)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getBounds(java.awt.Rectangle)) | Get the bounds of the component measured in pixels. The bounds specify the component's width, height, and origin relative to its parent. When using the one-argument version of this method, the caller is responsible for creating the `Rectangle` instance in which the result is returned. |
> | [Point getLocation()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getLocation())   [Point getLocation(Point)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getLocation(java.awt.Point)) | Gets the current location of the component relative to the parent's upper left corner measured in pixels. When using the one-argument version of `getLocation` method, the caller is responsible for creating the `Point` instance in which the result is returned. |
> | [Point getLocationOnScreen()](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#getLocationOnScreen()) | Returns the position relative to the upper left corner of the screen. |
> | [Insets getInsets()](http://download.oracle.com/javase/7/docs/api/java/awt/Container.html#getInsets()) | Get the size of the component's border. |
>
> **Specifying Absolute Size and Position**
>   
> (see
> [Doing Without a Layout Manager (Absolute Positioning)](../layout/none.html) for more information)
>
> | Method | Purpose || [void setLocation(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setLocation(int, int))   [void setLocation(Point)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setLocation(java.awt.Point)) | Set the location of the component, in pixels, relative to the parent's upper left corner. The two `int` arguments specify *x* and *y*, in that order. Use these methods to position a component when you are not using a layout manager. |
> | [void setSize(int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setSize(int, int))   [void setSize(Dimension)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setSize(java.awt.Dimension)) | Set the size of the component measured in pixels. The two `int` arguments specify width and height, in that order. Use these methods to size a component when you are not using a layout manager. |
> | [void setBounds(int, int, int, int)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setBounds(int, int, int, int))   [void setBounds(Rectangle)](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html#setBounds(java.awt.Rectangle)) | Set the size and location relative to the parent's upper left corner, in pixels, of the component. The four `int` arguments specify *x*, *y*, width, and height, in that order. Use these methods to position and size a component when you are not using a layout manager. |

[« Previous](toplevel.html)
•
[Trail](../TOC.html)
•
[Next »](text.html)

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

**Previous page:** Using Top-Level Containers
  
**Next page:** Using Text Components




A browser with JavaScript enabled is required for this page to operate properly.