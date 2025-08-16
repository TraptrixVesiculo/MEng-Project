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

[Other Useful Methods](misc.html)

Legacy File I/O Code

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Basic I/O](index.html)

[« Previous](misc.html) • [Trail](../TOC.html) • [Next »](summary.html)

# Legacy File I/O Code

## Interoperability With Legacy Code

Prior to the Java SE 7 release,
the `java.io.File` class was the mechanism used for
file I/O, but it had several drawbacks.

* Many methods didn't throw exceptions
  when they failed, so it was impossible to obtain a useful error message.
  For example, if a file deletion failed,
  the program would receive a "delete fail"
  but wouldn't know if it was because the file didn't exist,
  the user didn't have permissions, or there was some other problem.* The `rename` method didn't work consistently across platforms.* There was no real support for symbolic links.* More support for metadata was desired, such as file permissions, file owner,
        and other security attributes.* Accessing file metadata was inefficient.* Many of the `File` methods didn't scale.
            Requesting a large directory listing over a server could result in a hang.
            Large directories could also cause
            memory resource problems, resulting in a denial of service.* It was not possible to write reliable code that could recursively walk a file
              tree and respond appropriately if there were circular symbolic links.

Perhaps you have legacy code that uses `java.io.File`
and would like to take advantage of the
`java.nio.file.Path` functionality
with minimal impact to your code.

The `java.io.File` class provides the
[`toPath`](http://download.java.net/jdk7/docs/api/java/io/File.html#toPath()) method, which converts an old style `File` instance to a
`java.nio.file.Path` instance, as follows:

```

Path input = file.toPath();

```

You can then take advantage of the rich feature set available to the
`Path` class.

For example, assume you had some code that deleted a file:

```

file.delete();

```

You could modify this code to use the `Files.delete` method,
as follows:

```

Path fp = file.toPath();
Files.delete(fp);

```

Conversely, the
[`Path.toFile`](http://download.java.net/jdk7/docs/api/java/nio/file/Path.html#toFile()) method constructs a `java.io.File` object for a
`Path` object.

## Mapping java.io.File Functionality to java.nio.file

Because the Java implementation of file I/O has been completely re-architected
in the Java SE 7 release, you cannot swap one method for another method.
If you want to use the rich functionality offered by the `java.nio.file`
package, your easiest solution is to use the
[`File.toPath`](http://download.java.net/jdk7/docs/api/java/io/File.html#toPath()) method as suggested in the previous section. However,
if you don't want to use that approach or it is not sufficient for your needs,
you must rewrite your file I/O code.

There is no one-to-one correspondence between the two APIs,
but the following table
gives you a general idea of what functionality in the `java.io.File`
API maps to in the `java.nio.file` API and tells you where you can
obtain more information.

| java.io.File Functionality | java.nio.file Functionality | Tutorial Coverage |
| --- | --- | --- |
| `java.io.File` | `java.nio.file.Path` | [The Path Class](pathClass.html) |
| `java.io.RandomAccessFile` | The `SeekableByteChannel` functionality. | [Random Access Files](rafs.html) |
| `File.canRead`, `canWrite`, `canExecute` | `Files.isReadable`, `Files.isWritable`, and `Files.isExecutable`.  On UNIX file systems, the [File Attributes](fileAttr.html) package is used to check the nine file permissions. | [Checking a File or Directory](check.html)  [Managing Metadata](fileAttr.html) |
| `File.isDirectory()`, `File.isFile()`, and `File.length()` | `Files.isDirectory(Path, LinkOption...)`, `Files.isRegularFile(Path, LinkOption...)`, and `Files.size(Path)` | [Managing Metadata](fileAttr.html) |
| `File.lastModified()` and `File.setLastModified(long)` `Files.getLastModifiedTime(Path, LinkOption...)` and `Files.setLastMOdifiedTime(Path, FileTime)` [Managing Metadata](fileAttr.html) | | |
| The `File` methods that set various attributes: `setExecutable`, `setReadable`, `setReadOnly`, `setWritable` | These methods are replaced by the `Files` method `setAttribute(Path, String, Object, LinkOption...)`. | [Managing Metadata](fileAttr.html) || `new File(parent, "newfile")` | `parent.resolve("newfile")` | [Path Operations](pathOps.html) |
| `File.renameTo` | `Files.move` | [Moving a File or Directory](move.html) |
| `File.delete` | `Files.delete` | [Deleting a File or Directory](delete.html) |
| `File.createNewFile` | `Files.createFile` | [Creating Files](file.html#createFile) |
| `File.deleteOnExit` | Replaced by the `DELETE_ON_CLOSE` option specified in the `createFile` method. | [Creating Files](file.html#createFile) |
| `File.createTempFile` | `Files.createTempFile(Path, String, FileAttributes<?>)`, `Files.createTempFile(Path, String, String, FileAttributes<?>)` [Creating Files](file.html#createFile)  [Creating and Writing a File by Using Stream I/O](file.html#createStream)  [Reading and Writing Files by Using Channel I/O](file.html#channelio) | |
| `File.exists` | `Files.exists` and `Files.notExists` | [Verifying the Existence of a File or Directory](check.html) |
| `File.compareTo` and `equals` | `Path.compareTo` and `equals` | [Comparing Two Paths](pathOps.html#compare) |
| `File.getAbsolutePath` and `getAbsoluteFile` | `Path.toAbsolutePath` | [Converting a Path](pathOps.html#convert) |
| `File.getCanonicalPath` and `getCanonicalFile` | `Path.toRealPath` or `normalize` | [Converting a Path (`toRealPath`)](pathOps.html#convert)  [Removing Redundancies From a Path (`normalize`)](pathOps.html#normal) |
| `File.toURI` | `Path.toURI` | [Converting a Path](pathOps.html#convert) |
| `File.isHidden` | `Files.isHidden` | [Retrieving Information About the Path](pathOps.html#info) |
| `File.list` and `listFiles` | `Path.newDirectoryStream` | [Listing a Directory's Contents](dirs.html#listdir) |
| `File.mkdir` and `mkdirs` | `Path.createDirectory` | [Creating a Directory](dirs.html#create) |
| `File.listRoots` | `FileSystem.getRootDirectories` | [Listing a File System's Root Directories](dirs.html#listall) |
| `File.getTotalSpace`, `File.getFreeSpace`, `File.getUsableSpace` | `FileStore.getTotalSpace`, `FileStore.getUnallocatedSpace`, `FileStore.getUsableSpace`, `FileStore.getTotalSpace` | [File Store Attributes](fileAttr.html#store) |

[« Previous](misc.html)
•
[Trail](../TOC.html)
•
[Next »](summary.html)

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

**Previous page:** Other Useful Methods
  
**Next page:** Summary




A browser with JavaScript enabled is required for this page to operate properly.