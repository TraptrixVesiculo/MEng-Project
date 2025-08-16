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

The Path Class

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

[« Previous](path.html) • [Trail](../TOC.html) • [Next »](pathOps.html)

# The Path Class

The
[`Path`](http://download.java.net/jdk7/docs/api/java/nio/file/Path.html) class, introduced in the Java SE 7 release, is one of the primary
entrypoints of the
the
[`java.nio.file`](http://download.java.net/jdk7/docs/api/java/nio/file/package-summary.html) package.
If your application uses file I/O, you will want
to learn about the powerful features of this class.

---

**Version Note:** If you have pre-JDK7 code that uses `java.io.File`, you can still
take advantage of the `Path` class functionality by using the
[`File.toPath`](http://download.java.net/jdk7/docs/api/java/io/File.html#toPath()) method. See
[Legacy File I/O Code](legacy.html) for more information.

---

As its name implies, the `Path`
class is a programmatic representation of a path
in the file system. A `Path` object
contains the file name and directory list used to
construct the path, and is used to examine, locate,
and manipulate files.

A `Path` instance reflects the underlying platform.
In the Solaris OS, a `Path` uses the Solaris syntax
(`/home/joe/foo`) and
in Microsoft Windows, a `Path` uses the Windows syntax
(`C:\home\joe\foo`).
A `Path` is not system independent. You cannot compare
a `Path` from a Solaris file system and expect it to
match a `Path` from a Windows file system, even if the
directory structure is identical and both instances locate the same
relative file.

The file or directory corresponding to the `Path` might not exist.
You can create a `Path` instance and manipulate it
in various ways: you can append to it, extract pieces of it,
compare it to another path. At the appropriate time,
you can use the methods in the
[`Files`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html) class to check the existence of the file corresponding to the
`Path`, create the file, open it, delete it,
change its permissions, and so on.

The next page examines the `Path` class in detail.

[« Previous](path.html)
•
[Trail](../TOC.html)
•
[Next »](pathOps.html)

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

**Previous page:** What Is a Path? (And Other File System Facts)
  
**Next page:** Path Operations




A browser with JavaScript enabled is required for this page to operate properly.