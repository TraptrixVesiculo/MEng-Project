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

Deleting a File or Directory

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

[« Previous](check.html) • [Trail](../TOC.html) • [Next »](copy.html)

# Deleting a File or Directory

You can delete files, directories or links.
With symbolic links, the link is deleted and not the
target of the link.
With directories, the directory must be empty, or the deletion fails.

The `Files` class provides two deletion methods.

The
[`delete(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#delete(java.nio.file.Path)) method deletes the file or throws an exception if the deletion fails.
For example, if the file does not exist a
`NoSuchFileException` is thrown.
You can catch the exception to determine why the delete failed
as follows:

```

try {
    Files.delete(path);
} catch (NoSuchFileException x) {
    System.err.format("%s: no such file or directory%n", path);
} catch (DirectoryNotEmptyException x) {
    System.err.format("%s not empty%n", path);
} catch (IOException x) {
    //File permission problems are caught here.
    System.err.println(x);
}

```

The
[`deleteIfExists(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#deleteIfExists(java.nio.file.Path)) method also deletes the file, but if the file does not exist,
no exception is thrown.
Failing silently is useful when
you have multiple threads deleting files and you don't want to throw
an exception just because one thread did so first.

[« Previous](check.html)
•
[Trail](../TOC.html)
•
[Next »](copy.html)

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

**Previous page:** Checking a File or Directory
  
**Next page:** Copying a File or Directory




A browser with JavaScript enabled is required for this page to operate properly.