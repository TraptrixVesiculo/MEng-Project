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

[Result Count](countlimit.html)

Time Limit

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](countlimit.html) • [Trail](../TOC.html) • [Next »](faq.html)

# Time Limit

A time limit on a search places an upper bound
on the amount of time that the search operation will block waiting
for the answers.
This is useful when you don't want to wait too long for an answer.
If the time limit specified is exceeded before the search operation
can be completed, then a
[TimeLimitExceededException](http://download.oracle.com/javase/7/docs/api/javax/naming/TimeLimitExceededException.html) will be thrown.

To set the time limit of a search, pass the number of milliseconds
to
[SearchControls.setTimeLimit()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/SearchControls.html#setTimeLimit(int)).
The following [example](examples/SearchTimeLimit.java)
sets the time limit to 1 second.

```

// Set the search controls to limit the time to 1 second (1000 ms)
SearchControls ctls = new SearchControls();
ctls.setTimeLimit(1000);

```

To get this particular example to exceed its time limit,
you need to reconfigure it to use either a slow server, or a server that has lots
of entries.
Alternatively, you can use other tactics to make the search take longer than 1 second.

A time limit of zero means that no time limit has been set
and that calls to the directory will wait indefinitely for an answer.

[« Previous](countlimit.html)
•
[Trail](../TOC.html)
•
[Next »](faq.html)

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

**Previous page:** Result Count
  
**Next page:** Trouble Shooting Tips




A browser with JavaScript enabled is required for this page to operate properly.