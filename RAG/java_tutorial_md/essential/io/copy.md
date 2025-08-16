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

Copying a File or Directory

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

[« Previous](delete.html) • [Trail](../TOC.html) • [Next »](move.html)

# Copying a File or Directory

You can copy a file or directory by using the
[`copy(Path, Path, CopyOption...)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#copy(java.nio.file.Path, java.nio.file.Path, java.nio.file.CopyOption...)) method. The copy fails if the target file exists, unless the
`REPLACE_EXISTING` option is specified.

Directories can be copied. However, files inside the directory
are not copied, so the new directory is empty even when the original
directory contains files.

When copying a symbolic link, the target of the link is copied.
If you want to copy the link itself, and not the contents of the link,
specify either the `NOFOLLOW_LINKS` or
`REPLACE_EXISTING` option.

This method takes a varargs argument.
The following `StandardCopyOption` and `LinkOption`
enums are supported:

* `REPLACE_EXISTING` – Performs the copy even when
  the target file already exists. If the target is a symbolic link,
  the link itself is copied (and not the target of the link).
  If the target is a non-empty directory, the copy fails with
  the `FileAlreadyExistsException` exception.* `COPY_ATTRIBUTES` – Copies the file attributes
    associated with the file to the target file.
    The exact file attributes supported
    are file system and platform dependent,
    but `last-modified-time` is
    supported across platforms and is copied to the target file.* `NOFOLLOW_LINKS` – Indicates that symbolic
      links should not be followed. If the file to be copied is a
      symbolic link, the link is copied (and not the target of the link).

If you are not familiar with `enums`, see
[Enum Types](../../java/javaOO/enum.html).

The following shows how to use the `copy` method:

```

import static java.nio.file.StandardCopyOption.*;
...
Files.copy(source, target, REPLACE_EXISTING);

```

In addition to file copy, the `Files` class
also defines methods that may be used to copy between a file and
a stream. The
[`copy(InputStream, Path, CopyOptions...)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#copy(java.io.InputStream, java.nio.file.Path, java.nio.file.CopyOption...)) method may be used to copy all bytes from an input stream to a file. The
[`copy(Path, OutputStream)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#copy(java.nio.file.Path, java.io.OutputStream)) method may be used to copy all bytes from a file to an output stream.

The
[`Copy`](examples/Copy.java) example uses the `copy` and
`Files.walkFileTree` methods to support a recursive copy.
See
[Walking the File Tree](walk.html) for more information.

[« Previous](delete.html)
•
[Trail](../TOC.html)
•
[Next »](move.html)

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

**Previous page:** Deleting a File or Directory
  
**Next page:** Moving a File or Directory




A browser with JavaScript enabled is required for this page to operate properly.