[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Working with URLs

[What Is a URL?](definition.html)

[Creating a URL](creatingUrls.html)

[Parsing a URL](urlInfo.html)

[Reading Directly from a URL](readingURL.html)

[Connecting to a URL](connecting.html)

[Reading from and Writing to a URLConnection](readingWriting.html)

**Trail:** Custom Networking

[Home Page](../../index.html)
>
[Custom Networking](../index.html)

[« Previous](../overview/index.html) • [Trail](../TOC.html) • [Next »](definition.html)

# Lesson: Working with URLs

URL is the acronym for Uniform Resource Locator. It is a reference (an
address) to a resource on the Internet. You provide URLs to your
favorite Web browser so that it can locate files on the Internet in the
same way that you provide addresses on letters so that the post office
can locate your correspondents.

Java programs that interact with the Internet also may use URLs to find
the resources on the Internet they wish to access. Java programs can
use a class called
[`URL`](http://download.oracle.com/javase/7/docs/api/java/net/URL.html) in the `java.net` package to represent a URL
address.

---

**Terminology Note:** 
The term *URL* can be ambiguous.
It can refer to an Internet address or a
`URL` object in a Java program.
Where the meaning of URL needs to be
specific, this text uses "URL address" to mean an Internet address and
"`URL` object" to refer to an instance
of the `URL` class in a program.

---

## [What Is a URL?](definition.html)

A URL takes the form of a string that describes how to find a resource
on the Internet. URLs have two main components: the protocol needed to
access the resource and the location of the resource.

## [Creating a URL](creatingUrls.html)

Within your Java programs, you can create a URL object that represents
a URL address. The URL object always refers to an absolute URL but can
be constructed from an absolute URL, a relative URL, or from URL components.

## [Parsing a URL](urlInfo.html)

Gone are the days of parsing a URL to find out the host name, filename,
and other information. With a valid URL object you can call any of its
accessor methods to get all of that information from the URL without
doing any string parsing!

## [Reading Directly from a URL](readingURL.html)

This section shows how your Java programs can read from a URL using the
`openStream()` method.

## [Connecting to a URL](connecting.html)

If you want to do more than just read from a URL, you can connect to it
by calling `openConnection()` on the URL. The `openConnection()`
method returns a URLConnection object that you can use for more general
communications with the URL, such as reading from it, writing to it, or
querying it for content and other information.

## [Reading from and Writing to a URLConnection](readingWriting.html)

Some URLs, such as many that are connected to cgi-bin scripts, allow
you to (or even require you to) write information to the URL. For example,
a search script may require detailed query data to be written to the URL
before the search can be performed. This section shows you how to write
to a URL and how to get results back.

[« Previous](../overview/index.html)
•
[Trail](../TOC.html)
•
[Next »](definition.html)

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
  
**Next page:** What Is a URL?




A browser with JavaScript enabled is required for this page to operate properly.