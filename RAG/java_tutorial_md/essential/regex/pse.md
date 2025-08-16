[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Regular Expressions

[Regular Expressions](index.html)

[Introduction](intro.html)

[Test Harness](test_harness.html)

[String Literals](literals.html)

[Character Classes](char_classes.html)

[Predefined Character Classes](pre_char_classes.html)

[Quantifiers](quant.html)

[Capturing Groups](groups.html)

[Boundary Matchers](bounds.html)

[Methods of the Pattern Class](pattern.html)

[Methods of the Matcher Class](matcher.html)

Methods of the PatternSyntaxException Class

[Unicode Support](unicode.html)

[Additional Resources](resources.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Regular Expressions](index.html)

[« Previous](matcher.html) • [Trail](../TOC.html) • [Next »](unicode.html)

# Methods of the PatternSyntaxException Class

A
[`PatternSyntaxException`](http://download.oracle.com/javase/7/docs/api/java/util/regex/PatternSyntaxException.html) is an unchecked exception that indicates
a syntax error in a regular expression pattern. The
`PatternSyntaxException` class
provides the following methods to help you determine what went wrong:

* [`public String getDescription()`](http://download.oracle.com/javase/7/docs/api/java/util/regex/PatternSyntaxException.html#getDescription()): Retrieves the description of the error.* [`public int getIndex()`](http://download.oracle.com/javase/7/docs/api/java/util/regex/PatternSyntaxException.html#getIndex()): Retrieves the error index.* [`public String getPattern()`](http://download.oracle.com/javase/7/docs/api/java/util/regex/PatternSyntaxException.html#getPattern()): Retrieves the erroneous regular expression pattern.* [`public String getMessage()`](http://download.oracle.com/javase/7/docs/api/java/util/regex/PatternSyntaxException.html#getMessage()): Returns a multi-line string containing the description
        of the syntax error and its index, the erroneous regular-expression pattern, and a
        visual indication of the error index within the pattern.

The following source code,
[`RegexTestHarness2.java`](examples/RegexTestHarness2.java), updates our test harness to check for malformed regular expressions:

```


import java.io.Console;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.regex.PatternSyntaxException;

public class RegexTestHarness2 {

    public static void main(String[] args){
        Pattern pattern = null;
        Matcher matcher = null;

        Console console = System.console();
        if (console == null) {
            System.err.println("No console.");
            System.exit(1);
        }
        while (true) {
            try{
                pattern = 
                Pattern.compile(console.readLine("%nEnter your regex: "));

                matcher = 
                pattern.matcher(console.readLine("Enter input string to search: "));
            }
            catch(PatternSyntaxException pse){
                console.format("There is a problem with the regular expression!%n");
                console.format("The pattern in question is: %s%n",pse.getPattern());
                console.format("The description is: %s%n",pse.getDescription());
                console.format("The message is: %s%n",pse.getMessage());
                console.format("The index is: %s%n",pse.getIndex());
                System.exit(0);
            }
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

To run this test, enter `?i)foo` as the regular expression.
This mistake is a common scenario in which the programmer has forgotten the opening
parenthesis in the embedded flag expression `(?i)`.
Doing so will produce the following results:

```

Enter your regex: ?i)
There is a problem with the regular expression!
The pattern in question is: ?i)
The description is: Dangling meta character '?'
The message is: Dangling meta character '?' near index 0
?i)
^
The index is: 0

```

From this output, we can see that the syntax error is a dangling metacharacter (the question mark)
at index 0. A missing opening parenthesis is the culprit.

[« Previous](matcher.html)
•
[Trail](../TOC.html)
•
[Next »](unicode.html)

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

**Previous page:** Methods of the Matcher Class
  
**Next page:** Unicode Support




A browser with JavaScript enabled is required for this page to operate properly.