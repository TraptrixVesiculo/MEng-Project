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

File I/O (Featuring NIO.2)

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

[« Previous](objectstreams.html) • [Trail](../TOC.html) • [Next »](path.html)

# File I/O (Featuring NIO.2)

---

 **This section was updated to reflect features and
conventions of the upcoming Java SE 7 release.
You can download the current
[JDK7 snapshot](http://download.java.net/jdk7/binaries/)
from `java.net`.

The Java SE 6 version of the File I/O tutorial was brief,
but you can download the
[Java SE Tutorial 2008-03-14](https://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_Developer-Site/en_US/-/USD/ViewProductDetail-Start?ProductRef=tutorial-2008_03_14-oth-JPR@CDS-CDS_Developer) version of the tutorial which contains the earlier File I/O content.** 

---

The `java.nio.file` package and its related package,
`java.nio.file.attribute`, provide comprehensive support
for file I/O and for accessing the default file system.
Though the API has many classes,
you need to focus on only a few entry points. You will see that
this API is very intuitive and easy to use.

The tutorial starts by asking
[what is a path?](path.html) Then, the
[Path class](pathClass.html), the primary entry point for the package, is introduced.
Methods in the `Path` class relating to
[syntactic operations](pathOps.html) are explained. The tutorial then moves on to the other primary
class in the package, the `Files` class, which contains
methods that deal with file operations. First, some concepts common to many
[file operations](fileOps.html) are introduced. The tutorial then covers methods for
[checking](check.html),
[deleting](delete.html),
[copying](copy.html), and
[moving](move.html) files.

The tutorial shows how
[metadata](fileAttr.html) is managed, before moving on to
[file I/O](file.html) and
[directory I/O](dirs.html).
[Random access files](rafs.html) are explained and issues specific to
[symbolic and hard links](links.html) are examined.

Next, some of the very powerful, but more advanced, topics are covered.
First, the capability to
[recursively walk the file tree](walk.html) is demonstrated, followed by information about how to
[search for files using wild cards](find.html). Next, how to
[watch a directory for changes](notification.html) is explained and demonstrated. Then,
[methods that didn't fit elsewhere](misc.html) are given some attention.

Finally, if you have file I/O code written prior to the Java SE 7 release,
there is a
[map from the old API to the new API](legacy.html#mapping), as well as important information about the `File.toPath`
method for developers who would like to
[leverage the new API without rewriting existing code](legacy.html#interop).

[« Previous](objectstreams.html)
•
[Trail](../TOC.html)
•
[Next »](path.html)

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

**Previous page:** Object Streams
  
**Next page:** What Is a Path? (And Other File System Facts)




A browser with JavaScript enabled is required for this page to operate properly.