[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Getting Started
  
**Lesson:** The "Hello World!" Application

[The "Hello World!" Application](index.html)

["Hello World!" for the NetBeans IDE](netbeans.html)

["Hello World!" for Microsoft Windows](win32.html)

"Hello World!" for Solaris OS and Linux

[Home Page](../../index.html)
>
[Getting Started](../index.html)
>
[The "Hello World!" Application](index.html)

[« Previous](win32.html) • [Trail](../TOC.html) • [Next »](../application/index.html)

# "Hello World!" for Solaris OS and Linux

It's time to write your first
application! These detailed instructions are for users of
Solaris OS and Linux.
Instructions for other platforms are in
["Hello World!" for Microsoft Windows](win32.html) and
["Hello World!" for the NetBeans IDE](netbeans.html).

If you encounter problems with the instructions on this page, consult the
[Common Problems (and Their Solutions)](../problems/index.html).

* [A Checklist](#unix-1)
* [Creating Your First Application](#unix-2)
  + [Create a Source File](#unix-2a)
  + [Compile the Source File into a `.class` File](#unix-2b)
  + [Run the Program](#unix-2c)

---

## A Checklist  a checkmark

To write your first program, you'll need:

1. **The Java SE Development Kit 6 (JDK 6)**

   You can
   [download the Solaris OS or Linux version now](http://java.sun.com/javase/6/download.jsp). (Make sure you download the **JDK**, *not* the JRE.)
   Consult the
   [installation instructions](http://java.sun.com/javase/6/webnotes/install/index.html).
2. **A text editor**

   In this example, we'll use
   Pico, an editor available for many UNIX-based platforms.
   You can easily adapt these instructions
   if you use a different text editor,
   such as `vi` or `emacs`.

These two items
are all you'll need to write your first application.

---

## Creating Your First Application

Your first application, `HelloWorldApp`,
will simply display the greeting "Hello world!". To create this
program, you will:

* **Create a source file**

  A source file contains code, written in the Java programming
  language, that you and other programmers can understand. You
  can use any text editor to create and edit source files.
* **Compile the source file into a .class
  file**

  The Java programming language *compiler* (`javac`)
  takes your source file and translates its text into instructions
  that the Java virtual machine can understand.
  The instructions contained within this `.class` file
  are known as *bytecodes*.
* **Run the program**

  The Java application *launcher tool* (`java`) uses the Java virtual machine to run your application.

### Create a Source File

To create a source file, you have two options:

* You can save the file `HelloWorldApp.java`
  on your computer and avoid a lot of typing. Then, you can go straight
  to [Compile the Source File](#unix-2b).
* Or, you can use the following (longer) instructions.

First, open a shell, or "terminal," window.

![A new terminal window.](../../figures/getStarted/prompt.gif)

A new terminal window.

When you first bring up the prompt, your *current directory*
will usually be your *home directory*. You can change your current
directory to your home directory at any time by typing `cd`
at the prompt and then pressing  **Return**.

The source files you create should be kept in a separate directory.
You can create a directory by using the command `mkdir`. For
example, to create the directory `java` in your home directory,
use the following commands:

```

cd
mkdir java

```

To change your current directory to this new directory, you
then enter:

```

cd java

```

Now you can start creating your source file.

|  |  |  |
| --- | --- | --- |
| Start the Pico editor by typing `pico` at the prompt and pressing  **Return**. If the system responds with the message `pico: command not found`, then Pico is most likely unavailable. Consult your system administrator for more information, or use another editor. When you start Pico, it'll display a new, blank *buffer*. This is the area in which you will type your code. | |  | | --- | |  | |

Type the following code into the new buffer:

```

/**
 * The HelloWorldApp class implements an application that
 * simply prints "Hello World!" to standard output.
 */
class HelloWorldApp {
    public static void main(String[] args) {
        System.out.println("Hello World!"); // Display the string.
    }
}

```

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  |  | | --- | --- | --- | | **Be Careful When You Type** | uppercase letter A | lowercase letter A |   Type all code, commands, and file names exactly as shown. Both the compiler (`javac`) and launcher tool (`java`) are *case-sensitive*, so you must capitalize consistently.  `HelloWorldApp not equal sign helloworldapp` |

Save the code in a file with the name
`HelloWorldApp.java`.
In the Pico editor, you do this
by typing  **Ctrl-O**
and then, at the bottom where you see the prompt `File Name to write:`,
entering the directory in which you wish to create the file,
followed by `HelloWorldApp.java`. For example, if you wish to
save `HelloWorldApp.java` in the directory `/home/jdoe/java`,
then you type `/home/jdoe/java/HelloWorldApp.java`
and press  **Return**.

You can type  **Ctrl-X** to exit Pico.

### Compile the Source File into a `.class` File

Bring up another shell window.
To compile your source file, change
your current directory to the directory where your file is located.
For example, if your source directory is
`/home/jdoe/java`,
type the following command at the prompt and press
 **Return**:

```

cd /home/jdoe/java

```

If you enter `pwd` at the prompt, you should see the current
directory, which in this example has been changed to `/home/jdoe/java`.

If you enter `ls` at the prompt, you should see your file.

![Results of the ls command, showing the .java source file.](../../figures/getStarted/firstls.gif)

Results of the `ls` command, showing the `.java` source file.

Now are ready to compile the source file. At the prompt, type the following command and
press  **Return**.

```

javac HelloWorldApp.java

```

The compiler has generated a bytecode file, `HelloWorldApp.class`.
At the prompt, type
`ls`
to see the new file that was generated:
the following figure.

![Results of the ls command, showing the generated .class file.](../../figures/getStarted/secondls.gif)

Results of the `ls` command, showing the generated `.class` file.

Now that you have a `.class` file,
you can run your program.

If you encounter problems with the instructions in this step, consult the
[Common Problems (and Their Solutions)](../problems/index.html).

### Run the Program

In the same directory, enter at the prompt:

```

java HelloWorldApp

```

The next figure shows what you should now see.

![The output prints Hello World! to the screen.](../../figures/getStarted/result.gif)

The output prints "Hello World!" to the screen.

Congratulations! Your program works!

If you encounter problems with the instructions in this step, consult the
[Common Problems (and Their Solutions)](../problems/index.html).

[« Previous](win32.html)
•
[Trail](../TOC.html)
•
[Next »](../application/index.html)

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

**Previous page:** "Hello World!" for Microsoft Windows
  
**Next page:** A Closer Look at the "Hello World!" Application




A browser with JavaScript enabled is required for this page to operate properly.