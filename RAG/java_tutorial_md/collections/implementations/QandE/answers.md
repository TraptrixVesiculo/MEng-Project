[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Collections
  
**Lesson:** Implementations

[Home Page](../../../index.html)
>
[Collections](../../index.html)
>
[Implementations](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises:

### Questions

> 1. Question:
>    You plan to write a program that uses several basic
>    collection interfaces: `Set`, `List`,
>    `Queue`, and `Map`. You're not sure which
>    implementations will work best, so you decide to use general-purpose
>    implementations until you get a better idea how your program will work
>    in the real world. Which implementations are these?Answer:
>      
>    `Set`: `HashSet`
>      
>    `List`: `ArrayList`
>      
>    `Queue`: `LinkedList`
>      
>    `Map`: `HashMap`
>    Question:
>    If you need a `Set` implementation that provides value-ordered iteration, which class should you use?Answer:
>    `TreeSet` guarantees that the sorted set is in ascending element order, sorted according to the natural order of the elements or by the `Comparator` provided.
> 2. Question:
>    Which class do you use to access wrapper implementations?Answer:
>    You use the `Collections` class, which provides static methods that operate on or return collections.

### Exercises

> 1. Exercise:
>    Write a program that reads a text file, specified by the first
>    command line argument, into a `List`. The program
>    should then print random lines from the file, the number of lines
>    printed to be specified by the second command line argument.
>    Write the program so that a correctly-sized collection is
>    allocated all at once, instead of being gradually expanded as the
>    file is read in. Hint: To determine the number of lines in the
>    file, use
>    [`java.io.File.length`](http://download.oracle.com/javase/7/docs/api/java/io/File.html#length())
>    to obtain the size of the file, then divide by an assumed size of an
>    average line.Answer:
>    Since we're accessing the `List` randomly, we'll use
>    `ArrayList`. We estimate the number of lines by taking the
>    file size and dividing by 50. We then double that figure, since it's
>    more efficient to overestimate than to underestmate.
>
>    ```
>
>
>    import java.util.*;
>    import java.io.*;
>
>    public class FileList {
>        public static void main(String[] args) {
>            final int assumedLineLength = 50;
>            File file = new File(args[0]);
>            List<String> fileList = 
>                new ArrayList<String>((int)(file.length() / assumedLineLength) * 2);
>            BufferedReader reader = null;
>            int lineCount = 0;
>            try {
>                reader = new BufferedReader(new FileReader(file));
>                for (String line = reader.readLine(); line != null;
>                        line = reader.readLine()) {
>                    fileList.add(line);
>                    lineCount++;
>                }
>            } catch (IOException e) {
>                System.err.format("Could not read %s: %s%n", file, e);
>                System.exit(1);
>            } finally {
>                if (reader != null) {
>                    try {
>                        reader.close();
>                    } catch (IOException e) {}
>                }
>            }
>            int repeats = Integer.parseInt(args[1]);
>            Random random = new Random();
>            for (int i = 0; i < repeats; i++) {
>                System.out.format("%d: %s%n", i,
>                        fileList.get(random.nextInt(lineCount - 1)));
>            }
>        }
>    }
>
>    ```
>
>    This program actually spends most of its time reading in the file, so
>    pre-allocating the `ArrayList` has little affect on its
>    performance. Specifying an initial capacity in advance is more likely
>    to be useful when your program repeatly creates large
>    `ArrayList` objects without intervening I/O.

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

**Previous page:** Questions and Exercises: Implementations




A browser with JavaScript enabled is required for this page to operate properly.