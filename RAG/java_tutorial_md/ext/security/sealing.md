[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Extension Mechanism
  
**Lesson:** Making Extensions Secure

[Making Extensions Secure](index.html)

[Setting Privileges for Extensions](policy.html)

Sealing Packages in Extensions

[Home Page](../../index.html)
>
[The Extension Mechanism](../index.html)
>
[Making Extensions Secure](index.html)

[« Previous](policy.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Sealing Packages in Extensions

You can optionally *seal* packages in extension JAR files
as an additional security measure. If a package is sealed, all
classes defined in that package must originate from a single
JAR file.

Without sealing, a "hostile" program could create a class and define it
to be a member of one of your extension packages. The hostile software
would then have free access to package-protected members of your extension
package.

Sealing packages in extensions is no different than sealing any
JAR-packaged classes.
To seal your extension packages, you must add the Sealed
header to the manifest of the JAR file containing your extension. You can
seal individual packages by associating a Sealed header with
the packages' Name headers. A Sealed header not
associated with an individual package in the archive signals that all
packages are sealed. Such a "global" Sealed header is
overridden by any Sealed headers associated with
individual packages. The value associated with the Sealed
header is either true or false.

### Examples

> Let's look at a few sample manifest files. For these
> examples suppose that the JAR file contains these packages:
>
> ```
>
> com/myCompany/package_1/
> com/myCompany/package_2/
> com/myCompany/package_3/
> com/myCompany/package_4/
>
> ```
>
> Suppose that you want to seal all the packages. You could do so by
> simply adding an archive-level Sealed header to the manifest
> like this:
>
> ```
>
> Manifest-Version: 1.0
> Sealed: true
>
> ```
>
> All packages in any JAR file having this manifest will be sealed.
>
> If you wanted to seal only com.myCompany.package\_3, you
> could do so with this manifest:
>
> ```
>
> Manifest-Version: 1.0
>
> Name: com/myCompany/package_3/
> Sealed: true
>
> ```
>
> In this example the only Sealed header is that associated with
> the Name header of package com.myCompany.package\_3,
> so only that package is sealed. (The Sealed header is associated
> with the Name header because there are no blank lines between
> them.)
>
> For a final example, suppose that you wanted to seal all packages
> *except for* com.myCompany.package\_2. You could
> accomplish that with a manifest like this:
>
> ```
>
> Manifest-Version: 1.0
> Sealed: true
>
> Name: com/myCompany/package_2/
> Sealed: false
>
> ```
>
> In this example the archive-level Sealed: true header
> indicates that all of the packages in the JAR file
> are to be sealed. However, the manifest also has a
> Sealed: false header associated with package
> com.myCompany.package\_2, and that header overrides the archive-level
> sealing for that package. Therefore this manifest will cause
> all packages to be sealed except for com.myCompany.package\_2.

[« Previous](policy.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Setting Privileges for Extensions
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.