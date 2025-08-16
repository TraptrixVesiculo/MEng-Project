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

[Catching and Handling Exceptions](handling.html)

[The try Block](try.html)

[The catch Blocks](catch.html)

[The finally Block](finally.html)

[The try-with-resources Statement](tryResourceClose.html)

[Putting It All Together](putItTogether.html)

Specifying the Exceptions Thrown by a Method

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

[« Previous](putItTogether.html) • [Trail](../TOC.html) • [Next »](throwing.html)

# Specifying the Exceptions Thrown by a Method

The previous section showed how to write an exception
handler for the `writeList` method in the
`ListOfNumbers` class. Sometimes, it's appropriate
for code to catch exceptions that can occur within it.
In other cases, however, it's better to let a method further
up the call stack handle the exception. For example, if you
were providing the `ListOfNumbers` class as part
of a package of classes, you probably couldn't anticipate
the needs of all the users of your package. In this case,
it's better to *not* catch the exception and to allow a method
further up the call stack to handle it.

If the `writeList` method doesn't catch the checked
exceptions that can occur within it, the `writeList`
method must specify that it can throw these exceptions. Let's
modify the original `writeList` method to specify the
exceptions it can throw instead of catching them. To remind
you, here's the original version of the `writeList`
method that won't compile.

```

// Note: This method won't compile by design!
public void writeList() {
    PrintWriter out = 
               new PrintWriter(new FileWriter("OutFile.txt"));
    for (int i = 0; i < SIZE; i++) {
        out.println("Value at: " + i + " = " 
                     + vector.elementAt(i));
    }
    out.close();
}

```

To specify that `writeList` can throw two exceptions,
add a `throws` clause to the method declaration
for the `writeList` method. The `throws`
clause comprises the `throws` keyword followed by a
comma-separated list of all the exceptions thrown by that method.
The clause goes after the method name and argument list and before
the brace that defines the scope of the method; here's an example.

```

public void writeList() throws IOException,
                               ArrayIndexOutOfBoundsException {

```

Remember that `ArrayIndexOutOfBoundsException` is an
unchecked exception; including it in the `throws` clause is
not mandatory. You could just write the following.

```

public void writeList() throws IOException {

```

[« Previous](putItTogether.html)
•
[Trail](../TOC.html)
•
[Next »](throwing.html)

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

**Previous page:** Putting It All Together
  
**Next page:** How to Throw Exceptions




A browser with JavaScript enabled is required for this page to operate properly.