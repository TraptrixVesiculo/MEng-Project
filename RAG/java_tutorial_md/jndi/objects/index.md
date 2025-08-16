[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Java Objects in the Directory

[Storing and Reading Objects](store.html)

[Serializable Objects](serial.html)

**Trail:** Java Naming and Directory Interface(TM).

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)

[« Previous](../ldap/index.html) • [Trail](../TOC.html) • [Next »](store.html)

# Lesson: Java Objects in the Directory

Traditionally, directories have been used to store data. Users
and programmers think of the directory as a hierarchy of directory
entries, each containing a set of attributes. You look up an entry
from the directory and extract the attribute(s) of interest.

For applications written in the JavaTM programming language,
Java objects may sometimes be shared across applications.
For such applications, it makes sense to be able to use the directory as a
repository for Java objects.
The directory provides a centrally administered, and possibly
replicated, service for use by Java applications distributed
across the network.
For example, an application server might use the directory for
registering objects that represent the services that it manages so
that a client can later search the directory to locate those services
as needed. An example of JNDI used as a directory of
services is Apache DS. More information about this can be found at
[ApacheDS v1.0](http://directory.apache.org/apacheds/1.0/).

The JNDI provides
an object-oriented view of the directory,
thereby allowing Java objects to be
added to and retrieved from the directory without requiring the
client to manage data representation issues.
This lesson discusses the use of the directory for
storing and retrieving Java objects at a basic level.
The JNDI provides what are known as object and state factories for
creating and storing the objects accessed from the directory.
#### Object Factory
An object factory is a producer of objects. It accepts some information
about how to create an object, such as a reference, and then returns an
instance of that object.
For details about Object Factories and the format in which objects are
stored in the directory please refer to the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/objects/factory/index.html) .
#### State Factory
A state factory transforms an object into another object.
The input is the object and optional attributes, supplied to
Context.bind() and the output is another object and optional attributes,
to be stored in the underlying naming service or directory.
For details about State Factories and on how to write your own state factory
please refer to the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/objects/state/index.html) .

The next part of the lesson discusses how to access Objects in the Directory
It describes how serializable objects can be stored and read in the directory.
For other types of objects please check out the
[JNDI Tutorial](http://java.sun.com/products/jndi/tutorial/objects/index.html) .

[« Previous](../ldap/index.html)
•
[Trail](../TOC.html)
•
[Next »](store.html)

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
  
**Next page:** Storing and Reading Objects




A browser with JavaScript enabled is required for this page to operate properly.