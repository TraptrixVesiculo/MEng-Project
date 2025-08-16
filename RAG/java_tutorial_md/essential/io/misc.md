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

[Links, Symbolic or Otherwise](links.html)

[Walking the File Tree](walk.html)

[Finding Files](find.html)

[Watching a Directory for Changes](notification.html)

Other Useful Methods

[Legacy File I/O Code](legacy.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Basic I/O](index.html)

[« Previous](notification.html) • [Trail](../TOC.html) • [Next »](legacy.html)

# Other Useful Methods

A few useful methods did not fit elsewhere in this lesson and
are covered here.
This section covers the following:

* [Determining MIME Type](#mime)* [Default File System](#default)* [Path String Separator](#separator)* [File System's File Stores](#stores)

## Determining MIME Type

To determine the MIME type of a file, you might find the
[`probeContentType(Path)`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#probeContentType(java.nio.file.Path)) method useful. For example:

```

try {
    String type = Files.probeContentType(filename);
    if (type == null) {
        System.err.format("'%s' has an unknown filetype.%n", filename);
    } else if (!type.equals("text/plain") {
        System.err.format("'%s' is not a plain text file.%n", filename);
        continue;
    }
} catch (IOException x) {
    System.err.println(x);
}

```

Note that `probeContentType` returns null if the content
type cannot be determined.

The implementation of this method is highly platform specific and is not infallible.
The content type is determind by the platform's default file type detector.
For example, if the detector determines a file's content type to be
`application/x-java` based on the
`.class` extension, it might be fooled.

You can provide a custom
[`FileTypeDetector`](http://download.java.net/jdk7/docs/api/java/nio/file/spi/FileTypeDetector.html) if the default is not sufficient for your needs.

The
[`Email`](examples/Email.java) example uses the `probeContentType` method.

## Default File System

To retrieve the default file system, use the
[`getDefault`](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystems.html#getDefault()) method. Typically, this `FileSystems` method (note the plural)
is chained to one of the `FileSystem` methods (note the singular),
as follows:

```

PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:*.*");

```

## Path String Separator

The path separator for POSIX file systems is the forward slash, `/`,
and for Microsoft Windows is the backslash, `\`.
Other file systems might use other
delimiters. To retrieve the `Path` separator for the
default file system, you can use one of the following approaches:

```

String separator = File.separator;
String separator = FileSystems.getDefault().getSeparator();

```

The
[`getSeparator`](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystem.html#getSeparator()) method is also used to retrieve the path separator for any available
file system.

## File System's File Stores

A file system has one or more file stores to hold its files and
directories. The *file store* represents the underlying storage
device.
In UNIX operating systems,
each mounted file system is represented by a file store.
In Microsoft Windows, each volume is represented by a file store:
`C:`, `D:`, and so on.

To retrieve a list of all the file stores for the file system, you can
use the
[`getFileStores`](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystem.html#getFileStores()) method. This method returns an `Iterable`, which allows you to
use the
[enhanced for](../../java/nutsandbolts/for.html) statement to iterate over all the root directories.

```

for (FileStore store: FileSystems.getDefault().getFileStores()) {
   ...
}

```

If you want to retrive the file store where a particular file is located,
use the
[`getFileStore`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html#getFileStore(java.nio.file.Path)) method in the `Files` class, as follows:

```

Path file = ...;
FileStore store= Files.getFileStore(file);

```

The
[`DiskUsage`](examples/DiskUsage.java) example uses the `getFileStores` method.

[« Previous](notification.html)
•
[Trail](../TOC.html)
•
[Next »](legacy.html)

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

**Previous page:** Watching a Directory for Changes
  
**Next page:** Legacy File I/O Code




A browser with JavaScript enabled is required for this page to operate properly.