[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Internationalization
  
**Lesson:** Introduction
  
**Section:** A Quick Example

[Introduction](index.html)

[A Quick Example](quick.html)

Before Internationalization

[After Internationalization](after.html)

[Running the Sample Program](run.html)

[Internationalizing the Sample Program](steps.html)

[Checklist](checklist.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Introduction](index.html)

[« Previous](quick.html) • [Trail](../TOC.html) • [Next »](after.html)

# Before Internationalization

Suppose that you've written a program that displays three messages, as follows:

```

public class NotI18N {

    static public void main(String[] args) {

        System.out.println("Hello.");
        System.out.println("How are you?");
        System.out.println("Goodbye.");
    }
}

```

You've decided that this program needs to display these same messages
for people living in France and Germany. Unfortunately your programming
staff is not multilingual, so you'll need help translating the messages
into French and German. Since the translators aren't programmers,
you'll have to move the messages out of the source code and into text
files that the translators can edit. Also, the program must be flexible
enough so that it can display the messages in other languages, but
right now no one knows what those languages will be.

It looks like the program needs to be internationalized.

[« Previous](quick.html)
•
[Trail](../TOC.html)
•
[Next »](after.html)

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

**Previous page:** A Quick Example
  
**Next page:** After Internationalization




A browser with JavaScript enabled is required for this page to operate properly.