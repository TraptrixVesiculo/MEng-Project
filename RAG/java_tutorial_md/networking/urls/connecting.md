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

[Parsing a URL](urlInfo.html)

[Reading Directly from a URL](readingURL.html)

Connecting to a URL

[Reading from and Writing to a URLConnection](readingWriting.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working with URLs](index.html)

[« Previous](readingURL.html) • [Trail](../TOC.html) • [Next »](readingWriting.html)

# Connecting to a URL

After you've successfully created a `URL` object,
you can call the `URL` object's `openConnection`
method to get a `URLConnection` object, or one of its
protocol specific subclasses, e.g.
[`java.net.HttpURLConnection`](http://download.oracle.com/javase/7/docs/api/java/net/HttpURLConnection.html)

You can use this `URLConnection` object to setup parameters
and general request properties that you may need before connecting.
Connection to the remote object represented by the URL is only initiated
when the `URLConnection.connect` method is called.
When you do this
you are initializing a communication link
between your Java program and the URL over the network.
For example, you can open a connection to the Yahoo site
with the following code:

```

try {
    URL yahoo = new URL("http://www.yahoo.com/");
    URLConnection yahooConnection = yahoo.openConnection();
    yahooConnection.connect();

} catch (MalformedURLException e) {     // new URL() failed
    . . .
} catch (IOException e) {               // openConnection() failed
    . . .
}

```

A new `URLConnection` object is created every time by calling
the `openConnection` method of the protocol handler for this URL.

You are not always required to explicitly call the `connect`
method to initiate the connection. Operations that depend on being connected,
like `getInputStream`, `getOutputStream`, etc, will
implicitly perform the connection, if necessary.

Now that you've successfully connected to your URL, you can use the
`URLConnection` object to perform actions
such as reading from or writing
to the connection. The next section shows you how.

[« Previous](readingURL.html)
•
[Trail](../TOC.html)
•
[Next »](readingWriting.html)

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

**Previous page:** Reading Directly from a URL
  
**Next page:** Reading from and Writing to a URLConnection




A browser with JavaScript enabled is required for this page to operate properly.