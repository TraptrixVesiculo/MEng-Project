[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Numbers and Strings
  
**Section:** Strings

[Numbers and Strings](index.html)

[Numbers](numbers.html)

[The Numbers Classes](numberclasses.html)

[Formatting Numeric Print Output](numberformat.html)

[Beyond Basic Arithmetic](beyondmath.html)

[Summary of Numbers](numbersummary.html)

[Questions and Exercises](QandE/numbers-questions.html)

[Characters](characters.html)

[Strings](strings.html)

[Converting Between Numbers and Strings](converting.html)

Manipulating Characters in a String

[Comparing Strings and Portions of Strings](comparestrings.html)

[The StringBuilder Class](buffers.html)

[Summary of Characters and Strings](stringsummary.html)

[Questions and Exercises](QandE/characters-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Numbers and Strings](index.html)

[« Previous](converting.html) • [Trail](../TOC.html) • [Next »](comparestrings.html)

# Manipulating Characters in a String

The `String` class has a number of methods for examining the contents of strings, finding
characters or substrings within a string, changing case, and other tasks.

### Getting Characters and Substrings by Index

You can get the character at a particular index within a string by invoking the `charAt()`
accessor method. The index of the first character is 0, while
the index of the last character is `length()-1`.
For example, the following code gets the character at index 9 in a string:

```

String anotherPalindrome = "Niagara. O roar again!"; 
char aChar = anotherPalindrome.charAt(9);

```

Indices begin at 0, so the character at index 9 is 'O',
as illustrated in the following figure:

![Use the charAt method to get a character at a particular index.](../../figures/java/objects-charAt.gif)

If you want to get more than one consecutive character from a string, you can use the `substring` method.
The `substring` method has two versions,
as shown in the following table:

The `substring` Methods in the `String` Class

| Method | Description |
| `String substring(int beginIndex, int endIndex)` | Returns a new string that is a substring of this string. The first integer argument specifies the index of the first character. The second integer argument is the index of the last character - 1. |
| `String substring(int beginIndex)` | Returns a new string that is a substring of this string. The integer argument specifies the index of the first character. Here, the returned substring extends to the end of the original string. |

The following code gets from the Niagara palindrome the substring that
extends from index 11 up to, but not including, index 15, which is the word "roar":

```

String anotherPalindrome = "Niagara. O roar again!"; 
String roar = anotherPalindrome.substring(11, 15); 

```

![Use the substring method to get part of a string.](../../figures/java/objects-substring.gif)

### Other Methods for Manipulating Strings

Here are several other `String` methods for manipulating strings:

**Other Methods in the `String` Class for Manipulating Strings**

| Method | Description |
| `String[] split(String regex)`   `String[] split(String regex, int limit)` | Searches for a match as specified by the string argument (which contains a regular expression) and splits this string into an array of strings accordingly. The optional integer argument specifies the maximum size of the returned array. Regular expressions are covered in the lesson titled "Regular Expressions." |
| `CharSequence subSequence(int beginIndex, int endIndex)` Returns a new character sequence constructed from `beginIndex` index up until `endIndex` - 1. | |
| `String trim()` | Returns a copy of this string with leading and trailing white space removed. |
| `String toLowerCase()   String toUpperCase()` | Returns a copy of this string converted to lowercase or uppercase. If no conversions are necessary, these methods return the original string. |

### Searching for Characters and Substrings in a String

Here are some other `String` methods for finding characters or substrings within a string.
The `String` class provides accessor methods that
return the position within the string of a specific character or
substring: `indexOf()` and `lastIndexOf()`.
The `indexOf()` methods search forward from the beginning
of the string, and the `lastIndexOf()` methods search backward from
the end of the string. If a character or substring is not found, `indexOf()` and
`lastIndexOf()` return -1.

The `String` class also provides a search method,
`contains`, that returns true if the string
contains a particular character sequence. Use this method when
you only need to know that the string contains a character sequence,
but the precise location isn't important.

The following table describes the various string search
methods.

**The Search Methods in the `String` Class**

| Method | Description |
| `int indexOf(int ch)   int lastIndexOf(int ch)` | Returns the index of the first (last) occurrence of the specified character. |
| `int indexOf(int ch, int fromIndex)   int lastIndexOf(int ch, int fromIndex)` | Returns the index of the first (last) occurrence of the specified character, searching forward (backward) from the specified index. |
| `int indexOf(String str)   int lastIndexOf(String str)` | Returns the index of the first (last) occurrence of the specified substring. |
| `int indexOf(String str, int fromIndex)   int lastIndexOf(String str, int fromIndex)` | Returns the index of the first (last) occurrence of the specified substring, searching forward (backward) from the specified index. |
| `boolean contains(CharSequence s)` | Returns true if the string contains the specified character sequence. |

---

**Note:** `CharSequence` is an interface that is implemented by the `String` class.
Therefore, you can use a string as an argument for the `contains()` method.

---

### Replacing Characters and Substrings into a String

The `String` class has very few methods for inserting characters or substrings into a string.
In general, they are not needed: You can create a new string by concatenation of substrings you
have *removed* from a string with the substring that you want to insert.

The `String` class does have four methods for *replacing* found characters
or substrings, however. They are:

**Methods in the `String` Class for Manipulating Strings**

| Method | Description |
| `String replace(char oldChar, char newChar)` | Returns a new string resulting from replacing all occurrences of oldChar in this string with newChar. |
| `String replace(CharSequence target, CharSequence replacement)`  Replaces each substring of this string that matches the literal target sequence with the specified literal replacement sequence. | |
| `String replaceAll(String regex, String replacement)` | Replaces each substring of this string that matches the given regular expression with the given replacement. |
| `String replaceFirst(String regex, String replacement)` | Replaces the first substring of this string that matches the given regular expression with the given replacement. |

### An Example

The following class,
[`Filename`](examples/Filename.java), illustrates the use of `lastIndexOf()` and `substring()` to isolate different parts of a file name.

---

**Note:** The methods in the following `Filename` class don't
do any error checking and assume that their argument contains a full directory path and a filename with an extension.
If these methods were production code, they would verify that their arguments were properly constructed.

---

```


public class Filename {
    private String fullPath;
    private char pathSeparator, extensionSeparator;

    public Filename(String str, char sep, char ext) {
        fullPath = str;
        pathSeparator = sep;
        extensionSeparator = ext;
    }

    public String extension() {
        int dot = fullPath.lastIndexOf(extensionSeparator);
        return fullPath.substring(dot + 1);
    }

    public String filename() {  // gets filename without extension
        int dot = fullPath.lastIndexOf(extensionSeparator);
        int sep = fullPath.lastIndexOf(pathSeparator);
        return fullPath.substring(sep + 1, dot);
    }

    public String path() {
        int sep = fullPath.lastIndexOf(pathSeparator);
        return fullPath.substring(0, sep);
    }
}

```

Here is a program,
[`FilenameDemo`](examples/FilenameDemo.java), that constructs a `Filename` object and calls all of
its methods:

```


public class FilenameDemo {
    public static void main(String[] args) {
        final String FPATH = "/home/mem/index.html";
        Filename myHomePage = new Filename(FPATH,
                                           '/', '.');
        System.out.println("Extension = " + 
             myHomePage.extension());
        System.out.println("Filename = " + 
             myHomePage.filename());
        System.out.println("Path = " + 
             myHomePage.path());
    }
}

```

And here's the output from the program:

```

Extension = html
Filename = index
Path = /home/mem

```

As shown in the following figure, our `extension` method
uses `lastIndexOf` to locate the last occurrence of the
period (.) in the file name. Then `substring` uses the
return value of `lastIndexOf` to extract the file name
extension — that is, the substring from the period to the end
of the string. This code assumes that
the file name has a period in it; if the file name does not have a period,
`lastIndexOf` returns -1, and the substring method throws a
`StringIndexOutOfBoundsException`.

![The use of lastIndexOf and substring in the extension method in the Filename class.](../../figures/java/objects-lastIndexOf.gif)

Also, notice that the `extension` method uses `dot + 1` as the argument to `substring`.
If the period character (.) is the last character of the string, `dot + 1` is equal
to the length of the string, which is one larger than the largest index into the string
(because indices start at 0). This is a legal argument to
`substring` because that method accepts an index equal to, but not greater than, the length of
the string and interprets it to mean "the end of the string."

[« Previous](converting.html)
•
[Trail](../TOC.html)
•
[Next »](comparestrings.html)

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

**Previous page:** Converting Between Numbers and Strings
  
**Next page:** Comparing Strings and Portions of Strings




A browser with JavaScript enabled is required for this page to operate properly.