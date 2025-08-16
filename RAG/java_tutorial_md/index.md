[Search](search.html)
  
[Feedback](http://download.oracle.com/javase/feedback.html)

![Duke thinking about what to study](images/ThinkingDuke.png)
  
Not sure where to start?

The Java Tutorials are practical guides for programmers who want
to use the Java programming language to create applications. They
include hundreds of complete, working examples, and dozens of
lessons. Groups of related lessons are organized into "trails".

For the most accurate and up-to-date tutorials,
please access the latest version from Oracle's official website for the
Java SE Tutorials (Last Updated [03/17/2011](information/history.html)), which can be found at:
[http://download.oracle.com/javase/tutorial](http://download.oracle.com/javase/tutorial/).

The Java SE Tutorials primarily describe features in Java SE 6.
For best results, [download JDK 6](http://www.oracle.com/technetwork/java/javase/downloads/index.html).

### What's New

Enjoy quizzes? Take a minute to answer this quiz about Java applets.
[![Java Applets Quiz](images/quiz.jpg "Java Applets Quiz")](http://download.oracle.com/javase/tutorialJWS/flash/AppletQuiz/AppletQuiz.html)

The Java Tutorials are continuously updated to keep up with changes to
the Java Platform and to incorporate feedback from our readers.
Included in recent releases:

* The `JLayer` component, introduced in Java SE 7,
  is explained in [How to Decorate
  Components with JLayer](uiswing/misc/jlayer.html).

  * As of Java SE 7 build 130, the NIO.2 File I/O package has
    been updated, with new and simplified API. The
    [File I/O (Featuring NIO.2)](essential/io/fileio.html)
    section has been modified to reflect these changes.

    * Samples that demonstrates how to use `RowSet` objects
      have been added to the [JDBC trail](jdbc).
      Please see [Using RowSet Objects](jdbc/basics/rowset.html)
      for more information. In addition, a sample that shows you how to integrate
      JDBC with a GUI API, in particular the Swing API, has been added.
      Please see [Using JDBC with
      GUI API](jdbc/basics/jdbcswing.html) for more information.

      * The latest version of the [Unicode
        Standard](http://unicode.org/) is [Unicode
        6.0](http://www.unicode.org/versions/Unicode6.0.0/). The Java tutorial has new coverage for Unicode:
        + [Unicode](i18n/text/unicode.html), a lesson in
          the [Internationalization](i18n) trail.+ [Converting Latin Digits to Other
            Unicode Digits](i18n/text/shapedDigits.html)+ [Unicode Support](essential/regex/unicode.html), a page in
              the [Regular Expressions](essential/regex/) lesson.

        * As a result of
          [Project Coin](http://openjdk.java.net/projects/coin/),
          several changes were introduced to the Java language:
          + The [Primitive
            Data Types](java/nutsandbolts/datatypes.html) page has been updated to discuss binary literals
            and to mention that underscore characters can
            appear anywhere between digits in a numerical literal.+ [The switch
              Statement](java/nutsandbolts/switch.html) page has been updated to reflect the ability to
              switch on a `String` object.+ The [Diamond Operator](java/generics/gentypes.html#diamond)
                has been added to generics. See the
                [Type
                Inference](java/generics/gentypeinference.html#type-inference-instantiation) section for more information.+ Using non-reifiable parameters with varags methods is also new.
                  See [Using
                  Non-Reifiable Parameters with Varargs Methods](java/generics/non-reifiable-varargs-type.html) for more information.+ The ability to catch more than one type of exception with a single
                    exception handler has been added. See
                    [The `catch`
                    Blocks](essential/exceptions/catch.html) for more information.+ The `try`-with-resources statement ensures that a resource
                      (such as a `BufferedReader`) is closed when the program is
                      finished with it. See
                      [The
                      try-with-resources Statement](essential/exceptions/tryResourceClose.html) for more information.

The Java Tutorials include content for features in the upcoming Java SE 7
release. Java SE 7 specific content will be revised as necessary to
accommodate changes in feature specification before the final Java SE 7
release.

### Trails Covering the Basics

These trails are available in book form as *The Java
Tutorial, Fourth Edition*. To buy this book,
refer to the box to the right.

* [Getting Started](getStarted/index.html)
  — An introduction to Java technology and lessons on
  installing Java development software and using it to create a
  simple program.* [Learning the Java Language](java/index.html)
    — Lessons describing the essential concepts and features
    of the Java Programming Language.* [Essential Java Classes](essential/index.html)
      — Lessons on exceptions, basic input/output,
      concurrency, regular expressions, and the platform
      environment.* [Collections](collections/index.html) —
        Lessons on using and extending the Java Collections Framework.* [Swing](ui/index.html) — An introduction
          to the Swing GUI toolkit, with an overview of features and a
          visual catalog of components. See below for a more
          comprehensive tutorial on Swing.* [Deployment](deployment/index.html) —
            How to package applications and applets using JAR files, and
            deploy them using Java Web Start and Java Plug-in.* [Preparation
              for Java Programming Language Certification](extra/certification/index.html)
              — List of available training and tutorial resources.

### Creating Graphical User Interfaces

This trail is available in book form as *The JFC Swing
Tutorial*. To buy this book, refer to the box to the right.

* [Creating a GUI with
  Swing](uiswing/index.html) — A comprehensive introduction to GUI
  creation on the Java platform.

### Specialized Trails and Lessons

These trails and lessons are only available as web pages.

* [Custom Networking](networking/index.html)
  — An introduction to the Java platform's powerful
  networking features.* [The Extension Mechanism](ext/index.html)
    — How to make custom APIs available to all applications
    running on the Java platform.* [Full-Screen
      Exclusive Mode API](extra/fullscreen/index.html) — How to write applications
      that more fully utilize the user's graphics hardware.* [Generics](extra/generics/index.html) —
        An enhancement to the type system that supports operations on
        objects of various types while providing compile-time type
        safety. Note that this lesson is for advanced users. The [Java Language](java/index.html) trail contains a [Generics](java/generics/index.html) lesson that is
        suitable for beginners.* [Internationalization](i18n/index.html) —
          An introduction to designing software so that it can be easily
          be adapted (localized) to various languages and regions.* [JavaBeans](javabeans/index.html) —
            The Java platform's component technology.* [JDBC Database Access](jdbc/index.html) —
              Introduces an API for connectivity between the Java
              applications and a wide range of databases and a data sources.* [JMX](jmx/index.html)— Java Management
                Extensions provides a standard way of managing resources
                such as applications, devices, and services.* [JNDI](jndi/index.html)— Java Naming and
                  Directory Interface enables accessing the Naming and Directory
                  Service such as DNS and LDAP.* [JAXP](jaxp/index.html) — Introduces
                    the Java API for XML Processing (JAXP) 1.4 technology.* [RMI](rmi/index.html) — The Remote Method
                      Invocation API allows an object to invoke methods of
                      an object running on another Java Virtual Machine.* [Reflection](reflect/index.html) — An API
                        that represents ("reflects") the classes, interfaces, and
                        objects in the current Java Virtual Machine.* [Security](security/index.html) — Java
                          platform features that help protect applications from
                          malicious software.* [Sound](sound/index.html) — An API for
                            playing sound data from applications.* [2D Graphics](2d/index.html) — How to
                              display and print 2D graphics in applications.* [Sockets Direct Protocol](sdp/index.html) — How to
                                enable the Sockets Direct Protocol to take advantage of
                                InfiniBand.

---

Your use of this page [(http://download.oracle.com/javase/tutorial](http://download.oracle.com/javase/tutorial/) (Last Updated [03/17/2011](information/history.html)))
and all the material on pages under "The Java Tutorials" banner is subject to the
[Java SE Tutorial Copyright and License](information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Waving Duke | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |