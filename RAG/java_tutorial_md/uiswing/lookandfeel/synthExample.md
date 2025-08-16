[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing
  
**Lesson:** Modifying the Look and Feel
  
**Section:** The Synth Look and Feel

[Modifying the Look and Feel](index.html)

[How to Set the Look and Feel](plaf.html)

[The Synth Look and Feel](synth.html)

A Synth Example

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

[« Previous](synth.html) • [Trail](../TOC.html) • [Next »](nimbus.html)

# A Synth Example

In the lesson titled
[A GroupLayout Example](../../uiswing/layout/groupExample.html) , `GroupLayout` was used to create a search dialog box called "Find."
The program that created the dialog box, `Find.java`, used the cross
platform ("Metal") look and feel with the "Ocean" theme:

![Find.](../../figures/uiswing/lookandfeel/FindWithOcean.gif)

This lesson creates the same dialog box with Synth, using an external XML file.
Here is the listing of the
[`SynthDialog.java`](../examples/lookandfeel/SynthDialogProject/src/lookandfeel/SynthDialog.java)file.

`SynthDialog.java` is exactly the same as `Find.java`
except for the `initLookAndFeel()` method, which has been altered
to use the Synth look and feel with an external file called
`synthDemo.xml`. Here is the new `initLookAndFeel()` method:

```

private static void initLookAndFeel() {
   SynthLookAndFeel lookAndFeel = new SynthLookAndFeel();
       
   // SynthLookAndFeel load() method throws a checked exception
   // (java.text.ParseException) so it must be handled
   try {
      lookAndFeel.load(SynthDialog.class.getResourceAsStream("synthDemo.xml"),
                                                               SynthDialog.class);
      UIManager.setLookAndFeel(lookAndFeel);
   } 
            
   catch (ParseException e) {
      System.err.println("Couldn't get specified look and feel ("
                                   + lookAndFeel
                                    + "), for some reason.");
      System.err.println("Using the default look and feel.");
      e.printStackTrace();
   }
}

```

### The XML File

The XML file, `synthDemo.xml`, begins with a style bound to all regions. It is good
practice to do this to ensure that regions without a style bound to them will contain something.
This style makes all regions paint their background in an opaque color.
It also sets a default font and default colors.

```

  <!-- Style that all regions will use -->
  <style id="backingStyle">
    <!-- Make all the regions opaque-->
    <opaque value="TRUE"/>
    <font name="Dialog" size="14"/>
    <state>
      <color value="#D8D987" type="BACKGROUND"/>
      <color value="RED" type="FOREGROUND"/>
    </state>
  </style>
  <bind style="backingStyle" type="region" key=".*"/>

```

---

**Notes:**

1. The color definitions must be inside a <state> element. This permits changing colors
depending on state. The <state> element in `backingStyle` has no attributes and
is therefore applied to all regions, irrespective of their state. If a region has other states,
the states are merged with precedence given to state definitions that appear later in the file.

2. The font definition is not inside a <state> element because the font should *not* change
when there is a change of state (many components are sized depending on their font, and a change in font
could cause components to change in size unintentionally).

---

The next <style> element defined is for the text field, which is painted using an image.

```

  <style id="textfield">
    <insets top="4" left="6" bottom="4" right="6"/>
    <state>
       <font name="Verdana" size="14"/>
       <color value="#D2DFF2" type="BACKGROUND"/>
       <color value="#000000" type="TEXT_FOREGROUND"/>
    </state>
    <imagePainter method="textFieldBorder" path="images/textfield.png"
                  sourceInsets="4 6 4 6" paintCenter="false"/>
  </style>
  <bind style="textfield" type="region" key="TextField"/>

```

---

**Notes:**

1. The font and color definitions override the definitions in `backingStyle`.

2. The `insets` and `sourceInsets` are given the same values, which is just
a coincidence because they are unrelated to each other.

3. The BACKGROUND color, #D2DFF2, is a pale blue—the same color as the background in the image,
`textfield.png`.

4. `paintCenter` is `false` so that you can see the background color.

---

The next <style> element is for buttons that are painted with different images,
depending on the button state. When the mouse passes over the button, its appearance changes. When it
is clicked (PRESSED) the image changes again.

```

 <style id="button">
  	<!-- Shift the text one pixel when pressed -->
    <property key="Button.textShiftOffset" type="integer" value="1"/>
    <!-- set size of buttons -->
    <insets top="15" left="20" bottom="15" right="20"/>
    <state>
      <imagePainter method="buttonBackground" path="images/button.png"
                           sourceInsets="10 10 10 10" />
      <font name="Dialog" size="16"/>
      <color type="TEXT_FOREGROUND" value="#FFFFFF"/>
    </state>
              
    <state value="PRESSED"> 
      <imagePainter method="buttonBackground"
          path="images/button_press.png"
                   sourceInsets="10 10 10 10" />
    </state>
            
    <state value="MOUSE_OVER">    
      <imagePainter method="buttonBackground"
          path="images/button_over.png"
                 sourceInsets="10 10 10 10" />
    </state>
  </style>
  <bind style="button" type="region" key="Button"/>

```

---

**Notes:**

1. The font and color definitions inside the <state> element without attributes apply
to all button states. This is because the definitions of all states that apply (and the <state> element
without attributes is one of these) will merge and there are no
other font and color definitions that might take precedence.

2. The `sourceInsets` values are large enough that the curved corners of the button
image will not be stretched.

3. The order of the `PRESSED` and `MOUSE_OVER` states is important. Since the mouse will
always be over the button when it is pressed, both states will apply to a pressed button and the first state
defined (`PRESSED`) will apply. When the mouse is over the button but it is not pressed, only the
`MOUSE_OVER` state applies. If the order of the `PRESSED` and `MOUSE_OVER` states
is reversed, the `PRESSED` state image will never be used.

---

The next <style> element is for checkboxes that are painted with different icons,
depending on the checkbox state.

```

  <style id="checkbox">
    <imageIcon id="check_off" path="images/checkbox_off.png"/>
    <imageIcon id="check_on" path="images/checkbox_on.png"/>
    <property key="CheckBox.icon" value="check_off"/>
    <state value="SELECTED">   
      <property key="CheckBox.icon" value="check_on"/>
    </state>
  </style>
  <bind style="checkbox" type="region" key="Checkbox"/>	 

```

---

**Notes:**

1. You must use the <imageIcon> element to define any icons to be used.

2. The <insets> element and the `sourceInsets` attribute are not used with icons
because they are rendered in their fixed size and are not stretched.

3. The icon used to render the checkbox is the icon named in the `CheckBox.icon` property.
(see
[`javax/swing/plaf/synth/doc-files/componentProperties.html`](http://download.oracle.com/javase/7/docs/api/javax/swing/plaf/synth/doc-files/componentProperties.html)), which is the icon with id="check\_off" unless the checkbox state is `SELECTED`.

---

The `synthDemo.xml` file is constructed of the styles presented above, wrapped in
<synth></synth> tags. You can open the completed file by clicking
[`synthDemo.xml`](../examples/lookandfeel/SynthDialogProject/src/lookandfeel/synthDemo.xml).

---

**Try this:** 
Click the Launch button to run the SynthDialog example using
[Java™ Web Start](http://java.sun.com/products/javawebstart/index.jsp) ([download JDK 6](http://java.sun.com/javase/downloads/index.jsp)).
Alternatively, to compile and run the example yourself,
consult the
[example index](../examples/lookandfeel/index.html#SynthDialog).

[![Launches the SynthDialog example](../../images/jws-launch-button.png)](http://download.oracle.com/javase/tutorialJWS/uiswing/lookandfeel/ex6/SynthDialog.jnlp)


---

[« Previous](synth.html)
•
[Trail](../TOC.html)
•
[Next »](nimbus.html)

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

**Previous page:** The Synth Look and Feel
  
**Next page:** Nimbus Look and Feel




A browser with JavaScript enabled is required for this page to operate properly.