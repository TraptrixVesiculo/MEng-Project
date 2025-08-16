[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Learning the Java Language
  
**Lesson:** Packages

[Home Page](../../../index.html)
>
[Learning the Java Language](../../index.html)
>
[Packages](../index.html)

[« Previous](../QandE/packages-questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Creating and Using Packages

### Answers

> Question 1: Assume that you have written some classes. Belatedly, you
> decide that they should be split into three packages, as
> listed in the table below. Furthermore, assume that the
> classes are currently in the default package (they have
> no `package` statements).
> > |  |  |
> > | --- | --- |
> > | **Package Name** | **Class Name** |
> > | `mygame.server` | `Server` |
> > | `mygame.shared` | `Utilities` |
> > | `mygame.client` | `Client` |
> >
> > a. What line of code will you need to add to each source
> > file to put each class in the right package?
> >   
> > Answer 1a: The first line of each file
> > must specify the package:
> >
> > In `Client.java` add:
> > :   `package mygame.client;`
> >
> > In `Server.java` add:
> > :   `package mygame.server;`:
> >
> > In `Utilities.java` add:
> > :   `package mygame.shared;`
> >
> > b. To adhere to the directory structure, you will need to
> > create some subdirectories in your development directory,
> > and put source files in the correct subdirectories. What
> > subdirectories must you create? Which subdirectory does
> > each source file go in?
> >   
> >  Answer 1b: Within the `mygame`
> > directory, you need to create three subdirectories:
> > `client`,
> > `server`, and
> > `shared`.
> >
> > In `mygame/client/` place:
> > :   `Client.java`
> >
> > In `mygame/server/` place:
> > :   `Server.java`
> >
> > In `mygame/shared/` place:
> > :   `Utilities.java`
> >
> > c. Do you think you'll need to make any other changes to
> > the source files to make them compile correctly?
> > If so, what?
> >   
> >  Answer 1c: Yes, you need to add import statements.
> > `Client.java` and `Server.java` need to import the
> > `Utilities` class, which they can do in one of two ways:
> >
> > ```
> >
> > import mygame.shared.*;
> >        --or--
> > import mygame.shared.Utilities;
> >
> > ```
> >
> > Also, `Server.java` needs to import the `Client` class:
> >
> > ```
> >
> > import mygame.client.Client;
> >
> > ```

### Exercises

> Exercise 1: Download three source files:
>
> * [`Client`](question/Client.java)* [`Server`](question/Server.java)* [`Utilities`](question/Utilities.java)
>
> > a. Implement the changes you proposed in question 1,
> > using the source files you just downloaded.
> >   
> > b. Compile the revised source files. (*Hint:*
> > If you're invoking the compiler from the command line
> > (as opposed to using a builder), invoke the compiler from
> > the directory that contains the `mygame` directory
> > you just created.)
>
>  Answer 1: Download this zip file with the solution:
> <mygame.zip>  
> You might need to change your proposed import code to reflect our implementation.

[« Previous](../QandE/packages-questions.html)
•
[TOC](../../TOC.html)


---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Questions and Exercises: Creating and Using Packages




A browser with JavaScript enabled is required for this page to operate properly.