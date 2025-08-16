[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Naming and Directory Operations

[Naming and Directory Operations](index.html)

[Naming Exceptions](exception.html)

[Lookup an Object](lookup.html)

[List the Context](list.html)

[Add, Replace or Remove a Binding](bind.html)

[Rename](rename.html)

[Create and Destroy Subcontexts](create.html)

[Attribute Names](attrnames.html)

[Read Attributes](getattrs.html)

Modify Attributes

[Add, Replace Bindings with Attributes](bindattr.html)

[Search](search.html)

[Basic Search](basicsearch.html)

[Filters](filter.html)

[Scope](scope.html)

[Result Count](countlimit.html)

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](getattrs.html) • [Trail](../TOC.html) • [Next »](bindattr.html)

# Modify Attributes

The
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) interface contains methods for
modifying the attributes and attribute values of objects in
the directory.

## Using a List of Modifications

One way to modify the attributes of an object
is to supply a list of modification requests
(
[ModificationItem](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/ModificationItem.html)).
Each ModificationItem consists of a numeric constant indicating
the type of modification to make and an
[Attribute](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/Attribute.html) describing the modification to make.
Following are the three types of modifications:

* [ADD\_ATTRIBUTE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#ADD_ATTRIBUTE)* [REPLACE\_ATTRIBUTE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#REPLACE_ATTRIBUTE)* [REMOVE\_ATTRIBUTE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#REMOVE_ATTRIBUTE)

Modifications are applied in the order in which
they appear in the list.
Either all of the modifications are executed, or none are.

The following code creates a list of modifications.
It replaces the "mail" attribute's value with a
value of "geisel@wizards.com", adds an additional value to the
"telephonenumber" attribute, and removes the
"jpegphoto" attribute.

```

// Specify the changes to make
ModificationItem[] mods = new ModificationItem[3];

// Replace the "mail" attribute with a new value
mods[0] = new ModificationItem(DirContext.REPLACE_ATTRIBUTE,
    new BasicAttribute("mail", "geisel@wizards.com"));

// Add an additional value to "telephonenumber"
mods[1] = new ModificationItem(DirContext.ADD_ATTRIBUTE,
    new BasicAttribute("telephonenumber", "+1 555 555 5555"));

// Remove the "jpegphoto" attribute
mods[2] = new ModificationItem(DirContext.REMOVE_ATTRIBUTE,
    new BasicAttribute("jpegphoto"));

```

---

**Windows Active Directory:**
Active Directory defines "telephonenumber" to be a single-valued attribute,
contrary to [RFC 2256](http://ietf.org/rfc/rfc2256.txt).
To get this example to work against Active Directory, you must either
use an attribute other than "telephonenumber", or change the
DirContext.ADD\_ATTRIBUTE to DirContext.REPLACE\_ATTRIBUTE.

---

After creating this list of modifications, you can supply it
to
[modifyAttributes()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#modifyAttributes(javax.naming.Name, javax.naming.directory.ModificationItem[])) as follows.

```

// Perform the requested modifications on the named object
ctx.modifyAttributes(name, mods);

```

## Using Attributes

Alternatively, you can perform modifications by specifying
the type of modification and the attributes to which to apply the
modification.

For example, the following line replaces the attributes
(identified in orig)
associated with name with those in orig:

```

ctx.modifyAttributes(name, DirContext.REPLACE_ATTRIBUTE, orig);

```

Any other attributes of name remain unchanged.

Both of these uses of modifyAttributes() are demonstrated
in [the sample program](examples/ModAttrs.java). This
program modifies the attributes by using a modification list and then
uses the second form of modifyAttributes()
to restore the original attributes.

[« Previous](getattrs.html)
•
[Trail](../TOC.html)
•
[Next »](bindattr.html)

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

**Previous page:** Read Attributes
  
**Next page:** Add, Replace Bindings with Attributes




A browser with JavaScript enabled is required for this page to operate properly.