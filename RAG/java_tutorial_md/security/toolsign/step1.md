[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Signing Code and Granting It Permissions
  
**Section:** Steps for the Code Signer

[Signing Code and Granting It Permissions](index.html)

[Steps for the Code Signer](signer.html)

Download and Try the Sample Application

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

[See the Policy File Effects](rstep4.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Signing Code and Granting It Permissions](index.html)

[« Previous](signer.html) • [Trail](../TOC.html) • [Next »](step2.html)

# Download and Try the Sample Application

This lesson uses a simple application that we provide to you.

1. Create a file named `Count.java`
   on your local computer
   by either copying or downloading the
   [`Count.java`](examples/Count.java)
   source code.
   The examples in this lesson assume that you place `count` in
   the `C:\Test` directory.
  
2. The `count` application needs to access a text file containing the data it will process. Download a sample data file [**here**](examples/data), or use any other convenient text file as data.   
     


   ---

   **Important:**  Put your data file into a directory **other than** the directory containing your downloaded `count` class file. We suggest `C:\TestData\data`.   
     
   Later in this lesson you will see how an application running under a security manager cannot read a file unless it has explicit permission to do so. However, an application can *always* read a file from the same directory (or a subdirectory). It does not need explicit permission.

---

  
3. Compile and then run the
   `Count` application to see what it does.   
     
   When you run the `count` application, you need to
   specify (as an argument) the path name of a file to be read.  
      
   `java Count C:\TestData\data`

Here is a sample run:

```

    C:\Test>java Count C:\TestData\data
    Counted 65 chars.

```

[« Previous](signer.html)
•
[Trail](../TOC.html)
•
[Next »](step2.html)

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

**Previous page:** Steps for the Code Signer
  
**Next page:** Create a JAR File Containing the Class File




A browser with JavaScript enabled is required for this page to operate properly.