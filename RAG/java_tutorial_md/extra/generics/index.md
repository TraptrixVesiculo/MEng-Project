[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Generics

[Introduction](intro.html)

[Defining Simple Generics](simple.html)

[Generics and Subtyping](subtype.html)

[Wildcards](wildcards.html)

[Generic Methods](methods.html)

[Interoperating with Legacy Code](legacy.html)

[The Fine Print](fineprint.html)

[Class Literals as Runtime-Type Tokens](literals.html)

[More Fun with Wildcards](morefun.html)

[Converting Legacy Code to Use Generics](convert.html)

[Acknowledgements](acknowledgements.html)

**Trail:** Bonus

[Home Page](../../index.html)
>
[Bonus](../index.html)

[« Previous](../index.html) • [Trail](../TOC.html) • [Next »](intro.html)

# Lesson: Generics

### *by Gilad Bracha*

> ---
>
> **Note:** This lesson covers a language feature introduced in the
> latest release of the
> JavaTM 2 Platform Standard Edition version 5.0.
> Visit the [J2SE 5.0 download page](http://java.sun.com/j2se/1.5.0/download.jsp).
>
> ---
>
> Introduced in J2SE 5.0, this long-awaited enhancement to the type system
> allows a type or method to operate on objects of various types while providing
> compile-time type safety. It adds compile-time type safety to the Collections
> Framework and eliminates the drudgery of casting.
> > **[Introduction](intro.html)**
> >
> > **[Defining Simple Generics](simple.html)**
> >
> > **[Generics and Subtyping](subtype.html)**
> >
> > **[Wildcards](wildcards.html)**
> >
> > **[Generic Methods](methods.html)**
> >
> > **[Interoperating with Legacy Code](legacy.html)**
> >
> > **[The Fine Print](fineprint.html)**
> >
> > **[Class Literals as Runtime-Type Tokens](literals.html)**
> >
> > **[More Fun with Wildcards](morefun.html)**
> >
> > **[Converting Legacy Code to Use Generics](convert.html)**
> >
> > **[Acknowledgements](acknowledgements.html)**

[« Previous](../index.html)
•
[Trail](../TOC.html)
•
[Next »](intro.html)

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

**Previous page:** Table of Contents
  
**Next page:** Introduction




A browser with JavaScript enabled is required for this page to operate properly.