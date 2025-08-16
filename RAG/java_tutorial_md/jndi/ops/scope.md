[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Naming and Directory Operations
  
**Section:** Search

[Naming and Directory Operations](index.html)

[Naming Exceptions](exception.html)

[Lookup an Object](lookup.html)

[List the Context](list.html)

[Add, Replace or Remove a Binding](bind.html)

[Rename](rename.html)

[Create and Destroy Subcontexts](create.html)

[Attribute Names](attrnames.html)

[Read Attributes](getattrs.html)

[Modify Attributes](modattrs.html)

[Add, Replace Bindings with Attributes](bindattr.html)

[Search](search.html)

[Basic Search](basicsearch.html)

[Filters](filter.html)

Scope

[Result Count](countlimit.html)

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](filter.html) • [Trail](../TOC.html) • [Next »](countlimit.html)

# Scope

The default
[SearchControls](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html) specifies that the search is to be performed in the named context
(
[SearchControls.ONELEVEL\_SCOPE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#ONELEVEL_SCOPE)).
This default is used in the examples in the
[Search Filters section](filter.html).

In addition to this default, you can specify that
the search be performed in the *entire subtree* or
only in the named object.

## Search the Subtree

A search of the entire subtree searches the named object
and all of its descendants.
To make the search behave in this way, pass
[SearchControls.SUBTREE\_SCOPE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#SUBTREE_SCOPE) to
[SearchControls.setSearchScope()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#setSearchScope(int)) as follows.

```

// Specify the ids of the attributes to return
String[] attrIDs = {"sn", "telephonenumber", "golfhandicap", "mail"};
SearchControls ctls = new SearchControls();
ctls.setReturningAttributes(attrIDs);
ctls.setSearchScope(SearchControls.SUBTREE_SCOPE);

// Specify the search filter to match
// Ask for objects that have the attribute "sn" == "Geisel"
// and the "mail" attribute
String filter = "(&(sn=Geisel)(mail=*))";

// Search the subtree for objects by using the filter
NamingEnumeration answer = ctx.search("", filter, ctls);

```

[This example](examples/SearchSubtree.java)
searches the context ctx's subtree
for entries that satisfy the specified filter.
It finds the entry "cn= Ted Geisel, ou=People" in this subtree
that satisfies the filter.

```

# java SearchSubtree
>>>cn=Ted Geisel, ou=People
attribute: sn
value: Geisel
attribute: mail
value: Ted.Geisel@JNDITutorial.com
attribute: telephonenumber
value: +1 408 555 5252

```

## Search the Named Object

You can also search the named object.
This is useful, for example, to test whether the named
object satisfies a search filter.
To search the named object, pass
[SearchControls.OBJECT\_SCOPE](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#OBJECT_SCOPE) to setSearchScope().

```

// Specify the ids of the attributes to return
String[] attrIDs = {"sn", "telephonenumber", "golfhandicap", "mail"};
SearchControls ctls = new SearchControls();
ctls.setReturningAttributes(attrIDs);
ctls.setSearchScope(SearchControls.OBJECT_SCOPE);

// Specify the search filter to match
// Ask for objects that have the attribute "sn" == "Geisel"
// and the "mail" attribute
String filter = "(&(sn=Geisel)(mail=*))";

// Search the subtree for objects by using the filter
NamingEnumeration answer = 
    ctx.search("cn=Ted Geisel, ou=People", filter, ctls);

```

[`This example`](examples/SearchObject.java) tests whether the object "cn=Ted Geisel, ou=People" satisfies
the given filter.

```

# java SearchObject
>>>
attribute: sn
value: Geisel
attribute: mail
value: Ted.Geisel@JNDITutorial.com
attribute: telephonenumber
value: +1 408 555 5252

```

The example found one answer and printed it. Notice that the name of the
result is the empty string.
This is because the name of the object
is always named relative to the context of the search
(in this case, "cn=Ted Geisel, ou=People").

[« Previous](filter.html)
•
[Trail](../TOC.html)
•
[Next »](countlimit.html)

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

**Previous page:** Filters
  
**Next page:** Result Count




A browser with JavaScript enabled is required for this page to operate properly.