[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Software Setup

[Software Setup](index.html)

[LDAP Setup](content.html)

Java Application Setup

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Software Setup](index.html)

[« Previous](content.html) • [Trail](../TOC.html) • [Next »](../ops/index.html)

# Java Application Setup

To use the JNDI in your program, you need to set up
its compilation and execution environments.

## Importing the JNDI Classes

Following are the JNDI packages:

* [javax.naming](http://download.oracle.com/javase/7/docs/api/javax/naming/package-summary.html)* [javax.naming.directory](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/package-summary.html)* [javax.naming.event](http://download.oracle.com/javase/7/docs/api/javax/naming/event/package-summary.html)* [javax.naming.ldap](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/package-summary.html)* [javax.naming.spi](http://download.oracle.com/javase/7/docs/api/javax/naming/spi/package-summary.html)

The examples in this trail use classes and interfaces
from the first two packages. You need to
import these two packages into your program or import individual
classes and interfaces that you use.
The following two lines import all of the classes and interfaces from
the two packages javax.naming and javax.naming.directory.

```

import javax.naming.*;
import javax.naming.directory.*;

```

## Compilation Environment

To compile a program that uses the JNDI, you need access to the JNDI classes.
The
[Java SE 6](http://java.sun.com/javase/6/)
already include the JNDI classes, so if you are using it you need not take further actions.

If you are using an older version- Java 2 SDK v1.2 or earlier,
please refer to the main
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/basics/prepare/package.html ) for instructions on how to setup the compilation environment.

## Execution Environment

To run a program that uses the JNDI,
you need access to the JNDI classes and classes for any service
providers that the program uses.
The
[Java Runtime Environment (JRE) 6](http://java.sun.com/javase/6/)
already includes
the JNDI classes and service providers for LDAP, COS naming, the RMI registry
and the DNS .

If you are using some other
service providers, then you need to download and install their archive files in the
*JAVA\_HOME*/jre/lib/ext directory, where
*JAVA\_HOME* is the directory that contains
the JRE. The  [JNDI Web site](http://java.sun.com/products/jndi/#download) lists some service providers. You may download these providers or use
providers from other vendors.

If you are using an older version- JRE v1.2 or earlier, please refer to the main
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/basics/prepare/package.html ) for instructions on how to setup the runtime environment.

For using the examples in this trail, you'll need the LDAP service provider.

[« Previous](content.html)
•
[Trail](../TOC.html)
•
[Next »](../ops/index.html)

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

**Previous page:** LDAP Setup
  
**Next page:** Naming and Directory Operations




A browser with JavaScript enabled is required for this page to operate properly.