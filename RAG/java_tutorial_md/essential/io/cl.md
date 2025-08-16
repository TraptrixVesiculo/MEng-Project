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

[Character Streams](charstreams.html)

[Buffered Streams](buffers.html)

[Scanning and Formatting](scanfor.html)

[Scanning](scanning.html)

[Formatting](formatting.html)

I/O from the Command Line

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

[« Previous](formatting.html) • [Trail](../TOC.html) • [Next »](datastreams.html)

# I/O from the Command Line

A program is often run from the command line and interacts with the user in
the command line environment. The Java platform supports this kind of
interaction in two ways: through the Standard Streams and through the
Console.

## Standard Streams

Standard Streams are a feature of many operating systems.
By default, they read input from the keyboard and write output to the
display. They also support I/O on files and between programs, but
that feature is controlled by the command line interpreter, not the
program.

The Java platform supports three Standard Streams: *Standard
Input*, accessed through `System.in`; *Standard
Output*, accessed through `System.out`; and
*Standard Error*, accessed through `System.err`.
These objects are defined automatically and do not need to be opened.
Standard Output and Standard Error are both for output; having error
output separately allows the user to divert regular output to a file
and still be able to read error messages. For more information, refer
to the documentation for your command line interpreter.

You might expect the Standard Streams to be character streams,
but, for historical reasons, they are byte streams.
`System.out` and `System.err` are defined as
[`PrintStream`](http://download.oracle.com/javase/7/docs/api/java/io/PrintStream.html)
objects. Although it is technically a byte stream,
`PrintStream` utilizes an internal character stream object
to emulate many of the features of character streams.

By contrast, `System.in` is a byte stream with no character
stream features. To use Standard Input as a character stream, wrap
`System.in` in `InputStreamReader`.

```

InputStreamReader cin = new InputStreamReader(System.in);

```

## The Console

A more advanced alternative to the Standard Streams is the Console.
This is a single, predefined object of type
[`Console`](http://download.oracle.com/javase/7/docs/api/java/io/Console.html)
that has most of the features provided
by the Standard Streams, and others besides. The Console is
particularly useful for secure password entry. The Console object also provides
input and output streams that are true character streams, through its
`reader` and `writer` methods.

Before a program can use the Console, it must attempt to retrieve the Console
object by invoking `System.console()`. If the Console
object is available, this method returns it. If
`System.console` returns `NULL`, then Console
operations are not permitted, either because the OS doesn't support
them or because the program was launched in a noninteractive
environment.

The Console object supports secure password entry through its
`readPassword` method. This method helps secure password
entry in two ways. First, it suppresses echoing, so the password is
not visible on the user's screen. Second, `readPassword`
returns a character array, not a `String`, so the
password can be overwritten, removing it from memory as soon as it is
no longer needed.

The
[`Password`](examples/Password.java)
example is a prototype program for changing a user's password. It
demonstrates several `Console` methods.

```


import java.io.Console;
import java.util.Arrays;
import java.io.IOException;

public class Password {
    
    public static void main (String args[]) throws IOException {

        Console c = System.console();
        if (c == null) {
            System.err.println("No console.");
            System.exit(1);
        }

        String login = c.readLine("Enter your login: ");
        char [] oldPassword = c.readPassword("Enter your old password: ");

        if (verify(login, oldPassword)) {
            boolean noMatch;
            do {
                char [] newPassword1 =
                    c.readPassword("Enter your new password: ");
                char [] newPassword2 =
                    c.readPassword("Enter new password again: ");
                noMatch = ! Arrays.equals(newPassword1, newPassword2);
                if (noMatch) {
                    c.format("Passwords don't match. Try again.%n");
                } else {
                    change(login, newPassword1);
                    c.format("Password for %s changed.%n", login);
                }
                Arrays.fill(newPassword1, ' ');
                Arrays.fill(newPassword2, ' ');
            } while (noMatch);
        }

        Arrays.fill(oldPassword, ' ');

    }

    //Dummy verify method. 
    static boolean verify(String login, char[] password) {
        return true;
    }

    //Dummy change method.
    static void change(String login, char[] password) {}
}
        

```

`Password` follows these steps:

1. Attempt to retrieve the Console object. If the object is not
   available, abort.- Invoke `Console.readLine` to prompt for and read
     the user's login name.- Invoke `Console.readPassword` to prompt for and
       read the user's existing password.- Invoke `verify` to confirm that the user is
         authorized to change the password. (In this example,
         `verify` is a dummy method that always returns
         `true`.)- Repeat the following steps until the user enters the same
           password twice:
           1. Invoke `Console.readPassword` twice to prompt
              for and read a new password.- If the user entered the same password both times, invoke
                `change` to change it. (Again, `change`
                is a dummy method.)- Overwrite both passwords with blanks.- Overwrite the old password with blanks.

[« Previous](formatting.html)
•
[Trail](../TOC.html)
•
[Next »](datastreams.html)

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

**Previous page:** Formatting
  
**Next page:** Data Streams




A browser with JavaScript enabled is required for this page to operate properly.