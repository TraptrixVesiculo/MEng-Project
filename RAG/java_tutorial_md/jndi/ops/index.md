[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Naming and Directory Operations

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

[Time Limit](timelimit.html)

[Trouble Shooting Tips](faq.html)

**Trail:** Java Naming and Directory Interface(TM).

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)

[« Previous](../software/index.html) • [Trail](../TOC.html) • [Next »](exception.html)

# Lesson: Naming and Directory Operations

You can use the JNDI to perform naming operations, including
read operations and operations
for updating the namespace.
The following operations are described in this lesson:

* [Looking up an object](lookup.html)* [Listing the contents of a context](list.html)* [Adding, overwriting, and removing a binding](bind.html)* [Renaming an object](rename.html)* [Creating and destroying subcontexts](create.html)

## Configuration

Before performing any operation on a naming or directory service,
you need to acquire an *initial context*--the
starting point into the namespace.
This is because all methods on naming and directory services
are performed relative to some context.
To get an initial context, you must follow these steps.

1. Select the service provider of the
   corresponding service you want to access.- Specify any configuration
     that the initial context needs.- Call the
       [InitialContext](http://download.oracle.com/javase/7/docs/api/javax/naming/InitialContext.html#constructor_detail) constructor.

## Step1: Select the Service Provider for the Initial Context

You can specify the service provider to use for the initial context
by creating a set of *environment properties* (a Hashtable)
and adding the name of the service provider class to it.
Environment properties are described in detail in the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/beyond/env/index.html) 

If you are using the LDAP service provider from Sun Microsystems,
then your code would look like the following.

```

Hashtable env = new Hashtable();
env.put(Context.INITIAL_CONTEXT_FACTORY, 
	"com.sun.jndi.ldap.LdapCtxFactory");

```

To specify the file system service provider from Sun Microsystems,
you would write code that looks like the following.

```

Hashtable env = new Hashtable();
env.put(Context.INITIAL_CONTEXT_FACTORY, 
	"com.sun.jndi.fscontext.RefFSContextFactory");

```

You can also use
*system properties*
to specify the service provider to use.
Check out the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/beyond/index.html)  for details.

## Step2: Supply the Information Needed by the Initial Context

Clients of different directories might need various information
for contacting the directory.
For example, you might need to specify on which machine the server is running
and what information is needed to identify the user to the directory.
Such information is passed to the service provider via
environment properties.
The JNDI specifies some generic environment properties that service
providers can use.
Your service provider documentation will give details on the
information required for these properties.

The LDAP provider requires that the program specify the location of the LDAP
server, as well as user identity information.
To provide this information,
you would write code that looks as follows.

```

env.put(Context.PROVIDER_URL, "ldap://ldap.wiz.com:389");
env.put(Context.SECURITY_PRINCIPAL, "joeuser");
env.put(Context.SECURITY_CREDENTIALS, "joepassword");

```

This tutorial uses the LDAP service provider from
Sun Microsystems.
The examples assume that a server has been set up
on the local machine at port 389 with the root-distinguished name of
"o=JNDITutorial" and that no authentication is required for
updating the directory. They include the following code for
setting up the environment.

```

env.put(Context.PROVIDER_URL, "ldap://localhost:389/o=JNDITutorial");

```

If you are using a directory that is set up differently,
then you will need to set up these environment properties accordingly.
You will need to replace "localhost" with the name of that machine.
You can run these examples against any
[public directory servers](../../jndi/software/index.html) or your own server running on a different machine.
You will need to replace "localhost" with the name of that machine
and replace o=JNDITutorial with the naming context that is
available.

## Step3: Creating the Initial Context

You are now ready to create the initial context.
To do that, you pass to the
[InitialContext constructor](http://download.oracle.com/javase/7/docs/api/javax/naming/InitialContext.html#constructor_detail) the environment properties that you created previously:

```

Context ctx = new InitialContext(env);

```

Now that you have a reference to a
[Context](http://download.oracle.com/javase/7/docs/api/javax/naming/Context.html) object,
you can begin to access the naming service.

To perform directory operations, you need to use an
[InitialDirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InitialDirContext.html). To do that, use one of its
[constructors](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/InitialDirContext.html#constructor_detail):

```

DirContext ctx = new InitialDirContext(env);

```

This statement returns a reference to a
[DirContext](http://download.oracle.com/javase/7/docs/api/javax/naming/directory/DirContext.html) object for performing directory operations.

[« Previous](../software/index.html)
•
[Trail](../TOC.html)
•
[Next »](exception.html)

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
  
**Next page:** Naming Exceptions




A browser with JavaScript enabled is required for this page to operate properly.