[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Custom Networking
  
**Lesson:** Working with URLs

[Working with URLs](index.html)

[What Is a URL?](definition.html)

Creating a URL

[Parsing a URL](urlInfo.html)

[Reading Directly from a URL](readingURL.html)

[Connecting to a URL](connecting.html)

[Reading from and Writing to a URLConnection](readingWriting.html)

[Home Page](../../index.html)
>
[Custom Networking](../index.html)
>
[Working with URLs](index.html)

[« Previous](definition.html) • [Trail](../TOC.html) • [Next »](urlInfo.html)

# Creating a URL

The easiest way to create a `URL` object is from a `String`
that represents the human-readable form of the URL address.
This is typically the form that another person will use for a URL.
For example, the URL for the Gamelan site,
which is a directory of Java resources, takes the following form:

```

http://www.gamelan.com/ 
```

In your Java program, you can use a `String`
containing this text to create a `URL` object:

```

URL gamelan = new URL("http://www.gamelan.com/");

```

The `URL` object created above represents an *absolute URL*.
An absolute URL contains all of the information necessary to reach the
resource in question.
You can also create `URL` objects from a *relative URL*
address.

## Creating a URL Relative to Another

A relative URL contains only enough information to reach the resource
relative to (or in the context of) another URL.

Relative URL specifications are often used within HTML files. For example,
suppose you write an HTML file called `JoesHomePage.html`.
Within this page, are links to other pages, `PicturesOfMe.html`
and `MyKids.html`, that are on the same machine and
in the same directory as `JoesHomePage.html`. The links to
`PicturesOfMe.html` and `MyKids.html` from
`JoesHomePage.html` could be specified just as filenames,
like this:

```

<a href="PicturesOfMe.html">Pictures of Me</a>
<a href="MyKids.html">Pictures of My Kids</a>

```

These URL addresses are *relative URLs*. That is, the URLs are
specified relative to the file in which they are contained--`JoesHomePage.html`.

In your Java programs,
you can create a `URL`
object from a relative URL specification.
For example, suppose you know two URLs at the Gamelan site:

```

http://www.gamelan.com/pages/Gamelan.game.html
http://www.gamelan.com/pages/Gamelan.net.html

```

You can create `URL`
objects for these pages relative
to their common base URL:
`http://www.gamelan.com/pages/` like this:

```

URL gamelan = new URL("http://www.gamelan.com/pages/");
URL gamelanGames = new URL(gamelan, "Gamelan.game.html");
URL gamelanNetwork = new URL(gamelan, "Gamelan.net.html");

```

This code snippet uses the `URL` constructor
that lets you create a `URL`
object from another `URL` object (the base) and a relative URL
specification. The general form of this constructor is:

```

URL(URL baseURL, String relativeURL)

```

The first argument is a `URL` object
that specifies the base of the new
`URL`.
The second argument is a `String` that specifies the rest of the
resource name relative to the base. If `baseURL` is null, then this
constructor treats `relativeURL` like an absolute URL specification.
Conversely, if `relativeURL` is an absolute URL specification,
then the constructor ignores `baseURL`.

This constructor is also useful for creating `URL`
objects for named anchors (also called references) within a file.
For example, suppose the `Gamelan.network.html`
file has a named anchor called `BOTTOM` at the
bottom of the file. You can use the relative URL constructor to create
a `URL` object for it like this:

```

URL gamelanNetworkBottom = new URL(gamelanNetwork, "#BOTTOM");

```

## Other URL Constructors

The `URL` class provides two additional constructors for creating a `URL`
object. These constructors are useful when you are working with URLs,
such as HTTP URLs, that have host name, filename, port number, and
reference components in the resource name portion of the URL. These two
constructors are useful when you do not have a String containing the
complete URL specification, but you do know various components of the
URL.

For example, suppose you design a network browsing panel similar to a
file browsing panel that allows users to choose the protocol, host
name, port number, and filename. You can construct a `URL`
from the panel's components. The first constructor creates a
`URL` object from a protocol, host name, and filename. The
following code snippet creates a `URL` to the
`Gamelan.net.html` file at the Gamelan site:

```

new URL("http", "www.gamelan.com", "/pages/Gamelan.net.html");

```

This is equivalent to

```

new URL("http://www.gamelan.com/pages/Gamelan.net.html");

```

The first argument is the protocol, the second is the host name, and
the last is the pathname of the file. Note that the filename contains a
forward slash at the beginning. This indicates that the filename is
specified from the root of the host.

The final `URL` constructor adds the port number to the list
of arguments used in the previous constructor:

```

URL gamelan = new URL("http", "www.gamelan.com", 80,
                       "pages/Gamelan.network.html");

```

This creates a `URL` object for the following URL:

```

http://www.gamelan.com:80/pages/Gamelan.network.html

```

If you construct a `URL` object using one of these
constructors, you can get a `String`
containing the complete URL address
by using the `URL` object's `toString` method or the
equivalent `toExternalForm` method.

## URL addresses with Special characters

Some URL addresses contain special characters, for example the space character. Like this:

```

http://foo.com/hello world/

```

To make theses characters legal they need to encoded before passing
them to the URL constructor.

```

URL url = new URL("http://foo.com/hello%20world");

```

Encoding the special character(s) in this example is easy as there is only one
character that needs encoding, but for URL addresses that have several of these
characters or if you are unsure when writing your code what URL addresses you
will need to access, you can use the multi-argument constructors of the
[`java.net.URI`](http://download.oracle.com/javase/7/docs/api/java/net/URI.html) class to automatically take care of
the encoding for you.

```

URI uri = new URI("http", "foo.com", "/hello world/", "");

```

And then convert the URI to a URL.

```

URL url = uri.toURL();

```

## MalformedURLException

Each of the four `URL` constructors
throws a `MalformedURLException` if the
arguments to the constructor refer to a `null` or unknown protocol.
Typically, you want to catch and handle this exception by embedding
your URL constructor statements in a
`try`/`catch` pair,
like this:

```

try {
    URL myURL = new URL(. . .)
} catch (MalformedURLException e) {
    . . .
    // exception handler code here
    . . .
}

```

See
[Exceptions](../../essential/exceptions/index.html) for information about handling exceptions.

---

**Note:** 
`URL`s are "write-once" objects.
Once you've created a `URL` object,
you cannot change any of its attributes
(protocol, host name, filename, or port number).

---

[« Previous](definition.html)
•
[Trail](../TOC.html)
•
[Next »](urlInfo.html)

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

**Previous page:** What Is a URL?
  
**Next page:** Parsing a URL




A browser with JavaScript enabled is required for this page to operate properly.