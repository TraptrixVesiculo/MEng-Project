[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O
  
**Section:** File I/O (Featuring NIO.2)

[Basic I/O](index.html)

[I/O Streams](streams.html)

[Byte Streams](bytestreams.html)

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

Random Access Files

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

[« Previous](file.html) • [Trail](../TOC.html) • [Next »](dirs.html)

# Random Access Files

*Random access files* permit nonsequential, or random,
access to a file's contents.
To access a file randomly, you open the file, seek a particular
location, and read from or write to that file.

This functionality is possible with the
[`SeekableByteChannel`](http://download.java.net/jdk7/docs/api/java/nio/channels/SeekableByteChannel.html) interface. The `SeekableByteChannel` interface
extends channel I/O with the notion of a current position.
Methods enable you to set or query the position, and you can then
read the data from, or write the data to, that location.
The API consists of a few, easy to use, methods:

* [`position`](http://download.java.net/jdk7/docs/api/java/nio/channels/SeekableByteChannel.html#position()) – Returns the channel's current position* [`position(long)`](http://download.java.net/jdk7/docs/api/java/nio/channels/SeekableByteChannel.html#position(long)) – Sets the channel's position* [`read(ByteBuffer)`](http://download.java.net/jdk7/docs/api/java/nio/channels/SeekableByteChannel.html#read(java.nio.ByteBuffer)) – Reads bytes into the buffer from the channel* [`write(ByteBuffer)`](http://download.java.net/jdk7/docs/api/java/nio/channels/SeekableByteChannel.html#write(java.nio.ByteBuffer)) – Writes bytes from the buffer to the channel* [`truncate(long)`](http://download.java.net/jdk7/docs/api/java/nio/channels/SeekableByteChannel.html#truncate(long)) – Truncates the file (or other entity) connected to the channel

[Reading and Writing Files With Channel I/O](file.html#channelio) shows that the `Path.newByteChannel` methods return
an instance of a `SeekableByteChannel`.
On the default file system, you can use that
channel as is, or you can cast it to a
[`FileChannel`](http://download.java.net/jdk7/docs/api/java/nio/channels/FileChannel.html) giving you access to more advanced features, such as mapping a region
of the file directly into memory for faster access, locking a region of
the file, or reading and writing bytes from an absolute location without
affecting the channel's current position.

The following code snippet opens a file for both reading and writing
by using one of the `newByteChannel` methods. The
`SeekableByteChannel` that is returned is cast to
a `FileChannel`.
Then, 12 bytes are read from the beginning of the file,
and the string "I was here!" is written at that location.
The current position in the file is moved to
the end, and the 12 bytes from the beginning are appended.
Finally, the string, "I was here!" is appended, and the
channel on the file is closed.

```

String s = "I was here!\n";
byte data[] = s.getBytes();
ByteBuffer out = ByteBuffer.wrap(data);

ByteBuffer copy = ByteBuffer.allocate(12);

try (FileChannel fc = (FileChannel.open(file, READ, WRITE))) {
    //Read the first 12 bytes of the file.
    int nread;
    do {
        nread = fc.read(copy);
    } while (nread != -1 && copy.hasRemaining());

    //Write "I was here!" at the beginning of the file.
    fc.position(0);
    while (out.hasRemaining())
        fc.write(out);
    out.rewind();

    //Move to the end of the file.  Copy the first 12 bytes to
    //the end of the file.  Then write "I was here!" again.
    long length = fc.size();
    fc.position(length-1);
    copy.flip();
    while (copy.hasRemaining())
        fc.write(copy);
    while (out.hasRemaining())
        fc.write(out);
} catch (IOException x) {
    System.out.println("I/O Exception: " + x);
}

```

[« Previous](file.html)
•
[Trail](../TOC.html)
•
[Next »](dirs.html)

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

**Previous page:** Reading, Writing, and Creating Files
  
**Next page:** Creating and Reading Directories




A browser with JavaScript enabled is required for this page to operate properly.