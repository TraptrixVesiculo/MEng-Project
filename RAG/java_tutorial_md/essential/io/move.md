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

Moving a File or Directory

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

[« Previous](copy.html) • [Trail](../TOC.html) • [Next »](fileAttr.html)

# Moving a File or Directory

You can move a file or directory by using the
[`move(Path, Path, CopyOption...)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#move(java.nio.file.Path, java.nio.file.Path, java.nio.file.CopyOption...)) method.
The move fails if the target file exists,
unless the `REPLACE_EXISTING` option is specified.

Empty directories can be moved. If the directory is not empty,
the move is allowed when the directory can be
moved without moving the contents of that directory.
On UNIX systems,
moving a directory within the same partition generally consists
of renaming the directory. In that situation, this method works
even when the directory contains files.

This method takes a varargs argument –
the following `StandardCopyOption` enums are supported:

* `REPLACE_EXISTING` – Performs the move even
  when the target file already exists. If the target is a symbolic
  link, the symbolic link is replaced but what it points to is not affected.* `ATOMIC_MOVE` – Performs the move as an atomic
    file operation. If the file system does not support an atomic move,
    an exception is thrown. With an `ATOMIC_MOVE` you can move a file
    into a directory and be guaranteed that any process watching the directory
    accesses a complete file.

The following shows how to use the `move` method:

```

import static java.nio.file.StandardCopyOption.*;
...
Files.move(source, target, REPLACE_EXISTING);

```

Though you can implement the `move` method on a single
directory as shown,
the method is most often used with the file tree recursion mechanism.
For more information, see
[Walking the File Tree](walk.html).

[« Previous](copy.html)
•
[Trail](../TOC.html)
•
[Next »](fileAttr.html)

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

**Previous page:** Copying a File or Directory
  
**Next page:** Managing Metadata (File and File Store Attributes)




A browser with JavaScript enabled is required for this page to operate properly.