[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** The Platform Environment
  
**Section:** Configuration Utilities

[The Platform Environment](index.html)

[Configuration Utilities](config.html)

[Properties](properties.html)

Command-Line Arguments

[Environment Variables](env.html)

[Other Configuration Utilities](other.html)

[System Utilities](system.html)

[Command-Line I/O Objects](cl.html)

[System Properties](sysprop.html)

[The Security Manager](security.html)

[Miscellaneous Methods in System](sysmisc.html)

[PATH and CLASSPATH](paths.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[The Platform Environment](index.html)

[« Previous](properties.html) • [Trail](../TOC.html) • [Next »](env.html)

# Command-Line Arguments

A Java application can accept any number of arguments from the command
line. This allows the user to specify configuration information when
the application is launched.

The user enters command-line arguments when invoking the application
and specifies them after the name of the class to be run. For example,
suppose a Java application called `Sort` sorts lines in a
file. To sort the data in a file named `friends.txt`, a
user would enter:

```

java Sort friends.txt

```

When an application is launched, the runtime system passes the
command-line arguments to the application's main method via an array
of `String`s. In the previous example, the command-line
arguments passed to the `Sort` application in an array that
contains a single `String`: `"friends.txt"`.

### Echoing Command-Line Arguments

> The
> [`Echo`](examples/Echo.java)
> example displays each of its command-line arguments on a line by itself:
>
> ```
>
>
> public class Echo {
>     public static void main (String[] args) {
>         for (String s: args) {
>             System.out.println(s);
>         }
>     }
> }
>
>
> ```
>
> The following example shows how a user might run `Echo`.
> User input is in italics.
>
> ```
>
> java Echo Drink Hot Java
> Drink
> Hot
> Java
>
> ```
>
> Note that the application displays each word —
> `Drink`, `Hot`, and `Java` — on
> a line by itself. This is because the space character separates
> command-line arguments. To have `Drink`, `Hot`,
> and `Java` interpreted as a single argument, the user would
> join them by enclosing them within quotation marks.
>
> ```
>
> java Echo "Drink Hot Java"
> Drink Hot Java
>
> ```

### Parsing Numeric Command-Line Arguments

> If an application needs to support a numeric command-line argument, it
> must convert a `String` argument that represents a number,
> such as "34", to a numeric value.
> Here is a code snippet that converts a command-line
> argument to an `int`:
>
> ```
>
> int firstArg;
> if (args.length > 0) {
>     try {
>         firstArg = Integer.parseInt(args[0]);
>     } catch (NumberFormatException e) {
>         System.err.println("Argument must be an integer");
>         System.exit(1);
>     }
> }
>
> ```
>
> `parseInt` throws a `NumberFormatException` if
> the format of `args[0]` isn't valid. All of the
> `Number` classes — `Integer`, `Float`,
> `Double`, and so on — have `parseXXX` methods that
> convert a `String` representing a number to an object of
> their type.

[« Previous](properties.html)
•
[Trail](../TOC.html)
•
[Next »](env.html)

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

**Previous page:** Properties
  
**Next page:** Environment Variables




A browser with JavaScript enabled is required for this page to operate properly.