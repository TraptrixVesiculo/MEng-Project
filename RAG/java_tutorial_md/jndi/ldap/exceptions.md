[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users
  
**Section:** JNDI as an LDAP API

[Advanced Topics for LDAP Users](index.html)

[LDAP v3](ldap.html)

[JNDI as an LDAP API](jndi.html)

[How LDAP Operations Map to JNDI APIs](operations.html)

How LDAP Error Codes Map to JNDI Exceptions

[Security](security.html)

[Modes of Authenticating to LDAP](authentication.html)

[Authentication Mechanisms](auth_mechs.html)

[Anonymous](anonymous.html)

[Simple](simple.html)

[SASL](sasl.html)

[Digest-MD5](digest.html)

[SSL and Custom Sockets](ssl.html)

[More LDAP Operations](rename.html)

[LDAP Compare](compare.html)

[Search Results](result.html)

[LDAP Unsolicited Notifications](unsol.html)

[Connection Management](connect.html)

[Creation](create.html)

[Closing](close.html)

[Pooling](pool.html)

[Configuration](config.html)

[Frequently Asked Questions](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Advanced Topics for LDAP Users](index.html)

[« Previous](operations.html) • [Trail](../TOC.html) • [Next »](security.html)

# How LDAP Error Codes Map to JNDI Exceptions

The LDAP defines a set of status codes that are returned
with LDAP responses sent by the LDAP server
(see
[RFC 2251](http://ietf.org/rfc/rfc2251.txt)).
In the JNDI, error conditions are indicated as checked
exceptions that are subclasses of
[NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html). See the
[Naming Exceptions](../../jndi/ops/exception.html)  section for an overview of the JNDI exception classes.

The LDAP service provider translates the LDAP status code it receives
from the LDAP server to the appropriate subclass of
NamingException. The following table shows the mapping
between LDAP status codes and JNDI exceptions.

| LDAP Status Code | Meaning | Exception or Action |
| --- | --- | --- |
| 0 | Success | Report success. |
| 1 | Operations error | [NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) |
| 2 | Protocol error | [CommunicationException](http://download.oracle.com/javase/7/docs/api/javax/naming/CommunicationException.html) |
| 3 | Time limit exceeded. | [TimeLimitExceededException](http://download.oracle.com/javase/7/docs/api/javax/naming/TimeLimitExceededException.html) |
| 4 | Size limit exceeded. | [SizeLimitExceededException](http://download.oracle.com/javase/7/docs/api/javax/naming/SizeLimitExceededException.html) |
| 5 | Compared false. | Used by [DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, javax.naming.directory.Attributes)). Does not generate an exception. |
| 6 | Compared true. | Used by [DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, javax.naming.directory.Attributes)). Does not generate an exception. |
| 7 | Authentication method not supported. | [AuthenticationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationNotSupportedException.html) |
| 8 | Strong authentication required. | [AuthenticationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationNotSupportedException.html) |
| 9 | Partial results being returned. | If the environment property "java.naming.referral" is set to "ignore" or the contents of the error do not contain a referral, throw a [PartialResultException](http://download.oracle.com/javase/7/docs/api/javax/naming/PartialResultException.html). Otherwise, use contents to build a referral. |
| 10 | Referral encountered. | If the environment property "java.naming.referral" is set to "ignore", then ignore. If the property is set to "throw", throw [ReferralException](http://download.oracle.com/javase/7/docs/api/javax/naming/ReferralException.html). If the property is set to "follow", then the LDAP provider processes the referral. If the "java.naming.ldap.referral.limit" property has been exceeded, throw [LimitExceededException](http://download.oracle.com/javase/7/docs/api/javax/naming/LimitExceededException.html). |
| 11 | Administrative limit exceeded. | [LimitExceededException](http://download.oracle.com/javase/7/docs/api/javax/naming/LimitExceededException.html) |
| 12 | Unavailable critical extension requested. | [OperationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/OperationNotSupportedException.html) |
| 13 | Confidentiality required. | [AuthenticationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationNotSupportedException.html) |
| 14 | SASL bind in progress. | Used internally by the LDAP provider during authentication. |
| 16 | No such attribute exists. | [NoSuchAttributeException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/NoSuchAttributeException.html) |
| 17 | An undefined attribute type. | [InvalidAttributeIdentifierException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InvalidAttributeIdentifierException.html) |
| 18 | Inappropriate matching | [InvalidSearchFilterException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InvalidSearchFilterException.html) |
| 19 | A constraint violation. | [InvalidAttributeValueException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InvalidAttributeValueException.html) |
| 20 | An attribute or value already in use. | [AttributeInUseException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/AttributeInUseException.html) |
| 21 | An invalid attribute syntax. | [InvalidAttributeValueException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InvalidAttributeValueException.html) |
| 32 | No such object exists. | [NameNotFoundException](http://download.oracle.com/javase/7/docs/api/javax/naming/NameNotFoundException.html) |
| 33 | Alias problem | [NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) |
| 34 | An invalid DN syntax. | [InvalidNameException](http://download.oracle.com/javase/7/docs/api/javax/naming/InvalidNameException.html) |
| 35 | Is a leaf. | Used by the LDAP provider; usually doesn't generate an exception. |
| 36 | Alias dereferencing problem | [NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) |
| 48 | Inappropriate authentication | [AuthenticationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationNotSupportedException.html) |
| 49 | Invalid credentials | [AuthenticationException](http://download.oracle.com/javase/7/docs/api/javax/naming/AuthenticationException.html) |
| 50 | Insufficient access rights | [NoPermissionException](http://download.oracle.com/javase/7/docs/api/javax/naming/NoPermissionException.html) |
| 51 | Busy | [ServiceUnavailableException](http://download.oracle.com/javase/7/docs/api/javax/naming/ServiceUnavailableException.html) |
| 52 | Unavailable | [ServiceUnavailableException](http://download.oracle.com/javase/7/docs/api/javax/naming/ServiceUnavailableException.html) |
| 53 | Unwilling to perform | [OperationNotSupportedException](http://download.oracle.com/javase/7/docs/api/javax/naming/OperationNotSupportedException.html) |
| 54 | Loop detected. | [NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) |
| 64 | Naming violation | [InvalidNameException](http://download.oracle.com/javase/7/docs/api/javax/naming/InvalidNameException.html) |
| 65 | Object class violation | [SchemaViolationException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SchemaViolationException.html) |
| 66 | Not allowed on non-leaf. | [ContextNotEmptyException](http://download.oracle.com/javase/7/docs/api/javax/naming/ContextNotEmptyException.html) |
| 67 | Not allowed on RDN. | [SchemaViolationException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SchemaViolationException.html) |
| 68 | Entry already exists. | [NameAlreadyBoundException](http://download.oracle.com/javase/7/docs/api/javax/naming/NameAlreadyBoundException.html) |
| 69 | Object class modifications prohibited. | [SchemaViolationException](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SchemaViolationException.html) |
| 71 | Affects multiple DSAs. | [NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) |
| 80 | Other | [NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) |

[« Previous](operations.html)
•
[Trail](../TOC.html)
•
[Next »](security.html)

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

**Previous page:** How LDAP Operations Map to JNDI APIs
  
**Next page:** Security




A browser with JavaScript enabled is required for this page to operate properly.