[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Advanced Topics for LDAP Users

[Advanced Topics for LDAP Users](index.html)

[LDAP v3](ldap.html)

JNDI as an LDAP API

[How LDAP Operations Map to JNDI APIs](operations.html)

[How LDAP Error Codes Map to JNDI Exceptions](exceptions.html)

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

[« Previous](ldap.html) • [Trail](../TOC.html) • [Next »](operations.html)

# JNDI as an LDAP API

Both the JNDI and LDAP models define a hierarchical namespace in which
you name objects. Each object in the namespace may have
attributes that can be used to search for the object.
At this high level, the two models are similar, so it is not surprising
that the JNDI maps well to the LDAP.

## Models

You can think of an LDAP entry as a JNDI
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html).
Each LDAP entry contains a name and a set of attributes,
as well as an optional set of child entries.
For example, the LDAP entry "o=JNDITutorial" may have as its attributes
"objectclass" and "o", and it may have as its children
"ou=Groups" and "ou=People".

In the JNDI, the LDAP entry "o=JNDITutorial" is represented as a context
with the name "o=JNDITutorial" that has
two subcontexts, named: "ou=Groups" and "ou=People".
An LDAP entry's attributes are represented by the
[Attributes](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/Attributes.html) interface, whereas individual attributes are represented by the
[Attribute](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/Attribute.html) interface.

![A representation of LDAP and JNDI](../../figures/jndi/model.gif)

See [the next part of this lesson](operations.html)
for details on how the LDAP operations are accessed through the JNDI.

## Names

As a result of federation, the names that you supply to the JNDI's
context methods can span multiple
namespaces. These are called composite names.
When using the JNDI to access an LDAP service, you should be aware
that the forward slash character ("/") in
a string name has special meaning to the JNDI.
If the LDAP entry's name
contains this character, then you need to escape it
(using the backslash character ("\")).
For example, an LDAP entry with the name "cn=O/R" must be presented
as the string "cn=O\\/R" to the JNDI context methods.
For more information about Names check out the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/beyond/names/index.html) . The
[LdapName](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html) and
[Rdn](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/Rdn.html)  classes simplify creation and manipulation of LDAP names.

LDAP names as they are used in the protocol are always
fully qualified names that identify entries that start from the root
of the LDAP namespace (as defined by the server).
Following are some examples of fully qualified LDAP names.

```

cn=John Smith, ou=Marketing, o=Some Corporation, c=gb
cn=Vinnie Ryan, ou=People, o=JNDITutorial

```

In the JNDI, however, names are always *relative*;
that is, you always name an object relative to a context.
For example, you can name the entry "cn=Vinnie Ryan"
relative to the context named "ou=People, o=JNDITutorial".
Or you can name the entry "cn=Vinnie Ryan, ou=People"
relative to the context named "o=JNDITutorial".
Or, you can create an initial context that points at the root
of the LDAP server's namespace and name the entry
"cn=Vinnie Ryan, ou=People, o=JNDITutorial".

In the JNDI, you can also use LDAP URLs to name LDAP entries.
See the LDAP URL discussion in the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/ldap/misc/url.html)

[« Previous](ldap.html)
•
[Trail](../TOC.html)
•
[Next »](operations.html)

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

**Previous page:** LDAP v3
  
**Next page:** How LDAP Operations Map to JNDI APIs




A browser with JavaScript enabled is required for this page to operate properly.