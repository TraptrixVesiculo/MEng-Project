[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

Basic I/O

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

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

**Trail:** Essential Classes

[Home Page](../../index.html)
>
[Essential Classes](../index.html)

[« Previous](../exceptions/index.html) • [Trail](../TOC.html) • [Next »](streams.html)

# Lesson: Basic I/O

This lesson covers the Java platform classes used for basic I/O.
It first focuses on *I/O Streams*, a powerful concept that
greatly simplifies I/O operations. The lesson also looks at
serialization, which lets a program write whole objects out to streams
and read them back again. Then the lesson looks at file I/O and file system
operations, including random access files.

Most of the classes covered in the `I/O Streams`
section are in the `java.io` package.
Most of the classes covered in the `File I/O` section
are in the `java.nio.file` package.

## [I/O Streams](streams.html) * [Byte Streams](bytestreams.html) handle I/O of raw binary data.* [Character Streams](charstreams.html) handle I/O of character data, automatically handling translation to and from the local character set.* [Buffered Streams](buffers.html) optimize input and output by reducing the number of calls to the native API.* [Scanning and Formatting](scanfor.html) allows a program to read and write formatted text.* [I/O from the Command Line](cl.html) describes the Standard Streams and the Console object.* [Data Streams](datastreams.html) handle binary I/O of primitive data type and `String` values.* [Object Streams](objectstreams.html) handle binary I/O of objects.[File I/O (Featuring NIO.2)](fileio.html) + [What is a Path?](path.html) examines the concept of a path on a file system.+ [The Path Class](pathClass.html) introduces the cornerstone class of the `java.nio.file` package.+ [Path Operations](pathOps.html) looks at methods in the `Path` class that deal with syntactic operations.+ [File Operations](fileOps.html) introduces concepts common to many of the file I/O methods.+ [Checking a File or Directory](check.html) shows how to check a file's existence and its level of accessibility.+ [Deleting a File or Directory](delete.html).+ [Copying a File or Directory](copy.html).+ [Moving a File or Directory](move.html).+ [Managing Metadata](fileAttr.html) explains how to read and set file attributes.+ [Reading, Writing and Creating Files](file.html) shows the stream and channel methods for reading and writing files.+ [Random Access Files](rafs.html) shows how to read or write files in a non-sequentially manner.+ [Creating and Reading Directories](dirs.html) covers API specific to directories, such as how to list a directory's contents.+ [Links, Symbolic or Otherwise](links.html) covers issues specific to symbolic and hard links.+ [Walking the File Tree](walk.html) demonstrates how to recursively visit each file and directory in a file tree.+ [Finding Files](find.html) shows how to search for files using pattern matching.+ [Watching a Directory for Changes](notification.html) shows how to use the watch service to detect files that are added, removed or updated in one or more directories.+ [Other Useful Methods](misc.html) covers important API that didn't fit elsewhere in the lesson.+ [Legacy File I/O Code](legacy.html) shows how to leverage `Path` functionality if you have older code using the `java.io.File` class. A table mapping `java.io.File` API to `java.nio.file` API is provided.[Summary](summary.html)A summary of the key points covered in this trail.[Questions and Exercises](QandE/questions.html)Test what you've learned in this trail by trying these questions and exercises.The I/O Classes in ActionMany of the examples in the next trail, [Custom Networking](../../networking/index.html) use the I/O streams described in this lesson to read from and write to network connections. --- **Security consideration:**  Some I/O operations are subject to approval by the current security manager. The example programs contained in these lessons are standalone applications, which by default have no security manager. To work in an applet, most of these examples would have to be modified. See [What Applets Can and Cannot Do](../../deployment/applet/security.html) for information about the security restrictions placed on applets. ---

[« Previous](../exceptions/index.html)
•
[Trail](../TOC.html)
•
[Next »](streams.html)

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
  
**Next page:** I/O Streams




A browser with JavaScript enabled is required for this page to operate properly.