[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applications

[Quick Tour of Controlling Applications](index.html)

[Observe Application Freedom](step1.html)

[See How to Restrict Applications](step2.html)

[Set up the Policy File to Grant the Required Permissions](step3.html)

[Open the Policy File](wstep1.html)

[Grant the Required Permissions](wstep2.html)

[Save the Policy File](wstep3.html)

See the Policy File Effects

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applications](index.html)

[« Previous](wstep3.html) • [Trail](../TOC.html) • [Next »](../sigcert/index.html)

# See the Policy File Effects

Now that you have added the required policy entry to
the `mypolicy` policy file,
you should be able to read the specified properties
when you execute the `GetProps` application with
a security manager, as shown in the following figure.

![the GetProps application can now read the specified properties](../../figures/security/step6.gif)

As noted at the end of the
[Quick Tour of Controlling Applets](../tour1/index.html)
lesson, whenever you run an unsigned applet, or an application with a security manager,
the policy files that are loaded and used by default are the ones
specified in the **"security properties file"**,
which is located at

```

  Windows:
    java.home\lib\security\java.security 
  UNIX:
    java.home/lib/security/java.security

```

**Note:**   *java.home* indicates the directory into which the JRE was installed.

There are two possible ways you can have the
`mypolicy` file
be considered as part of the overall policy, in addition to the policy files specified in
the security properties file. You can either specify the additional policy file in a
property passed to the runtime system, as described in
[Approach 1](#Approach1),
or add a line in the security properties
file specifying the additional policy file, as discussed in
[Approach 2](#Approach2).

### Approach 1

> You can use a `-Djava.security.policy` interpreter
> command line argument to specify a
> policy file that should be used in addition to the ones
> specified in the security properties file.
>
> Make sure that you are in the directory containing `GetProps.class`
> and `mypolicy`. Then you can
> run the `GetProps` application and pass the
> `mypolicy` policy file to the
> interpreter by typing the following command on one line:
>
> ```
>
> java -Djava.security.manager
>      -Djava.security.policy=mypolicy GetProps
>
> ```
>
> **Note:** Remember that `-Djava.security.manager` is
> required in order to run an application with a security manager,
> as shown in the [See How to Restrict Applications](step2.html) 
> step.
>
> The program reports the values of the `"user.home"` and
> `"java.home"` properties.
>
> If the application still reports an error,
> something is wrong in the policy file.
> Use the Policy Tool to check the policy entry you just created in the
> [Set up the Policy File to Grant the Required Permissions](step3.html) 
> step.

### Approach 2

> You can specify a number of URLs
> in `policy.url.n` properties in the security properties file, and
> all the designated policy files will get loaded.
> So one way to have your `mypolicy` file's policy entries considered by the
> `java` interpreter is to add
> an entry specifying that policy file in the security properties file.
>
> You created such an entry in the last part of the
> [Quick Tour of Controlling Applets](../tour1/index.html)
> lesson. If your security properties file still has that entry,
> you're ready to run the application. Otherwise you need
> to add the entry. To do so, open the security properties file
> in an editor suitable for editing an
> ASCII text file. Then add the following line after the line
> containing `policy.url.2`:
> > If you're on a Windows system, add
> >
> > ```
> >
> > policy.url.3=file:/C:/Test/mypolicy
> >
> > ```
> >
> > If you're on a UNIX system, add
> >
> > ```
> >
> > policy.url.3=file:${user.home}/test/mypolicy
> >
> > ```
> >
> > On a UNIX system you can alternatively explicitly specify your home directory, as in
> >
> > ```
> >
> > policy.url.3=file:/home/susanj/test/mypolicy
> >
> > ```

### Run the Application

> Now you should be able to successfully run the following.
>
> ```
>
> java -Djava.security.manager GetProps
>
> ```
>
> As with approach 1, if you still get a security exception,
> something is wrong in the policy file.
> Use the Policy Tool to check the policy entry you just created in the
> [Set up the Policy File to Grant the Required Permissions](step3.html) 
> step. Then fix any typos or other errors.
>
> ---
>
> **Important:** You do not need to include the `mypolicy` file unless you are running this Tutorial lesson. To exclude this file, open the security properties file and delete the line you just added.
>
> Before continuing, you may want to delete the line you just
> added in the security properties file (or comment it out), since you probably
> do not want the `mypolicy` file included when you are not running
> the tutorial
> lessons.
>
> ---

[« Previous](wstep3.html)
•
[Trail](../TOC.html)
•
[Next »](../sigcert/index.html)

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

**Previous page:** Save the Policy File
  
**Next page:** API and Tools Use for Secure Code and File Exchanges




A browser with JavaScript enabled is required for this page to operate properly.