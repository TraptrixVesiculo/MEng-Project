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

Capturing Groups

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

[« Previous](quant.html) • [Trail](../TOC.html) • [Next »](bounds.html)

# Capturing Groups

In the
[previous section](quant.html), we saw how quantifiers attach to one character,
character class, or capturing group at a time. But until now, we have not
discussed the notion of capturing groups in any detail.

*Capturing groups* are a way to treat multiple characters
as a single unit. They are created by placing the characters to
be grouped inside a set of parentheses. For example,
the regular expression `(dog)` creates a single group containing the letters `"d" "o"` and `"g"`.
The portion of the input string that matches the capturing group
will be saved in memory for later recall via backreferences (as discussed
below in the section,
[Backreferences](#backref)).

### Numbering

As described in the
[`Pattern`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) API,
capturing groups are numbered by counting their opening parentheses from left to right. In
the expression `((A)(B(C)))`, for example,
there are four such groups:

1. `((A)(B(C)))`- `(A)`- `(B(C))`- `(C)`

To find out how many groups are present in the
expression, call the `groupCount` method on a matcher object. The `groupCount`
method returns an `int` showing the number of capturing groups present in the matcher's pattern. In this
example, `groupCount` would return the number `4`, showing that the pattern contains 4 capturing groups.

There is also a special group, group 0, which always represents
the entire expression. This group is not
included in the total reported by
`groupCount`. Groups beginning with `(?`
are pure, *non-capturing groups*
that do not capture text and do not count towards the group total.
(You'll see examples of non-capturing groups later in the section
[Methods of the Pattern Class](pattern.html).)

It's important to understand how groups are numbered
because some `Matcher` methods accept an `int` specifying a particular group number as a parameter:

* [`public int start(int group)`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html#start(int)):
  Returns the start index of the subsequence captured by the given
  group during the previous match operation.

  * [`public int end (int group)`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html#end(int)):
    Returns the index of the last character, plus one, of the subsequence captured by the
    given group during the previous match operation.

    * [`public String group (int group)`](http://download.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html#group(int)):
      Returns the input subsequence captured by the given group during the previous match operation.

### Backreferences

The section of the input string matching the
capturing group(s) is saved in memory for later recall via
*backreference*.
A backreference is specified in the
regular expression as a backslash (`\`) followed by a
digit indicating the number of the group to be recalled.
For example, the expression `(\d\d)` defines one capturing group matching two digits in a row,
which
can be recalled later in the expression via the backreference `\1`.

To match any 2 digits, followed by the exact same two digits, you would use `(\d\d)\1` as the regular expression:

```
 
Enter your regex: (\d\d)\1
Enter input string to search: 1212
I found the text "1212" starting at index 0 and ending at index 4.

```

If you change the last two digits the match will fail:

```
 
Enter your regex: (\d\d)\1
Enter input string to search: 1234
No match found.

```

For nested capturing groups, backreferencing works in exactly the same way: Specify a backslash followed
by the number of the group to be recalled.

[« Previous](quant.html)
•
[Trail](../TOC.html)
•
[Next »](bounds.html)

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

**Previous page:** Quantifiers
  
**Next page:** Boundary Matchers




A browser with JavaScript enabled is required for this page to operate properly.