[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O
  
**Section:** I/O Streams

[Basic I/O](index.html)

[I/O Streams](streams.html)

[Byte Streams](bytestreams.html)

Character Streams

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

[Legacy File I/O Code](legacy.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Basic I/O](index.html)

[« Previous](bytestreams.html) • [Trail](../TOC.html) • [Next »](buffers.html)

# Character Streams

The Java platform stores character values using Unicode conventions.
Character stream I/O automatically translates this internal
format to and from the local character set. In Western locales,
the local character set is usually an 8-bit superset of ASCII.

For most applications, I/O with character streams is no more
complicated than I/O with byte streams. Input and output done with
stream classes automatically translates to and from the local
character set. A program that uses character streams in place of byte
streams automatically adapts to the local character set and is ready
for internationalization — all without extra effort by the
programmer.

If internationalization isn't a priority, you can simply use the
character stream classes without paying much attention to character
set issues. Later, if internationalization becomes a priority, your
program can be adapted without extensive recoding. See the
[Internationalization](../../i18n/index.html)
trail for more information.

## Using Character Streams

All character stream classes are descended from
[`Reader`](http://download.oracle.com/javase/7/docs/api/java/io/Reader.html)
and
[`Writer`](http://download.oracle.com/javase/7/docs/api/java/io/Writer.html). As with byte streams, there are character stream classes that
specialize in file I/O:
[`FileReader`](http://download.oracle.com/javase/7/docs/api/java/io/FileReader.html) and
[`FileWriter`](http://download.oracle.com/javase/7/docs/api/java/io/FileWriter.html).
The
[`CopyCharacters`](examples/CopyCharacters.java)
example illustrates these classes.

```


import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class CopyCharacters {
    public static void main(String[] args) throws IOException {
        FileReader inputStream = null;
        FileWriter outputStream = null;

        try {
            inputStream = new FileReader("xanadu.txt");
            outputStream = new FileWriter("characteroutput.txt");

            int c;
            while ((c = inputStream.read()) != -1) {
                outputStream.write(c);
            }
        } finally {
            if (inputStream != null) {
                inputStream.close();
            }
            if (outputStream != null) {
                outputStream.close();
            }
        }
    }
}

```

`CopyCharacters` is very similar to
`CopyBytes`. The most important difference is that
`CopyCharacters` uses `FileReader` and
`FileWriter` for input and output in place of
`FileInputStream` and `FileOutputStream`.
Notice that both `CopyBytes` and `CopyCharacters`
use an `int` variable to read to and write from. However, in
`CopyCharacters`, the `int` variable holds a
character value in its last 16 bits; in `CopyBytes`, the
`int` variable holds a `byte` value in its last
8 bits.

### Character Streams that Use Byte Streams Character streams are often "wrappers" for byte streams. The character stream uses the byte stream to perform the physical I/O, while the character stream handles translation between characters and bytes. `FileReader`, for example, uses `FileInputStream`, while `FileWriter` uses `FileOutputStream`. There are two general-purpose byte-to-character "bridge" streams: [`InputStreamReader`](http://download.oracle.com/javase/7/docs/api/java/io/InputStreamReader.html) and [`OutputStreamWriter`](http://download.oracle.com/javase/7/docs/api/java/io/OutputStreamWriter.html). Use them to create character streams when there are no prepackaged character stream classes that meet your needs. The [sockets lesson](../../networking/sockets/readingWriting.html) in the [networking trail](../../networking/index.html) shows how to create character streams from the byte streams provided by socket classes.Line-Oriented I/OCharacter I/O usually occurs in bigger units than single characters. One common unit is the line: a string of characters with a line terminator at the end. A line terminator can be a carriage-return/line-feed sequence (`"\r\n"`), a single carriage-return (`"\r"`), or a single line-feed (`"\n"`). Supporting all possible line terminators allows programs to read text files created on any of the widely used operating systems. Let's modify the `CopyCharacters` example to use line-oriented I/O. To do this, we have to use two classes we haven't seen before, [`BufferedReader`](http://download.oracle.com/javase/7/docs/api/java/io/BufferedReader.html) and [`PrintWriter`](http://download.oracle.com/javase/7/docs/api/java/io/PrintWriter.html). We'll explore these classes in greater depth in [Buffered I/O](buffers.html) and [Formatting](formatting.html). Right now, we're just interested in their support for line-oriented I/O. The [`CopyLines`](examples/CopyLines.java) example invokes `BufferedReader.readLine` and `PrintWriter.println` to do input and output one line at a time. ``` import java.io.FileReader; import java.io.FileWriter; import java.io.BufferedReader; import java.io.PrintWriter; import java.io.IOException; public class CopyLines { public static void main(String[] args) throws IOException { BufferedReader inputStream = null; PrintWriter outputStream = null; try { inputStream = new BufferedReader(new FileReader("xanadu.txt")); outputStream = new PrintWriter(new FileWriter("characteroutput.txt")); String l; while ((l = inputStream.readLine()) != null) { outputStream.println(l); } } finally { if (inputStream != null) { inputStream.close(); } if (outputStream != null) { outputStream.close(); } } } } ``` Invoking `readLine` returns a line of text with the line. `CopyLines` outputs each line using `println`, which appends the line terminator for the current operating system. This might not be the same line terminator that was used in the input file. There are many ways to structure text input and output beyond characters and lines. For more information, see [Scanning and Formatting](scanfor.html).

[« Previous](bytestreams.html)
•
[Trail](../TOC.html)
•
[Next »](buffers.html)

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

**Previous page:** Byte Streams
  
**Next page:** Buffered Streams




A browser with JavaScript enabled is required for this page to operate properly.