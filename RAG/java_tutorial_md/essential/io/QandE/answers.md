[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Essential Classes
  
**Lesson:** Basic I/O

[Home Page](../../../index.html)
>
[Essential Classes](../../index.html)
>
[Basic I/O](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises: Basic I/O

## Questions

Question 1. What class and method would you use to read a few pieces of data that
are at known positions near the end of a large file?

Answer 1. `Files.newByteChannel`
returns an instance of `SeekableByteChannel` which allows you to
read from (or write to) any position in the file.

Question 2. When invoking `format`,
what is the best way to indicate a new line?

Answer 2.
Use the `%n` conversion — the `\n`
escape is not platform independent!

Question 3. How would you determine the MIME type of a file?

Answer 3. The `Files.probeContentType`
method uses the platform's underlying file type detector to evaluate and return
the MIME type.
  

Question 4. What method(s) would you use to determine whether a file is a symbolic link?

Answer 4. You would use the `Files.isSymbolicLink` method.

## Exercises

Exercise 1. Write an example that counts the number of times a particular
character, such as `e`, appears in a file.
The character can be specified at the command line. You can use
[`xanadu.txt`](../examples/xanadu.txt) as the input file.

Answer 1. See
[`CountLetter.java`](CountLetter.java) for the solution.

Exercise 2. The file
[`datafile`](datafile) begins with a single `long` that tells you the offset
of a single `int` piece of data within the same file.
Write a program that gets the `int` piece of data.
What is the `int` data?

Answer 2. `123`. See
[`FindInt.java`](FindInt.java) for the solution.

[« Previous](../QandE/questions.html)
•
[TOC](../../TOC.html)


---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../../../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../../../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Questions and Exercises: Basic I/O




A browser with JavaScript enabled is required for this page to operate properly.