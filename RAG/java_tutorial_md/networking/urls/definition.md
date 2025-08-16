[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Working with URLs

[Working with URLs](index.html)

What Is a URL?

[Creating a URL](creatingUrls.html)

[Parsing a URL](urlInfo.html)

[Reading Directly from a URL](readingURL.html)

[Connecting to a URL](connecting.html)

[Reading from and Writing to a URLConnection](readingWriting.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working with URLs](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](creatingUrls.html)

# What Is a URL?

If you've been surfing the Web, you have undoubtedly heard the term URL
and have used URLs to access HTML pages from the Web.

It's often easiest, although not entirely accurate, to think of a URL
as the name of a file on the World Wide Web because most URLs refer to
a file on some machine on the network. However, remember that URLs also
can point to other resources on the network, such as database queries
and command output.

---

**Definition:** 
URL is an acronym for *Uniform Resource Locator*
and is a reference (an address) to a resource on the Internet.

---

The following is an example of a URL which addresses the
`java.sun.com` website:

![A URL with the protocol identifier and resource name labeled.](../../figures/networking/4url.gif)

As in the previous diagram, a URL has two main components:

* Protocol identifier* Resource name

Note that the protocol identifier and the resource name are separated
by a colon and two forward slashes. The protocol identifier indicates
the name of the protocol to be used to fetch the resource. The example
uses the Hypertext Transfer Protocol (HTTP), which is typically used to
serve up hypertext documents. HTTP is just one of many different
protocols used to access different types of resources on the net. Other
protocols include File Transfer Protocol (FTP), Gopher, File, and
News.

The resource name is the complete address to the resource. The format
of the resource name depends entirely on the protocol used, but for
many protocols, including HTTP, the resource name contains one or more
of the components listed in the following table:

|  |  |
| --- | --- |
| Host Name | The name of the machine on which the resource lives. |
| Filename | The pathname to the file on the machine. |
| Port Number | The port number to which to connect (typically optional). |
| Reference | A reference to a named anchor within a resource that usually identifies a specific location within a file (typically optional). |

For many protocols, the host name and the filename are required, while
the port number and reference are optional. For example, the resource
name for an HTTP URL must specify a server on the network (Host Name)
and the path to the document on that machine (Filename); it also can
specify a port number and a reference. In the URL for the Java Web
site `java.sun.com` is the host name
and an empty path or the trailing slash is shorthand for
the file named `/index.html`.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](creatingUrls.html)

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

**Previous page:** Working with URLs
  
**Next page:** Creating a URL




A browser with JavaScript enabled is required for this page to operate properly.