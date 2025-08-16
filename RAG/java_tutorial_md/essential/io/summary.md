[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O

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

[Random Access Files](rafs.html)

[Creating and Reading Directories](dirs.html)

[Links, Symbolic or Otherwise](links.html)

[Walking the File Tree](walk.html)

[Finding Files](find.html)

[Watching a Directory for Changes](notification.html)

[Other Useful Methods](misc.html)

[Legacy File I/O Code](legacy.html)

Summary

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Basic I/O](index.html)

[« Previous](legacy.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# Summary

The `java.io` package contains many classes that your programs can use
to read and write data. Most of the classes implement sequential access streams.
The sequential access streams can be divided into two groups:
those that read and write bytes and those that read and write Unicode characters.
Each sequential access stream has a speciality,
such as reading from or writing to a file, filtering data as its read or written,
or serializing an object.

The `java.nio.file` package provides extensive support for file
and file system I/O.
This is a very comprehensive API, but the key entry points are as follows:

* The `Path` class has methods for manipulating a path.* The `Files` class has methods for file operations,
    such as moving, copy, deleting, and also methods for retrieving and
    setting file attributes.* The `FileSystem` class has a variety of methods for
      obtaining information about the file system.

More information on NIO.2 can be found on the
[OpenJDK: NIO](http://openjdk.java.net/projects/nio/) project website on
[java.net](http://home.java.net/). This site includes resources for features provided by NIO.2 that are
beyond the scope of this tutorial,
such as multicasting, asynchronous I/O, and creating your own
file system implementation.

[« Previous](legacy.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** Legacy File I/O Code
  
**Next page:** Questions and Exercises: Basic I/O




A browser with JavaScript enabled is required for this page to operate properly.