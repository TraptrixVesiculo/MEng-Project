[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** New features in JDK 5.0 and JDK 6

[New features in JDK 5.0 and JDK 6](index.html)

[Retrieving Distinguished Name](dn.html)

Standard LDAP Controls

[Paged Results Control](paged-results.html)

[Sort Control](sort.html)

[Manage Referral Control](mdsaIT.html)

[Manipulating LdapName (Distinguished Name)](ldapname.html)

[Manipulating Relative Distringuished Name (RDN)](rdn.html)

[Setting Timeout for Ldap Operations](readtimeout.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[New features in JDK 5.0 and JDK 6](index.html)

[« Previous](dn.html) • [Trail](../TOC.html) • [Next »](paged-results.html)

# Standard LDAP Controls

In LDAP v3, a Control is a message that enhances the existing LDAP
operation by associating it with more information useful to the server or the
client.
A control can be either a request control or a response control.
A request control is sent from the client to the server along with an
LDAP request.
A response control is sent from the server to the client along with
an LDAP response.
Either is represented by the interface
[javax.naming.ldap.Control](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/Control.html)

See the controls lesson in the
 [JNDI tutorial](http://java.sun.com/products/jndi/tutorial/ldap/ext/)
if you haven't programmed using controls before.

In this lesson we will discuss the standard LDAP controls that are
added to JDK 5.0.
The necessary LDAP controls are already supported in the LDAP
Booster Pack extension package available for the JNDI/LDAP
service provider under com.sun.jndi.ldap.ctl package.
The LDAP controls that are standardized by IETF are now made available
in the javax.naming.ldap package of JDK through the following classes.

* [ManageReferralControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/ManageReferralControl.html) ([RFC 3296](http://www.ietf.org/rfc/rfc3296.txt))* [PagedResultsControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/PagedResultsControl.html) ([RFC 2696](http://www.ietf.org/rfc/rfc2696.txt))* [PagedResultsResponseControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/PagedResultsResponseControl.html)* [SortControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/SortControl.html) ([RFC 2891](http://www.ietf.org/rfc/rfc2891.txt))* [SortKey](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/SortKey.html)* [SortResponseControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/SortResponseControl.html)* [BasicControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/BasicControl.html)

[« Previous](dn.html)
•
[Trail](../TOC.html)
•
[Next »](paged-results.html)

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

**Previous page:** Retrieving Distinguished Name
  
**Next page:** Paged Results Control




A browser with JavaScript enabled is required for this page to operate properly.