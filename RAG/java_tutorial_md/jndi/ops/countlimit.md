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

[Scope](scope.html)

Result Count

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](scope.html) • [Trail](../TOC.html) • [Next »](timelimit.html)

# Result Count

Sometimes, a query might produce too many answers
and you want to limit the number
of answers returned. You can do this by using the
count limit search control.
By default, a search does not have a count limit--it will return all answers that it finds.
To set the count limit of a search, pass the number
to
[SearchControls.setCountLimit()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#setCountLimit(long)).

[The following example](examples/SearchCountLimit.java)
sets the count limit to 1.
> ```
>
> // Set the search controls to limit the count to 1
> SearchControls ctls = new SearchControls();
> ctls.setCountLimit(1);
>
> ```

If the program attempts to get
more than the count limit number of results, then a
[SizeLimitExceededException](http://download.oracle.com/javase/7/docs/api/javax/naming/SizeLimitExceededException.html) will be thrown.
So if a program has set a count limit, then it should either differentiate
this exception from other
[NamingExceptions](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) or keep track of the count limit and not request more
than that number of results.

Specifying a count limit for a search is one way of controlling the
resources (such as memory and network bandwidth) that your application
consumes. Other ways to control the resources consumed are
to narrow your
[search filter](filter.html)
(be more specific about what you seek),
start your search in the appropriate context,
and use the appropriate [scope](scope.html).

[« Previous](scope.html)
•
[Trail](../TOC.html)
•
[Next »](timelimit.html)

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

**Previous page:** Scope
  
**Next page:** Time Limit




A browser with JavaScript enabled is required for this page to operate properly.