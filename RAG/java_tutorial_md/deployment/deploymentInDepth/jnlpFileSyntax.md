[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Deployment In-Depth
  
**Section:** Java Network Launch Protocol

[Deployment In-Depth](index.html)

[Deployment Toolkit](depltoolkit_index.html)

[Deploying an Applet](runAppletFunction.html)

[Customizing the Loading Screen](customizeLoadingScreen.html)

[Deploying a Java Web Start Application](createWebStartLaunchButtonFunction.html)

[Changing the Launch Button](changeLaunchButtonOfJWS.html)

[Checking the Client JRE Software Version](jreVersionCheck.html)

[Java Network Launch Protocol](jnlp.html)

Structure of the JNLP File

[Deployment Best Practices](bestPractices.html)

[Reducing the Download Time](reducingDownloadTime.html)

[Avoiding Unnecessary Update Checks](avoidingUnnecessaryUpdateChecks.html)

[Signing JAR Files Only When Necessary](signing.html)

[Ensuring the Presence of the JRE Software](ensuringJRE.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Deployment In-Depth](index.html)

[« Previous](jnlp.html) • [Trail](../TOC.html) • [Next »](bestPractices.html)

# Structure of the JNLP File

This topic describes the syntax of the Java Network Launch Protocol
(JNLP) file for rich Internet applications (RIAs).

The following code snippet shows a sample
JNLP file for a Java Web Start application:

```

<?xml version="1.0" encoding="UTF-8"?>
<jnlp spec="1.0+" codebase="" href="">
    <information>
        <title>Dynamic Tree Demo</title>
        <vendor>Dynamic Team</vendor>
        <icon href="sometree-icon.jpg"/>
        <offline-allowed/>
    </information>
    <resources>
        <!-- Application Resources -->
        <j2se version="1.6+"
              href="http://java.sun.com/products/autodl/j2se"/>
        <jar href="DynamicTreeDemo.jar" main="true" />

    </resources>
    <application-desc
         name="Dynamic Tree Demo Application"
         main-class="webstartComponentArch.DynamicTreeApplication"
         width="300"
         height="300">
     </application-desc>
     <update check="background"/>
</jnlp>

```

The following table describes the elements and attributes commonly used in JNLP files.
Click the parent link to view an element's parent.

---

**Note:** This table does not include all possible contents of the JNLP file. For more information, see the
[Java Network Launching Protocol and API Specification](http://java.sun.com/javase/technologies/desktop/javawebstart/download-spec.html).

---

**Commonly Used Elements and Attributes in a JNLP file**

    | Element | Attributes | Description | Since | Required |
| --- | --- | --- | --- | --- |
| jnlp |  | The topmost xml element for a JNLP file. | 1.0 | Yes |
|  | spec | Value of the attribute can be 1.0, 1.5, or 6.0, or can use wildcards such as 1.0+. It denotes the minimum version of the JNLP Specification that this JNLP file can work with. | 1.0 |  |
|  | codebase | The base location for all relative URLs specified in `href` attributes in the JNLP file. | 1.0 |  |
|  | href | The URL of the JNLP file itself. | 1.0 |  |
|  | version | The version of the RIA being launched, as well as the version of the JNLP file itself. | 1.0 |  |
| information [parent](#jnlp) |  | Contains other elements that describe the RIA and its source. | 1.0 | Yes |
|  | os | The operating system for which this information element should be considered. | 1.5.0 |  |
|  | arch | The architecture for which this information element should be considered. | 1.5.0 |  |
|  | platform | The platform for which this information element should be considered. | 1.5.0 |  |
|  | locale | The locale for which this information element should be considered. | 1.5.0 |  |
| title [parent](#information) |  | The title of the RIA. | 1.0 | Yes |
| vendor [parent](#information) |  | The provider of the RIA. | 1.0 | Yes |
| homepage [parent](#information) |  | The homepage of the RIA. | 1.0 |  |
|  | href | A URL pointing to where more information about this RIA can be found. | 1.0 | Yes |
| description [parent](#information) |  | A short statement describing the RIA. | 1.0 |  |
|  | kind | An indicator as to the type of description. Legal values are one-line, short, and tooltip. | 1.0 |  |
| icon [parent](#information) |  | An icon that can be used to identify the RIA to the user. | 1.0 |  |
|  | href | A URL pointing to the icon file. Can be in one of the following formats: gif, jpg, png, ico. | 1.0 | Yes |
|  | kind | Indicates the suggested use of the icon, can be: default, selected, disabled, rollover, splash, or shortcut. | 1.0 |  |
|  | width | Can be used to indicate the resolution of the image. | 1.0 |  |
|  | height | Can be used to indicate the resolution of the image. | 1.0 |  |
|  | depth | Can be used to indicate the resolution of the image. | 1.0 |  |
| offline-allowed [parent](#information) |  | Indicates that this RIA can operate when the client system is disconnected from the network. | 1.0 |  |
| shortcut [parent](#information) |  | Can be used to indicate the RIA's preferences for desktop integration. | 1.5.0 |  |
|  | online | Can be used to describe the RIA's preference for creating a shortcut to run online or offline. | 1.5.0 |  |
| desktop [parent](#information) |  | Can be used to indicate the RIA's preference for putting a shortcut on the user's desktop. | 1.5.0 |  |
| menu [parent](#information) |  | Can be used to indicate the RIA's preference for putting a menu item in the user's start menus. | 1.5.0 |  |
|  | sub-menu | Can be used to indicate the RIA's preference for where to place the menu item. | 1.5.0 |  |
| association [parent](#information) |  | Can be used to hint to the JNLP client that the RIA wants to be registered with the operating system as the primary handler of certain extensions and a certain mime-type. | 1.5.0 |  |
|  | extensions | A list of file extensions (separated by spaces) that the RIA requests it be registered to handle. | 1.5.0 |  |
|  | mime-type | The mime-type that the RIA requests it be registered to handle. | 1.5.0 |  |
| related-content [parent](#information) |  | An additional piece of related content that can be integrated with the RIA. | 1.5.0 |  |
|  | href | A URL pointing to the related content. | 1.5.0 | Yes |
| update [parent](#jnlp) |  | The preferences for how RIA updates should be handled by the JNLP client. | 1.6.0 |  |
|  | check | The preference for when the JNLP client should check for updates. Value can be always, timeout, or background.. | 1.6.0 |  |
|  | policy | The preference for how the JNLP client should handle a RIA update when a new version is available before the RIA is launched. Values can be always, prompt-update, or prompt-run. | 1.6.0 |  |
|  |  |  | 1.0 |  |
| security [parent](#jnlp) |  | Can be used to request enhanced permissions. | 1.0 |  |
| all-permissions [parent](#security) |  | Requests that the RIA be run with all permissions. | 1.0 |  |
| j2ee-application-client-permissions [parent](#security) |  | Requests that the RIA be run with a permission set that meets the security specifications of the J2EE application client environment. | 1.0 |  |
| resources [parent](#jnlp) |  | Describes all the resources that are needed for the RIA. | 1.0 | Yes |
|  | os | The operating system for which the resources element should be considered. | 1.0 |  |
|  | arch | The architecture for which the resources element should be considered. | 1.0 |  |
|  | locale | The locales for which the resources element should be considered. |  |  |
| java or j2se [parent](#resources) |  | Versions of Java software to run the RIA with. | 1.6.0 (java) |  |
|  | version | Ordered list of version ranges to use. | 1.0 | Yes |
|  | href | The URL denoting the supplier of this version of Java software, and from where it can be downloaded. | 1.0 |  |
|  | java-vm-args | An additional set of standard and non-standard virtual machine arguments that the RIA would prefer the JNLP client use when launching the JRE software. | 1.0 |  |
|  | initial-heap-size | The initial size of the Java heap. | 1.0 |  |
|  | max-heap-size | The maximum size of the Java heap. | 1.0 |  |
| jar [parent](#resources) |  | A JAR file that is part of the RIA's classpath. | 1.0 | Yes |
|  | href | The URL of the JAR file. | 1.0 | Yes |
|  | version | The requested version of the JAR file. Requires using the version-based download protocol | 1.0 |  |
|  | main | Indicates if this JAR file contains the class containing the `main` method of the RIA. | 1.0 |  |
|  | download | Indicates that this JAR file can be downloaded lazily, or when needed. | 1.0 |  |
|  | size | The downloadable size of the JAR file in bytes. | 1.0 |  |
|  | part | Can be used to group resources together so that they are downloaded at the same time. | 1.0 |  |
| nativelib [parent](#resources) |  | A JAR file that contains native libraries in its root directory. | 1.0 |  |
|  | href | The URL of the JAR file. | 1.0 | Yes |
|  | version | The requested version of the JAR file. Requires using the version-based download protocol | 1.0 |  |
|  | download | Can be used to indicate this JAR file can be downloaded lazily. | 1.0 |  |
|  | size | The downloadable size of the JAR file in bytes. | 1.0 |  |
|  | part | Can be used to group resources together so they will be downloaded at the same time. | 1.0 |  |
| extension [parent](#resources) |  | A pointer to an additional component-desc or installer-desc to be used with this RIA. | 1.0 |  |
|  | href | The URL to the additional extension JNLP file. | 1.0 | Yes |
|  | version | The version of the additional extension JNLP file. | 1.0 |  |
|  | name | The name of the additional extension JNLP file | 1.0 |  |
| ext-download [parent](#extension) |  | Can be used in an extension element to denote the parts contained in a component-extension. | 1.0 |  |
|  | ext-part | The name of a part that can be expected to be found in the extension. | 1.0 | Yes |
|  | download | Can be used to indicate this extension can be downloaded eagerly or lazily. | 1.0 |  |
|  | part | Denotes the name of a part in this JNLP file in which to include the extension. | 1.0 |  |
| package [parent](#resources) |  | Can be used to indicate to the JNLP client which packages are implemented in which JAR files. | 1.0 |  |
|  | name | Package name contained in the JAR files of the given part. | 1.0 | Yes |
|  | part | Part name containing the JAR files that include the given package name. | 1.0 | Yes |
|  | recursive | Can be used to indicate that all package names, beginning with the given name, can be found in the given part. | 1.0 |  |
| property [parent](#resources) |  | Defines a system property that will be available through the `System.getProperty` and `System.getProperties` methods. | 1.0 |  |
|  | name | Name of the system property. | 1.0 | Yes |
|  | value | Value of the system property. | 1.0 | Yes |
|  |  | Note: A JNLP file must contain one of the following: application-desc, applet-desc, component-desc, or installer-desc. | 1.0 | Yes |
| application-desc [parent](#jnlp) |  | Denotes this is the JNLP file for an application. | 1.0 |  |
|  | main-class | The name of the class containing the `public static void main(String[])` method of the application. | 1.0 | Yes |
| argument [parent](#applicationdesc) |  | Each argument contains (in order) an additional argument to be passed to the `main` method. | 1.0 |  |
| applet-desc [parent](#jnlp) |  | Denotes this is the JNLP file for an applet. | 1.0 |  |
|  | main-class | The name of the main applet class. | 1.0 | Yes |
|  | documentbase | The document base for the applet as a URL. | 1.0 |  |
|  | name | Name of the applet. | 1.0 | Yes |
|  | width | The width of the applet in pixels. | 1.0 | Yes |
|  | height | The height of the applet in pixels. | 1.0 | Yes |
| param [parent](#appletdesc) |  | A set of parameters that can be passed to the applet. | 1.0 |  |
|  | name | The name of this parameter. | 1.0 | Yes |
|  | value | The value of this parameter. | 1.0 | Yes |
| component-desc [parent](#jnlp) |  | Denotes this is the JNLP file for a component extension. | 1.0 |  |
| installer-desc [parent](#jnlp) |  | Denotes this is the JNLP file for an installed extension. | 1.0 |  |
|  | main-class | The name of the class containing the `public static void main(String[])` method of the installer. | 1.0 | Yes |

#### Encoding JNLP Files

Java Web Start software supports encoding of JNLP files in any character
encoding supported by the Java platform.
For more information about character encoding in the Java platform, see the
[Supported Encodings Guide](http://java.sun.com/javase/6/docs/technotes/guides/intl/encoding.doc.html).
To encode a JNLP file, specify an encoding in the XML prolog of that file.
For example, the following line indicates that the JNLP file is encoded in UTF-16.

```

<?xml version="1.0" encoding="utf-16"?>

```

---

**Note:** The XML prolog itself must be UTF-8-encoded.

---

[« Previous](jnlp.html)
•
[Trail](../TOC.html)
•
[Next »](bestPractices.html)

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

**Previous page:** Java Network Launch Protocol
  
**Next page:** Deployment Best Practices




A browser with JavaScript enabled is required for this page to operate properly.