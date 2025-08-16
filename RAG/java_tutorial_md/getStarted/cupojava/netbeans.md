[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Getting Started
  
**Lesson:** The "Hello World!" Application

[The "Hello World!" Application](index.html)

"Hello World!" for the NetBeans IDE

["Hello World!" for Microsoft Windows](win32.html)

["Hello World!" for Solaris OS and Linux](unix.html)

[Home Page](../../index.html)
>
[Getting Started](../index.html)
>
[The "Hello World!" Application](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](win32.html)

# "Hello World!" for the NetBeans IDE

It's time to write your first
application! These detailed instructions are for users of
the NetBeans IDE.
The NetBeans IDE runs on the Java platform,
which means that you can
use it with any operating system for which there is a
JDK 6
available.
These operating systems include Microsoft Windows,
Solaris OS, Linux, and Mac OS X.

* [A Checklist](#netbeans-1)
* [Creating Your First Application](#netbeans-2)
  + [Create an IDE Project](#netbeans-2a)
  + [Add JDK 6 to the Platform List (if necessary)](#netbeans-jdk)
  + [Add Code to the Generated Source File](#netbeans-2b)
  + [Compile the Source File](#netbeans-2c)
  + [Run the Program](#netbeans-2d)
* [Continuing the Tutorial with the NetBeans IDE](#netbeans-3)

---

## A Checklist  a checkmark

To write your first program, you'll need:

1. **The Java SE Development Kit 6 (JDK 6)**

   * For Microsoft Windows, Solaris OS, and Linux: <http://java.sun.com/javase/6/download.jsp>
   * For Mac OS X: <http://connect.apple.com>
2. **The NetBeans IDE**

   * For all platforms:
     <http://www.netbeans.info/downloads/index.php>

---

## Creating Your First Application

Your first application, `HelloWorldApp`,
will simply display the greeting "Hello World!". To create this
program, you will:

* **Create an IDE project**

  When you create an IDE project, you create an environment in which to build and run your applications.
  Using IDE projects eliminates configuration issues
  normally associated with
  developing on the command line. You can build or
  run your application by choosing a single menu item within the IDE.
* **Add code to the generated source file**

  A source file contains code, written in the Java programming
  language, that you and other programmers can understand. As
  part of creating an IDE project, a skeleton
  source file will be automatically generated. You will then modify the source
  file to add the "Hello World!" message.
* **Compile the source file into a .class file**

  The IDE invokes the Java programming language *compiler* `(javac)`,
  which takes your source file and translates its text into instructions
  that the Java virtual machine can understand.
  The instructions contained within this file are known as *bytecodes*.
* **Run the program**

  The IDE invokes the Java application *launcher tool* (`java`), which uses
  the Java virtual machine to run your application.

### Create an IDE Project

To create an IDE project:

1. Launch the NetBeans IDE.

   * On Microsoft Windows systems, you can use the NetBeans IDE item in the Start menu.
   * On Solaris OS and Linux systems, you execute the IDE launcher script by navigating to the IDE's `bin` directory and typing `./netbeans.`
   * On Mac OS X systems, click the NetBeans IDE application icon.- In the NetBeans IDE, choose File | New Project.

     ![NetBeans IDE with the File | New Project menu item selected.](../../figures/getStarted/nb-javatutorial-newprojectmenu.gif)

     NetBeans IDE with the File | New Project menu item selected.
   - In the New Project wizard, expand the General category and select Java Application as shown in the following figure:

     ![NetBeans IDE, New Project wizard, Choose Project page.](../../figures/getStarted/nb-javatutorial-project1.gif)

     NetBeans IDE, New Project wizard, Choose Project page.
   - In the Name and Location page of the wizard, do the following (as shown in the figure below):

     * In the Project Name field, type `Hello World App`.
     * In the Create Main Class field, type `helloworldapp.HelloWorldApp`.
     * Leave the Set as Main Project checkbox selected.

     ![NetBeans IDE, New Project wizard, Name and Location page.](../../figures/getStarted/nb-javatutorial-project2.gif)

     NetBeans IDE, New Project wizard, Name and Location page.
   - Click Finish.

The project is created and opened in the IDE. You should see the following components:

* The Projects window, which contains a tree view of the components of the project, including source files, libraries that your code depends on, and so on.
* The Source Editor window with a file called `HelloWorldApp` open.
* The Navigator window, which you can use to quickly navigate between elements within the selected class./

  ![NetBeans IDE with the HelloWorldApp project open.](../../figures/getStarted/nb-javatutorial-project-opened.gif)

  NetBeans IDE with the HelloWorldApp project open.

---

### Add JDK 6 to the Platform List (if necessary)

It may be necessary to add JDK 6 to the IDE's list of available platforms.
To do this, choose Tools | Java Platform Manager as shown in the following
figure:

![Selecting the Java Platform Manager from the Tools Menu](../../figures/getStarted/nb-javatutorial-platform-manager.gif)

Selecting the Java Platform Manager from the Tools Menu

If you don't see JDK 6 (which might appear as 1.6 or 1.6.0)
in the list of installed platforms, click "Add Platform", navigate to your
JDK 6 install directory, and click "Finish". You should now see this newly
added platform:

![The Java Platform Manager from the Tools Menu](../../figures/getStarted/nb-javatutorial-add-platform.gif)

The Java Platform Manager

To set this JDK as the default for all projects, you can
run the IDE with the `--jdkhome` switch on the command line, or by entering the path to the JDK in the `netbeans_j2sdkhome` property of your `INSTALLATION_DIRECTORY/etc/netbeans.conf` file.

To specify this JDK for the current project only, select Hello World App
in the Projects pane, choose File | "Hello World App" Properties, click
on Libraries, then select JDK 6 under the Java Platform pulldown menu.
You should see a screen similar to the following:

![](../../figures/getStarted/nb-javatutorial-properties2.gif)

The IDE is now configured for JDK 6.

---

### Add Code to the Generated Source File

When you created this project, you left the Create Main Class checkbox selected in the
New Project wizard. The IDE has therefore created a skeleton class for you.
You can add the "Hello World!" message to the
skeleton code by replacing the line:

```

// TODO code application logic here

```

with the line:

```

System.out.println("Hello World!"); // Display the string.

```

Optionally, you can replace these four lines of generated code:

```

/**
 *
 * @author
 */

```

with these lines:

```

/**
 * The HelloWorldApp class implements an application that
 * simply prints "Hello World!" to standard output.
 */

```

These four lines are a code comment and do not affect how the program runs.
Later sections of this tutorial explain the use and format of code comments.

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  |  | | --- | --- | --- | | **Be Careful When You Type** | uppercase letter A | lowercase letter A |   Type all code, commands, and file names exactly as shown. Both the compiler (`javac`) and launcher (`java`) are *case-sensitive*, so you must capitalize consistently.  `HelloWorldApp not equal sign helloworldapp` |

Save your changes by choosing File | Save.

The file should look something like the following:

```

/*
 * HelloWorldApp.java
 *
 * Created on February 5, 2006, 6:43 PM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

package helloworldapp;

/**
 * The HelloWorldApp class implements an application that
 * simply prints "Hello World!" to standard output.
 */
public class HelloWorldApp {

    /** Creates a new instance of HelloWorldApp */
    public HelloWorldApp() {
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Hello World!"); // Display the string.
    }

}

```

### Compile the Source File into a .class File

To compile your source file, choose Build | Build Main Project from the IDE's main menu.

The Output window opens and displays output similar to what you see in the
following figure:

![Output window showing results of building the HelloWorld project.](../../figures/getStarted/nb-javatutorial-project-compiled.gif)

Output window showing results of building the HelloWorld project.

If the build output concludes with the statement
`BUILD SUCCESSFUL`, congratulations! You have
successfully compiled your program!

If the build output concludes with the statement
`BUILD FAILED`, you probably have a syntax error
in your code. Errors are reported in the Output window as hyper-linked text.
You double-click such a hyper-link to navigate to the source of an error. You can
then fix the error and once again choose Build | Build Main Project.

When you build the project, the bytecode file `HelloWorldApp.class` is generated. You can see where the new file is generated by opening the Files window and expanding the `Hello World App/build/classes/helloworldapp` node as shown in the following figure.

![Files window, showing the generated .class file.](../../figures/getStarted/nb-javatutorial-files-window.gif)

Files window, showing the generated .class file.

Now that you have built the project,
you can run your program.

### Run the Program

From the IDE's menu bar, choose Run | Run Main Project.

The next figure shows what you should now see.

![The program prints Hello World! to the Output window (along with other output from the build script).](../../figures/getStarted/nb-javatutorial-project-run.gif)

The program prints "Hello World!" to the Output window (along with other output from the build script).

Congratulations! Your program works!

## Continuing the Tutorial with the NetBeans IDE

The next few pages of the tutorial will explain the code in this simple application.
After that, the lessons go deeper into core language features and provide many more examples.
Although the rest of the tutorial does not give specific instructions about using
the NetBeans IDE, you can easily use the IDE to write and run the sample code. The following
are some tips on using the IDE and explanations of some IDE behavior that you are likely to see:

* Once you have created a project in the IDE, you can add files to the
  project using the New File wizard. Choose File | New File, and then select a template
  in the wizard, such as the Empty Java File template.
* You can compile and run an individual file (as opposed to a whole project) using
  the IDE's Compile File (F9) and Run File (Shift-F6) commands.
  If you use the Run Main Project command, the IDE will run the file that the IDE associates
  as the main class of the main project. Therefore, if you create an additional class in your HelloWorldApp project and
  then try to run that file with the Run Main Project command, the IDE will run the `HelloWorldApp` file
  instead.
* You might want to create separate IDE projects for sample applications that include more than one source file.
* As you are typing in the IDE, a code completion box might periodically appear.
  You can either ignore the
  code completion box and keep typing, or you can select one of the suggested expressions.
  If you would prefer not to have the code completion box automatically appear, you
  can turn off the feature. Choose Tools | Options, click the Editor tab, and clear the
  Auto Popup Completion Window checkbox.
* If you try to rename the node for a source file in the Projects window, the IDE
  prompts you with the Rename dialog box to lead you through the options of renaming the class
  and the updating of code that refers to that class.
  Click Next to display the Refactoring window, which contains a tree view of changes to be made.
  Then click Do Refactoring to apply the changes. This sequence of clicks might seem unnecessary if you
  have just a single class in your project, but it is very useful when your changes affect
  other parts of your code in larger projects.
* For a more thorough guide to the features of the NetBeans IDE, see the
  [NetBeans IDE Docs and Support page](http://www.netbeans.org/kb/index.html) or explore the documentation available from the IDE's Help menu.

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](win32.html)

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

**Previous page:** The "Hello World!" Application
  
**Next page:** "Hello World!" for Microsoft Windows




A browser with JavaScript enabled is required for this page to operate properly.