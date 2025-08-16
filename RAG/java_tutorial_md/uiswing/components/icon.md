[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Using Swing Components

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

How to Use Icons

[How to Use Borders](border.html)

[Solving Common Component Problems](problems.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Using Swing Components](index.html)

[« Previous](model.html) • [Trail](../TOC.html) • [Next »](border.html)

# How to Use Icons

Many Swing components, such as labels, buttons, and tabbed
panes, can be decorated with an *icon* — a
fixed-sized picture. An icon is an object that adheres to the
[`Icon`](http://download.oracle.com/javase/7/docs/api/javax/swing/Icon.html)
interface. Swing provides a particularly useful implementation
of the `Icon` interface:
[`ImageIcon`](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html), which paints an icon from a GIF, JPEG, or PNG image.

Here's a snapshot of an application with three labels, two
decorated with an icon:

![An example of using image icons to decorate labels.](../../figures/uiswing/components/LabelDemoMetal.png)

The program uses one image icon to contain and paint the
yellow splats. One statement creates the image icon and two
more statements include the image icon on each of the two
labels:

```

ImageIcon icon = createImageIcon("images/middle.gif",
                                 "a pretty but meaningless splat");
label1 = new JLabel("Image and Text", icon, JLabel.CENTER);
...
label3 = new JLabel(icon);

```

The `createImageIcon` method (used in the
preceding snippet) is one we use in many of our code samples.
It finds the specified file and returns an
`ImageIcon` for that file, or `null`
if that file couldn't be found. Here is a typical
implementation:

```

/** Returns an ImageIcon, or null if the path was invalid. */
protected ImageIcon createImageIcon(String path,
                                           String description) {
    java.net.URL imgURL = getClass().getResource(path);
    if (imgURL != null) {
        return new ImageIcon(imgURL, description);
    } else {
        System.err.println("Couldn't find file: " + path);
        return null;
    }
}

```

In the preceding snippet, the first argument to the
`ImageIcon` constructor is relative to the location
of the current class, and will be resolved to an
absolute URL. The `description` argument is a string
that allows [assistive technologies](../misc/access.html)
to help a visually impaired user understand what information the
icon conveys.

Generally, applications provide their own set of images used
as part of the application, as is the case with the images used
by many of our demos. You should use the
`Class` `getResource` method to obtain the
path to the image. This allows the application to verify that
the image is available and to provide sensible error handling if
it is not. When the image is not part of the application,
`getResource` should not be used and the
`ImageIcon` constructor is used directly. For
example:

```

ImageIcon icon = new ImageIcon("images/middle.gif",
                               "a pretty but meaningless splat");

```

When you specify a filename or URL to an `ImageIcon`
constructor, processing is blocked until after the image data is
completely loaded or the data location has proven to be invalid.
If the data location is invalid (but non-null), an
`ImageIcon` is still successfully created; it just
has no size and, therefore, paints nothing. As shown in the
`createImageIcon` method, it is advisable to first
verify that the URL points to an existing file before passing it
to the `ImageIcon` constructor. This allows graceful
error handling when the file isn't present. If you want more
information while the image is loading, you can register an
observer on an image icon by calling its
`setImageObserver` method.

Under the covers, each image icon uses an
[`Image`](http://download.oracle.com/javase/7/docs/api/java/awt/Image.html)
object to hold the image data.

The rest of this section covers the following topics:

* [A More Complex Image Icon Example](#example)
* [Loading Images Using getResource](#getresource)
* [Loading Images Into Applets](#applet)
* [Improving Perceived Performance When Loading Image Icons](#efficiency)
* [Creating a Custom Icon Implementation](#custom)
* [The Image Icon API](#api)
* [Examples that Use Icons](#eg)

### A More Complex Image Icon Example
> Here's an application that uses six image icons. Five of them display thumbnail
> images and the sixth diplays the full size the photograph.
>
> ![The initial view of the IconDemo application.](../../figures/uiswing/components/IconDemoApp.png)
>
> ---
>
> **Try this:**
>
> 1. Click the Launch button to run IconDemo using
>    [Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp)
>    ([download
>    JDK 6](http://java.sun.com/javase/downloads/index.jsp)). Or, to compile and run the example yourself, consult
>    the [example
>    index](../examples/components/index.html#IconDemo).
>
>    [![Launches the IconDemo example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/components/ex6/IconDemo.jnlp)
> 2. Click any of the thumbnail images to view the full size photographs.
> 3. Hold the mouse over a photograph. A tool tip appears that
>    displays the photograph caption.
>
> ---
>
> > **IconDemoApp** demonstrates icons used in the
> > following ways:
> >
> > * As a GUI element attached to a button (the thumbnail images on the buttons).
> > * To display an image (the five photographs).
> >
> > The photographs are loaded in a separate thread by
> > `loadimages.execute`. The `loadimages`
> > code is shown a little later in this section.
> >
> > The `ThumbnailAction` class, an inner class in
> > [`IconDemoApp.java`](../examples/components/IconDemoProject/src/components/IconDemoApp.java), is a descendant of `AbstractAction` that manages our full
> > size image icon, a thumbnail version, and its description.
> > When the `actionPerformed` method is called the full size image
> > is loaded into the main display area. Each button has its own instance of
> > `ThumbnailAction` which specifies a different image to show.
> >
> > ```
> >
> > /**
> >  * Action class that shows the image specified in it's constructor.
> >  */
> > private class ThumbnailAction extends AbstractAction{
> >     
> >     /**
> >      *The icon if the full image we want to display.
> >      */
> >     private Icon displayPhoto;
> >     
> >     /**
> >      * @param Icon - The full size photo to show in the button. 
> >      * @param Icon - The thumbnail to show in the button.
> >      * @param String - The descriptioon of the icon.  
> >      */
> >     public ThumbnailAction(Icon photo, Icon thumb, String desc){
> >         displayPhoto = photo;
> >         
> >         // The short description becomes the tooltip of a button.
> >         putValue(SHORT_DESCRIPTION, desc);
> >         
> >         // The LARGE_ICON_KEY is actually the key for setting the 
> >         // icon when an Action is applied to a button.
> >         putValue(LARGE_ICON_KEY, thumb);
> >     }
> >     
> >     /**
> >      * Shows the full image in the main area and sets the application title.
> >      */
> >     public void actionPerformed(ActionEvent e) {
> >         photographLabel.setIcon(displayPhoto);
> >         setTitle("Icon Demo: " + getValue(SHORT_DESCRIPTION).toString());
> >     }
> > }
> >
> > ```
>
> ### Loading Images Using getResource
> > Most often, an image icon's data comes from an image file.
> > There are a number of valid ways that your application's class
> > and image files may be configured on your file server. You
> > might have your class files in a JAR file, or your image files
> > in a JAR file; they might be in the same JAR file, or they might
> > be in different JAR files. The following figures illustrate a
> > few of the ways these files can be configured:
> >
> > |  |  |
> > | --- | --- |
> > | Diagram showing MyDemo.class and images/myImage.png under the parent directory | Diagram showing MyDemo.class and image.jar under the parent directory |
> > | Class file next to an image directory containing the image file, in PNG format. | Class file in same directory as JAR file. The JAR file was created with all the images in an `images` directory. |
> > | Diagram showing MyDemo.jar and image.jar under the parent directory | Diagram showing MyDemo.class and images/myImage.png in the same JAR file |
> > | Class file in one JAR file and the images in another JAR file. | Class and image files in same JAR file. |
> >
> > If you are writing a real-world application, it is likely (and
> > recommended) that you put your files into a package. For more
> > information on packages, see
> > [Creating and Using Packages](../../java/package/packages.html)
> > in the
> > [Learning the Java Language](../../java/)
> > trail. Here are some possible configurations using a package named
> > "omega":
> >
> > |  |  |
> > | --- | --- |
> > | Diagram showing omega package with MyDemo.class and image/myImage.png | Diagram showing omega package with MyDemo.class and image.jar |
> > | Class file in directory named `omega`. Image in `omega/images` directory. | Class file in `omega` directory. Image in JAR file not inside of `omega` directory, but created with `omega/images` hierarchy. |
> > | Diagram showing omega.jar which contains omega/MyDemo.class and omega/images/myImage.png |
> > | One big JAR file with class files under `omega` directory and image files under `omega/images` directory. |
> >
> > All seven configurations shown are valid, and the same code reads
> > the image:
> >
> > ```
> >
> > java.net.URL imageURL = myDemo.class.getResource("images/myImage.gif");
> > ...
> > if (imageURL != null) {
> >     ImageIcon icon = new ImageIcon(imageURL);
> > }
> >
> > ```
> >
> > The `getResource` method causes the class loader to
> > look through the directories and JAR files in the program's class
> > path, returning a URL as soon as it finds the desired file. In the
> > example the MyDemo program attempts to load the
> > `images/myImage.png` file from the `omega`
> > class. The class loader looks through the directories and JAR files
> > in the program's class path for `/omega/images/myImage.png`.
> > If the class loader finds the
> > file, it returns the URL of the JAR file or directory that
> > contained the file. If another JAR file or directory in the
> > class path contains the `images/myImage.png` file, the
> > class loader returns the first instance that contains the file.
> >
> > Here are three ways to specify the class path:
> >
> > * Using the `-cp` or `-classpath`
> >   command-line argument. For example, in the case where the images are in
> >   a JAR file named `images.jar` and the class file is in the
> >   current directory:
> >
> >   ```
> >
> >   java -cp  .;images.jar  MyDemo  [Microsoft Windows]
> >   java -cp ".;images.jar" MyDemo  [Unix-emulating shell on Microsoft
> >                                   Windows — you must quote the path]
> >   java -cp  .:images.jar  MyDemo  [Unix]
> >
> >   ```
> >
> >   If your image and class files are in separate JAR files, your
> >   command line will look something like:
> >
> >   ```
> >
> >   java -cp .;MyDemo.jar;images.jar MyDemo  [Microsoft Windows]
> >
> >   ```
> >
> >   In the situation where all the files are in one JAR file, you can
> >   use either of the following commands:
> >
> >   ```
> >
> >   java -jar MyAppPlusImages.jar
> >   java -cp .;MyAppPlusImages.jar MyApp  [Microsoft Windows]
> >
> >   ```
> >
> >   For more information, see the
> >   [JAR Files](../../deployment/jar/)
> >   trail.
> > * In the program's JNLP file (used by Java Web Start). For example,
> >   here is the JNLP file used by `DragPictureDemo`:
> >
> >   ```
> >
> >   <?xml version="1.0" encoding="utf-8"?>
> >   <!-- JNLP File for DragPictureDemo -->
> >   <jnlp
> >     spec="1.0+"
> >     codebase="http://download.oracle.com/javase/tutorialJWS/src/uiswing/misc/examples"
> >     href="DragPictureDemo.jnlp">
> >     <information>
> >       <title>DragPictureDemo</title>
> >       <vendor>The Java(tm) Tutorial: Sun Microsystems, Inc.</vendor>
> >       <homepage href="http://download.oracle.com/javase/tutorial/uiswing/misc/examples/index.html#DragPictureDemo"/>
> >       <description>DragPictureDemo</description>
> >       <description kind="short">A demo showing how to install
> >           data transfer on a custom component.</description>
> >       <offline-allowed/>
> >     </information>
> >     <resources>
> >       <j2se version="1.6+"/>
> >       <jar href="allClasses.jar"/>
> >       <jar href="images.jar"/>
> >     </resources>
> >     <application-desc main-class="DragPictureDemo"/>
> >   </jnlp>
> >
> >   ```
> >
> >   In this example, the class files and the images files are in separate
> >   JAR files. The JAR files are specified using the XML `jar`
> >   tag.
> > * Setting the `CLASSPATH` environment variable. This last
> >   approach is *not recommended*. If `CLASSPATH` is not
> >   set, the current directory (".") followed by the location of the system
> >   classes shipped with the JRE are used by default.
> >
> > Most of the Swing Tutorial examples put the images in an
> > `images` directory under the directory that contains the
> > examples' class files. When we create JAR files for the examples, we
> > keep the same relative locations, although often we put the class
> > files in a different JAR file than the image JAR file. No matter where
> > the class and image files are in the file system — in one JAR
> > file, or in multiple JAR files, in a named package, or in the default
> > package — the same code finds the image files using
> > `getResource`.
> >
> > For more information, see
> > [Accessing Resources in a Location-Independent Manner](http://java.sun.com/javase/6/docs/technotes/guides/lang/resources.html)
> > and the
> > [Application Development Considerations](http://java.sun.com/javase/6/docs/technotes/guides/javaws/developersguide/development.html).
>
> ### Loading Images Into Applets
> > Applets generally load image data from the computer that served up
> > the applet. The `APPLET` tag is where you specify information about
> > the images used in the applet. For more information on the `APPLET` tag
> > see
> > [Using the APPLET Tag](../../deployment/applet/html.html)
>
> ### Improving Perceived Performance When Loading Image Icons
> > Because the photograph images can be slow to access,
> > [`IconDemoApp.java`](../examples/components/IconDemoProject/src/components/IconDemoApp.java)
> > uses a `SwingWorker` to improve the performance of the program as
> > perceived by the user.
> >
> > **Background image loading** — the program
> > uses a
> > [javax.swing.SwingWorker](http://download.oracle.com/javase/7/docs/api/javax/swing/SwingWorker.html)
> > object to load each photograph image and compute it's thumbnail in a background thread.
> > Using a `SwingWorker` prevents the program from appearing to freeze
> > up while loading and scaling the images.
> >
> > Here's the code to process each image:
> >
> > ```
> >
> > /**
> >  * SwingWorker class that loads the images a background thread and calls publish
> >  * when a new one is ready to be displayed.
> >  *
> >  * We use Void as the first SwingWorker param as we do not need to return
> >  * anything from doInBackground().
> >  */
> > private SwingWorker loadimages = new SwingWorker() {
> >     
> >     /**
> >      * Creates full size and thumbnail versions of the target image files.
> >      */
> >     @Override
> >     protected Void doInBackground() throws Exception {
> >         for (int i = 0; i < imageCaptions.length; i++) {
> >             ImageIcon icon;
> >             icon = createImageIcon(imagedir + imageFileNames[i], imageCaptions[i]);
> >             
> >             ThumbnailAction thumbAction;
> >             if(icon != null){
> >                 
> >                 ImageIcon thumbnailIcon = new
> >                      ImageIcon(getScaledImage(icon.getImage(), 32, 32));
> >
> >                 
> >                 thumbAction = new ThumbnailAction(icon, thumbnailIcon, imageCaptions[i]);
> >
> >             } else {
> >                 // the image failed to load for some reason
> >                 // so load a placeholder instead
> >                 thumbAction = new ThumbnailAction(placeholderIcon, placeholderIcon, imageCaptions[i]);
> >             }
> >             publish(thumbAction);
> >         }
> >         // unfortunately we must return something, and only null is valid to
> >         // return when the return type is void.
> >         return null;
> >     }
> >     
> >     /**
> >      * Process all loaded images.
> >      */
> >     @Override
> >     protected void process(List chunks) {
> >         for (ThumbnailAction thumbAction : chunks) {
> >             JButton thumbButton = new JButton(thumbAction);
> >             // add the new button BEFORE the last glue
> >             // this centers the buttons in the toolbar
> >             buttonBar.add(thumbButton, buttonBar.getComponentCount() - 1);
> >         }
> >     }
> > };
> >
> > ```
> >
> > SwingWorker invokes the `doInBackground` method in a background thread.
> > The method places a full size image, thumbnail size image and caption into a
> > `ThumbnailAction` object. The SwingWorker then delivers the
> > `ThumbnailAction` to the `process` method. The
> > `process` method executes on the event dispatch thread and updates
> > the GUI by adding a button to the toolbar. `JButton` has a constructor that
> > takes an action object. The action object determines a number of the button's properties.
> > In our case the button icon, the caption and the action to be performed when the button
> > is pressed is all determined by the `ThumbnailAction`.
> >
> > **Overhead** — this program eventually loads all the source
> > images into memory. This may not be desirable in all situations. Loading a number
> > of very large files could cause the program to allocate a very large amount or memory.
> > Care should be taken to manage the number and size of images that are loaded.
> >
> > As with all performance-related issues, this technique is
> > applicable in some situations and not others. Also the technique described
> > here is designed to improve the program's perceived performance, but
> > does not necessarily impact its real performance.
>
> ### Creating a Custom Icon Implementation
>
> > The `createImageIcon` method returns null when it cannot find an image,
> > but what should the program do then? One possibility would be to ignore that
> > image and move on. Another option would be to provide some sort of default icon
> > to display when the real one cannot be loaded. Making another call to
> > `createImageIcon` might result in another null so using that is not
> > a good idea. Instead lets create a custom `Icon` implementation.
> >
> > ![An example of MissingIcon.](../../figures/uiswing/components/MissingIconDemo.png)
> >
> > You can find the implementation of the custom icon class in
> > [`MissingIcon.java`](../examples/components/IconDemoProject/src/components/MissingIcon.java). Here are the interesting parts of its code:
> >
> > ```
> >
> > /**
> >  * The "missing icon" is a white box with a black border and a red x.
> >  * It's used to display something when there are issues loading an
> >  * icon from an external location.
> >  *
> >  * @author Collin Fagan
> >  */
> > public class MissingIcon implements Icon{
> >     
> >     private int width = 32;
> >     private int height = 32;
> >     
> >     private BasicStroke stroke = new BasicStroke(4);
> >     
> >     public void paintIcon(Component c, Graphics g, int x, int y) {
> >         Graphics2D g2d = (Graphics2D) g.create();
> >         
> >         g2d.setColor(Color.WHITE);
> >         g2d.fillRect(x +1 ,y + 1,width -2 ,height -2);
> >         
> >         g2d.setColor(Color.BLACK);
> >         g2d.drawRect(x +1 ,y + 1,width -2 ,height -2);
> >         
> >         g2d.setColor(Color.RED);
> >         
> >         g2d.setStroke(stroke);
> >         g2d.drawLine(x +10, y + 10, x + width -10, y + height -10);
> >         g2d.drawLine(x +10, y + height -10, x + width -10, y + 10);
> >         
> >         g2d.dispose();
> >     }
> >     
> >     public int getIconWidth() {
> >         return width;
> >     }
> >     
> >     public int getIconHeight() {
> >         return height;
> >     }
> > }
> >
> > ```
> >
> > The `paintIcon` method is passed a `Graphics` object.
> > The `Graphics` object gives the `paintIcon`
> > method access to the entire
> > Java2D API. For more information about painting and Java2D, see
> > [Performing Custom Painting](../painting/index.html).
> >
> > The following code demonstrates how the `MissingIcon` class
> > is used in the `SwingWorker` `doInBackground` method.
> >
> > ```
> >
> > private MissingIcon placeholderIcon = new MissingIcon();
> >
> > ...
> > if(icon != null) {
> >     ...
> >
> > } else {
> >     // the image failed to load for some reason
> >     // so load a placeholder instead
> >     thumbAction = new ThumbnailAction(placeholderIcon, placeholderIcon, imageCaptions[i]);
> > }
> >
> > ```
> >
> > Using a custom icon has a few implications:
> >
> > * Because the icon's appearance is determined dynamically, the icon
> >   painting code can use any information — component and application
> >   state, for example — to determine what to paint.
> > * Depending on the platform and the type of image, you may get a
> >   performance boost with custom icons, since painting simple shapes can
> >   sometimes be faster than copying images.
> > * Because `MissingIcon` does not do any file I/O there
> >   is no need for separate threads to load the image.
>
> ### The Image Icon API
>
> > The following tables list the commonly used `ImageIcon`
> > constructors and methods. Note that `ImageIcon` is not a
> > descendent of `JComponent` or even of
> > `Component`.
> >
> > The API for using image icons falls into these categories:
> >
> > * [Setting, Getting, and Painting the Image Icon's Image](#contents)* [Setting or Getting Information about the Image Icon](#info)* [Watching the Image Icon's Image Load](#loadstatus)
> >
> > Setting, Getting, and Painting the Image Icon's
> > Image
> >
> > | Method or Constructor | Purpose |
> > | [ImageIcon()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#ImageIcon())  [ImageIcon(byte[])](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#ImageIcon(byte[]))  [ImageIcon(byte[], String)](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#ImageIcon(byte[], java.lang.String))  [ImageIcon(Image)](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#ImageIcon(java.awt.Image)) | Create an `ImageIcon` instance, initializing it to contain the specified image. The first argument indicates the source — image, byte array, filename, or URL — from which the image icon's image should be loaded. The source must be in a format supported by the `java.awt.Image` class: namely GIF, JPEG, or PNG. The second argument, when present, provides a description for the image. The description may also be set via `setDescription` and provides useful textual information for [assistive technologies](../misc/access.html). |
> > | [void setImage(Image)](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#setImage(java.awt.Image))  [Image getImage()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#getImage()) | Set or get the image displayed by the image icon. |
> > | [void paintIcon(Component, Graphics, int, int)](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#paintIcon(java.awt.Component, java.awt.Graphics, int, int)) | Paint the image icon's image in the specified graphics context. You would override this only if you're implementing a custom icon that performs its own painting. The `Component` object is used as an image observer. You can rely on the default behavior provided by `Component` class, and pass in any component. The two `int` arguments specify the top-left corner where the icon is painted. |
> > | [URL getResource(String)](http://download.oracle.com/javase/7/docs/api/java/lang/ClassLoader.html#getResource(java.lang.String)) in (*java.lang.ClassLoader*) | Find the resource with the given name. For more information, see [Loading Images Using getResource](#getresource). |
> > | [InputStream getResourceAsStream(String)](http://download.oracle.com/javase/7/docs/api/java/lang/ClassLoader.html#getResourceAsStream(java.lang.String)) in (*java.lang.ClassLoader*) | Find the resource with the given name and return an input stream for reading the resource. For more information, see the [Loading Images Into Applets](#applet) discussion. |
> >
> > Setting or Getting Information about the Image Icon
> >
> > | Method | Purpose |
> > | [void setDescription(String)](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#setDescription(java.lang.String))  [String getDescription()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#getDescription()) | Set or get a description of the image. This description is intended for use by [assistive technologies](../misc/access.html). |
> > | [int getIconWidth()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#getIconWidth())  [int getIconHeight()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#getIconHeight()) | Get the width or height of the image icon in pixels. |
> >
> > Watching the Image Icon's Image Load
> >
> > | Method | Purpose |
> > | [void setImageObserver(ImageObserver)](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#setImageObserver(java.awt.image.ImageObserver))  [ImageObserver getImageObserver()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#getImageObserver()) | Set or get an image observer for the image icon. |
> > | [int getImageLoadStatus()](http://download.oracle.com/javase/7/docs/api/javax/swing/ImageIcon.html#getImageLoadStatus()) | Get the loading status of the image icon's image. The values returned by this method are defined by `MediaTracker`. |
>
> ### Examples that Use Icons
>
> > The following table lists just a few of the many examples that use
> > `ImageIcon`.
> >
> > | Example | Where Described | Notes |
> > | --- | --- | --- |
> > | [`LabelDemo`](../examples/components/index.html#LabelDemo) | This section and  [How to Use Labels](../components/label.html) | Demonstrates using icons in an application's label, with and without accompanying text. |
> > | [`IconDemo`](../examples/components/index.html#IconDemo) | This section | Uses a label to show large images; uses buttons that have both images and text. |
> > | [`CustomIconDemo`](../examples/components/index.html#CustomIconDemo) | This section | Uses a custom icon class implemented by [`ArrowIcon.java`](../examples/components/CustomIconDemoProject/src/components/ArrowIcon.java). |
> > | [`TumbleItem`](../examples/components/index.html#TumbleItem) | [How to Make Applets](../components/applet.html) | An applet. Uses image icons in an animation. Shows how to call `ImageIcon`'s `paintIcon` method. |
> > | [`ButtonDemo`](../examples/components/index.html#ButtonDemo) | [How to Use Buttons, Check Boxes, and Radio Buttons](../components/button.html) | Shows how to use icons in an application's buttons. |
> > | [`CheckBoxDemo`](../examples/components/index.html#CheckBoxDemo) | [How to Use Check Boxes](../components/button.html#checkbox) | Uses multiple GIF images. |
> > | [`TabbedPaneDemo`](../examples/components/index.html#TabbedPaneDemo) | [How to Use Tabbed Panes](../components/tabbedpane.html) | Demonstrates adding icons to tabs in a tabbed pane. |
> > | [`DialogDemo`](../examples/components/index.html#DialogDemo) | [How to Make Dialogs](../components/dialog.html) | Shows how to use standard icons in dialogs. |
> > | [`TreeIconDemo`](../examples/components/index.html#TreeIconDemo) | [How to Use Trees](../components/tree.html) | Shows how to change the icons displayed by a tree's nodes. |
> > | [`ActionDemo`](../examples/misc/index.html#ActionDemo) | [How to Use Actions](../misc/action.html) | Shows how to specify the icon in a tool-bar button or menu item using an `Action`. |
> > | [`FileChooserDemo2`](../examples/components/index.html#FileChooserDemo2) | [How to Use File Choosers](../components/filechooser.html) | Uses a `PNG` image. Shows how to implement an image previewer and an image filter in a file chooser. |
> >
> > ---
> >
> > **Note:** The photographs used in the [`IconDemo`](../examples/components/index.html#IconDemo)
> > are copyright ©2006
> > [spriggs.net](http://photos.spriggs.net/)
> > and licenced under a
> > [Creative Commons Licence](http://creativecommons.org/licenses/by-sa/3.0/).
> >
> > ---

[« Previous](model.html)
•
[Trail](../TOC.html)
•
[Next »](border.html)

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

**Previous page:** How to Use Models
  
**Next page:** How to Use Borders




A browser with JavaScript enabled is required for this page to operate properly.