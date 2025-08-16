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

File Operations

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

[« Previous](pathOps.html) • [Trail](../TOC.html) • [Next »](check.html)

# File Operations

The
[`Files`](http://download.java.net/jdk7/docs/api/java/nio/file/Files.html) class is the other primary entrypoint of the `java.nio.file`
package. This class offers a rich set of static methods
for reading, writing, and manipulating files and directories.
The `Files` methods work on instances of
`Path` objects.
Before proceeding to the remaining sections,
you should familiarize yourself with the following common concepts:

* [Releasing System Resources](#resources)* [Catching Exceptions](#exception)* [Varargs](#varargs)* [Atomic Operations](#atomic)* [Method Chaining](#chaining)* [What *Is* a Glob?](#glob)* [Link Awareness](#linkaware)

## Releasing System Resources

Many of the resources that are used in this API, such as streams or channels,
implement or extend the
[`java.io.Closeable`](http://download.oracle.com/javase/7/docs/api/java/io/Closeable.html) interface. A requirement of a `Closeable` resource is that the
`close` method must be invoked to release the resource
when no longer required. Neglecting to close a resource can have a
negative implication on an application's performance.
The `try-`with-resources statement, described in the
next section, handles this step for you.

## Catching Exceptions

With file I/O, unexpected conditions are a fact of life:
a file exists (or doesn't exist) when expected, the program doesn't
have access to the file system, the default file system implementation
does not support a particular function, and so on.
Numerous errors can be encountered.

All methods that access the file system can throw an `IOException`.
It is best practice to catch these exceptions by
embedding these methods into a `try-`with-resources statement,
introduced in the Java SE 7 release.
The `try-`with-resources statement has the advantage that
the compiler automatically generates the code to close the resource(s)
when no longer required.
The following code shows how this might look:

```

Charset charset = Charset.forName("US-ASCII");
String s = ...;
try (BufferedWriter writer = Files.newBufferedWriter(file, charset)) {
    writer.write(s, 0, s.length());
} catch (IOException x) {
    System.err.format("IOException: %s%n", x);
}

```

For more information, see
[The try-with-resources Statement](../../essential/exceptions/tryResourceClose.html).

Alternatively, you can embed the file I/O methods in a `try` block
and then catch any exceptions in a `catch` block.
If your code has opened any streams or channels, you should
close them in a `finally` block.
The previous example would look something like the following using
the try-catch-finally approach:

```

Charset charset = Charset.forName("US-ASCII");
String s = ...;
BufferedWriter writer = null;
try {
    writer = Files.newBufferedWriter(file, charset);
    writer.write(s, 0, s.length());
} catch (IOException x) {
    System.err.format("IOException: %s%n", x);
} finally {
    if (writer != null) writer.close();
}

```

For more information, see
[Catching and Handling Exceptions](../../essential/exceptions/handling.html).

In addition to `IOException`,
many specific exceptions extend
[`FileSystemException`](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystemException.html). This class has some useful methods that return the file involved
[(`getFile`)](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystemException.html#getFile()), the detailed message string
[(`getMessage`)](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystemException.html#getMessage()), the reason why the file system operation failed
[(`getReason`)](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystemException.html#getReason()), and the "other" file involved, if any
[(`getOtherFile`)](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystemException.html#getOtherFile()).

The following code snippet shows how the `getFile`
method might be used:

```

try (...) {
    ...    
} catch (NoSuchFileException x) {
    System.err.format("%s does not exist\n", x.getFile());
}

```

For purposes of clarity,
the file I/O examples in this lesson may not show
exception handling, but your code should always include it.

## Varargs

Several `Files` methods accept an arbitrary
number of arguments when flags are specified.
For example, in the following method signature, the ellipses
notation after the `CopyOption` argument
indicates that the method accepts a variable number of arguments,
or *varargs*, as they are typically called:

```

Path Files.move(Path, Path, CopyOption...)

```

When a method accepts a varargs argument, you can
pass it a comma-separated list of values or an
array (`CopyOption[]`) of values.

In the `move` example, the method can be invoked as follows:

```

import static java.nio.file.StandardCopyOption.*;

Path source = ...;
Path target = ...;
Files.move(source, target, REPLACE_EXISTING, ATOMIC_MOVE);

```

For more information about varargs syntax, see
[Arbitrary Number of Arguments](../../java/javaOO/arguments.html#varargs).

## Atomic Operations

Several `Files` methods, such as `move`,
can perform certain operations atomically in some file systems.

An *atomic file operation* is an operation that
cannot be interrupted or "partially" performed. Either the entire
operation is performed or the operation fails.
This is important when you have multiple processes operating
on the same area of the file system, and you need to guarantee that
each process accesses a complete file.

## Method Chaining

Many of the file I/O methods support the concept of *method chaining*.

You first invoke a method that returns an object.
You then immediately invoke a method on *that* object, which
returns yet another object, and so on. Many of the I/O examples
use the following technique:

```

String value = Charset.defaultCharset().decode(buf).toString();
UserPrincipal group = file.getFileSystem().getUserPrincipalLookupService().lookupPrincipalByName("me");

```

This technique produces compact code and enables you to avoid
declaring temporary variables that you don't need.

## What *Is* a Glob?

Two methods in the `Files` class accept a glob
argument, but what is a *glob*?

You can use glob syntax to specify pattern-matching behavior.

A glob pattern is specified as a string and is matched against other
strings, such as directory or file names. Glob syntax follows several
simple rules:

* An asterisk, `*`, matches any number of characters (including none).* Two asterisks, `**`, works like `*` but crosses
    directory boundaries.
    This syntax is generally used for matching complete paths.* A question mark, `?`, matches exactly one character.* Braces specify a collection of subpatterns. For example:
        + `{sun,moon,stars}` matches "sun", "moon", or "stars."+ `{temp*,tmp*}` matches all strings beginning with "temp" or
            "tmp."* Square brackets convey a set of single characters or, when the
          hyphen character (`-`) is used, a range of characters.
          For example:
          + `[aeiou]` matches any lowercase vowel.+ `[0-9]` matches any digit.+ `[A-Z]` matches any uppercase letter.+ `[a-z,A-Z]` matches any uppercase or lowercase letter.Within the square brackets, `*`, `?`, and `\`
          match themselves.* All other characters match themselves.* To match
              `*`, `?`, or the other special characters,
              you can escape them by using the backslash character, `\`.
              For example: `\\` matches a single backslash, and
              `\?` matches the question mark.

Here are some examples of glob syntax:

* `*.html` – Matches all strings that end in *.html** `???` – Matches all strings with exactly three letters
    or digits* `*[0-9]*` – Matches all strings containing a numeric value* `*.{htm,html,pdf}` – Matches any string ending with
        *.htm*, *.html* or *.pdf** `a?*.java` – Matches any string beginning with
          `a`, followed by at least
          one letter or digit, and ending with *.java** `{foo*,*[0-9]*}` – Matches any string beginning with
            *foo* or any string containing a numeric value

---

**Note:** If you are typing the glob pattern at the keyboard and it contains one
of the special characters, you must put the pattern in quotes
(`"*"`), use the backslash (`\*`), or use
whatever escape mechanism is supported at the command line.

---

The glob syntax is powerful and easy to use.
However, if it is not sufficient for your needs,
you can also use a regular expression.
For more information, see the
[Regular Expressions](../../essential/regex/index.html) lesson.

For more information about the glob sytnax, see the API specification for the
[`getPathMatcher`](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystem.html#getPathMatcher(java.lang.String)) method in the `FileSystem` class.

## Link Awareness

The `Files` class is "link aware."
Every `Files` method either detects what to do when
a symbolic link is encountered, or it provides an option
enabling you to configure the behavior when a symbolic link
is encountered.

[« Previous](pathOps.html)
•
[Trail](../TOC.html)
•
[Next »](check.html)

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

**Previous page:** Path Operations
  
**Next page:** Checking a File or Directory




A browser with JavaScript enabled is required for this page to operate properly.