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

[Creating a Package](createpkgs.html)

Naming a Package

[Using Package Members](usepkgs.html)

[Managing Source and Class Files](managingfiles.html)

[Summary of Creating and Using Packages](summary-package.html)

[Questions and Exercises](QandE/packages-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Packages](index.html)

[« Previous](createpkgs.html) • [Trail](../TOC.html) • [Next »](usepkgs.html)

# Naming a Package

With programmers worldwide writing classes and interfaces using the Java
programming language, it is likely
that many programmers
will use the same name for different types. In fact, the
previous example does just that: It defines a `Rectangle`
class when there is already a `Rectangle` class in
the `java.awt` package. Still, the compiler allows both
classes to have the same name if they are in different
packages. The fully qualified name of each `Rectangle` class includes
the package name. That is, the fully qualified name of the `Rectangle`
class in the `graphics` package is `graphics.Rectangle`,
and the fully qualified name of the `Rectangle` class
in the `java.awt` package is `java.awt.Rectangle`.

This works well unless two independent programmers
use the same name for their packages. What prevents this problem? Convention.

### Naming Conventions

Package names are written in all lowercase to avoid conflict with the names of classes or interfaces.

Companies use their reversed Internet domain name to begin their package
names—for example, `com.example.orion`
for a package named `orion` created by a programmer at `example.com`.

Name collisions that occur within
a single company need to be handled by convention within that company,
perhaps by including the
region or the project name after the company name
(for example, `com.company.region.package`).

Packages in the Java language itself begin with `java.` or `javax.`

In some cases, the internet domain name may not be a valid
package name. This can occur if the domain name contains a
hyphen or other special character, if the package name
begins with a digit or other character that is illegal to
use as the beginning of a Java name, or if the package
name contains a reserved Java keyword, such as "int".
In this event, the suggested convention is to add an underscore.
For example:

**Legalizing Package Names**

| Domain Name | Package Name Prefix |
| clipart-open.org | org.clipart\_open |
| free.fonts.int | int\_.fonts.free |
| poetry.7days.com | com.\_7days.poetry |

[« Previous](createpkgs.html)
•
[Trail](../TOC.html)
•
[Next »](usepkgs.html)

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

**Previous page:** Creating a Package
  
**Next page:** Using Package Members




A browser with JavaScript enabled is required for this page to operate properly.