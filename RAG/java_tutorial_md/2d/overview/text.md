[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** 2D Graphics
  
**Lesson:** Overview of the Java 2D API Concepts

[Overview of the Java 2D API Concepts](index.html)

[Coordinates](coordinate.html)

[Java 2D Rendering](rendering.html)

[Geometric Primitives](primitives.html)

Text

[Images](images.html)

[Printing](printing.html)

[Home Page](../../index.html)
>
[2D Graphics](../index.html)
>
[Overview of the Java 2D API Concepts](index.html)

[« Previous](primitives.html) • [Trail](../TOC.html) • [Next »](images.html)

# Text

The Java 2D™ API has various text rendering capabilities including methods for
rendering strings and entire classes for setting font attributes and performing
text layout.

If you just want to draw a static text string, the most direct way to render it directly
through the `Graphics` class by using the
`drawString` method. To specify the font, you use the
`setFont` method of the `Graphics` class.

If you want to implement your own text-editing routines or need more control
over the layout of the text than the text components provide, you can use the
Java 2D text layout classes in the `java.awt.font` package.

## Fonts

The shapes that a font uses to represent the characters in a string are called
*glyphs*. A particular character or combination of characters might be represented
as one or more glyphs. For example, *á* might
be represented by
two glyphs, whereas the ligature *fi* might be
represented by a single glyph.

A *font* can be thought of as a collection of glyphs. A single font might have
many *faces*,
such as italic and regular. All of the
faces in a font have similar typographic features and can be recognized as
members of the same *family*. In other words, a collection of glyphs with a
particular style form a
*font face*. A collection of font faces forms a
*font family*. The collection of font families
forms the set of fonts that are available on the system.

When you are using the Java 2D API, you specify fonts by using an instance of
`Font`. You can determine what fonts are available by calling the static method
`GraphicsEnvironment.getLocalGraphicsEnvironment` and then
querying the returned `GraphicsEnvironment`. The
`getAllFonts` method returns an array that contains
`Font` instances for all of the fonts available on the
system. The `getAvailableFontFamilyNames` method returns a list of the
available font families.

## Text Layout

Before text can be displayed, it must be laid out so that the characters are
represented by the appropriate glyphs in the proper positions. The following are
two Java 2D mechanisms for managing text layout:

* The `TextLayout` class
  manages text layout, highlighting, and hit detection. The facilities provided
  by `TextLayout` handle the most common cases, including
  strings with mixed fonts, mixed languages, and bidirectional text. .
* You can create the own `GlyphVector` objects by using
  the `Font` class and then rendering each `GlyphVector` object through
  the `Graphics2D` class. Thus, you can
  completely control how text is shaped and positioned. .

## Rendering Hints for Text

The Java 2D API enables you to control the quality of shapes and text rendering by using
*rendering hints*. Rendering hints are encapsulated by the
`java.awt.RenderingHints` class.

As applied to text, this capability
is used for antialiasing (which is also known as an smooth edges).
For example, the `KEY_TEXT_ANTIALIASING` hint enables you
to control the antialiasing of text separately from the antialiasing of
other shapes. To learn more about rendering hints see the
[Controlling Rendering Quality](../advanced/quality.html) lesson.

[« Previous](primitives.html)
•
[Trail](../TOC.html)
•
[Next »](images.html)

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

**Previous page:** Geometric Primitives
  
**Next page:** Images




A browser with JavaScript enabled is required for this page to operate properly.