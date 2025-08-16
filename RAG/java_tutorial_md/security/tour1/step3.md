[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Quick Tour of Controlling Applets

[Quick Tour of Controlling Applets](index.html)

[Observe Applet Restrictions](step1.html)

[Set up a Policy File to Grant the Required Permission](step2.html)

[Start Policy Tool](wstep1.html)

[Grant the Required Permission](wstep2.html)

[Save the Policy File](wstep3.html)

See the Policy File Effects

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Quick Tour of Controlling Applets](index.html)

[« Previous](wstep3.html) • [Trail](../TOC.html) • [Next »](../tour2/index.html)

# See the Policy File Effects

Now that you have created the `mypolicy` policy file,
you can
execute the `WriteFile` applet to create and to write the
file `writetest`, as shown in the following figure.

![WriteFile can now access writetest](../../figures/security/step5.gif)

  

Whenever you run an applet, or an application with a security manager,
the policy files that are loaded and used by default are the ones
specified in the **"security properties file"**,
which is located in one of the following directories:

```

  Windows:
    java.home\lib\security\java.security 
  UNIX:
    java.home/lib/security/java.security

```

**Note:**   The java.home environment variable names the directory into which the JRE was installed.

The policy file locations are specified as the values of properties whose names take the form

```

policy.url.n

```

Where `n` indicates a number. Specify each property
value in a line that takes the following form:

```

policy.url.n=URL

```

Where *URL* is a URL specification.
For example, the default policy files, sometimes referred to as
the system and user policy files, respectively,
are defined in the security properties file as

```

policy.url.1=file:${java.home}/lib/security/java.policy
policy.url.2=file:${user.home}/.java.policy

```

> ---
>
> **Note:** Use of the notation `${propName}`
> in the security properties file is a way of
> specifying the value of a property. Thus `${java.home}` will be
> replaced at runtime by the actual value of the `"java.home"` property,
> which indicates the directory into which the JRE was installed, and
> `${user.home}` will be
> replaced by the value of the `"user.home"` property, for
> example, `C:\Windows`.
>
> ---

In the [previous step](step2.html)
you did not modify one of these existing policy files. You created a new policy file
named `mypolicy`. There are two possible ways you can have the
`mypolicy` file
be considered as part of the overall policy, in addition to the policy files specified in
the security properties file. You can either specify the additional policy file in a
property passed to the runtime system, as described in
[Approach 1](#Approach1),
or add a line in the security properties
file specifying the additional policy file, as described in
[Approach 2](#Approach2).
> ---
>
> **Note:** On a UNIX system, you must have DNS
> configured in order for the `WriteFile` program
> to be downloaded from the public web site, shown in the command below.
> You need to have `dns`
> in the list of lookup services for hosts in your
> `/etc/nsswitch.conf` file, as in
>
> ```
>
>     hosts:    dns files nis
>
> ```
>
> You also need a `/etc/resolv.conf` file
> with a list of nameservers.
> Consult your system administrator for more information.
>
> ---

### Approach 1

> You can use the `appletviewer`
> command-line argument, `-J-Djava.security.policy`, to specify a
> policy file that should be used, in addition to the ones
> specified in the security properties file.
> To run the `WriteFile` applet with your new
> `mypolicy` policy file included, type the following in the
> directory in which `mypolicy` is stored:
>
> ```
>
> appletviewer -J-Djava.security.policy=mypolicy  
>  http://download.oracle.com/javase/tutorial/security/tour1/examples/WriteFile.html
>
> ```
>
> > ---
> >
> > **Notes:**
> >
> > * Type this command as a single line, with a space between
> >   `mypolicy` and the URL, and no spaces in the URL. Multiple lines
> >   are used in this example for legibility purposes.
> >
> >   * If this command line is longer than the maximum number of
> >     characters you are allowed to type on a single line, do the following.
> >     Create and save a text file containing the full
> >     command, and name the file with a `.bat` extension,
> >     for example, `wf.bat`. Then in your command
> >     window, type the name of the `.bat` file instead of the command.
> >
> > ---
> >
> > If the applet still reports an error,
> > you must troubleshoot the policy file.
> > Use the Policy Tool to open the `mypolicy` file
> > (using **File** > **Open**) and
> > check the policy entries you just created in the
> > previous step,
> > [Set Up a Policy File to Grant the Required Permissions](step2.html).
> >
> > To view or edit an existing policy entry, click on the line displaying that entry in the main
> > Policy Tool window, then choose the **Edit Policy Entry** button.
> > You can also double-click the line for that entry.
> >
> > This launches the same type of Policy Entry dialog box that displays when you
> > are adding a new policy entry after choosing the **Add Policy Entry** button,
> > except in this case the dialog box is filled in with
> > the existing policy entry information. To change the information,
> > retype it (for the **CodeBase** and **SignedBy**
> > values) or add, remove, or modify permissions.
>
> ### Approach 2
>
> > You can specify a number of URLs (including ones of the form "http://")
> > in `policy.url.n` properties in the security properties file, and
> > all the designated policy files will get loaded.
> >
> > So one way to have our `mypolicy` file's policy entry considered
> > by the `appletviewer` is to add
> > an entry specifying that policy file in the security properties file.
> >
> > ---
> >
> > **Important:**  If you are running your own copy of the JDK,
> > you can easily edit your
> > security properties file. If you are running a version shared
> > with other users, you may only be able to modify the system-wide
> > security properties file if you have write access to it or if you ask your
> > system administrator to modify the file when appropriate. However,
> > it's probably not appropriate for you to make modifications to a system-wide policy file
> > for this tutorial test. We suggest that you just read the following to see how it is done
> > or that you install your own private version of the JDK to use for the tutorial
> > lessons.
> >
> > ---
> >
> > To modify the security properties file, open it in an editor suitable for editing an
> > ASCII text file. Then add the following line after the line starting with
> > `policy.url.2`:
> >
> > ```
> >
> >   Windows:
> >     policy.url.3=file:/C:/Test/mypolicy
> >   UNIX:
> >     policy.url.3=file:${user.home}/test/mypolicy
> >
> > ```
> >
> > On a UNIX system you can also explicitly specify your home directory:
> >
> > ```
> >
> > policy.url.3=file:/home/susanj/test/mypolicy
> >
> > ```
> >
> > Now you can run the following:
> >
> > ```
> >
> > appletviewer http://download.oracle.com/javase/tutorial/security1.2/tour1/examples/WriteFile.html
> >
> > ```
> >
> > Type this command on one line, without spaces in the URL.
> >
> > If you still get a security exception, you must troubleshoot
> > your new policy file.
> > Use the Policy Tool to check the policy entry you just created in the
> > previous step,
> > [Set Up a Policy File to Grant the Required Permissions](step2.html).
> > Change any typos or other errors.
> > > ---
> > >
> > > **Important:** The `mypolicy` policy file is also used in the
> > > [Quick Tour of Controlling Applications](../tour2/index.html)
> > > lesson. You do not need to include the `mypolicy` file unless you are running this Tutorial lesson. To exclude this file, open the security properties file and delete the line you just added.
> > >
> > > ---
> > >
> > > [« Previous](wstep3.html)
> > > •
> > > [Trail](../TOC.html)
> > > •
> > > [Next »](../tour2/index.html)
> > >
> > > ---
> > >
> > > Problems with the examples? Try [Compiling and Running
> > > the Examples: FAQs](../../information/run-examples.html).
> > >   
> > > Complaints? Compliments? Suggestions? [Give
> > > us your feedback](http://download.oracle.com/javase/feedback.html).
> > >
> > > Your use of this page and all the material on pages under "The Java Tutorials" banner,
> > > and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
> > > and License](../../information/license.html).
> > > Additionally, any example code contained in any of these Java
> > > Tutorials pages is licensed under the
> > > [Code
> > > Sample License](http://developers.sun.com/license/berkeley_license.html).
> > >
> > > |  |  |  |  |  |
> > > | --- | --- | --- | --- | --- |
> > > | |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |
> > >
> > > **Previous page:** Save the Policy File
> > >   
> > > **Next page:** Quick Tour of Controlling Applications
> > >
> > >
> > >
> > >
> > > A browser with JavaScript enabled is required for this page to operate properly.