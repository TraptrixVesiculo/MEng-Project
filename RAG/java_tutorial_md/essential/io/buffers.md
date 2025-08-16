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

[Byte Streams](bytestreams.html)

[Character Streams](charstreams.html)

Buffered Streams

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

[« Previous](charstreams.html) • [Trail](../TOC.html) • [Next »](scanfor.html)

# Buffered Streams

Most of the examples we've seen so far use *unbuffered* I/O.
This means each read or write request is
handled directly by the underlying OS. This can make a program much less
efficient, since each such request often triggers disk access, network
activity, or some other operation that is relatively expensive.

To reduce this kind of overhead, the Java platform implements
*buffered* I/O streams. Buffered input streams read data from a
memory area known as a *buffer*; the native input API is
called only when the buffer is empty. Similarly, buffered output
streams write data to a buffer, and the native output API is called
only when the buffer is full.

A program can convert an unbuffered stream into a buffered stream using
the wrapping idiom we've used several times now, where the unbuffered
stream object is passed to the constructor for a buffered stream
class. Here's how you might modify the constructor invocations in the
`CopyCharacters` example to use buffered I/O:

```

        inputStream = 
            new BufferedReader(new FileReader("xanadu.txt"));
        outputStream = 
            new BufferedWriter(new FileWriter("characteroutput.txt"));

```

There are four buffered stream classes used to wrap unbuffered
streams:
[`BufferedInputStream`](http://download.oracle.com/javase/7/docs/api/java/io/BufferedInputStream.html)
and
[`BufferedOutputStream`](http://download.oracle.com/javase/7/docs/api/java/io/BufferedOutputStream.html)
create buffered byte streams, while
[`BufferedReader`](http://download.oracle.com/javase/7/docs/api/java/io/BufferedReader.html)
and
[`BufferedWriter`](http://download.oracle.com/javase/7/docs/api/java/io/BufferedWriter.html)
create buffered character streams.

## Flushing Buffered Streams

It often makes sense to write out a buffer at critical points, without
waiting for it to fill. This is known as *flushing* the
buffer.

Some buffered output classes support *autoflush*, specified by an
optional constructor argument. When autoflush is enabled, certain key events
cause the buffer to be flushed. For example, an autoflush
`PrintWriter` object flushes the buffer on every
invocation of `println` or `format`. See
[Formatting](formatting.html) for more on these methods.

To flush a stream manually, invoke its `flush` method. The
`flush` method is valid on any output stream, but has no
effect unless the stream is buffered.

[« Previous](charstreams.html)
•
[Trail](../TOC.html)
•
[Next »](scanfor.html)

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

**Previous page:** Character Streams
  
**Next page:** Scanning and Formatting




A browser with JavaScript enabled is required for this page to operate properly.