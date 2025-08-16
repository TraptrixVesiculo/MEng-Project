[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Extension Mechanism
  
**Lesson:** Creating and Using Extensions

[Creating and Using Extensions](index.html)

[Installed Extensions](install.html)

[Download Extensions](download.html)

Understanding Extension Class Loading

[Home Page](../../index.html)
>
[The Extension Mechanism](../index.html)
>
[Creating and Using Extensions](index.html)

[« Previous](download.html) • [Trail](../TOC.html) • [Next »](../security/index.html)

# Understanding Extension Class Loading

The extension framework makes use of the class-loading delegation mechanism.
When the runtime environment needs to load a new class
for an application, it looks for the
class in the following locations, in order:

1. **Bootstrap classes**: the runtime classes in
   rt.jar, internationalization classes in i18n.jar,
   and others.
2. **Installed extensions**: classes in JAR files in the
   lib/ext directory of the JRE,
   and in the system-wide, platform-specific extension directory
   (such as /usr/jdk/packages/lib/ext
   on the SolarisTM Operating System,
   but note that use of this directory applies only to
   JavaTM 6 and later).
3. **The class path**: classes,
   including classes in JAR files, on paths specified by the
   system property java.class.path. If a JAR file on the class path has
   a manifest with the `Class-Path` attribute,
   JAR files specified by the `Class-Path` attribute
   will be searched also.
   By default, the `java.class.path` property's value
   is `.`, the current directory.
   You can change the value by using the
   -classpath or -cp command-line options, or
   setting the `CLASSPATH` environment variable.
   The
   command-line options override the setting of the `CLASSPATH`
   environment variable.

The precedence list tells you, for example, that the class path is
searched only if a class to be loaded hasn't been found among the
classes in rt.jar, i18n.jar or the installed extensions.

Unless your software instantiates its own class loaders for
special purposes, you don't really need to know much more than to
keep this precedence list in mind. In particular, you should be
aware of any class name conflicts that might be present. For example,
if you list a class on the class path, you'll get unexpected
results if the runtime environment instead loads another class
of the same name that it found in an installed extension.

### The Java Class Loading Mechanism

> The Java platform uses a delegation model for
> loading classes. The basic idea is that every class loader has a
> "parent" class loader. When loading a class, a class loader first
> "delegates" the search for the class to its parent class loader before
> attempting to find the class itself.
>
> Here are some highlights of the class-loading API:
>
> * Constructors in java.lang.ClassLoader and its subclasses
>   allow you to specify a parent when you instantiate a new class loader.
>   If you don't explicitly specify a parent, the virtual machine's system
>   class loader will be assigned as the default parent.* The loadClass method in ClassLoader performs
>     these tasks, in order, when called to load a class:
>     1. If a class has already been loaded, it returns it.* Otherwise, it delegates the search for the new class
>          to the parent class loader.* If the parent class loader does not find the class,
>            loadClass calls the method findClass
>            to find and load the class.* The findClass method of ClassLoader searches
>       for the class in the current class loader if the class wasn't found by
>       the parent class loader. You will probably want to override this method
>       when you instantiate a class loader subclass in your application.* The class java.net.URLClassLoader
>         serves as the basic class loader for extensions
>         and other JAR files, overriding the findClass method of
>         java.lang.ClassLoader to search one or more specified URLs for
>         classes and resources.
>
> To see a sample application that uses some of the API as it
> relates to JAR files, see the
> [Using JAR-related APIs](../../deployment/jar/apiindex.html) lesson in this tutorial.

### Class Loading and the java Command

> The Java platform's class-loading mechanism
> is reflected in the java command.
>
> * In the java tool, the
>   -classpath option is a shorthand way to set the
>   java.class.path property.
> * The
>   -cp and -classpath options are equivalent.
> * The -jar option runs applications
>   that are packaged in JAR files. For a description and examples of
>   this option, see the
>   [Running JAR-Packaged Software](../../deployment/jar/run.html) lesson in this tutorial.

[« Previous](download.html)
•
[Trail](../TOC.html)
•
[Next »](../security/index.html)

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

**Previous page:** Download Extensions
  
**Next page:** Making Extensions Secure




A browser with JavaScript enabled is required for this page to operate properly.