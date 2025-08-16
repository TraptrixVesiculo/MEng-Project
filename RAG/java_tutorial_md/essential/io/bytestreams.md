[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O
  
**Section:** I/O Streams

[Basic I/O](index.html)

[I/O Streams](streams.html)

Byte Streams

[Character Streams](charstreams.html)

[Buffered Streams](buffers.html)

[Scanning and Formatting](scanfor.html)

[Scanning](scanning.html)

[Formatting](formatting.html)

[I/O from the Command Line](cl.html)

[Data Streams](datastreams.html)

[Object Streams](objectstreams.html)

[File I/O (Featuring NIO.2)](fileio.html)

[What Is a Path? (And Other File System Facts)](path.html)

[The Path Class](pathClass.html)

[Path Operations](pathOps.html)

[File Operations](fileOps.html)

[Checking a File or Directory](check.html)

[Deleting a File or Directory](delete.html)

[Copying a File or Directory](copy.html)

[Moving a File or Directory](move.html)

[Managing Metadata (File and File Store Attributes)](fileAttr.html)

[Reading, Writing, and Creating Files](file.html)

[Random Access Files](rafs.html)

[Creating and Reading Directories](dirs.html)

[Links, Symbolic or Otherwise](links.html)

[Walking the File Tree](walk.html)

[Finding Files](find.html)

[Watching a Directory for Changes](notification.html)

[Other Useful Methods](misc.html)

[Legacy File I/O Code](legacy.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Basic I/O](index.html)

[« Previous](streams.html) • [Trail](../TOC.html) • [Next »](charstreams.html)

# Byte Streams

Programs use *byte streams* to perform input and output of
8-bit bytes. All byte stream classes are descended from
[`InputStream`](http://download.oracle.com/javase/7/docs/api/java/io/InputStream.html) and
[`OutputStream`](http://download.oracle.com/javase/7/docs/api/java/io/OutputStream.html).

There are many byte stream classes. To demonstrate how byte streams
work, we'll focus on the file I/O byte streams,
[`FileInputStream`](http://download.oracle.com/javase/7/docs/api/java/io/FileInputStream.html) and
[`FileOutputStream`](http://download.oracle.com/javase/7/docs/api/java/io/FileOutputStream.html). Other kinds of byte streams are
used in much the same way; they differ mainly in the way they are
constructed.

## Using Byte Streams

We'll explore `FileInputStream` and
`FileOutputStream` by examining an example program named
[`CopyBytes`](examples/CopyBytes.java), which uses byte streams to copy `xanadu.txt`, one byte at
a time.

```


import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyBytes {
    public static void main(String[] args) throws IOException {
        FileInputStream in = null;
        FileOutputStream out = null;
        try {
            in = new FileInputStream("xanadu.txt");
            out = new FileOutputStream("outagain.txt");
            int c;

            while ((c = in.read()) != -1) {
                out.write(c);
            }

        } finally {
            if (in != null) {
                in.close();
            }
            if (out != null) {
                out.close();
            }
        }
    }
}

```

`CopyBytes` spends most of its time in a simple loop that
reads the input stream and writes the output stream, one byte at a
time, as shown in
the following figure.

![Simple byte stream input and output.](../../figures/essential/byteStream.png)

Simple byte stream input and output.

Notice that `read()` returns an `int` value. If
the input is a stream of bytes, why doesn't `read()` return
a `byte` value? Using a `int` as a return type
allows `read()` to use -1 to indicate that it has reached the
end of the stream.

## Always Close Streams

Closing a stream when it's no longer needed is very important —
so important that `CopyBytes` uses a
`finally` block to guarantee that both streams will be
closed even if an error occurs. This practice helps avoid serious
resource leaks.

One possible error is that `CopyBytes` was unable to open
one or both files. When that happens, the stream variable
corresponding to the file never changes from its initial
`null` value. That's why `CopyBytes` makes sure
that each stream variable contains an object reference before invoking
`close`.

## When Not to Use Byte Streams

`CopyBytes` seems like a normal program, but it actually
represents a kind of low-level I/O that you should avoid. Since
`xanadu.txt` contains character data, the best approach is
to use [character streams](charstreams.html), as discussed
in the next section. There are
also streams for more complicated data types. Byte streams should only
be used for the most primitive I/O.

So why talk about byte streams? Because all other stream types are
built on byte streams.

[« Previous](streams.html)
•
[Trail](../TOC.html)
•
[Next »](charstreams.html)

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

**Previous page:** I/O Streams
  
**Next page:** Character Streams




A browser with JavaScript enabled is required for this page to operate properly.