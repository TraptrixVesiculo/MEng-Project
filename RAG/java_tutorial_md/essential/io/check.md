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

Checking a File or Directory

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

[« Previous](fileOps.html) • [Trail](../TOC.html) • [Next »](delete.html)

# Checking a File or Directory

You have a `Path` instance representing a file or directory,
but does that file exist on the file system?
Is it readable? Writable? Executable?

## Verifying the Existence of a File or Directory

The methods in the `Path` class are syntactic,
meaning that they operate on the `Path` instance.
But eventually you must access the file system to
verify that a particular `Path`
exists, or does not exist. You can do so with the
[`exists(Path, LinkOption...)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#exists(java.nio.file.Path, java.nio.file.LinkOption...)) and the
[`notExists(Path, LinkOption...)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#notExists(java.nio.file.Path, java.nio.file.LinkOption...)) methods. Note that `!Files.exists(path)` is not
equivalent to `Files.notExists(path)`.
When you are testing a file's existence, three results are possible:

* The file is verified to exist.* The file is verified to not exist.* The file's status is unknown. This result can occur when
      the program does not have access to the file.

If both `exists` and `notExists` return
`false`, the existence of the file cannot be verified.

## Checking File Accessibility

To verify that the program can access a file as needed, you can use the
[`isReadable(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#isReadable(java.nio.file.Path)),
[`isWritable(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#isWritable(java.nio.file.Path)), and
[`isExecutable(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#isExecutable(java.nio.file.Path)) methods.

The following code snippet verifies that a particular file exists
and that the program has the ability to execute the file.

```

Path file = ...;
boolean isRegularExecutableFile = Files.isRegularFile(file) &
                                  Files.isReadable(file) &
                                  Files.isExecutable(file);

```

---

**Note:** Once any of these methods completes, there is no guarantee that the file
can be accessed. A common security flaw in many applications is to perform a check and
then access the file. For more information, use your favorite search engine to look
up `TOCTTOU` (pronounced *TOCK-too*).

---

## Checking Whether Two Paths Locate the Same File

When you have a file system that uses symbolic links, it is possible to have
two different paths that locate the same file.
The
[`isSameFile(Path, Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#isSameFile(java.nio.file.Path, java.nio.file.Path)) method compares two paths to determine if they locate the same file on
the file system. For example:

```

Path p1 = ...;
Path p2 = ...;

if (Files.isSameFile(p1, p2)) {
    //Logic when the paths locate the same file
}

```

[« Previous](fileOps.html)
•
[Trail](../TOC.html)
•
[Next »](delete.html)

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

**Previous page:** File Operations
  
**Next page:** Deleting a File or Directory




A browser with JavaScript enabled is required for this page to operate properly.