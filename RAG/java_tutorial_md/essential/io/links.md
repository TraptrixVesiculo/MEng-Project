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

[Random Access Files](rafs.html)

[Creating and Reading Directories](dirs.html)

Links, Symbolic or Otherwise

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

[« Previous](dirs.html) • [Trail](../TOC.html) • [Next »](walk.html)

# Links, Symbolic or Otherwise

As mentioned previously,
the `java.nio.file` package, and the `Path` class in particular,
is "link aware."
Every `Path` method either detects what to do when a symbolic
link is encountered, or it provides an option enabling you to configure the
behavior when a symbolic link is encountered.

The discussion so far has been about
[symbolic or *soft* links](path.html#symlink), but some file systems also support hard links.
*Hard links* are more restrictive than symbolic links, as follows:

* The target of the link must exist.* Hard links are generally not allowed on directories.* Hard links are not allowed to cross partitions or volumes.
      Therefore, they cannot exist across file systems.* A hard link looks, and behaves, like a regular file,
        so they can be hard to find.* A hard link is, for all intents and purposes, the same entity as the original file.
          They have the same file permissions, time stamps, and so on.
          All attributes are identical.

Because of these restrictions, hard links are not used as often as
symbolic links, but the `Path` methods work seamlessly with hard links.

Several methods deal specifically with links
and are covered in the following sections:

* [Creating a Symbolic Link](#symLink)* [Creating a Hard Link](#hardLink)* [Detecting a Symbolic Link](#detect)* [Finding the Target of a Link](#read)

## Creating a Symbolic Link

If your file system supports it, you can create a symbolic
link by using the
[`createSymbolicLink(Path, Path, FileAttribute<?>)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#createSymbolicLink(java.nio.file.Path, java.nio.file.Path, java.nio.file.attribute.FileAttribute...)) method. The second `Path` argument represents the target file
or directory and might or might not exist.
The following code snippet creates a symbolic link with default permissions:

```

Path newLink = ...;
Path target = ...;
try {
    Files.createSymbolicLink(newLink, target);
} catch (IOException x) {
    System.err.println(x);
} catch (UnsupportedOperationException x) {
    //Some file systems do not support symbolic links.
    System.err.println(x);
}

```

The `FileAttributes` vararg enables you to specify initial
file attributes that are set atomically when the link is created.
However, this argument is intended for future use and is not currently
implemented.

## Creating a Hard Link

You can create a hard (or *regular*) link to an existing file by using the
[`createLink(Path, Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#createLink(java.nio.file.Path, java.nio.file.Path)) method. The second `Path` argument locates the existing file,
and it must exist or a `NoSuchFileException` is thrown.
The following code snippet shows how to create a link:

```

Path newLink = ...;
Path existingFile = ...;
try {
    Files.createLink(newLink, existingFile);
} catch (IOException x) {
    System.err.println(x);
} catch (UnsupportedOperationException x) {
    //Some file systems do not support adding an existing file to a directory.
    System.err.println(x);
}

```

## Detecting a Symbolic Link

To determine whether a `Path` instance is a symbolic link,
you can use the
[`isSymbolicLink(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#isSymbolicLink(java.nio.file.Path)) method.
The following code snippet shows how:

```

Path file = ...;
boolean isSymbolicLink = Files.isSymbolicLink(file);

```

For more information, see
[Managing Metadata](fileAttr.html).

## Finding the Target of a Link

You can obtain the target of a symbolic link by using the
[`readSymbolicLink(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#readSymbolicLink(java.nio.file.Path)) method, as follows:

```

Path link = ...;
try {
    System.out.format("Target of link '%s' is '%s'%n", link, Files.readSymbolicLink(link));
} catch (IOException x) {
    System.err.println(x);
}

```

If the `Path` is not a symbolic link, this method throws a
`NotLinkException`.

[« Previous](dirs.html)
•
[Trail](../TOC.html)
•
[Next »](walk.html)

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

**Previous page:** Creating and Reading Directories
  
**Next page:** Walking the File Tree




A browser with JavaScript enabled is required for this page to operate properly.