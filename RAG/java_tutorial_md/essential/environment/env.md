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

[Command-Line Arguments](cmdLineArgs.html)

Environment Variables

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

[« Previous](cmdLineArgs.html) • [Trail](../TOC.html) • [Next »](other.html)

# Environment Variables

Many operating systems use *environment variables* to pass
configuration information to applications. Like properties in the Java
platform, environment variables are key/value pairs, where both
the key and the value are strings. The conventions for setting and
using environment variables vary between operating systems, and also
between command line interpreters. To learn how to pass environment
variables to applications on your system, refer to your system
documentation.

### Querying Environment Variables

On the Java platform, an application uses `System.getEnv` to
retrieve environment variable values. Without an argument,
`getEnv` returns a read-only instance of
`java.util.Map`, where the map keys are the environment
variable names, and the map values are the environment variable
values. This is demonstrated in the
[`EnvMap`](examples/EnvMap.java)
example:

```


import java.util.Map;

public class EnvMap {
    public static void main (String[] args) {
        Map<String, String> env = System.getenv();
        for (String envName : env.keySet()) {
            System.out.format("%s=%s%n", envName, env.get(envName));
        }
    }
}


```

With a `String` argument, `getEnv` returns the
value of the specified variable. If the variable is not defined,
`getEnv` returns `null`. The
[`Env`](examples/Env.java)
example uses `getEnv` this way to query specific environment
variables, specified on the command line:

```


public class Env {
    public static void main (String[] args) {
        for (String env: args) {
            String value = System.getenv(env);
            if (value != null) {
                System.out.format("%s=%s%n", env, value);
            } else {
                System.out.format("%s is not assigned.%n", env);
            }
        }
    }
}


```

### Passing Environment Variables to New Processes

When a Java application uses a
[`ProcessBuilder`](http://download.oracle.com/javase/7/docs/api/java/lang/ProcessBuilder.html)
object to create a new process, the default set of environment
variables passed to the new process is the same set provided to the
application's virtual machine process. The application can change this
set using `ProcessBuilder.environment`.

### Platform Dependency Issues

There are many subtle differences between the way environment
variables are implemented on different systems. For example, Windows
ignores case in environment variable names, while UNIX does not. The
way environment variables are used also varies. For example, Windows
provides the user name in an environment variable called
`USERNAME`, while UNIX implementations might provide the
user name in `USER`, `LOGNAME`, or both.

To maximize portability, never refer to an environment variable when
the same value is available in a system property. For example, if the
operating system provides a user name, it will always be available in
the system property `user.name`.

[« Previous](cmdLineArgs.html)
•
[Trail](../TOC.html)
•
[Next »](other.html)

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

**Previous page:** Command-Line Arguments
  
**Next page:** Other Configuration Utilities




A browser with JavaScript enabled is required for this page to operate properly.