[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Basic I/O
  
**Section:** I/O Streams
  
**Subsection:** Scanning and Formatting

[Basic I/O](index.html)

[I/O Streams](streams.html)

[Byte Streams](bytestreams.html)

[Character Streams](charstreams.html)

[Buffered Streams](buffers.html)

[Scanning and Formatting](scanfor.html)

Scanning

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

[« Previous](scanfor.html) • [Trail](../TOC.html) • [Next »](formatting.html)

# Scanning

Objects of type
[`Scanner`](http://download.oracle.com/javase/7/docs/api/java/util/Scanner.html)
are useful for breaking down formatted input into tokens and
translating individual tokens according to their data type.

## Breaking Input into Tokens

By default, a scanner uses white space to separate tokens.
(White space characters include blanks, tabs, and line terminators. For
the full list, refer to the documentation for
[`Character.isWhitespace`](http://download.oracle.com/javase/7/docs/api/java/lang/Character.html#isWhitespace(char)).)
To see how scanning works, let's look at
[`ScanXan`](examples/ScanXan.java),
a program that reads the individual words in `xanadu.txt`
and prints them out, one per line.

```


import java.io.*;
import java.util.Scanner;

public class ScanXan {
    public static void main(String[] args) throws IOException {
        Scanner s = null;
        try {
            s = new Scanner(new BufferedReader(new FileReader("xanadu.txt")));

            while (s.hasNext()) {
                System.out.println(s.next());
            }
        } finally {
            if (s != null) {
                s.close();
            }
        }
    }
}

```

Notice that `ScanXan` invokes `Scanner`'s
`close` method when it is done with the scanner object.
Even though a scanner is not a stream, you need to close it to
indicate that you're done with its underlying stream.

The output of `ScanXan` looks like this:

```

In
Xanadu
did
Kubla
Khan
A
stately
pleasure-dome
...

```

To use a different token separator, invoke
`useDelimiter()`, specifying a regular expression.
For example, suppose you wanted the token separator to be a comma,
optionally followed by white space. You would invoke,

```

s.useDelimiter(",\\s*");

```

## Translating Individual Tokens

The `ScanXan` example treats all input tokens as
simple `String` values. `Scanner` also supports
tokens for all of the Java language's primitive types (except for
`char`), as well as `BigInteger` and
`BigDecimal`. Also, numeric values can use thousands
separators. Thus, in a `US` locale, `Scanner`
correctly reads the string "32,767" as representing an integer value.

We have to mention the locale, because thousands separators and
decimal symbols are locale specific. So, the following example would
not work correctly in all locales if we didn't specify that the
scanner should use the `US` locale. That's not something
you usually have to worry about, because your input data usually comes
from sources that use the same locale as you do. But this example is
part of the Java Tutorial and gets distributed all over the world.

The
[`ScanSum`](examples/ScanSum.java)
example reads a list of `double` values and adds them up.
Here's the source:

```


import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class ScanSum {
    public static void main(String[] args) throws IOException {
        Scanner s = null;
        double sum = 0;
        try {
            s = new Scanner(
                    new BufferedReader(new FileReader("usnumbers.txt")));
            s.useLocale(Locale.US);


            while (s.hasNext()) {
                if (s.hasNextDouble()) {
                        sum += s.nextDouble();
                    } else {
                        s.next();
                    }   
            }
        } finally {
            s.close();
        }

        System.out.println(sum);
    }
}



```

And here's the sample input file,
[`usnumbers.txt`](examples/usnumbers.txt)

```

8.5
32,767
3.14159
1,000,000.1

```

The output string is "1032778.74159". The period will be a different
character in some locales, because `System.out` is a
`PrintStream` object, and that class doesn't provide a way
to override the default locale. We could override the locale for the
whole program — or we could just use formatting, as described in
the next topic,
[Formatting](formatting.html).

[« Previous](scanfor.html)
•
[Trail](../TOC.html)
•
[Next »](formatting.html)

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

**Previous page:** Scanning and Formatting
  
**Next page:** Formatting




A browser with JavaScript enabled is required for this page to operate properly.