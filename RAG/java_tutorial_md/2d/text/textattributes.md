[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Working with Text APIs
  
**Section:** Advanced Text Display

[Working with Text APIs](index.html)

[Selecting a Font](fonts.html)

[Measuring Text](measuringtext.html)

[Advanced Text Display](advanced.html)

[Displaying Antialiased Text by Using Rendering Hints](renderinghints.html)

Using Text Attributes to Style Text

[Drawing Multiple Lines of Text](drawmulstring.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Working with Text APIs](index.html)

[« Previous](renderinghints.html) • [Trail](../TOC.html) • [Next »](drawmulstring.html)

# Using Text Attributes to Style Text

Applications typically need the capability to apply the following text attributes:

* *Underline* – A line that is drawn underneath text
* *Strikethrough* – A horizontal line that is drawn through the text
* *Superscript* or *Subscript*
  – A text or a letter that appears slightly above a line or correspondingly below a line
* *Kerning* – The adjustment of the space between characters

These and other text attributes can be applied by using the Java 2D™ `TextAttribute` class.

To apply these text attributes by add them to a `Font` object. For example:

```

Map<TextAttribute, Object> map = new Hashtable<TextAttribute, Object>();
map.put(TextAttribute.KERNING, TextAttribute.KERNING_ON);
font = font.deriveFont( map );
graphics.setFont( font );

```

The code example represented below shows the application of text attributes in the following order:

1. Sample string (no text attributes applied)- Kerning- Kerning and Underlining- Kerning,Underlining and Strikethrough- Kerning,Underlining, Strikethrough and Color

---

**Note:** If you don't see the applet running, you need to install [release 6 of the Java SE Development Kit (JDK)](http://java.sun.com/javase/downloads/index.jsp).

---

The complete code for this applet is in
[`AttributedText.java`](examples/AttributedText.java).

[« Previous](renderinghints.html)
•
[Trail](../TOC.html)
•
[Next »](drawmulstring.html)

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

**Previous page:** Displaying Antialiased Text by Using Rendering Hints
  
**Next page:** Drawing Multiple Lines of Text




A browser with JavaScript enabled is required for this page to operate properly.