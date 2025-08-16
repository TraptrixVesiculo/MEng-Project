[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O

[Basic I/O](index.html)

I/O Streams

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](bytestreams.html)

# I/O Streams

An *I/O Stream* represents an input source or an output
destination. A stream can represent many different kinds of sources
and destinations, including disk files, devices, other programs, and
memory arrays.

Streams support many different kinds of data, including simple bytes,
primitive data types, localized characters, and objects. Some streams
simply pass on data; others manipulate and transform the data in
useful ways.

No matter how they work internally, all streams present the same simple
model to programs that use them: A stream is a sequence of data.
A program uses an *input stream* to read data from a source, one
item at a time:

![Reading information into a program.](../../figures/essential/io-ins.gif)

Reading information into a program.

A program uses an *output stream* to write data to a destination,
one item at time:

![Writing information from a program.](../../figures/essential/io-outs.gif)

Writing information from a program.

In this lesson, we'll see streams that can handle all kinds of data,
from primitive values to advanced objects.

The data source and data destination pictured above can be anything
that holds, generates, or consumes data. Obviously this includes disk
files, but a source or destination can also be another program, a
peripheral device, a network socket, or an array.

In the next section, we'll use the most basic kind of streams, byte
streams, to demonstrate the common operations of Stream I/O.
For sample input, we'll use the example file
[`xanadu.txt`](examples/xanadu.txt), which contains the following verse:

```

In Xanadu did Kubla Khan
A stately pleasure-dome decree:
Where Alph, the sacred river, ran
Through caverns measureless to man
Down to a sunless sea.

```

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](bytestreams.html)

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

**Previous page:** Basic I/O
  
**Next page:** Byte Streams




A browser with JavaScript enabled is required for this page to operate properly.