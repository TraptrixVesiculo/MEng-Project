[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel

[Modifying the Look and Feel](index.html)

[How to Set the Look and Feel](plaf.html)

The Synth Look and Feel

[A Synth Example](synthExample.html)

[Nimbus Look and Feel](nimbus.html)

[Changing the Look of Nimbus](custom.html)

[Resizing a Component](size.html)

[Changing the Color Theme](color.html)

[For More Information](info.html)

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)
>
[Modifying the Look and Feel](index.html)

[« Previous](plaf.html) • [Trail](../TOC.html) • [Next »](synthExample.html)

# The Synth Look and Feel

Creating a custom look and feel, or modifying an existing one,
can be a daunting task. The
[`javax.swing.plaf.synth`](http://download.oracle.com/javase/7/docs/api/javax/swing/plaf/synth/package-summary.html) package can be used to create a custom look and feel with much less effort.
You can create a Synth look and feel
either programatically or through the use of an external XML file.
The discussion below is devoted to the
creation of a Synth look and feel using an external XML file.
Creating a Synth L&F programatically is discussed in the API
documentation.

With the Synth look and feel, you provide the "look." Synth itself
provides the "feel." Thus, you can think of the Synth L&F as a "skin."

### The Synth Architecture

Recall from the previous topic that it is the responsibility of each
L&F to provide a concrete implementation for each of the many
ComponentUI subclasses defined by Swing. The Synth L&F takes care of
this for you. To use Synth, you need not create any ComponentUIs—rather
you need only specify how each component is painted, along with
various properties that effect the layout and size.

Synth operates at a more granular level than a component—this granular level
is called a "region." Each component has one or more regions. Many components have
only one region, such as JButton. Others have multiple regions, such
as `JScrollBar`. Each of the `ComponentUIs` provided by Synth associates a
`SynthStyle` with each of the regions defined by the `ComponentUI`. For
example, Synth defines three regions for `JScrollBar`: the track, the
thumb and the scroll bar itself. The `ScrollBarUI` (the `ComponentUI`
subclass defined for `JScrollBar`) implementation for Synth associates a
`SynthStyle` with each of these regions.

![Synth Architecture Drawing.](../../figures/uiswing/lookandfeel/synthArch.gif)

`SynthStyle` provides style information used by the Synth `ComponentUI`
implementation. For example, `SynthStyle` defines the foreground and
background color, font information, and so forth. In addition, each `SynthStyle`
has a `SynthPainter` that is used to paint the region. For example,
`SynthPainter` defines the two methods `paintScrollBarThumbBackground` and
`paintScrollBarThumbBorder`, which are used to paint the scroll bar
thumb regions.

Each of the `ComponentUIs` in Synth obtain `SynthStyles` using a
`SynthStyleFactory`. There are two ways to define a `SynthStyleFactory`:
through a Synth XML file, or programatically. The following code
shows how to load an XML file dictating the look of Synth—beneath the
covers this creates a `SynthStyleFactory` implementation populated with
`SynthStyles` from the XML file:

```

  SynthLookAndFeel laf = new SynthLookAndFeel();
  laf.load(MyClass.class.getResourceAsStream("laf.xml"), MyClass.class);
  UIManager.setLookAndFeel(laf);

```

The programmatic route involves creating an implementation of
`SynthStyleFactory` that returns `SynthStyles`. The following code
creates a custom `SynthStyleFactory` that returns distinct `SynthStyles`
for buttons and trees:

```

 class MyStyleFactory extends SynthStyleFactory {
     public SynthStyle getStyle(JComponent c, Region id) {
         if (id == Region.BUTTON) {
             return buttonStyle;
         }
         else if (id == Region.TREE) {
             return treeStyle;
         }
         return defaultStyle;
     }
 }
 SynthLookAndFeel laf = new SynthLookAndFeel();
 UIManager.setLookAndFeel(laf);
 SynthLookAndFeel.setStyleFactory(new MyStyleFactory());

```

### The XML File

An explanation of the DTD for the Synth XML file can be found at
[`javax.swing.plaf.synth/doc-files/synthFileFormat.html`.](http://download.oracle.com/javase/7/docs/api/javax/swing/plaf/synth/doc-files/synthFileFormat.html)

When you load a Synth look and feel, only those GUI components (or regions) for which there is a definition (a "style" bound
to the region, as discussed below) are rendered. There is no default
behavior for any components—without style definitions in the Synth XML file, the GUI is a blank canvas.

To specify the rendering of a component (or region), your XML file must contain a <style> element, which is then *bound*
to the region using the <bind> element. As an example, let's define a style that includes the
font, foreground color, and background color, and then bind that style to all components. It is a good idea
to include such an element in your Synth XML file while you are developing it—then, any components you haven't yet defined will at
least have colors and a font:

```

<synth>
  <style id="basicStyle">
    <font name="Verdana" size="16"/>
    <state>
      <color value="WHITE" type="BACKGROUND"/>
      <color value="BLACK" type="FOREGROUND"/>
    </state>
  </style>
  <bind style="basicStyle" type="region" key=".*"/>
</synth>

```

Let's analyse this style definition:

1. The <style> element is the basic building block of the Synth XML file. It contains all the information needed to
   describe a region's rendering. A <style> element can describe more than one region, as is done here. In
   general, though, it is best to create a <style> element for each component or region. Note that the <style> element
   is given an
   identifier, the string "basicStyle." This identifier will be used later in the <bind> element.
  
2. The <font> element of the <style> element sets the font to Verdana, size 16.
  
3. The <state> element of the <style> element will be discussed below. The <state> element of a region
   can have one, or a mixture, of seven possible values. When the value is not specified, the definition applies to all states,
   which is
   the intention here. Therefore, the background and foreground colors "for all states" are defined in this element.
  
4. Finally, the <style> element with the identifier "basicStyle" that has just been defined is *bound* to all regions.
   The <bind> element binds "basicStyle" to "region" types. Which region type or types the binding applies to is given by
   the "key" attribute, which is ".\*" in this case, the regular expression for "all."

Let's look at the pieces of the Synth XML file before creating some working examples. We'll start with the
<bind> element, showing how a given <style> is applied to a component or region.

### The <bind> Element

Whenever a <style> element is defined, it must be bound to one or more components or regions before it has an effect. The <bind> element is used for this purpose. It requires three attributes:

1. `style` is the unique identifier of a previously defined style.
  
2. `type` is either "name" or "region." If `type` is a name, obtain the name with the `component.getName()` method.
   If `type` is a region, use the appropriate constant defined in the `Region` class in the `javax.swing.plaf.synth package.`
  
3. `key` is a regular expression used to determine which components or regions the style is bound to.

A Region is a way of identifying a component or part of a component. Regions are based on
the constants in the
[`Region`](http://download.oracle.com/javase/7/docs/api/javax/swing/plaf/synth/Region.html)
class, modified by stripping out underscores:

For example, to identify the SPLIT\_PANE region you would use SPLITPANE, splitpane, or SplitPane (case insensitive).

When you bind a style to a region, that style will apply to *all* of the components with that region. You can bind a
style to more than one
region, and you can bind more than one style to a region. For example,

```

<style id="styleOne">
   <!-- styleOne definition goes here -->
</style>

<style id="styleTwo">
   <!-- styleTwo definition goes here -->
</style>

<bind style="styleOne" type="region" key="Button"/>
<bind style="styleOne" type="region" key="RadioButton"/>
<bind style="styleOne" type="region" key="ArrowButton"/>

<bind style="styleTwo" type="region" key="ArrowButton"/>



```

You can bind to individual, named components, whether or not they are *also* bound as regions. For example, suppose you want to have the "OK" and
"Cancel" buttons in your GUI
treated differently than all the other buttons. First, you would give the OK and Cancel buttons names, using the
`component.setName()` method. Then, you would define three styles: one for buttons in general (region = "Button"),
one for the OK button (name = "OK"),
and one for the Cancel button (name = "Cancel"). Finally, you would bind these styles like this:

```

<bind style="styleButton" type="region" key="Button">
<bind style="styleOK" type="name" key="OK">
<bind style="styleCancel" type="name" key="Cancel">

```

As a result, the "OK" button is bound to *both* "styleButton" and "styleOK," while the "Cancel" button is
bound to *both* "styleButton" and "styleCancel."

When a component or region is bound to more than one style, the styles are merged

---

**Note:** Just as a style can be bound to multiple regions or names, multiple styles can be bound to a region or name. These multiple
styles are merged for the region or name. Precedence is given to styles defined later in the file.

---

### The <state> Element

The <state> element allows you to define a look for a region that depends on its "state." For example, you will
usually want a button that has been `PRESSED` to look different than the button in its `ENABLED` state. There are seven
possible values for <state> that are defined in the Synth XML DTD. They are:

1. ENABLED
2. MOUSE\_OVER
3. PRESSED
4. DISABLED
5. FOCUSED
6. SELECTED
7. DEFAULT

You can also have composite states, separated by 'and'—for example, ENABLED and FOCUSED. If you do not specify a value,
the defined look will apply to all states.

As an example, here is a style that specifies painters per state. All buttons are painted a certain way, unless the state is "PRESSED,"
in which case they are painted differently:

```

<style id="buttonStyle">
  <property key="Button.textShiftOffset" type="integer" value="1"/>
  <insets top="10" left="10" right="10" bottom="10"/>

  <state>
    <imagePainter method="buttonBackground" path="images/button.png"
                         sourceInsets="10 10 10 10"/>
  </state>
  <state value="PRESSED">
    <color value="#9BC3B1" type="BACKGROUND"/>
    <imagePainter method="buttonBackground" path="images/button2.png"
                        sourceInsets="10 10 10 10"/>
  </state>
</style>
<bind style="buttonStyle" type="region" key="Button"/>


```

Ignoring the <property> and <insets> elements for the moment, you can see that a pressed button is
painted differently than an unpressed button.

The <state> value that is used is the defined state that most closely matches the state of the region.
Matching is determined by the number of values that match the state of the region. If none of the
state values match, then the state with no value is used. If there are matches, the state with the most individual
matches will be chosen. For example, the following code defines three states:

```

<state id="zero">
  <color value="RED" type="BACKGROUND"/>
</state>
<state value="SELECTED and PRESSED" id="one">
  <color value="RED" type="BACKGROUND"/>
</state>
<state value="SELECTED" id="two">
  <color value="BLUE" type="BACKGROUND"/>
</state>

```

If the state of the region contains at least SELECTED and PRESSED, state one will
be chosen. If the state contains SELECTED, but not does not contain PRESSED, state two will be used. If
the state contains neither SELECTED nor PRESSED, state zero will be used.

When the current state matches the same number of values for two state definitions, the one that is used is
the first one defined in the style.
For example, the `MOUSE_OVER` state is always true of a `PRESSED` button (you can't press a button
unless the mouse is over it). So, if the
`MOUSE_OVER` state is declared first, it will always be chosen over `PRESSED`, and any painting
defined for `PRESSED` will not be done.

```

<state value="PRESSED"> 
   <imagePainter method="buttonBackground" path="images/button_press.png"
	                  sourceInsets="9 10 9 10" />
   <color type="TEXT_FOREGROUND" value="#FFFFFF"/>      
</state>
      
<state value="MOUSE_OVER">    
   <imagePainter method="buttonBackground" path="images/button_on.png"
	                  sourceInsets="10 10 10 10" />
   <color type="TEXT_FOREGROUND" value="#FFFFFF"/>
</state>

```

The code above will work properly. However, if you reverse the order of the `MOUSE_OVER`
and `PRESSED` states in the file, the `PRESSED` state will never be used. This is because any
state that is `PRESSED` state is *also* a `MOUSE_OVER` state. Since the
`MOUSE_OVER` state was defined first, it is the one that will be used.

### Colors and Fonts

The <color> element requires two attributes:

1. `value` can be any one of the `java.awt.Color` constants, such as RED, WHITE, BLACK, BLUE, etc. It can also be a hex representation of
   RGB values, such as #FF00FF or #326A3B.
  
2. `type` describes where the color applies—it can be BACKGROUND, FOREGROUND, FOCUS, TEXT\_BACKGROUND,
   OR TEXT\_FOREGROUND.

For example:

```

  <style id="basicStyle">
    <state>
      <color value="WHITE" type="BACKGROUND"/>
      <color value="BLACK" type="FOREGROUND"/>
    </state>
  </style>

```

The <font> element has three attributes:

1. `name`—the name of the font. For example, Arial or Verdana.
  
2. `size`—the size of the font in pixels.
  
3. `style` (optional)—BOLD, ITALIC, OR BOLD ITALIC. If omitted, you get a normal font.

For example:

```

  <style id="basicStyle">
    <font name="Verdana" size="16"/>
  </style>

```

Each of the <color> element and the <font> element has an alternate usage. Each can have an
`id` attribute or an `idref` attribute. Using the `id` attribute, you can
define a color that you can reuse later by using the `idref` attribute. For example,

```

<color id="backColor" value="WHITE" type="BACKGROUND"/>
<font id="textFont" name="Verdana" size="16"/>
...
...
...
<color idref="backColor"/>
<font idref="textFont"/>

```

### Insets

The `insets` add to the size of a component as it is drawn. For example, without insets,
a button with a caption of `Cancel` will be just large enough to contain the caption
in the chosen font. With an <insets> element like this

```

<insets top="15" left="20" right="20" bottom="15"/>,

```

the button will be made larger by 15 pixels above and below the caption and 20 pixels to the left and
right of the caption.

### Painting With Images

Synth's file format allows customizing the painting by way of images. Synth's image painter breaks an image
into nine distinct areas: top, top right, right, bottom right, bottom, bottom left, left, top left,
and center. Each of the these areas is painted into the destination. The top, left, bottom, and right
edges are tiled or stretched, while the corner portions
(`sourceInsets`) remain fixed.

---

**Note:** There is no relation between the <insets> element and the `sourceInsets` attribute. The
<insets> element defines the space taken up by a region, while the `sourceInsets` attributes
define how to paint an image. The <insets> and `sourceInsets` will often be similar, but
they need not be.

---

You can specify whether the center
area should be painted with the `paintCenter` attribute. The following image shows the nine areas:

![Nine Image Areas.](../../figures/uiswing/lookandfeel/regions.gif)

Let's create a button as an example. To do this we can
use the following image (shown larger than its actual size):

![Button Image.](../../figures/uiswing/lookandfeel/bigButton.png)

The red box at the upper left corner is 10 pixels square (including the box border)—it shows the
corner region that should not be stretched when painting. To achieve this, the top and
left `sourceInsets` should be set to 10.
We'll use the following style and binding:

```

<style id="buttonStyle">
   <insets top="15" left="20" right="20" bottom="15"/>
   <state>
      <imagePainter method="buttonBackground" path="images/button.png"
        sourceInsets="10 10 10 10"/>
   </state>
</style>
<bind style="buttonStyle" type="region" key="button"/>

```

The lines inside the <state> element specify that the background of buttons should be painted using the
image `images/button.png`. That path is relative to the Class that is passed into
SynthLookAndFeel's load method. The `sourceInsets`
attribute specifies the areas of the image that are not to be stretched. In this case the top, left, bottom, and right insets
are each 10. This will cause the painter not to stretch a 10 x 10 pixel area at each corner of the image.

The <bind> binds `buttonStyle` to all buttons.

The <imagePainter> element provides all the information needed to render a portion of a region.
It requires only a few attributes:

* method—this specifies which of the methods in the `javax.swing.plaf.synth.SynthPainter`
  class is to be used for painting. The `SynthPainter` class contains about 100 methods that
  begin with `paint`. When you determine which one you need, you remove the `paint`
  prefix, change the remaining first letter to lowercase, and use the result as the `method` attribute.
  For example, the `SynthPainter` method `paintButtonBackground` becomes the attribute
  `buttonBackground`.
  
* path—the path to the image to be used, relative to the Class that is passed into
  SynthLookAndFeel's load method.
  
* sourceInsets—the insets in pixels, representing the width and height of the corner areas that
  should not be stretched
  They map to the top, left, bottom, and right, in that order.
  
* paintCenter (optional) : This attribute lets you keep the center of an image
  or get rid of it (in a text field, for example,
  so text can be drawn).

The listing below shows the XML code for loading different images depending on the <state>
of the button

```

  <style id="buttonStyle">
    <property key="Button.textShiftOffset" type="integer" value="1"/>
    <insets top="15" left="20" right="20" bottom="15"/>
    <state>
      <imagePainter method="buttonBackground" path="images/button.png"
                    sourceInsets="10 10 10 10"/>
    </state>
    <state value="PRESSED">
      <imagePainter method="buttonBackground" path="images/button2.png"
                    sourceInsets="10 10 10 10"/>
    </state>
  </style>
  <bind style="buttonStyle" type="region" key="button"/>

```

button2.png shows the depressed version of button.png, shifted one pixel to the right. The line

```

<property key="Button.textShiftOffset" type="integer" value="1"/>

```

shifts the button text accordingly, as discussed in the next section.

### The <property> Element

<property> elements are used to add key value pairs to a <style> element. Many components use the key
value pairs for configuring their visual appearance.

The <property> element has three attributes:

* `key`—the name of the property.
  
* `type`—the data type of the property.
  
* `value`—the value of the property.

There is a property table (`componentProperties.html`) that lists the properties each component supports:
[`javax/swing/plaf/synth/doc-files/componentProperties.html`](http://download.oracle.com/javase/7/docs/api/javax/swing/plaf/synth/doc-files/componentProperties.html).

Since the button2.png image shifts the visual button one pixel when it is depressed, we should also shift the
button text. There is a button property that does this:

```

<property key="Button.textShiftOffset" type="integer" value="1"/>

```

### An Example

Here is an example, using the button style defined above. The button style, plus a "backing style"
with definitions of font and colors that are bound to all regions (similar to the "basicStyle" shown
in the section titled "The XML File," above) are combined in
[`buttonSkin.xml`](../examples/lookandfeel/SynthApplicationProject/src/lookandfeel/buttonSkin.xml)Here is a listing of `buttonSkin.xml`:

```

<!-- Synth skin that includes an image for buttons -->
<synth>
  <!-- Style that all regions will use -->
  <style id="backingStyle">
    <!-- Make all the regions that use this skin opaque-->
    <opaque value="TRUE"/>
    <font name="Dialog" size="12"/>
    <state>
      <!-- Provide default colors -->
      <color value="#9BC3B1" type="BACKGROUND"/>
      <color value="RED" type="FOREGROUND"/>
    </state>
  </style>
  <bind style="backingStyle" type="region" key=".*"/>
  <style id="buttonStyle">
    <!-- Shift the text one pixel when pressed -->
    <property key="Button.textShiftOffset" type="integer" value="1"/>
    <insets top="15" left="20" right="20" bottom="15"/>
    <state>
      <imagePainter method="buttonBackground" path="images/button.png"
                    sourceInsets="10 10 10 10"/>
    </state>
    <state value="PRESSED">
      <imagePainter method="buttonBackground" path="images/button2.png"
                    sourceInsets="10 10 10 10"/>
    </state>
  </style>
  <!-- Bind buttonStyle to all JButtons -->
  <bind style="buttonStyle" type="region" key="button"/> 
</synth>

```

We can load this XML file to use the Synth look and feel for a simple application called
`SynthApplication.java`. The GUI for this application includes a button and a label. Every time the
button is clicked, the label increments.

---

**Note:** The label is painted, even though `buttonSkin.xml` does not contain a style for it. This is because
there is a general "backingStyle" that includes a font and colors.

---

Here is the listing of the
[`SynthApplication.java`](../examples/lookandfeel/SynthApplicationProject/src/lookandfeel//SynthApplication.java)file.

---

**Try this:** 
Click the Launch button to run the SynthApplication example using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/lookandfeel/index.html#SynthApplication).

[![Launches the SynthApplication example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/lookandfeel/ex6/SynthApplication.jnlp)


---

### Painting With Icons

Radio buttons and check boxes typically render their state by fixed-size icons. For these, you
can create an icon and bind it to the appropriate property (refer to the properties table,
[`javax/swing/plaf/synth/doc-files/componentProperties.html`](http://download.oracle.com/javase/7/docs/api/javax/swing/plaf/synth/doc-files/componentProperties.html)).
For example, to paint radio buttons that are selected or unselected, use this code:

```

<style id="radioButton">
   <imageIcon id="radio_off" path="images/radio_button_off.png"/>
   <imageIcon id="radio_on" path="images/radio_button_on.png"/>
   <property key="RadioButton.icon" value="radio_off"/>
   <state value="SELECTED">   
      <property key="RadioButton.icon" value="radio_on"/>
   </state>
</style>
<bind style="radioButton" type="region" key="RadioButton"/>	 

```

### Custom Painters

Synth's file format allows for embedding arbitrary objects by way of the
[`long-term persistence of JavaBeans components`](http://java.sun.com/products/jfc/tsc/articles/persistence3)
. This ability is particularly useful in providing your own painters
beyond the image-based ones Synth provides. For example, the following XML code specifies that
a gradient should be rendered in the background of text fields:

```

<synth>
  <object id="gradient" class="GradientPainter"/>
  <style id="textfield">
    <painter method="textFieldBackground" idref="gradient"/>
  </style>
  <bind style="textfield" type="region" key="textfield"/>
</synth>

```

Where the GradientPainter class looks like this:

```

public class GradientPainter extends SynthPainter {
   public void paintTextFieldBackground(SynthContext context,
                                        Graphics g, int x, int y,
                                        int w, int h) {
      // For simplicity this always recreates the GradientPaint. In a
      // real app you should cache this to avoid garbage.
      Graphics2D g2 = (Graphics2D)g;
      g2.setPaint(new GradientPaint((float)x, (float)y, Color.WHITE,
                 (float)(x + w), (float)(y + h), Color.RED));
      g2.fillRect(x, y, w, h);
      g2.setPaint(null);
   }
}

```

### Conclusion

In this lesson, we have covered the use of the `javax.swing.plaf.synth` package to create
a custom look and feel. The emphasis of the lesson has been on using an external XML file to define the
look and feel. The next lesson presents a sample application that creates a search dialog box using the Synth
framework with an XML file.

[« Previous](plaf.html)
•
[Trail](../TOC.html)
•
[Next »](synthExample.html)

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

**Previous page:** How to Set the Look and Feel
  
**Next page:** A Synth Example




A browser with JavaScript enabled is required for this page to operate properly.