[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Essential Classes
  
**Lesson:** Exceptions

[Exceptions](index.html)

[What Is an Exception?](definition.html)

[The Catch or Specify Requirement](catchOrDeclare.html)

Catching and Handling Exceptions

[The try Block](try.html)

[The catch Blocks](catch.html)

[The finally Block](finally.html)

[The try-with-resources Statement](tryResourceClose.html)

[Putting It All Together](putItTogether.html)

[Specifying the Exceptions Thrown by a Method](declaring.html)

[How to Throw Exceptions](throwing.html)

[Chained Exceptions](chained.html)

[Creating Exception Classes](creating.html)

[Unchecked Exceptions — The Controversy](runtime.html)

[Advantages of Exceptions](advantages.html)

[Summary](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Essential Classes](../index.html)
>
[Exceptions](index.html)

[« Previous](catchOrDeclare.html) • [Trail](../TOC.html) • [Next »](try.html)

# Catching and Handling Exceptions

This section describes how to use the three
exception handler components — the `try`,
`catch`, and `finally` blocks — to write
an exception handler.
Then, the `try-`with-resources statement, introduced
in Java SE 7, is explained. The `try-`with-resources
statement is particularly suited to situations that use
`Closeable` resources, such as streams.

The last part of this section walks
through an example and analyzes what occurs during various scenarios.

The following example defines and implements a class named
`ListOfNumbers`. When constructed, `ListOfNumbers`
creates an `ArrayList` that contains 10 `Integer`
elements with sequential values 0 through 9. The `ListOfNumbers`
class also defines a method named `writeList`, which writes the
list of numbers into a text file called `OutFile.txt`. This
example uses output classes defined in `java.io`, which are
covered in
[Basic I/O](../io/index.html).

```

//Note: This class won't compile by design!
import java.io.*;
import java.util.List;
import java.util.ArrayList;

public class ListOfNumbers {

  private List<Integer> list;
  private static final int SIZE = 10;

  public ListOfNumbers () {
    list = new ArrayList<Integer>(SIZE);
      for (int i = 0; i < SIZE; i++) {
        list.add(new Integer(i));
    }
  }

  public void writeList() {
    PrintWriter out = new PrintWriter(
      new FileWriter("OutFile.txt"));

    for (int i = 0; i < SIZE; i++) {
      out.println("Value at: " + i + " = " + list.get(i));
    }
    out.close();
  }
}

```

The first line in boldface is a call to a constructor. The constructor
initializes an output stream on a file. If the file cannot be opened,
the constructor throws an `IOException`. The second
boldface line is a call to the `ArrayList` class's
`get` method, which throws an
`IndexOutOfBoundsException` if the value of its
argument is too small (less than 0) or too large (more than
the number of elements currently contained by the `ArrayList`).

If you try to compile the
[`ListOfNumbers`](examples/ListOfNumbers.java) class, the compiler prints an error message about the exception thrown by
the `FileWriter` constructor. However, it does not
display an error message about the exception thrown by
`get`. The reason is that the exception thrown
by the constructor, `IOException`, is a checked exception,
and the one thrown by the `get` method,
`IndexOutOfBoundsException`, is an unchecked
exception.

Now that you're familiar with the `ListOfNumbers`
class and where the exceptions can be thrown within it, you're
ready to write exception handlers to catch and handle those exceptions.

[« Previous](catchOrDeclare.html)
•
[Trail](../TOC.html)
•
[Next »](try.html)

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

**Previous page:** The Catch or Specify Requirement
  
**Next page:** The try Block




A browser with JavaScript enabled is required for this page to operate properly.