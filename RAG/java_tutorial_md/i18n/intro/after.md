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

[Before Internationalization](before.html)

After Internationalization

[Running the Sample Program](run.html)

[Internationalizing the Sample Program](steps.html)

[Checklist](checklist.html)

[Home Page](../../index.html)
>
[Internationalization](../index.html)
>
[Introduction](index.html)

[« Previous](before.html) • [Trail](../TOC.html) • [Next »](run.html)

# After Internationalization

The source code for the internationalized program follows. Notice that
the text of the messages is not hardcoded.

```

import java.util.*;

public class I18NSample {

    static public void main(String[] args) {

        String language;
        String country;

        if (args.length != 2) {
            language = new String("en");
            country = new String("US");
        } else {
            language = new String(args[0]);
            country = new String(args[1]);
        }

        Locale currentLocale;
        ResourceBundle messages;

        currentLocale = new Locale(language, country);

        messages = ResourceBundle.getBundle("MessagesBundle",
                                           currentLocale);
        System.out.println(messages.getString("greetings"));
        System.out.println(messages.getString("inquiry"));
        System.out.println(messages.getString("farewell"));
    }
}

```

To compile and run this program,
you need these source files:

* [`I18NSample.java`](examples/I18NSample.java)* [`MessagesBundle.properties`](examples/MessagesBundle.properties)* [`MessagesBundle_de_DE.properties`](examples/MessagesBundle_de_DE.properties)* [`MessagesBundle_en_US.properties`](examples/MessagesBundle_en_US.properties)* [`MessagesBundle_fr_FR.properties`](examples/MessagesBundle_fr_FR.properties)

[« Previous](before.html)
•
[Trail](../TOC.html)
•
[Next »](run.html)

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

**Previous page:** Before Internationalization
  
**Next page:** Running the Sample Program




A browser with JavaScript enabled is required for this page to operate properly.