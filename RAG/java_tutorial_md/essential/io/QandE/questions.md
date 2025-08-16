[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O

[Basic I/O](../index.html)

[I/O Streams](../streams.html)

[Byte Streams](../bytestreams.html)

[Character Streams](../charstreams.html)

[Buffered Streams](../buffers.html)

[Scanning and Formatting](../scanfor.html)

[Scanning](../scanning.html)

[Formatting](../formatting.html)

[I/O from the Command Line](../cl.html)

[Data Streams](../datastreams.html)

[Object Streams](../objectstreams.html)

[File I/O (Featuring NIO.2)](../fileio.html)

[What Is a Path? (And Other File System Facts)](../path.html)

[The Path Class](../pathClass.html)

[Path Operations](../pathOps.html)

[File Operations](../fileOps.html)

[Checking a File or Directory](../check.html)

[Deleting a File or Directory](../delete.html)

[Copying a File or Directory](../copy.html)

[Moving a File or Directory](../move.html)

[Managing Metadata (File and File Store Attributes)](../fileAttr.html)

[Reading, Writing, and Creating Files](../file.html)

[Random Access Files](../rafs.html)

[Creating and Reading Directories](../dirs.html)

[Links, Symbolic or Otherwise](../links.html)

[Walking the File Tree](../walk.html)

[Finding Files](../find.html)

[Watching a Directory for Changes](../notification.html)

[Other Useful Methods](../misc.html)

[Legacy File I/O Code](../legacy.html)

[Summary](../summary.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[Basic I/O](../index.html)

[« Previous](../summary.html) • [Trail](../../TOC.html) • [Next »](../../concurrency/index.html)

# Questions and Exercises: Basic I/O

## Questions

1. What class and method would you use to read a few pieces of data that
are at known positions near the end of a large file?

2. When invoking `format`, what is the best way to indicate
a new line?

3. How would you determine the MIME type of a file?

4. What method(s) would you use to determine whether a file is a symbolic link?

## Exercises

1. Write an example that counts the number of times a particular
character, such as `e`, appears in a file.
The character can be specified at the command line. You can use
[`xanadu.txt`](../examples/xanadu.txt) as the input file.

2. The file
[`datafile`](datafile) begins with a single `long` that tells you the offset
of a single `int` piece of data within the same file.
Write a program that gets the `int` piece of data.
What is the `int` data?

[Check your answers.](answers.html)

[« Previous](../summary.html)
•
[Trail](../../TOC.html)
•
[Next »](../../concurrency/index.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Summary
  
**Next page:** Concurrency




A browser with JavaScript enabled is required for this page to operate properly.