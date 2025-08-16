[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Software Setup

[LDAP Setup](content.html)

[Java Application Setup](package.html)

**Trail:** Java Naming and Directory Interface(TM).

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)

[« Previous](../overview/index.html) • [Trail](../TOC.html) • [Next »](content.html)

# Lesson: Software Setup

## Required Software

Following is a list of the software/systems that you need:

* [Java platform software](#JDK)* [Service provider software](#PROVIDER)* [Naming and directory server software](#SERVER)

---

### Java Platform Software

JNDI is included in the Java SE Platform.

To run the applets, you can use any Java-compatible Web browser,
such as
[Firefox](http://www.mozilla.com/firefox/), or
[Internet Explorer v5](http://www.microsoft.com/ie/) or later.
To ensure that your applets take full advantage of the latest
features of the Java platform software, you can use the
[Java Plug-in](http://java.sun.com/products/plugin/)
with your Web browser.

---

 **Note 1:**
If you are using JDK release prior to v 1.3, then you can use the
JNDI software available from the
[JNDI Web site](http://java.sun.com/products/jndi).

---

### Service Provider Software

The JNDI API is a generic API for accessing any naming or directory
service.
Actual access to a naming or directory service is enabled by plugging in a
service provider under the JNDI.
An overview of the JNDI architecture and the role of
service providers is given in the
[JNDI Overview](../../jndi/overview/index.html)  lesson.

A *service provider* is software that maps the JNDI API
to actual calls to the naming or directory server.
Typically, the roles
of the service provider and that of the naming/directory server
differ.
In the terminology of client/server software, the JNDI and the service provider
are the *client*
(called the *JNDI client*) and
the naming/directory server is the *server*.

Clients and servers may interact in many ways.
In one common way, they use a network protocol so that the
client and server can exist autonomously in a networked environment.
The server typically supports many different clients,
not only JNDI clients, provided that the clients conform to the
specified protocol.
The JNDI does not dictate any particular style of interaction between
JNDI clients and servers. For example,
at one extreme the client and server could be
the same entity.

You need to obtain the classes for the service providers that you will
be using.
For example, if you plan to use the JNDI to access
an LDAP directory server, then you would need software for
an LDAP service provider.

The JDK comes with service providers for:

* Light Weight Directory Protocol (LDAP)* CORBA Common Object Services naming (COS naming)* RMI registry* Domain Name Service (DNS)

If you are interested in other providers please check the
[JNDI Web site](http://java.sun.com/products/jndi/serviceproviders.html) for download information.

---

 **Note 2:**
The above service providers are bundled with JDK since
v 1.3 except the DNS service Provider which was made available since
JDK v 1.4.

---

This tutorial uses only the LDAP Service provider.
When using the LDAP service provider, you need either to
set up your own server or to have access to an
existing server, as explained next.

### Naming and Directory Server Software

Once you have obtained the service provider software, you
then need to set up or have
access to a corresponding naming/directory server.
Setting up a naming/directory server is typically the job of a network
system administrator.
Different vendors have different installation procedures for
their naming/directory servers.
Some require special machine privileges before the server can be installed.
You should consult the naming/directory server software's installation
instructions.

For the directory examples in this tutorial, you need
access to an LDAP server.
If you would like to take a quick tour of what
LDAP is check out [here](http://en.wikipedia.org/wiki/LDAP).
You can use any LDAP-compliant server of your choice.
The Sun Java Directory Server, which runs on many platforms, including Windows,
is available for evaluation at:
[Sun Java Directory Server home](http://wwws.sun.com/software/products/directory_srvr/home_directory.html).

You can also download free LDAP servers below:

* [OpenDS](https://opends.dev.java.net/)
* [OpenLDAP](http://www.OpenLDAP.org/)
* [Fedora Directory Server](http://directory.fedora.redhat.com/)
* [Apache Directory Server](http://directory.apache.org)

A publicly accessible server is available at: ldap://ldap.openldap.org Naming Context: dc=OpenLDAP,dc=org

[« Previous](../overview/index.html)
•
[Trail](../TOC.html)
•
[Next »](content.html)

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
  
**Next page:** LDAP Setup




A browser with JavaScript enabled is required for this page to operate properly.