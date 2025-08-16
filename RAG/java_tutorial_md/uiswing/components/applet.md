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

How to Make Applets

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

[« Previous](componentlist.html) • [Trail](../TOC.html) • [Next »](button.html)

# How to Make Applets

This section covers `JApplet` —
a class that enables applets to use Swing components.
`JApplet` is a subclass of
[`java.applet.Applet`](http://download.oracle.com/javase/7/docs/api/java/applet/Applet.html), which is covered in the
[Applets](../../deployment/applet/index.html) trail. If you've never written a regular applet before,
we urge you to read that trail
before proceeding with this section.
The information provided in that trail
applies to Swing applets,
with a few exceptions that this section explains.

Any applet that contains Swing components must be
implemented with a subclass of
[`JApplet`](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html).
Here's a Swing version of one of the applets that helped make Java famous
—
an animation applet that (in its most well known configuration)
shows our mascot Duke doing cartwheels:

Your browser is completely ignoring the <APPLET> tag!

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

You can find the main source code for this applet in
[`TumbleItem.java`](../examples/components/TumbleItemProject/src/components/TumbleItem.java).

This section discusses the following topics:

* [Features Provided by JApplet](#features)* [Threads in Applets](#thread)* [Using Images in a Swing Applet](#images)* [Embedding an Applet in an HTML Page](#plugin)* [The JApplet API](#api)* [Applet Examples](#eg)

### Features Provided by JApplet

> Because `JApplet` is a top-level Swing container,
> each Swing applet has a root pane.
> The most noticeable effects of the root pane's presence
> are support for adding a [menu bar](menu.html)
> and the need to use a content pane.
>
> As described in
> [Using Top-Level Containers](toplevel.html),
> each top-level container such as a `JApplet`
> has a single content pane.
> The content pane makes Swing applets
> different from regular applets in the following ways:
>
> * You add components to a Swing applet's content pane,
>   not directly to the applet.
>   [Adding Components to the Content Pane](toplevel.html#contentpane)
>   shows you how.* You set the layout manager on a Swing applet's content pane,
>     not directly on the applet.* The default layout manager for a Swing applet's content pane is
>       `BorderLayout`.
>       This differs from the default layout manager for
>       `Applet`, which is `FlowLayout`.* You should not put painting code directly in a `JApplet`
>         object.
>         See
>         [Performing Custom Painting](../painting/index.html) for examples of how to perform custom painting in applets.

### Threads in Applets

> Swing components should be created, queried, and manipulated
> on the event-dispatching thread,
> but browsers don't invoke applet "milestone" methods
> from that thread.
> For this reason,
> the milestone methods —
> `init`,
> `start`,
> `stop`,
> and `destroy` —
> should use the `SwingUtilities` method
> `invokeAndWait`
> (or, if appropriate, `invokeLater`)
> so that code that refers to the Swing components
> is executed on the event-dispatching thread.
> More information about these methods and the event-dispatching thread
> is in
> [Concurrency in Swing](../concurrency/index.html).
>
> Here is an example of an `init` method:
>
> ```
>
> public void init() {
>     //Execute a job on the event-dispatching thread:
>     //creating this applet's GUI.
>     try {
>         javax.swing.SwingUtilities.invokeAndWait(new Runnable() {
>             public void run() {
>                 createGUI();
>             }
>         });
>     } catch (Exception e) {
>         System.err.println("createGUI didn't successfully complete");
>     }
> }
>
> private void createGUI() {
>     JLabel label = new JLabel(
>                        "You are successfully running a Swing applet!");
>     label.setHorizontalAlignment(JLabel.CENTER);
>     label.setBorder(BorderFactory.createMatteBorder(1,1,1,1,Color.black));
>     getContentPane().add(label, BorderLayout.CENTER);
> }
>
> ```
>
> The `invokeLater` method
> is not appropriate for this implementation
> because it allows `init`
> to return before initialization is complete,
> which can cause applet problems
> that are difficult to debug.
>
> The `init` method in `TumbleItem`
> is more complex,
> as the
> following code shows.
> Like the first example,
> this `init` method implementation
> uses `SwingUtilities.invokeAndWait`
> to execute the GUI creation code
> on the event-dispatching thread.
> This `init` method
> sets up a
> [Swing timer](../misc/timer.html) to fire action events the update the animation.
> Also, `init` uses
> [`javax.swing.SwingWorker`](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html) to create a background task
> that loads the animation image files,
> letting the applet present a GUI
> right away, without waiting for all resources to be loaded.
>
> ```
>
> private void createGUI() {
>     ...
>     animator = new Animator();
>     animator.setOpaque(true);
>     animator.setBackground(Color.white);
>     setContentPane(animator);
>     ...
> }
>
> public void init() {
>     loadAppletParameters();
>
>     //Execute a job on the event-dispatching thread:
>     //creating this applet's GUI.
>     try {
>         javax.swing.SwingUtilities.invokeAndWait(new Runnable() {
>             public void run() {
>                 createGUI();
>             }
>         });
>     } catch (Exception e) { 
>         System.err.println("createGUI didn't successfully complete");
>     }
>
>     //Set up the timer that will perform the animation.
>     timer = new javax.swing.Timer(speed, this);
>     timer.setInitialDelay(pause);
>     timer.setCoalesce(false);
>     timer.start(); //Start the animation.
>
>     //Background task for loading images.
>     SwingWorker worker = (new SwingWorker() {
>             public ImageIcon[] doInBackground() {
>                 final ImageIcon[] innerImgs = new ImageIcon[nimgs];
>             ...//Load all the images...
>             return imgs;
>         }
>         public void done() {
>             //Remove the "Loading images" label.
>             animator.removeAll();
>             loopslot = -1;
>             try {
>                 imgs = get();
>             } ...//Handle possible exceptions
>         }
>
>     }).execute();
> }
>
> ```
>
> You can find the applet's source code in
> [`TumbleItem.java`](../examples/components/TumbleItemProject/src/components/TumbleItem.java).
> To find all the files required for the applet,
> see the
> [example index](../examples/components/index.html#TumbleItem).

### Using Images in a Swing Applet

> The `Applet` class provides the
> `getImage` method for
> loading images into an applet.
> The `getImage` method creates
> and returns an `Image` object
> that represents the loaded image.
> Because Swing components use `Icon`s
> rather than `Image`s to refer to pictures,
> Swing applets tend not to use `getImage`.
> Instead Swing applets create instances of
> `ImageIcon` — an icon loaded from an image file.
> `ImageIcon` comes with a code-saving benefit:
> it handles image tracking automatically.
> Refer to
> [How to Use Icons](../components/icon.html) for more information.
>
> The animation of Duke doing cartwheels
> requires 17 different pictures.
> The applet uses one `ImageIcon` per picture
> and loads them in its `init` method.
> Because images can take a long time to load,
> the icons are loaded in a separate thread
> implemented by a `SwingWorker` object.
> Here's the code:
>
> ```
>
> public void init() {
>     ...
>     imgs = new ImageIcon[nimgs];
>     (new SwingWorker() {
>         public ImageIcon[] doInBackground() {
>             //Images are numbered 1 to nimgs,
>             //but fill array from 0 to nimgs-1.
>             for (int i = 0; i < nimgs; i++) {
>                 imgs[i] = loadImage(i+1);
>             }
>             return imgs;
>         }
>         ...
>     }).execute();
>
> }
> ...
> protected ImageIcon loadImage(int imageNum) {
>     String path = dir + "/T" + imageNum + ".gif";
>     int MAX_IMAGE_SIZE = 2400;  //Change this to the size of
>                                  //your biggest image, in bytes.
>     int count = 0;
>     BufferedInputStream imgStream = new BufferedInputStream(
>        this.getClass().getResourceAsStream(path));
>     if (imgStream != null) {
>         byte buf[] = new byte[MAX_IMAGE_SIZE];
>         try {
>             count = imgStream.read(buf);
>             imgStream.close();
>         } catch (java.io.IOException ioe) {
>             System.err.println("Couldn't read stream from file: " + path);
>             return null;
>         }
>         if (count <= 0) {
>             System.err.println("Empty file: " + path);
>             return null;
>         }
>         return new ImageIcon(Toolkit.getDefaultToolkit().createImage(buf));
>     } else {
>         System.err.println("Couldn't find file: " + path);
>         return null;
>     }
> }
>
> ```
>
> The `loadImage` method
> loads the image for the specified frame of animation.
> It uses
> the `getResourceAsStream` method
> rather than the usual `getResource` method
> to get the images.
> The resulting code isn't pretty,
> but `getResourceAsStream`
> is more efficient than `getResource`
> for loading images from JAR files into applets that are executed
> using Java Plug-inTM software.
> For further details, see
> [Loading Images Into Applets](../components/icon.html#applet).

### Embedding an Applet in an HTML Page

> You can deploy a simple applet by using the `applet`
> tag.
> Here's the `applet` tag for the cartwheeling Duke applet:
>
> ```
>
> <applet code="TumbleItem.class" 
>         codebase="examples/"
>         archive="tumbleClasses.jar, tumbleImages.jar"
>         width="600" height="95">
>     <param name="maxwidth" value="120">
>     <param name="nimgs" value="17">
>     <param name="offset" value="-57">
>     <param name="img" value="images/tumble">
>
> Your browser is completely ignoring the <applet> tag!
> </applet>
>
> ```
>
> To deploy more sophisticated applets that will work seamlessly in multiple environments,
> see
> [Deploying an Applet](../../deployment/applet/deployingApplet.html) in the
> [Applets](../../deployment/applet/index.html) lesson.

### The JApplet API

> The next table lists the interesting methods
> that `JApplet` adds to the applet API.
> They give you access to features provided by the root pane.
> Other methods you might use are defined by the
> [`Component`](http://download.oracle.com/javase/7/docs/api/java/awt/Component.html) and
> [`Applet`](http://download.oracle.com/javase/7/docs/api/java/applet/Applet.html) classes.
> See [Component Methods](jcomponent.html#complookapi)
> for a list of commonly used `Component` methods,
> and
> [Applets](../../deployment/applet/index.html) for help in using `Applet` methods.
>
> | Method | Purpose |
> | --- | --- |
> | [void setContentPane(Container)](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#setContentPane(java.awt.Container))   [Container getContentPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#getContentPane()) | Set or get the applet's content pane. The content pane contains the applet's visible GUI components and should be opaque. |
> | [void setRootPane(JRootPane)](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#setRootPane(javax.swing.JRootPane))   [JRootPane getRootPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#getRootPane()) | Create, set, or get the applet's root pane. The root pane manages the interior of the applet including the content pane, the glass pane, and so on. |
> | [void setJMenuBar(JMenuBar)](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#setJMenuBar(javax.swing.JMenuBar))   [JMenuBar getJMenuBar()](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#getJMenuBar()) | Set or get the applet's menu bar to manage a set of menus for the applet. |
> | [void setGlassPane(Component)](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#setGlassPane(java.awt.Component))   [Component getGlassPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#getGlassPane()) | Set or get the applet's glass pane. You can use the glass pane to intercept mouse events. |
> | [void setLayeredPane(JLayeredPane)](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#setLayeredPane(javax.swing.JLayeredPane))   [JLayeredPane getLayeredPane()](http://download.oracle.com/javase/7/docs/api/javax/swing/JApplet.html#getLayeredPane()) | Set or get the applet's layered pane. You can use the applet's layered pane to put components on top of or behind other components. |

### Applet Example

> This table shows examples of Swing applets
> and where those examples are described.
>
> | Example | Where Described | Notes |
> | --- | --- | --- |
> | [`TumbleItem`](../examples/components/index.html#TumbleItem) | This page | An animation applet |

[« Previous](componentlist.html)
•
[Trail](../TOC.html)
•
[Next »](button.html)

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

**Previous page:** How to Use Various Components
  
**Next page:** How to Use Buttons, Check Boxes, and Radio Buttons




A browser with JavaScript enabled is required for this page to operate properly.