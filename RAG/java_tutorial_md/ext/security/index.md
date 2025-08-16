[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Making Extensions Secure

[Setting Privileges for Extensions](policy.html)

[Sealing Packages in Extensions](sealing.html)

**Trail:** The Extension Mechanism

[Home Page](../../index.html)
>
[The Extension Mechanism](../index.html)

[« Previous](../basics/index.html) • [Trail](../TOC.html) • [Next »](policy.html)

# Lesson: Making Extensions Secure

Now that you have seen how to use extensions,
you may be wondering what security privileges extensions have.
If you are developing an extension that does file I/O, for example,
you will need to know how your
extension is granted the appropriate permissions for reading
and writing files. Conversely, if you are thinking about using an extension
developed by someone else, you will want to understand clearly what
security privileges the extension has and how to change those
privileges should you desire to do so.

This lesson shows you how the
JavaTM platform's security architecture
treats extensions. You will see how to tell what privileges are granted
to extension software, and you will learn how to modify extension
privileges by following some simple steps. In addition, you will learn
how to seal packages within your extensions to restrict access to
specified parts of your code.

This lesson has two sections:

### [Setting Privileges for Extensions](policy.html)

> This section contains some examples that show you what conditions
> must be met for extensions to be granted permissions to perform
> security-sensitive operations.

### [Sealing Packages in Extensions](sealing.html)

> You can optionally seal packages in extension JAR files as an additional
> security measure. If a package is sealed, it means that all classes
> defined in that package must originate from a single JAR file. This
> section shows you how to modify an extension's manifest to seal
> extension packages.

### Additional Documentation

> You will find links and references to relevant security documentation at
> appropriate places throughout this lesson.
>
> For complete information on security, you can refer to the following:
>
> * [Security Features in Java SE](../../security/index.html) trail (in this tutorial)
> * [Security guide](http://download.oracle.com/javase/7/docs/technotes/guides/security)

[« Previous](../basics/index.html)
•
[Trail](../TOC.html)
•
[Next »](policy.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Setting Privileges for Extensions




A browser with JavaScript enabled is required for this page to operate properly.