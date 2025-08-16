[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Overview of JNDI

[Naming Package](naming.html)

[Directory and LDAP Packages](dir.html)

[Event and Service Provider Packages](event.html)

**Trail:** Java Naming and Directory Interface(TM).

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)

[« Previous](../concepts/index.html) • [Trail](../TOC.html) • [Next »](naming.html)

# Lesson: Overview of JNDI

The Java Naming and
Directory Interface™ (JNDI)
is an application programming interface (API) that
provides
[naming](naming.html)
and
[directory](dir.html)
functionality to applications written using the Java™ programming language.
It is defined to be independent of any specific directory service
implementation.
Thus a variety of directories -new, emerging, and already deployed can be accessed in a common way.

## Architecture

The JNDI architecture consists of an API
and a service provider interface (SPI).
Java applications use the JNDI API to access a variety of naming
and directory services.
The SPI enables a variety of naming and directory services to be plugged in
transparently, thereby allowing the Java application using the JNDI API
to access their services. See the following figure.

![JNDI Architecture](../../figures/jndi/jndiarch.gif)

## Packaging

JNDI is included in the Java SE Platform.
To use the JNDI, you must have the JNDI classes
and one or more service providers.
The JDK includes service providers for the
following naming/directory services:

* Lightweight Directory Access Protocol (LDAP)* Common Object Request Broker Architecture (CORBA) Common Object Services (COS) name service* Java Remote Method Invocation (RMI) Registry* Domain Name Service (DNS)

Other service providers can be downloaded from the
[JNDI Web site](http://java.sun.com/products/jndi/serviceproviders.html)
or obtained from other vendors.

The JNDI is divided into five packages:

* [javax.naming](naming.html)* [javax.naming.directory](dir.html)* [javax.naming.ldap](dir.html)* [javax.naming.event](event.html)* [javax.naming.spi](event.html)

The next part of the lesson has a brief description of the JNDI packages.

[« Previous](../concepts/index.html)
•
[Trail](../TOC.html)
•
[Next »](naming.html)

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
  
**Next page:** Naming Package




A browser with JavaScript enabled is required for this page to operate properly.