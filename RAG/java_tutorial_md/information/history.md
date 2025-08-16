# What's new and What's Old? The History of the Tutorial

![](../images/shoeline2.GIF)
![](../images/shoeline2.GIF)

**17 March 2011** —

This update features:

* The `JLayer` component, introduced in Java SE 7,
  is explained in [How to Decorate
  Components with JLayer](../uiswing/misc/jlayer.html).* As of Java SE 7 build 130, the NIO.2 File I/O package has
    been updated, with new and simplified API. The
    [File I/O (Featuring NIO.2)](../essential/io/fileio.html)
    section has been modified to reflect these changes.* Samples that demonstrates how to use `RowSet` objects
      have been added to the [JDBC trail](../jdbc).
      Please see [Using RowSet Objects](../jdbc/basics/rowset.html)
      for more information. In addition, a sample that shows you how to integrate
      JDBC with a GUI API, in particular the Swing API, has been added.
      Please see [Using JDBC with
      GUI API](../jdbc/basics/jdbcswing.html) for more information.

**21 Feb 2011 - JDK 7 Developer Preview Release** —

This update features:

* The latest version of the [Unicode
  Standard](http://unicode.org/) is [Unicode
  6.0](http://www.unicode.org/versions/Unicode6.0.0/). The Java tutorial has new coverage for Unicode:
  + [Unicode](../i18n/text/unicode.html), a lesson in
    the [Internationalization](../i18n) trail.+ [Converting Latin Digits to Other
      Unicode Digits](../i18n/text/shapedDigits.html)+ [Unicode Support](../essential/regex/unicode.html), a page in
        the [Regular Expressions](../essential/regex/) lesson.

  * As a result of
    [Project Coin](http://openjdk.java.net/projects/coin/),
    several changes were introduced to the Java language:
    + The [Primitive
      Data Types](../java/nutsandbolts/datatypes.html) page has been updated to discuss binary literals
      and to mention that underscore characters can
      appear anywhere between digits in a numerical literal.+ [The switch
        Statement](../java/nutsandbolts/switch.html) page has been updated to reflect the ability to
        switch on a `String` object.+ The [Diamond Operator](../java/generics/gentypes.html#diamond)
          has been added to generics. See the
          [Type
          Inference](../java/generics/gentypeinference.html#type-inference-instantiation) section for more information.+ Using non-reifiable parameters with varags methods is also new.
            See [Using
            Non-Reifiable Parameters with Varargs Methods](../java/generics/non-reifiable-varargs-type.html) for more information.+ The ability to catch more than one type of exception with a single
              exception handler has been added. See
              [The `catch`
              Blocks](../essential/exceptions/catch.html) for more information.+ The `try`-with-resources statement ensures that a resource
                (such as a `BufferedReader`) is closed when the program is
                finished with it. See
                [The
                try-with-resources Statement](../essential/exceptions/tryResourceClose.html) for more information.

**18 Oct 2010** —

This update features:

* For several months the Java SE Tutorials were not available as a
  download. We are happy to report that the very popular bundle
  is back and available through on the [front page](../index.html)
  through the link under the "Tutorial Resources" box to the right.* Do the Java Tutorials seem overwhelming to you? We have
    added a new [Learning Paths](../tutorialLearningPaths.html) page.* The new [Fork/Join](../essential/concurrency/forkjoin.html) page,
      part of the [Concurrency
      lesson](../essential/concurrency/index.html), describes how you can use the Fork/Join framework to take
      advantage of multiple processors.
      This feature is available now in the Java SE 7 release available on
      [java.net](http://dlc.sun.com.edgesuite.net/jdk7/binaries/index.html).* The [JDBC Basics](../jdbc/basics) lesson has been completely
        revamped, including updated sample code that you can download,
        compile, and run – the code has been configured for Java DB and MySQL.
        See [Getting Started](../jdbc/basics/gettingstarted.html)
        for more information.* Finally, a small, but notable, change is that the standalone JNDI tutorial,
          previously available on java.sun.com, has been moved to the Java SE
          documentation archive on
          [download.oracle.com](http://download.oracle.com/javase/jndi/tutorial/)
          and many broken links in the tutorial have been fixed.
          The [front page of the JNDI tutorial](../jndi/)
          has been modified accordingly, and redirects are in place ensuring a
          seamless transition.

**7 July 2010** —

This tutorial update represents the first release under its new
home at `download.oracle.com`. Redirects are in place,
so any attempt to access the tutorials at
`java.sun.com/docs/books/tutorial` will be redirected to the new
location. We hope this will be a seamless transition for our many
tutorial readers,
but please let us know if you encounter any problems.

Also included in this release:

* [Customizing the Loading Experience](../deployment/doingMoreWithRIA/customizeRIALoadingExperience.html) explains how to provide a customized
  loading progress indicator for a rich Internet application,
  a feature first introduced in the JDK 6 Update 18
  release and enhanced in the Java SE 6 Update 21 release.* A new trail introducing [Java
    API for XML Processing (JAXP) 1.4 technology](../jaxp).
    (This was previously released on `java.sun.com/webservices/references`.)

**12 January 2010** —

This update features:

* [Developing
  Draggable Applets](../deployment/applet/draggableApplet.html) – a new topic describing
  how to create an applet that can be dragged outside
  of a browser and dynamically converted into a Java Web Start
  application.* [Sending Messages
    to Other Applets](../deployment/applet/iac.html) has been rewritten.* Previously, a number of the [Swing
      examples](../uiswing/examples/components/index.html), which are distributed as NetBeans projects,
      were missing a tag that prevented them from being
      opened in NetBeans 6.5 or later. The missing tag has been added to
      all `project.xml` files.* Various minor errors, typos, and broken links have been fixed.

**23 September 2009** —

This update features:

* A Deployment tutorial that covers a wide range of topics about the development
  and deployment of rich Internet applications. The Deployment tutorial contains the
  following lessons:
  + [Applets](../deployment/applet/index.html)
  + [Java Web Start](../deployment/webstart/index.html)
  + [Doing More With Rich Internet Applications](../deployment/doingMoreWithRIA/index.html)
  + [Deployment In-Depth](../deployment/deploymentInDepth/index.html)* A new section in the Swing look and feel lesson showing how to use the
    new [Nimbus](../uiswing/lookandfeel/nimbus.html) look and feel.* A new Swing page describing [How to
      Create Translucent and Shaped Windows](../uiswing/misc/trans_shaped_windows.html).* A new Interfaces and Inheritance page discussing
        [Polymorphism](../java/IandI/polymorphism.html).* As always, we have fixed numerous bugs, typos and broken links.

**27 May 2009** —

This update features:

* An entirely reworked [File I/O](../essential/io/fileio.html)
  lesson, featuring NIO.2. This functionality is part of JDK7, which is available
  now through the [Open JDK](http://download.java.net/jdk7/binaries/)
  project on [java.net](http://java.net/).* A new facility for gathering feedback about the tutorial. At the bottom of
    each content page, you can leave a publicly viewable comment.
    Leaving a comment using the [JS-Kit](http://js-kit.com/)
    mechanism is similar to leaving a blog comment. Let us know what you think!* A new specialized trail covering [Sockets Direct Protocol](../sdp),
      also new in JDK7.* Fixed typos and broken links.

**14 March 2008** —

This update features:

* The [Drag and Drop](../uiswing/dnd/) lesson has
  been completely rewritten and updated to JDK 6.* An updated Copyright page.* A new License page that allows
      our users to modify tutorial content for limited non-commercial
      purposes.* We are moving our downloads to the Sun Download Center.
        You are required to accept the license in order to download
        the Java Tutorials.* We are retiring the feature where we name the releases and will
          be using dates from now on.* Besides the work listed here, there are many fixed broken links,
            typos and other miscellaneous errata.

**Antediluvian Chili Pepper Day\*, 1 August 2007** —

This push completes the tutorial update to JDK 6, with the exception of
the Swing drag and drop lesson, which is marked as such. There are many updated
pages, but the more notable changes are:

* [Performing Custom Painting](../uiswing/painting), a new lesson.* [How to Print Text](../uiswing/misc/printtext.html), a new page.* [Laying Out Components
      Within a Container](../uiswing/layout), an updated lesson.* [How to Use Icons](../uiswing/components/icon.html), with an
        updated demo by reader Collin Fagan.

\*OK, we made this up, or rather Collin did. :-)

**National Honesty Day, 30 April 2007** —

This update focuses on the Swing tutorial — we have updated 80% of the
material in the Swing tutorial to the JDK 6 release.

A significant part of this effort makes our examples easier than ever to use!
The Swing examples are now packaged ready to use in NetBeans IDE. Check out the
[examples index](../uiswing/examples/components/index.html)
for any of the Swing lessons (this link takes you to the Components lesson, there
is a separate index for each Swing lesson)
and you can download a zip file for any demo.
Or you can visit the Check out the
[Running Tutorial Examples in NetBeans IDE](examples.html) page
for more information on how to use the examples with NetBeans. Visit the
[NetBeans IDE download page](http://www.netbeans.info/downloads/index.php)
to obtain release 5.5 of NetBeans IDE (it's free).

Some of our brand new and significantly updated sections include:

* [Learning Swing with NetBeans IDE](../uiswing/learn), a new lesson!* [The Synth Look and Feel](../uiswing/lookandfeel/synth.html)* [How to Integrate with the Desktop Class](../uiswing/misc/desktop.html)* [How to Use Modality in Dialogs](../uiswing/misc/modality.html)* [How to Print Tables](../uiswing/misc/printtable.html)* [How to Create a Splash Screen](../uiswing/misc/splashscreen.html)* [How to Use the System Tray](../uiswing/misc/systemtray.html)* [How to Use Tables](../uiswing/components/table.html)

**Area Code Day, 10 November 2006** —

Check out the new
[Java Tutorials' Blog](http://blogs.sun.com/thejavatutorials/)!

[The Java™
Tutorial (4th edition)](http://www.amazon.com/gp/product/0321334205/sr=8-2/qid=1153852829/ref=pd_bbs_2/102-5355251-5123312?ie=UTF8) is now available in print.
This update of the tutorial includes an [Errata](errata.html)
page for the first printing. Our publisher, Addison Wesley, informs us
that several translations of this book are already in progress.

For this update, all of the specialized trails, except for Reflection,
have been updated to release 6. The newly updated sections include:

* [Internationalization](../i18n)* [JavaBeans](../javabeans)* [JDBC Database Access](../jdbc)* [RMI](../rmi)* [Security](../security)* [Sound](../sound)* [2D Graphics](../2d)

Plus, there are two all-new specialized trails:

* [Java Naming and Directory Interface (JNDI)](../jndi)* [Java Management Extensions (JMX)](../jmx)

Also, the update of the Swing trail to release 6 is in progress
and includes these sections:

* [Swing Concurrency](../uiswing/concurrency)
  is a new lesson that replaces the old "How to Use Threads"
  section. It covers the new class `javax.swing.SwingWorker`.* [How to Use Tabbed Panes](../uiswing/components/tabbedpane.html)* [Modifying the Look and Feel](../uiswing/lookandfeel)
      is a new lesson that includes the previous
      [How to Set the Look and Feel](../uiswing/lookandfeel/plaf.html)
      page. Note that this section is still in progress.

The new look and feel of the tutorial has been further refined.
Many of you have sent us feedback and we have been listening.
The TOC on the left-side of the page can now be toggled.
See the "Hide the TOC" button in the banner at the top of the page.

Also, there is a new [Compiling and
Running the Examples FAQ](run-examples.html) available at the bottom of most every
page in the tutorial.

**National Watermelon Day, 3 August 2006** —

The core tutorial is now updated to release JDK 6.
This is in preparation
for a new printed edition of
[The Java™
Tutorial (4th edition)](http://www.amazon.com/gp/product/0321334205/sr=8-2/qid=1153852829/ref=pd_bbs_2/102-5355251-5123312?ie=UTF8) that you can pre-order on
[Amazon](http://www.amazon.com) or through many other booksellers.
This online update includes the following sections:

* [Getting Started](../getStarted) (with a new NetBeans section)* [Object-Oriented Programming Concepts](../java/concepts)* [Language Basics](../java/nutsandbolts)* [Classes and Objects](../java/javaOO)* [Interfaces and Inheritance](../java/IandI)* [Numbers and Strings](../java/data)* [Generics](../java/generics)* [Packages](../java/package)* [Exceptions](../essential/exceptions)* [Basic I/O](../essential/io/)* [Concurrency](../essential/concurrency)* [Regular Expressions](../essential/regex)* [The Platform Environment](../essential/environment)* [Swing](../ui), a new trail that shows the
                            many capabilities of Swing and features a sophisticated
                            PasswordStore demo by Swing engineer, Scott Violet
                            (source included)
                            Deployment* [Preparation
                              for Java Programming Language Certification](../extra/certification/index.html)

The following update is also complete, though not part of the published
tutorial:

* [Custom Networking](../networking)* [The Extension Mechanism](../ext)

All examples in the basic tutorial and in the Swing tutorial have
been updated to compile against the 6.0 release.
Applets and Java web start applications
require 6.0 to run. (The one exception are the applets in the
deployment/applet section that will run under 1.4 and 1.5.)

You may notice that some very old parts of the tutorial have been
removed. The previous version of the tutorial is now available
via download. See the download page.

Finally, the tutorial itself has gotten a facelift, with a new look
and feel. Let us know what you think about these changes
and please let us know if you find any problems. Send feedback via our
[feedback
form](http://developers.sun.com/contact/tutorial_feedback.jsp).

**Nutcracker Release, 23 December 2005** —

The Java Tutorial update to JDK 5.0 is now complete.
This includes these sections of the tutorial:

* [Getting Started](../getStarted/index.html)* [Object-Oriented Programming Concepts](../java/concepts/index.html)* [Language Basics](../java/nutsandbolts/index.html)* [Objects Basics and Simple Data Objects](../java/data/index.html)* [Classes and Inheritance](../java/javaOO/index.html)* [Interfaces and Packages](../java/package/index.html)* [Handling Errors Using Exceptions](../essential/exceptions/index.html)* [Threads: Doing Two or More Tasks at Once](../essential/concurrency/index.html)* [Collections](../collections/index.html)* [I/O](../essential/io/index.html)* [Deployment](../deployment/index.html), a new trail that includes:
                      + [Applets](../deployment/applet/index.html)+ [Java Web Start](../deployment/webstart/index.html)+ [Packaging Programs in JAR Files](../deployment/jar/index.html)

Other changes include:

* Several of the very old, out-of-date sections have been
  archived and are now available via download. See the
  download page for a complete
  list of available bundles.* You'll notice that the old applet and JAR sections have been
    updated and moved to the new Deployment trail. You may notice
    redirects if you have absolute links to the old pages.* We fixed the broken [search](../search.html) feature:
      it wasn't limiting its search to the tutorial. This is now
      working correctly.* Across the tutorial, 1.0 and 1.1 examples have been removed.
        The release 5 examples are located in "ex5" directories.* We have a new
          [feedback
          form](http://developers.sun.com/contact/tutorial_feedback.jsp). It looks different, but your feedback goes to the same
          place. Although our workload prevents us from responding to each
          email, rest assured we do read it.* Finally, we fixed the usual broken links, typos, and other errata.

**Dorothy's Birthday Release, 15 April 2005** —

The following sections have been updated to 5.0:

* [Language Basics](../java/nutsandbolts/index.html)* [Classes and Inheritance](../java/javaOO/index.html)* [Object Basics and Simple Data Objects](../java/data/index.html)* [Collections](../collections/index.html)

The following sections were updated to 5.0 in our last release,
but have since been updated to reflect reader or reviewer feedback:

* [Object-Oriented Programming Concepts](../java/concepts/index.html)* [Interfaces and Packages](../java/package/index.html)* [Threads: Doing Two or More Tasks At Once](../essential/concurrency/index.html)* [Handling Errors with Exceptions](../essential/exceptions/index.html)

Other changes include:

* At readers' request,
  we changed the Feedback Form link at the top of each window
  to bring up a new window
  so you don't lose the page you're giving feedback about.* We started adding ZIP files so you can easily download
    all the examples for a particular chapter.* We added 5.0 versions (including web start links)
      of the examples in two Swing lessons: Getting Started with Swing
      and Learning Swing by Example.* We moved several applets back to the pages where they're
        referred to. Please
        [let
        us know](http://developers.sun.com/contact/tutorial_feedback.jsp) how you feel about this. Another alternative
        for some of these that aren't truly integrated with their page
        is to make them web started applications.* We made many small changes — which you probably won't notice
          — to clean up our HTML, reduce code sample line length where
          necessary,
          and generally enable better generation of book files from the HTML files.* Finally, we fixed the usual broken links, typos, and other errata.

**Anya's Birthday Release, 14 Feb 2005** —

The following sections have been updated to 5.0 (though most are still
pending engineering review):

* [Object-Oriented Programming Concepts](../java/concepts/index.html)* [Interfaces and Packages](../java/package/index.html)* [Handling Errors Using Exceptions](../essential/exceptions/index.html)* [Threads: Doing Two or More Tasks at Once](../essential/concurrency/index.html)* JAR Files

Other, minor changes that you might notice include:

* In the chapters where the content hasn't yet been updated,
  we have updated some of the images. In some cases, this might lead
  to a mismatch between the text (or code) and the image.* We have modified the page headers and the copyright notices.
    This will cause each page to be updated, even if the content hasn't
    yet changed.* Our [search page](../search.html) has been fixed.
      Thanks to those of you who reported that it was broken.* Finally, we fixed the usual broken links, typos, and other errata.

**Swing Book Release #2, 11 March 2004** —

* Added an information page for our just-published book,
  *The JFC Swing Tutorial, Second Edition*.
  It includes pointers to other pages
  describing and book and CD contents,
  as well as errata.* Added questions and exercises, along with answers,
    to the Swing trail.
    These reflect the Questions and Exercises section
    at the end of every non-reference chapter in the new book.* Updated the
      [table sorting](../uiswing/components/table.html#sorting)
      example
      to use a much more recent, functional, and robust version
      of `TableSorter`.* The usual miscellaneous fixes.

**Swing Book Release, 20 February 2004** —

* Updated the first two lessons of
  the [Swing trail](../uiswing/index.html)
  to 1.4 (with notes about what's expected in 1.5):
  [Getting Started with
  Swing](../uiswing/start/index.html) and [Learning
  Swing by Example](../uiswing/learn/index.html).* Throughout the tutorial,
    made the usual fixes to broken links, typos, and other errata.

**Maya's Birthday Release, 3 November 03** —

* With the exception of the first two lessons,
  the [Swing trail](../uiswing/index.html)
  has now been updated to 1.4
  (with notes about what's expected in 1.5)
  and reflects what will be published in the upcoming book.
  We'll note the biggest changes here,
  but with so many changes, we can't mention them all.* After consulting with the Swing engineers,
    we changed our thread safety recommendations
    and updated all but a few straggling 1.4 Swing examples
    to be thread safe.
    The newest recommendation is this:
    **Build the GUI on the event-dispatching thread.**
    See How to Use Threads for details.* Updated all pages in the Swing
      [layout](../uiswing/layout/index.html)
      and
      [events](../uiswing/events/index.html)
      lessons to 1.4.* Updated the accessibility, actions, threads, and timer pages in the
        [Using Other Swing Features](../uiswing/misc/index.html)
        lesson to 1.4.* In the
          [Using Swing Components](../uiswing/components/index.html)
          lesson,
          updated the applet, root pane, spinner, split pane, tabbed pane,
          table, tool bar, tool tip, tree, and all text component pages
          to 1.4. Created pages for separators and formatted text fields.* Completely rewrote the [painting](../uiswing/painting/index.html)
            lesson.
            Instead of featuring only the API in the `Graphics` class,
            it now simply tells you what's special about painting Swing components
            and refers you to the 2D trail for details.* Throughout the tutorial,
              made the usual fixes to broken links, typos, and other errata.

**Victoria Day (Canada), 19 May 03** —

* Added two completely new and
  much-requested pages to the Swing part of the tutorial:
  How to Use Data Transfer
  (which covers drag and drop and cut/copy/paste) and
  [How to Use the Focus Subsystem](../uiswing/misc/focus.html).
  Many thanks to Shannon Hickey and Scott Violet for their reviews
  of these rather long and technically complex sections.* Drastically changed the text and examples for
    [How to Use SpringLayout](../uiswing/layout/spring.html).
    It's still unfinished, but should now be more useful.
    Many of the
    [examples](../uiswing/layout/spring.html#eg)
    use a `SpringUtilities` class
    that makes it easy to build grids of cells,
    including columns of label-text field pairs.* Updated the following Swing component reference pages to 1.4:
      [lists](../uiswing/components/list.html),
      [panels](../uiswing/components/panel.html),
      [progress bars](../uiswing/components/progress.html),
      [menus](../uiswing/components/menu.html),
      [scroll panes](../uiswing/components/scrollpane.html), and
      [sliders](../uiswing/components/slider.html).
      Added a list of examples to the
      [formatted
      text field](../uiswing/components/formattedtextfield.html#eg) section.* Updated a couple of other Swing reference pages to 1.4:
        borders, icons.* Updated applet tags throughout the tutorial to use `APPLET`
          instead of `OBJECT`/`EMBED`.
          This should make them execute successfully in
          recent versions of Java Plug-in.
          Changed a couple of applets to use `getResourceAsStream`
          instead of `getResource` to load their images —
          this is more efficient for applets using Java Plug-in.* Throughout the Swing examples,
            invoked `setOpaque(true)` on
            `JPanel`s used as content panes,
            to account for the fact that
            panels are no longer opaque by default
            in every look and feel we distribute.
            (GTK+, added in 1.4.2, has transparent panels.)
            Where possible, changed examples that use
            `p = new JPanel(); p.setLayout(l)`
            to use `p = new JPanel(l)`,
            to avoid the unnecessary creation
            of `FlowLayout` objects.* Rewrote and reorganized much of the early part of the
              [Swing components](../uiswing/components/index.html) lesson.
              This included adding two new pages,
              with some new material and some extracted from other pages:
              Using HTML in Swing Components and
              [Using Models](../uiswing/components/model.html).* Miscellaneous fixes to broken links, typos, and the like.

**Year of the Black Sheep (China), 3 February 03** —

* Reorganized and updated Setting the Look and Feel.
  It even has information on the GTK and Windows XP look and feels,
  which will be introduced in 1.4.2.* Added source code for the 1.4 events demos.
    We had released the demos in runnable form soon after our last update,
    but without the source code.* Updated the following pages in the components lesson
      to reflect 1.4 (and make any other improvements we could):
      [JComponent](../uiswing/components/jcomponent.html),
      [button](../uiswing/components/button.html),
      [combo box](../uiswing/components/combobox.html),
      [color chooser](../uiswing/components/colorchooser.html),
      and
      [frame](../uiswing/components/frame.html).* Updated/added examples in the components lesson.
        New demo: FrameDemo2. Added PNG support to FileChooserDemo2.
        Changed ListDemo to not add a person if they already exist.
        Added a text input dialog to DialogDemo.* Fixed the
          [Creating Classes answer page](../java/javaOO/QandE/creating-answers.html)
          to actually contain answers.* Updated our standard headers and footers to be more usable
            by people with disabilities. These changes should be invisible
            to our other readers.* Miscellaneous fixes to broken links, typos, and the like.

**Onion Market Day (Switzerland), 25 November 02** —

* We changed our external links to bring up new, blank windows
  instead of named windows. Although this might result in
  an excess of windows, it should solve the problem of people
  losing the named windows.* We added many 1.4 examples to two of the Swing trail's lessons:
    Using Swing Components and Using Other Swing Features.
    These examples can be launched using
    JavaTM Web Start,
    and the source files now list what other files they need.
    The overall Swing example index
    now points to all versions of the examples for each lesson.* We added a page on
      [key bindings](../uiswing/misc/keybinding.html)
      to the Using Other Swing Features lesson.
      We also updated the
      [action](../uiswing/misc/action.html)
      and
      [accessibility](../uiswing/misc/access.html) pages.* In the [Swing components](../uiswing/components/index.html)
        lesson,
        we changed the order of the pages and updated all the pages
        up through and including buttons.* We're still in the process of updating the
          [Creating a GUI with JFC/Swing](../uiswing/index.html) trail to
          1.4.
          You might notice some changes or notes about changes we plan to make.* We added a Java Web Start page
            to help people install and use that software.* Miscellaneous fixes to broken links and typos.

**Robinson Crusoe's Birthday, 30 September 02** —

* We added a **new lesson!** [Regular Expressions](../essential/regex/index.html)
  covers the `java.util.regex` API introduced in the
  [1.4 release](http://java.sun.com/j2se/1.4/download.html) of the
  JavaTM 2 Platform Standard Edition.
  Regular expressions can be used as a tool to search, edit, or manipulate text or
  data. This package uses Perl-like syntax,
  but our lesson doesn't assume that you've had previous experience with
  regular expressions.* The Tutorial **front page has completely changed**,
    and the
    [java.sun.com](http://download.oracle.com/javase/tutorial/)
    one now looks different from the downloaded one.
    The content of the two pages remains nearly identical.* We added a **search box** to the
      [Tutorial front page.](../index.html)* We retired the **Servlets** trail, since it's out of date
        and other tutorials have updated servlet coverage.
        For links to the newer coverage
        and to a downloadable form of the old trail,
        see the old trailhead.* We added a page of **printing tips**:
          Improving Printing Performance.
          It includes strategies that you can use starting
          in both 1.3 and 1.4.1.* We added a file describing the **license for our code examples**.
            Unless otherwise licensed, all our code is available under this
            license.* Notice is hereby given: We plan to
              **retire the Trail Map**.* We're in the process of updating the
                [Creating a GUI with JFC/Swing](../uiswing/index.html) trail to
                1.4.
                You might notice some changes or notes about changes we plan to make.* Lots of miscellaneous fixes to broken links and typos.

**Magha Puja Day (Thailand), 4 March 02** —

* The [1.4 version of the
  Java 2 Platform Standard Edition](http://java.sun.com/j2se/1.4/download.html) was released recently. We're in the
  process of updating the
  [Creating a GUI with JFC/Swing](../uiswing/index.html) trail to 1.4.
  The [Full-Screen Exclusive Mode API](../extra/fullscreen/index.html)
  covers a brand new API in the 1.4 release; programmers who write games or
  other graphic-intensive applications should read this trail.* Lots of miscellaneous fixes to broken links and typos.

**Underdog Day (World), 19 December 01** — Maintenance Release

* We removed our survey from the Web site. We want to thank everyone for their
  thoughtful responses. Your feedback will help us improve the Tutorial
  and plan for the future.* Lots of miscellaneous fixes to broken links and typos, including updates
    in the [Creating a GUI with JFC/Swing](../uiswing/index.html) trail.

**Chulalongkorn Day (Thailand), 23 October 01** —

* New survey! Please spend a few minutes
  filling out our survey. Your feedback will help us improve the Tutorial
  and plan for the future. We've also included some localization
  questions to help us learn what languages you'd like us to provide
  translations in.* Lots of miscellaneous fixes to broken links and typos.

**Golden Week (Japan), 3 May 01** —

* New lesson!
  User Interfaces that Swing: A Quick Start Guide.
  is a quick start guide to using Swing components to build user interfaces.
  It is built around several progressively complicated examples. (This lesson started life
  as a chapter in our latest book, *The Java Tutorial, Third Edition*.)* Another new lesson! For programmers who write games or other graphic-intensive apps, check out
    the new [Full-Screen Exclusive Mode API](../extra/fullscreen/index.html) lesson.
    This API will be included in the 1.4 release of the Java 2 Standard Edition.* Miscellaneous fixes to broken links and typos.

**Glarius Festival (Switzerland), 1 April 01** —

* Completely updated the
  [I/O: Reading and Writing (but no 'rithmetic)](../essential/io/index.html) lesson.* Reorganized the order of lessons in the [Essential](../essential/index.html) trail.* Miscellaneous fixes to broken links and typos.

**Minor Update, 28 Feb 01** —

* Miscellaneous fixes to broken links and typos.

**Rolling Blackouts Release, 3 Feb 01** —

* Added Questions and Exercises for all trails included in the new book,
  The Java Tutorial Third Edition.* Added new book pages to support the new book,
    The Java Tutorial Third Edition. (The TOC includes a handy set of links
    to all the answers for the Questions & Exercises.)* Updated the
      [Getting Started](../getStarted/index.html) trail.
      We updated the material for 1.3 and added Questions and Exercises.* Updated the
        [Interfaces and Packages](../java/package/index.html) lesson.
        We updated the material for 1.3 and added Questions and Exercises.* Miscellaneous fixes to broken links and typos.

**Edvard Munch's Birthday, 12 Dec 00** —

* Updated the
  [Learning the Java Language trail](../java/index.html).
  We updated the material for 1.3 and added Questions and Exercises
  to the Language Basics section.* Updated the servlets trail
    to refer to the Tomcat 3.x and 4.0 implementations. These releases support
    the 2.2 and 2.3 versions of Java Servlet technology.* The Tomcat version of the Servlets Bookstore Example can now be
      downloaded as a zip file.* Miscellaneous fixes to broken links and typos.

**Friday the 13th, 13 Oct 00** —

* Added information to the IDL trail
  about the idlj compiler,
  which is part of the 1.3 release.
  Updated links to the idlj compiler, its documentation, and the OMG site.* Updated the servlets trail
    to refer to Java Servlet 2.2 API Docs.* Updated the
      Bingo example to fix some thread safety issues.* Updated the API links in most of the basic trails
        to point to the 1.3 versions (instead of 1.2).* Miscellaneous fixes to broken links and typos.

**Tutorial Fifth Anniversary, 31 May 00** —

* Added Werner van Mook's Mac adaptation of the
  instructions for writing and compiling your first programs:
  First Cup of Java (Mac OS).* Added questions and exercises to the end of the
    [Getting Started](../getStarted/index.html) trail
    and to the first three lessons in the
    [Learning the Java Language](../java/index.html) trail.* Rewrote portions of the first lessons in the
      Learning the Java Language trail.* Miscellaneous fixes to broken links and typos.

**Zeppo Marx's Birthday (1901), 25 February 00** —

* Did reconstructive work on the Learning the Java Language trail.
  Lots of new examples added. Cleaned up.* Fixed a subtle bug in SwingWorker source code.
    See How to Use Threads in the Swing trail.* Adjusted JTable page, examples to reflect 1.3.
      See [How to Use Tables](../uiswing/components/table.html)
      in the Swing trail.* Miscellaneous fixes to broken links and typos.

**Thanksgiving (USA), 24 November 99** —

* Added a new lesson to the JavaBeans(tm) trail,
  [Using the BeanContext API](../javabeans/beancontext/index.html),
  that covers The Extensible Runtime Containment and Services Protocol.* Added some information about JTable in 1.3 in the Swing trail.
    Also, added a new 1.3 JTable example.* Began updating and rewriting the Learning the Java Language trail.
      This work includes adding exercises and questions to each section.* Added the [glossary](glossary.html)
        from the java.sun.com website and began linking
        terms to it.* Did a partial conversion to our new icon scheme for identifying
          the target of our links.
          + ![](../images/glossaryIcon.gif)
            looks up a glossary term+ ![](../images/sourceIcon.gif)
              links to a `.java` file+ ![](../images/apiIcon.gif)
                link to a page within the javadocs hosted at java.sun.com+ ![](../images/otherIcon.gif)
                  links to a page outside of the tutorial+ ![](../images/tutorialIcon.gif)
                    links to a page in a different lesson within the tutorialIntra-tutorial links (black) update the page in the current browser window,
          while extra-tutorial links (colored links) bring up a new browser window.

**Vegetarian Day (World), 1 October 99** —

* Removed the survey. Thank you for your responses.* Added a [really big index](../reallybigindex.html)
    that lists every content page in the tutorial in order.* Added a resources page
      that lists Java programming resources outside of the tutorial.* Added [Your First Cup of Java (for UNIX)](../getStarted/cupojava/unix.html).* Added [feedback form](http://developers.sun.com/contact/tutorial_feedback.jsp).
          Please use this form to contact us instead of sending mail directly.
          It will help direct your mail to the right person.* Modified our tools to provide automatic next and previous links,
            automatic page titles, and automatic page headers and footers.
            This change should be largely unnoticeable to readers except that
            these page elements should contain fewer errors and inconsistencies.* Created a tool that automatically generated trail-level TOC pages.
              This change should be largely unnoticeable to readers except that
              these pages should contain fewer errors and inconsistencies.* Fixed various broken links, typographical, and other errors.* Put all of the images on the Swing Components Visual Index.* Updated API links to point to Java 2 SDK docs.* Thanks to our two delightful summer interns, Ray and Indra,
                      we were able to do a lot of clean up including fixing omissions,
                      making clarifications, adding examples, and so on.* We did a pass and cleaned up most of the pending issues.
                        The only remaining pendings are in the BINGO lesson,
                        which has not been completed,
                        and in one of the book pages for the Second Edition.
                        We hope, but do not promise, to clean up the remaining ones
                        for the next tutorial update.

**National Smile Week :), 3 August 99** —

* Added the 2D applets to the list of applets
  page, for a total of 77 applets in the Tutorial.
  Also, provided Java Plug-in tags for running the 2D applets.* Added [detailed instructions](../getStarted/cupojava/index.html)
    for compiling and running a Java program in Windows.* Posted a survey.* Created a tutorial announcements mailing list to which tutorial
        readers can subscribe.* Added common problems pages to some trails that didn't have them.* Clarified and fixed various errors reported by readers.

**Fiesta de San Fermin (Spain), 7 July 99** —

* Fixed most of the pending issues in the Swing trail.
  Fixed a few pending issues in other trails.* Fixed some problems with one example in the security trail.* Made some minor modifications to the page format
      and did some clean up on our tools.
      This has minor repercussions for API links.* Cleaned up the image directories and removed unused images.
        This reduced the size of the tutorial by about 1.5 Meg.* Added coverage of JSDK 2.1 in the servlets trail.* Modified our coverage of finalization in the
            Java language trail and in effected examples.* Fixed typos, broken links, a couple of broken applets,
              and other reader reported problems.* Updated the instructions for running the BINGO program.* Became a mirror for WinHelp version of tutorial.

**Memorial Day (USA), 28 May 99** —

* Announced the Swing book.* Due to overwhelming reader feedback,
    we changed our format again.
    We removed the left-hand border and modified the headers
    and footers to include a link to the search page.* Fixed typos and other errors in the Learning Java,
      Essential Classes, and Custom Networking
      trails in response to reader e-mail.

**Lei Day (Hawaii) update, 5 May 99** —
We made some changes to our new page format in resonse to reader feedback.

* Because of reader feedback, we added
  a navigation area to the bottom of each page.* Implemented a max width of 460 for images to prevent
    large images from creating a page that is too wide.

**Lei Day (Hawaii), 1 May 99** —

* Modified our page format. It now includes
  search on every content page.* Created examples indexes for all examples in the Swing trail.
    If readers like it, we plan to do this for all trails.* Reviewed the code for all example programs in the Swing trail.* Did a final pass in preparation for converting from HTML to
        book format. This included everything from fixing typos to
        tweaking comments in source files to adding a few paragraphs
        of new information.* Added a second custom layout manager example: GraphPaperLayout.* Added new examples and content to the 2d trail.

**World Culture Day, 12 March 99** —
We marched through the Swing trail preparing for copyedit.
Here's what we did:

* Internally reviewed and edited all .html pages in the Swing trail
  in the first 7 lessons. In some cases, this amounted to a major
  rewrite.* Added \*a lot\* of material to the component how-to pages
    that covers aspects of the components that had previously been omitted.
    Typically, the additional material covers more advanced component
    features.* Reviewed example code, ran all examples,
      and modified as appropriate.* Researched and resolved many pending issues. (Some still remain.)* Performed "example audits" and updated the tables of examples.* Reviewed and updated API tables everywhere.* Fixed various bugs and clarity issues reported by readers.* Filled in "glue" pages.* Added information about common problems in many places.* Tied sections together better by adding links.* Made the layout and events sections similar to how-to
                      pages by adding API and examples tables.

**Joe's 40th Birthday, 21 Jan 99**

* Updated the drawing lesson to Swing.* Made various improvements to the Swing trail.* Some front page cleanup.

**Winter Solstice, 21 Dec 98**

* **Added Search Capability**!* Added preliminary draft of Converting to Swing lesson.* Added links to resources and examples for Drag 'n Drop.* Some image clean up, which shrunk the tutorial by about .75 Megs.* Made various improvements to the Swing trail,* Fixed various broken link and typos.

**Enlightenment of the Buddha (Japan), 8 Dec 98**

* Minor typo and broken link fixes.* Getting first two lessons in Swing trail ready for copyedit.* Removed all .class files from tutorial except those necessary
      for running applets. This shrank the tutorial by 1.5 Megs.

**Day of the Artisans (Mexico), 4 Dec 98**

* **Note**: CD-ROM build.
  This is the version of the tutorial
  that appears on the CD-ROM for
  **The Java Tutorial *Continued***.* Integrated all copyedits and other changes from the
    continued book into 5 trails:
    overview, internationalization,
    sound, 2D, and RMI.* Made lots of little improvements to the Swing trail,
      especially in swingOverview and swingStart.
      Reorganized material about text.* Updated programs to use Swing 1.1
        (from Swing 1.0.3 and Swing 1.1 Beta 3)
        and JDK 1.2.

**Aron's Birthday, 6 Nov 98**

* Substantially reorganized the
  **Creating a GUI with JFC/Swing** trail.
  The Swing-based User Interface trail replaces
  the old AWT-based User Interface trail,
  which is available only by download.
  We still have some work to do to complete the transition.
  Please bear with us during construction!* Miscellaneous fixes to typos, broken links, and program bugs.

**Universal Children's Day, 5 Oct 98**

* Converted the examples and text in
  **Laying Out Components within a Container**
  to use Swing.* Several updates to the **Using Swing Components** lesson.* Converted many applets to use Java Plug-in.* Updated to JDK 1.1.7 and Swing 1.1 Beta 3.* Converted old UI trail to a downloadable archive.* Removed reference objects trail.* Miscellaneous fixes to typos, broken links, and program bugs.

**Labor Day Release, 7 Sept 98**

* Added **Overview of the JDK**.* Added **Java Sound** trail.* Added **Working with Java 2D Graphics** trail.* Added **JDBC Database Access** trail.* Added **Using Java RMI** trail.* Reviewed and edited **Programming with Java IDL** trail.* Added new material and examples to the
              **Using Swing Components**
              lesson.

**Laine's Birthday Release, An Update, 14 Aug 98**

* Added **Programming with Java IDL** trail.* Added **Security in JDK 1.2** trail.* Reviewed and edited various trails and lesson.* Added new material and examples to the
        **Using Swing Components**
        lesson.* Fixed miscellaneous typos and broken links.
          Made minor improvements to text and examples all over the place.

**Laine's Birthday Release, 3 Aug 98**

* Added **Collections** trail.* Added **Servlets** trail.* Added **The Java Extensions Mechanism** trail.* Added Reference Objects trail.* Added new material and examples to the
          **Using Swing Components**
          lesson.
          Completed technical reviews for many pages and integrated
          engineering feedback.* Reviewed and edited
            **javabeans** and
            **jar** trails.* Fixed miscellaneous typos and broken links.
              Made minor improvements to text and examples all over the place.

**The Summer Solstice Release, 26 June 98**

* Added a lot of new material and examples to the
  **Using Swing Components**
  lesson.* Updated information about
    **`hashCode` and
    `equals`**.* Added a **bios** page that contains
      information about our contributing authors.* Reviewed and edited
        **internationalization**,
        **reflection**, and
        **native** trails.* Fixed miscellaneous typos and broken links.
          Improved some text and some examples.

**Nettle Day (UK), 29 May 98**

* Added **JAR** trail.* Added 4 new topics to the internationalization trail:
    **comparing strings**,
    **text boundaries**,
    **conversions**, and a
    **checklist for
    internationalizing existing programs**.* Added demo programs to the date and number formatting lessons.* Reorganized **JavaBeans** trail.* Added a lot of new material and examples to the
          **Using Swing Components**
          lesson.* Reviewed **native methods**
            trail and made associated changes and fixes.* Fixed miscellaneous typos and broken links.
              Improved some text and some examples.

**Arbor Day, 24 April 98**

* WooHoo! New **front page**!
  New **Trail map**!* New look for trail-level TOC.html files.
    Also, removed lesson-level TOC.html files. Instead
    we now provide a link to the appropriate place within
    the trail-level TOC.html files.* Continued to add new pages to the
      **Using Swing Components**
      lesson.* Added a new lesson to the internationalizaton trail
        covering **formatting**.* Added trail on **reflection**.* Added some information to the
            **native methods** trail for
            Mac programmers.* Fixed typos, broken links,
              and various other minor problems with content* Removed the old internationalization trail.* Removed old native methods trail...provide a
                  **downloadable archive** instead.* Updated **errata page**
                    for second edition of the book.

**The Vernal Equinox, 20 March 98**

* Changed the background color to white.* Finished integrating figures from the new, second, edition of the book.
    Figures and images are now kept together at the top-level instead of
    sprinkled throughout the lesson directories.* Added **book.html**
      and related pages for the second editon of the book.
      Changed the page design of the **book.html**
      and related pages for the first edition to match the second edition.* Did a bunch of work behind the scenes on our tools and processes.
        This is the first update of the tutorial from our new workspace
        with our new makefiles and build process.* Because of our lovely new tools, we can now easily
          provide a downloadable archive of all of the examples
          in the book.
          See **Download the Tutorial**
          for the `ftp` links.* Fixed various typos and other minor problems with content.* Updated the
              **Swing**
              material relating to the JDK 1.2.

**Saturnalia, 22 December 97**
> ***The long awaited update!*** —
> this is a *major* update of the tutorial.
> Almost every file has been touched in some way.
>
> This release of the online tutorial corresponds with the
> release of the 2nd edition of *The Java Tutorial* book
> and is the version of the online tutorial that appears on
> the CD-ROM that accompanies that book.
>
> The changes are in progress, but to a large extent
> we have integrated 1.1 information into
> the existing trails, lessons, and examples. This is
> in sharp contrast to the 1.1 notes that were littered
> throughout the previous version of the tutorial and
> were, admittedly, somewhat confusing.
>
> Also, we are in the process of integrating copyedit and
> other changes made to the book version, into the online version.
> This has been completed thoroughly in some areas of the online
> tutorial, and spottily in other areas. We will continue
> with this process throughout the coming months.
>
> New lessons in this tutorial that first appeared in print
> in the 2nd edition of *The Java Tutorial* book:
>
> * **The Java Phenomenon*** **Migrating to 1.1*** **A Preview of Things to Come**
>
> New trails for this version of the tutorial
> that haven't yet made it to print:
>
> * Added a **Putting It All Together** trail
>   that provides a large, real-world, client/server example and analyzes it.* Got a totally new **JavaBeans Tutorial**
>     by Andy Quinn!

**8 July 97**

* One of the goals of the tutorial is to document the latest and greatest
  from JavaSoft *as it is released*.
  To this end, we've added a lesson about
  **Using Swing Components**.
  The Swing release is an early release of part of the JFC.
  This information is only available from the Java Tutorial.* Added a trail, **Java Security 1.1**,
    covering the new 1.1 security APIs.* Updated the The JavaBeans(tm) Tutorial by Greg Voss.* Promoted **Writing Global Programs** to
        a trail. This trail is still in progress, but it contains new material
        including several excellent demos from
        **Taligent**.* Added information about the 1.1 release in our
          **To 1.1 — And Beyond!** trail.* Made the usual fixes to broken links, typos, and other errata.

**14 May 97**
> We improved and added more 1.1 information in existing sections.
> We added more examples of and information about
> the various types of event listeners to
> **Handling Events**.
> We also fixed the AroundTheWorld applet used in
> **Writing Global Programs.**

**28 April 97**
> We added a new trail,
> **To 1.1 — And Beyond!**,
> which is the headquarters for features added to the JDK after 1.0.
> Also, the **Learning the Java Language**
> and **Essential Java Classes** trails
> now have notes that point out material that is affected by 1.1.
> And finally, we reorganized our top-level files to make them more
> accessible.

**3 March 97**
> Added a brand new trail introducing JavaBeans!
> This trail, JavaBeans Tutorial, written by Greg Voss,
> shows you the ins and outs of developing programs
> using the JavaBeans technology.

**19 February 97**

* Our new "guest author" program debuts in this release of the tutorial
  with a completely new trail about
  writing native methods by Beth Stearns. Check it out:
  **Using the Java Native Interface (JNI)**.* Merged copyediting changes from the book into the on-line version in
    these two trails:
    **Getting Started** and
    **Writing Applets**.* Updated
      **Writing Global Programs**
      to work with the FCS JDK 1.1 release.* The usual miscellaneous fixes.

**24 December 96**
> Miscellaneous fixes.
> Also, added a new lesson describing new features of the JDK for
> **Writing Global Programs**.

**6 June 96** — Released the Sixth DRAFT.
> This draft is the version on which the book version is based.
> The book and online versions aren't exactly the same —
> for example, none of the copyeditor's changes
> have made it into the online tutorial yet.
> Also, the online tutorial's figures haven't been updated
> to be the same as those in the book.
> Notable content changes since the fifth draft include:
>
> * Finished the Common Problems pages.* Added information on the Macintosh JDK.* Added an applet anatomy section to Getting Started.* Improved the talk server example in the applet communication lesson.

**28 Mar 96** — Released the Fifth DRAFT.
> Many pages in this draft have been rewritten
> or expanded upon.
> (If you've sent us comments and don't see them reflected in this draft,
> please don't be insulted —
> we haven't finished incorporating reviewer comments.)
> Some of the notable changes include:
>
> * Revised Application Anatomy lesson
>   and moved it to the Getting Started trail:
>   **The Anatomy of a Java Application**.
>   We plan to write an equivalent section
>   for applets.* Did major rewrites of the following lessons in the Java trail:
>     **The Nuts and Bolts of the Java
>     Language** and
>     **Objects and Classes in Java**.* Added new pages to the applet overview:
>       Adding an Applet to an HTML Page
>       and
>       **Summary**.* Beefed up the applet threads pages:
>         **Threads in Applets**.* Added a discussion of peers to the UI trail:
>           **Details of the Component Architecture**.* Added material to the native methods trail,
>             **Integrating Native Methods into Java Programs**,
>             including passing data into and out of native methods
>             and accessing Java objects.* Removed some trails: comparison to C/C++, troubleshooting, and tools.
>               This information has been (or will be) incorporated into other
>               trails/lessons.

**4 Mar 96** — Released the Fourth DRAFT
> Among the normal bug, typo and broken link fixes, this draft includes
> revisions to many of our old trails and lessons, plus this new material:
>
> * Added a new lesson to
>   **Integrating Native Methods into Java Programs**
>   trail.* Added new material to and/or wrote from scratch 4 lessons in the
>     **Writing Applets**
>     trail. Including:
>     **Creating an Applet User Interface**,
>     **Communicating with Other Programs**,
>     **Understanding Applet Capabilities and Restrictions**,
>     and
>     **Finishing an Applet**.
>     (The first three have since been reorganized into two trails:
>     **Taking Advantage of the Applet API**
>     and
>     **Practical Considerations when Writing Applets**.

**24 Feb 96** — Released the Third DRAFT
> Among the normal bug, typo and broken link fixes, this draft includes
> revisions to many of our old trails and lessons, plus this new material:
>
> * Added a lot of new material to
>   Creating an Applet User Interface.* Added new lessons to the
>     **Creating a User Interface**
>     trail. Including:
>     + **Laying Out Components within a Container**
>       Please note that 3 pages are still under construction.+ **Using Components, the GUI Building Blocks**
>         Each component now has a page describing how to use it.+ **Working with Graphics**
>           There's now information on how to draw primitive graphics (including text)
>           and images, plus information on performing animation. The animation pages
>           include information on how to eliminate flashing, using update() and double
>           buffering. They also have information on using MediaTracker.* Added a new trail:
>       **Custom Networking*** Added a new lesson,
>         **Input and Output Streams**
>         to the
>         **Essential Java Classes** trail.

**23 Jan 96** — Updated the Second DRAFT

* Updated links to point to new FCS1.0 JDK release.* Fixed bugs where some applets and sources files were missing.* Miscellaneous fixes of typos, bugs, and broken links.

**18 Jan 96** — Updated the Second DRAFT

* Changed the **Creating a User
  Interface**
  trail to reflect the event changes introduced in Beta2.
  Specifically, keyboard event handlers now have to return false,
  unless they want the event to be dropped.
  The Conversion example program and the overview were affected.* Revised the structure of the tutorial
    to reflect what we're going to be able to finish
    by the time the book version is due to the printer.* Added a very preliminary lesson on Java's object features —
      **Java Objects**.* Fixed various typos, bugs and broken links.

**12 Dec 95** — Updated the Second DRAFT

* Made the few changes necessary to reflect Beta2 instead of Beta.* Fixed various typos, bugs and broken links.* Added a new lesson,
      **Handling Errors using Exceptions**, in the
      **Essential Java Classes**
      trail.

**13 Nov 95** — Updated the Second DRAFT

* Made the few changes necessary to reflect Beta instead of Pre-Beta.* Changed the name of this document from
    "The Java Programmer's Guide" to
    "The Java Language Tutorial: Object-Oriented Programming for the Internet."
    Why the long name?
    This document is going to be published as a book,
    and we wanted to make sure the title
    was as descriptive as possible,
    without requiring much prior knowledge of the potential buyer.* Added ALT text to our link graphics,
      so that people using non-graphical browsers
      can understand the information the graphic was conveying.* Added a new lesson,
        **Laying Out Components Within a Container**, in the
        **Creating a User Interface**
        trail.

**2 Oct 95** — Released the Second DRAFT

* Everything was updated to reflect the new APIs (except for *The "run:"
  Protocol Handler* and *The "text/plain" Content Handler*
  in the **Getting Started**
  trail).* We fixed many typos, clarified many obfuscations, fixed
    broken links and miscommunications.* We got a face-lift with new icons and a new page design.* And, we added these trails and lessons:
        + The
          **Writing Applets**
          trail has a new lesson:
          **Overview of Applets**
          which describes
          how applets work and how you use the Applet class to create an applet.+ The new
            **Creating a User Interface**
            trail has two new lessons:
            **Overview of UI Elements** which
            introduces you to the objects that the Java development environment
            provides for building UIs, and
            **Laying Out Components within a Container**
            which tells you how to use each of the Components provided in the AWT.+ We've also added the
              **Integrating Native Methods into Java Programs**
              trail that shows you how to integrate native methods
              into your Java programs.+ And finally, we've added two new lessons:
                **Threads of Control**
                and
                **Object-Oriented Programming Concepts**.

**18 May 95**
> Released the First DRAFT