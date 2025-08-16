[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** The Platform Environment

[The Platform Environment](index.html)

[Configuration Utilities](config.html)

[Properties](properties.html)

[Command-Line Arguments](cmdLineArgs.html)

[Environment Variables](env.html)

[Other Configuration Utilities](other.html)

[System Utilities](system.html)

[Command-Line I/O Objects](cl.html)

[System Properties](sysprop.html)

[The Security Manager](security.html)

[Miscellaneous Methods in System](sysmisc.html)

PATH and CLASSPATH

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[The Platform Environment](index.html)

[« Previous](sysmisc.html) • [Trail](../TOC.html) • [Next »](QandE/questions.html)

# PATH and CLASSPATH

This section explains how to use the
`PATH` and `CLASSPATH` environment
variables on Microsoft Windows, Solaris, and Linux.
Consult the installation instructions
included with your installation of the Java Development Kit (JDK)
software bundle for current information.

After installing the software,
the JDK directory will have the structure shown below.

![JDK directory structure](../../figures/essential/environment-directories.gif)

The `bin` directory contains both the compiler
and the launcher.

### Update the PATH Variable (Microsoft Windows NT/2000/XP)

You can run Java applications just fine without setting the
`PATH` variable. Or, you can optionally set it as a
convenience.

Set the `PATH` variable if you want to be able to
conveniently run the executables (`javac.exe`,
`java.exe`, `javadoc.exe`, and so on)
from any directory without having to type the full path of the
command. If you do not set the `PATH` variable,
you need to specify the full path to the executable every time
you run it, such as:

```

C:\Program Files\Java\jdk1.6.0\bin\javac MyClass.java

```

---

**Note:** It is useful to set the `PATH` permanently so it will
persist after rebooting. To set it permanently, add the full path of
the `jdk1.6.0` bin directory to the `PATH`
variable. Set the `PATH` as follows.

---

To make a permanent change to the CLASSPATH variable, use the System
icon in the Control Panel. The precise procedure varies depending on
the version of Windows.

The `PATH` can be a series of directories separated by
semicolons (;). Microsoft Windows looks for programs in the
`PATH` directories in order, from left to right.
You should have only one `bin` directory for the JDK
in the path at a time (those following the first are ignored),
so if one is already present, you can update that particular entry.

### Update the PATH Variable (Solaris and Linux)

You can run the JDK just fine without setting the `PATH`
variable, or you can optionally set it as a convenience. However,
you should set the path variable if you want to be able to run
the executables (`javac`, `java`,
`javadoc`, and so on) from any directory without
having to type the full path of the command. If you do not set
the `PATH` variable, you need to specify the full
path to the executable every time you run it, such as:

```

% /usr/local/jdk1.6.0/bin/javac MyClass.java

```

To find out if the path is properly set, execute:

```

% java -version

```

This will print the version of the `java` tool,
if it can find it. If the version is old or you get the
error **java: Command not found**, then the path is not properly set.

To set the path permanently, set the path in your startup file.

For C shell (`csh`), edit the startup file `(~/.cshrc`):

```

set path=(/usr/local/jdk1.6.0/bin )

```

For `bash`, edit the startup file (`~/.bashrc`):

```

PATH=/usr/local/jdk1.6.0/bin:
export PATH

```

For `ksh`, the startup file is named by the
environment variable, `ENV`. To set the path:

```

PATH=/usr/local/jdk1.6.0/bin:
export PATH

```

For `sh`, edit the profile file (`~/.profile`):

```

PATH=/usr/local/jdk1.6.0/bin:
export PATH

```

Then load the startup file and verify that the path is set by repeating
the `java` command:

For C shell (`csh`):

```

% source ~/.cshrc
% java -version

```

For `ksh`, `bash`, or `sh`:

```

% . /.profile
% java -version

```

### Checking the CLASSPATH variable (All platforms)

The `CLASSPATH` variable is one way to tell applications,
including the JDK tools, where to look for user classes.
(Classes that are part of the JRE, JDK platform, and extensions
should be defined through other means, such as the bootstrap class path
or the extensions directory.)

The preferred way to specify the class path is by using the
`-cp` command line switch. This allows the
`CLASSPATH` to be set individually for each application without
affecting other applications.
*Setting the `CLASSPATH` can be tricky and should be
performed with care.*

The default value of the class path is ".", meaning that only the
current directory is searched. Specifying either the CLASSPATH
variable or the `-cp` command line switch overrides this
value.

To check whether `CLASSPATH` is set on Microsoft Windows
NT/2000/XP, execute the following:

```

C:> echo %CLASSPATH%       

```

On Solaris or Linux, execute the following:

```

% echo $CLASSPATH

```

If `CLASSPATH` is not set you will get a
**CLASSPATH: Undefined variable** error (Solaris or Linux)
or simply **%CLASSPATH%** (Microsoft Windows NT/2000/XP).

To modify the `CLASSPATH`, use the same procedure you used
for the `PATH` variable.

Class path wildcards
allow you to include an entire directory of `.jar`
files in the class path without explicitly naming them individually.
For more information, including an explanation of class path wildcards,
and a detailed description on how to clean up the `CLASSPATH`
environment variable, see the
[Setting the Class Path](http://java.sun.com/javase/6/docs/technotes/tools/windows/classpath.html)
technical note.

[« Previous](sysmisc.html)
•
[Trail](../TOC.html)
•
[Next »](QandE/questions.html)

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

**Previous page:** Miscellaneous Methods in System
  
**Next page:** Questions and Exercises: The Platform Environment




A browser with JavaScript enabled is required for this page to operate properly.