[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** Naming and Directory Operations

[Naming and Directory Operations](index.html)

Naming Exceptions

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

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[Naming and Directory Operations](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](lookup.html)

# Naming Exceptions

Many methods in the JNDI packages throw a
[NamingException](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingException.html) when they need to indicate that the operation requested cannot
be performed.
Commonly, you will see a try/catch
wrapper around the methods that can throw a NamingException:
> ```
>
> try {
>     Context ctx = new InitialContext();
>     Object obj = ctx.lookup("somename");
> } catch (NamingException e) {
>     // Handle the error
>     System.err.println(e);
> }
>
> ```

#### Exception Class Hierarchy

The JNDI has a rich exception hierarchy stemming from
the NamingException class.
The class names of the exceptions are self-explanatory and are listed
[here](http://download.oracle.com/javase/7/docs/api/javax/naming/package-tree.html)  .

To handle a particular subclass of
NamingException specially, you catch the
subclass separately.
For example, the following code specially treats the AuthenticationException
and its subclasses.
> ```
>
> try {
>     Context ctx = new InitialContext();
>     Object obj = ctx.lookup("somename");
> } catch (AuthenticationException e) {
>     // attempt to reacquire the authentication information
>     ...
> } catch (NamingException e) {
>     // Handle the error
>     System.err.println(e);
> }
>
> ```

#### Enumerations

Operations such as
[Context.list()](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html#list(javax.naming.Name)) 
and
[DirContext.search()](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html#search(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls))  return a
[NamingEnumeration](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingEnumeration.html) . In
these cases, if an error occurs and no results are returned,
then NamingException or one of its appropriate subclasses will be
thrown at the time that the method is invoked. If an error occurs but
there are some results to be returned, then a NamingEnumeration is
returned so that you can get those results. When all of the results are
exhausted, invoking
[NamingEnumeration.hasMore()](http://download.oracle.com/javase/7/docs/api/javax/naming/NamingEnumeration.html#hasMore())  will cause a
NamingException (or one of its subclasses) to be
thrown to indicate the
error. At that point, the enumeration becomes invalid and no more
methods should be invoked on it.

For example, if you perform a search() and specify a
count limit (*n*) of how many answers to return,
then the search()
will return an enumeration consisting of at most *n*
results. If the number of results exceeds *n*, then
when NamingEnumeration.hasMore() is invoked for the *n+1*
time, a SizeLimitExceededException will be thrown.
See the  [count limit discussion](countlimit.html)
of this lesson for a sample code.

#### Examples in This Tutorial

In the inline sample code that is embedded within the text of
this tutorial, the try/catch clauses are usually omitted for
the sake of readability. Typically, because only code
fragments are shown here, only the lines that are directly useful in
illustrating a concept are included.
You will see appropriate placements of the
try/catch clauses for NamingException
if you look in the source files that
accompany this tutorial.

The Exceptions in the javax.naming package can be found
[here](http://download.oracle.com/javase/7/docs/api/javax/naming/package-summary.html) .

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](lookup.html)

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

**Previous page:** Naming and Directory Operations
  
**Next page:** Lookup an Object




A browser with JavaScript enabled is required for this page to operate properly.