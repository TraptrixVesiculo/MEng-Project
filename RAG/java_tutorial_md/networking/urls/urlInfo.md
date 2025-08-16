[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Working with URLs

[Working with URLs](index.html)

[What Is a URL?](definition.html)

[Creating a URL](creatingUrls.html)

Parsing a URL

[Reading Directly from a URL](readingURL.html)

[Connecting to a URL](connecting.html)

[Reading from and Writing to a URLConnection](readingWriting.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working with URLs](index.html)

[« Previous](creatingUrls.html) • [Trail](../TOC.html) • [Next »](readingURL.html)

# Parsing a URL

The `URL` class provides several methods that let you query
`URL` objects.
You can get the protocol, authority, host name,
port number, path, query, filename, and reference from a URL using these accessor methods:

**`getProtocol`**: Returns the protocol identifier component of the URL. **`getAuthority`**: Returns the authority component of the URL. **`getHost`**: Returns the host name component of the URL. **`getPort`**: Returns the port number component of the URL. The `getPort` method returns an integer that is the port number. If the port is not set, `getPort` returns -1. **`getPath`**: Returns the path component of this URL. **`getQuery`**: Returns the query component of this URL. **`getFile`**: Returns the filename component of the URL. The `getFile` method returns the same as `getPath`, plus the concatenation of the value of `getQuery, if any. getRef: Returns the reference component of the URL.`

---

**Note:**  Remember that not all URL addresses contain
these components. The URL class provides these methods because HTTP URLs
do contain these components and are perhaps the most commonly used URLs.
The URL class is somewhat HTTP-centric.

---

You can use these `getXXX` methods to get information
about the URL regardless of the constructor that you used to create the
URL object.

The URL class, along with these accessor methods, frees you from ever
having to parse URLs again! Given any string specification of a URL,
just create a new URL object and call any of the accessor methods
for the information you need. This small example program creates
a URL from a string specification and then uses the URL object's
accessor methods to parse the URL:

```


import java.net.*;
import java.io.*;

public class ParseURL {
    public static void main(String[] args) throws Exception {
        URL aURL = new URL("http://java.sun.com:80/docs/books/tutorial"
                           + "/index.html?name=networking#DOWNLOADING");
        System.out.println("protocol = " + aURL.getProtocol());
	System.out.println("authority = " + aURL.getAuthority());
        System.out.println("host = " + aURL.getHost());
        System.out.println("port = " + aURL.getPort());
        System.out.println("path = " + aURL.getPath());
        System.out.println("query = " + aURL.getQuery());
        System.out.println("filename = " + aURL.getFile());
        System.out.println("ref = " + aURL.getRef());
    }
}

```

Here's the output displayed by the program:

```

protocol = http
authority = java.sun.com:80
host = java.sun.com
port = 80
path = /docs/books/tutorial/index.html
query = name=networking
filename = /docs/books/tutorial/index.html?name=networking
ref = DOWNLOADING

```

[« Previous](creatingUrls.html)
•
[Trail](../TOC.html)
•
[Next »](readingURL.html)

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

**Previous page:** Creating a URL
  
**Next page:** Reading Directly from a URL




A browser with JavaScript enabled is required for this page to operate properly.