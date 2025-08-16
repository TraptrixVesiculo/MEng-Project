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

Reading Directly from a URL

[Connecting to a URL](connecting.html)

[Reading from and Writing to a URLConnection](readingWriting.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working with URLs](index.html)

[« Previous](urlInfo.html) • [Trail](../TOC.html) • [Next »](connecting.html)

# Reading Directly from a URL

After you've successfully created a `URL`,
you can call the `URL`'s
`openStream()` method to get a stream from which you
can read the contents of the URL. The `openStream()`
method returns a
[`java.io.InputStream`](http://download.oracle.com/javase/7/docs/api/java/io/InputStream.html) object, so reading from a URL is as easy as reading from an input stream.

The following small Java program uses `openStream()` to get an input
stream on the URL `http://www.yahoo.com/`.
It then opens a `BufferedReader`
on the input stream and reads from the `BufferedReader`
thereby reading from the URL.
Everything read is copied to the standard output stream:

```


import java.net.*;
import java.io.*;

public class URLReader {
    public static void main(String[] args) throws Exception {
	URL yahoo = new URL("http://www.yahoo.com/");
	BufferedReader in = new BufferedReader(
				new InputStreamReader(
				yahoo.openStream()));

	String inputLine;

	while ((inputLine = in.readLine()) != null)
	    System.out.println(inputLine);

	in.close();
    }
}

```

When you run the program, you should see, scrolling by in your command
window, the HTML commands and textual content from the HTML file
located at `http://www.yahoo.com/`.
Alternatively, the program might hang
or you might see an exception stack trace. If either of the latter two
events occurs, you may have to
[set the proxy host](_setProxy.html) so
that the program can find the Yahoo server.

[« Previous](urlInfo.html)
•
[Trail](../TOC.html)
•
[Next »](connecting.html)

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

**Previous page:** Parsing a URL
  
**Next page:** Connecting to a URL




A browser with JavaScript enabled is required for this page to operate properly.