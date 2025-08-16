[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Regular Expressions

[Regular Expressions](index.html)

[Introduction](intro.html)

Test Harness

[String Literals](literals.html)

[Character Classes](char_classes.html)

[Predefined Character Classes](pre_char_classes.html)

[Quantifiers](quant.html)

[Capturing Groups](groups.html)

[Boundary Matchers](bounds.html)

[Methods of the Pattern Class](pattern.html)

[Methods of the Matcher Class](matcher.html)

[Methods of the PatternSyntaxException Class](pse.html)

[Unicode Support](unicode.html)

[Additional Resources](resources.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Regular Expressions](index.html)

[« Previous](intro.html) • [Trail](../TOC.html) • [Next »](literals.html)

# Test Harness

This section defines a reusable test harness,
[`RegexTestHarness.java`](examples/RegexTestHarness.java)
, for exploring the regular expression
constructs supported by this API.
The command to run this code is `java RegexTestHarness`;
no command-line arguments are accepted.
The application loops repeatedly, prompting the user for a regular expression
and input string. Using this test harness is optional,
but you may find it convenient for exploring the test cases
discussed in the following pages.

```


import java.io.Console;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class RegexTestHarness {

    public static void main(String[] args){
        Console console = System.console();
        if (console == null) {
            System.err.println("No console.");
            System.exit(1);
        }
        while (true) {

            Pattern pattern = 
            Pattern.compile(console.readLine("%nEnter your regex: "));

            Matcher matcher = 
            pattern.matcher(console.readLine("Enter input string to search: "));

            boolean found = false;
            while (matcher.find()) {
                console.format("I found the text \"%s\" starting at " +
                   "index %d and ending at index %d.%n",
                    matcher.group(), matcher.start(), matcher.end());
                found = true;
            }
            if(!found){
                console.format("No match found.%n");
            }
        }
    }
}


```

Before continuing to the next section, save and compile this code to ensure that your development environment supports the required packages.

[« Previous](intro.html)
•
[Trail](../TOC.html)
•
[Next »](literals.html)

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

**Previous page:** Introduction
  
**Next page:** String Literals




A browser with JavaScript enabled is required for this page to operate properly.