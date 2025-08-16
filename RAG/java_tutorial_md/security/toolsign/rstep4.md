[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Receiver

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

[Download and Try the Sample Application](step1.html)

[Create a JAR File Containing the Class File](step2.html)

[Generate Keys](step3.html)

[Sign the JAR File](step4.html)

[Export the Public Key Certificate](step5.html)

[Steps for the Code Receiver](receiver.html)

[Observe the Restricted Application](rstep1.html)

[Import the Certificate as a Trusted Certificate](rstep2.html)

[Set Up a Policy File to Grant the Required Permission](rstep3.html)

[Start Policy Tool](wstep1.html)

[Specify the Keystore](wstep2.html)

[Add a Policy Entry with a SignedBy Alias](wstep3.html)

[Save the Policy File](wstep4.html)

See the Policy File Effects

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](wstep4.html) • [Trail](../TOC.html) • [Next »](../toolfilex/index.html)

# See the Policy File Effects

In the previous steps you created an entry in the `raypolicy`
policy file granting code
signed by `susan` permission to read files from the
`C:\TestData\` directory (or
the `testdata` directory in your home directory if
you're working on UNIX).
Now you should be able to successfully
execute the `Count` program to read and to
count the characters in a file from the specified directory, even when
you run the application with a security manager.

As described at the end of the
[Quick Tour of Controlling Applets](../tour1/index.html)
lesson, there are two possible ways you can have the
`raypolicy` file be considered as part of the overall policy,
in addition to the policy files specified in the security properties file.
The first approach is to specify the additional policy file
in a property passed to the runtime system.
The second approach is to add a line in the security properties
file specifying the additional policy file.

### Approach 1

> You can use a `-Djava.security.policy` command-line
> argument to specify a policy file that should be used in addition to or
> instead of the ones specified in the security properties file.
>
> To run the `Count` application and have the
> `raypolicy` policy file included, type the
> following while in the directory containing the
> `sCount.jar` and `raypolicy` files:
>
> ```
>
> java -Djava.security.manager -Djava.security.policy=raypolicy
>   -cp sCount.jar Count C:\TestData\data
>
> ```
>
> Note: The command should be typed on a single line, with a space
> between `raypolicy` and `-cp`.
>
> The program should report the number of characters in the specified
> file.
>
> If it still reports an error, something is wrong in the policy file.
> Use the Policy Tool to check the permission you just created in the
> [previous step](rstep3.html), and change any
> typos or other errors.

### Approach 2

> You can specify a number of URLs -- including ones of the form "http://" --
> in `policy.url.n` properties in the security properties file, and
> all the designated policy files will get loaded.
>
> So one way to have your `raypolicy` file's policy entries considered by the
> interpreter is to add an entry indicating that file in the security properties file.
>
> ---
>
> **Important:**  If you are running your own copy of the JDK,
> you can easily edit your
> security properties file. If you are running a version shared
> with others, you may only be able to modify the system-wide
> security properties file if you have write access to it or if you ask your
> system administrator to modify the file when appropriate. However,
> it's probably not appropriate for you to make modifications to a system-wide policy file
> for this tutorial test; we suggest that you just read the following to see how it's done
> or that you install your own private version of the JDK to use for the tutorial
> lessons.
>
> ---
>
> The security properties file is located at
>
> ```
>
>   Windows:
>     java.home\lib\security\java.security 
>   UNIX:
>     java.home/lib/security/java.security
>
> ```
>
> The *`java.home`* portion indicates the directory into which
> the JRE was installed.
>
> To modify the security properties file, open it in an editor suitable for editing an
> ASCII text file. Then add the following line after the line starting with
> `policy.url.2`:
>
> ```
>
>   Windows:
>     policy.url.3=file:/C:/Test/raypolicy
>   UNIX:
>     policy.url.3=file:${user.home}/test/raypolicy
>
> ```
>
> On a UNIX system you can alternatively explicitly specify your home directory, as in
>
> ```
>
> policy.url.3=file:/home/susanj/test/raypolicy
>
> ```
>
> Next, in your command window, go to the directory containing the
> `sCount.jar` file, that is, the `C:\Test`
> or `~/test` directory.
> Type the following command on one line:
>
> ```
>
> java -Djava.security.manager
>         -cp sCount.jar Count C:\TestData\data
>
> ```
>
> As with approach 1, if the program still reports an error,
> something is wrong with the policy file.
> Use the Policy Tool to check the permission you just created in the
> [previous step](rstep3.html), and change any
> typos or other errors.
> > ---
> >
> > **Important:** Before continuing, you may want to delete the line you just
> > added in the security properties file (or comment it out), since you probably
> > do not want the `raypolicy` file included when you are not running
> > the tutorial lessons.
> >
> > ---

[« Previous](wstep4.html)
•
[Trail](../TOC.html)
•
[Next »](../toolfilex/index.html)

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
  
**Next page:** Exchanging Files




A browser with JavaScript enabled is required for this page to operate properly.