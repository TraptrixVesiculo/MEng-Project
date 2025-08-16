[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Packages
  
**Section:** Creating and Using Packages

[Packages](index.html)

[Creating and Using Packages](packages.html)

Creating a Package

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

[« Previous](packages.html) • [Trail](../TOC.html) • [Next »](namingpkgs.html)

# Creating a Package

To create a package, you choose a name for the package (naming conventions are discussed in
the next section) and put a `package` statement with that name at the top of *every source file* that
contains the types (classes, interfaces, enumerations, and annotation types) that you want to include in the package.

The package statement (for example, `package graphics;`) must be the first line in the source file. There can be
only one package statement in each source file, and it applies to all types in the file.

---

**Note:** If you put multiple types in a single source file, only one can be `public`,
and it must have the same name as the source file. For example, you can define
`public class Circle`  in the file `Circle.java`, define `public interface Draggable`
in the file `Draggable.java`, define `public enum Day` in the file `Day.java`, and so forth.

You can include non-public types in the same file as a public type
(this is strongly discouraged, unless the non-public types are small and closely
related to the public type), but only the public type
will be accessible from outside of the package. All the top-level, non-public types will be *package private*.

---

If you put the graphics interface and classes listed in the preceding section in a package called `graphics`,
you would need six source files, like this:

```

//in the Draggable.java file
package graphics;
public interface Draggable {
    . . .
}

//in the Graphic.java file
package graphics;
public abstract class Graphic {
    . . .
}

//in the Circle.java file
package graphics;
public class Circle extends Graphic implements Draggable {
    . . .
}

//in the Rectangle.java file
package graphics;
public class Rectangle extends Graphic implements Draggable {
    . . .
}

//in the Point.java file
package graphics;
public class Point extends Graphic implements Draggable {
    . . .
}

//in the Line.java file
package graphics;
public class Line extends Graphic implements Draggable {
    . . .
}

```

If you do not use a `package` statement, your type
ends up in an unnamed package. Generally speaking, an unnamed package
is only for small or temporary applications or when you are just
beginning the development process.
Otherwise, classes and interfaces belong
in named packages.

[« Previous](packages.html)
•
[Trail](../TOC.html)
•
[Next »](namingpkgs.html)

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

**Previous page:** Creating and Using Packages
  
**Next page:** Naming a Package




A browser with JavaScript enabled is required for this page to operate properly.