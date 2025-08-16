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

Finding Files

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

[« Previous](walk.html) • [Trail](../TOC.html) • [Next »](notification.html)

# Finding Files

If you have ever used a shell script, you have most likely used
pattern matching to locate files. In fact, you have probably
used it extensively. If you haven't used it, pattern matching uses
special characters to create a pattern and then file names can
be compared against that pattern.
For example, in most shell scripts,
the asterisk, `*`, matches any number of
characters. For example, the following command
lists all the files in the current directory that end in
`.html`:

```

% ls *.html

```

The `java.nio.file` package provides programmatic support
for this useful feature. Each file system implementation provides a
[`PathMatcher`](http://download.java.net/jdk7/docs/api/java/nio/file/PathMatcher.html). You can retrieve a file system's `PathMatcher` by using the
[`getPathMatcher(String)`](http://download.java.net/jdk7/docs/api/java/nio/file/FileSystem.html#getPathMatcher(java.lang.String)) method in the `FileSystem` class.
The following code snippet fetches the path matcher for the default file system:

```

String pattern = ...;
PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:" + pattern);

```

The string argument passed to `getPathMatcher` specifies
the syntax flavor and the pattern to be matched. This example
specifies *glob* syntax. If you are unfamiliar with glob syntax, see
[What Is a Glob?](fileOps.html#glob).

Glob syntax is easy to use and flexible but, if you prefer,
you can also use regular expressions, or *regex*, syntax.
For further information about regex, see the
[Regular Expressions](../regex/index.html) lesson.
Some file system implementations might support other syntaxes.

If you want to use some other form of string-based pattern matching,
you can create your own `PathMatcher` class.
The examples in this page use glob syntax.

Once you have created your `PathMatcher` instance, you are
ready to match files against it. The `PathMatcher` interface
has a single method,
[`matches`](http://download.java.net/jdk7/docs/api/java/nio/file/PathMatcher.html#matches(java.nio.file.Path)), that takes a `Path` argument and returns a
boolean: It either matches the pattern, or it does not.
The following code snippet
looks for files that end in `.java` or `.class`
and prints those files to standard output:

```

PathMatcher matcher = FileSystems.getDefault().getPathMatcher("glob:*.{java,class}");

Path filename = ...;
if (matcher.matches(filename)) {
    System.out.println(filename);
}

```

## Recursive Pattern Matching

Searching for files that match a particular pattern goes hand-in-hand with
walking a file tree. How many times do you know a file is *somewhere*
on the file system, but where? Or perhaps you need to find
all files in a file tree that have a particular file extension.

The
[`Find`](examples/Find.java) example does precisely that. `Find` is similar to the UNIX
`find` utility, but has pared down functionally.
You can extend this example to include other functionality.
For example, the `find` utility supports the `-prune` flag
to exclude an entire subtree from the search. You could implement that
functionality by returning `SKIP_SUBTREE` in the
`preVisitDirectory` method.
To implement the `-L` option, which follows symbolic links,
you could use the four-argument `walkFileTree` method and
pass in the `FOLLOW_LINKS` enum (but make sure that
you test for circular links in the `visitFile` method).

To run the Find application, use the following format:

```

% java Find <path> -name "<glob_pattern>"

```

The pattern is placed inside quotation marks so any wildcards are not
interpreted by the shell. For example:

```

% java Find . -name "*.html"

```

Here is the source code for the `Find` example:

```

/**
 * Sample code that finds files that match the specified glob pattern.
 * For more information on what constitutes a glob pattern, see
 * http://download.oracle.com/javase/tutorial/essential/io/fileOps.html#glob
 *
 * The file or directories that match the pattern are printed to
 * standard out.  The number of matches is also printed.
 *
 * When executing this application, you must put the glob pattern
 * in quotes, so the shell will not expand any wild cards:
 *              java Find . -name "*.java"
 */

import java.io.*;
import java.nio.file.*;
import java.nio.file.attribute.*;
import static java.nio.file.FileVisitResult.*;
import static java.nio.file.FileVisitOption.*;
import java.util.*;


public class Find {

    public static class Finder extends SimpleFileVisitor<Path> {
        private final PathMatcher matcher;
        private int numMatches = 0;

        Finder(String pattern) {
            matcher = FileSystems.getDefault().getPathMatcher("glob:" + pattern);
        }

        //Compares the glob pattern against the file or directory name.
        void find(Path file) {
            Path name = file.getFileName();
            if (name != null && matcher.matches(name)) {
                numMatches++;
                System.out.println(file);
            }
        }

        //Prints the total number of matches to standard out.
        void done() {
            System.out.println("Matched: " + numMatches);
        }

        //Invoke the pattern matching method on each file.
        @Override
        public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) {
            find(file);
            return CONTINUE;
        }

        //Invoke the pattern matching method on each directory.
        @Override
        public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) {
            find(dir);
            return CONTINUE;
        }

        @Override
        public FileVisitResult visitFileFailed(Path file, IOException exc) {
            System.err.println(exc);
            return CONTINUE;
        }
    }

    static void usage() {
        System.err.println("java Find <path> -name \"<glob_pattern>\"");
        System.exit(-1);
    }

    public static void main(String[] args) throws IOException {

        if (args.length < 3 || !args[1].equals("-name"))
            usage();

        Path startingDir = Paths.get(args[0]);
        String pattern = args[2];

        Finder finder = new Finder(pattern);
        Files.walkFileTree(startingDir, finder);
        finder.done();
    }
}

```

Recursively walking a file tree is covered in
[Walking the File Tree](walk.html).

[« Previous](walk.html)
•
[Trail](../TOC.html)
•
[Next »](notification.html)

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

**Previous page:** Walking the File Tree
  
**Next page:** Watching a Directory for Changes




A browser with JavaScript enabled is required for this page to operate properly.