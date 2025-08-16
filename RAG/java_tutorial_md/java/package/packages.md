[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Packages

[Packages](index.html)

Creating and Using Packages

[Creating a Package](createpkgs.html)

[Naming a Package](namingpkgs.html)

[Using Package Members](usepkgs.html)

[Managing Source and Class Files](managingfiles.html)

[Summary of Creating and Using Packages](summary-package.html)

[Questions and Exercises](QandE/packages-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Packages](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](createpkgs.html)

# Creating and Using Packages

To make types easier to
find and use, to avoid naming conflicts, and to control access,
programmers bundle groups of related types into packages.

---

**Definition:** 
A *package* is a grouping of related types
providing access protection and name space management.
Note that *types* refers to classes, interfaces, enumerations,
and annotation types. Enumerations and annotation types are special
kinds of classes and interfaces, respectively, so *types*
are often referred to in this
lesson
simply as *classes and interfaces*.

---

The types that are part of the Java platform
are members of various packages that bundle classes by function:
fundamental classes are in `java.lang`, classes for
reading and writing (input and output) are in `java.io`,
and so on. You can put your types in packages too.

Suppose you write a group of classes
that represent graphic objects, such as circles,
rectangles, lines, and points. You also write an interface,
`Draggable`,
that classes implement if they can be dragged with the mouse.

```

//in the Draggable.java file
public interface Draggable {
    . . .
}

//in the Graphic.java file
public abstract class Graphic {
    . . .
}

//in the Circle.java file
public class Circle extends Graphic implements Draggable {
    . . .
}

//in the Rectangle.java file
public class Rectangle extends Graphic implements Draggable {
    . . .
}

//in the Point.java file
public class Point extends Graphic implements Draggable {
    . . .
}

//in the Line.java file
public class Line extends Graphic implements Draggable {
    . . .
}

```

You should bundle these classes and the interface in a package
for several reasons, including the following:

* You and other programmers can easily determine that these
  types are related.* You and other programmers know where to find types
    that can provide graphics-related functions.* The names of your types won't conflict with the type names
      in other packages because the package creates a new namespace.* You can allow types within the package to have unrestricted
        access to one another yet still restrict access for types outside
        the package.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](createpkgs.html)

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

**Previous page:** Packages
  
**Next page:** Creating a Package




A browser with JavaScript enabled is required for this page to operate properly.