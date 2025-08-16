[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Collections
  
**Lesson:** Interfaces

[Interfaces](../index.html)

[The Collection Interface](../collection.html)

[The Set Interface](../set.html)

[The List Interface](../list.html)

[The Queue Interface](../queue.html)

[The Map Interface](../map.html)

[Object Ordering](../order.html)

[The SortedSet Interface](../sorted-set.html)

[The SortedMap Interface](../sorted-map.html)

[Summary of Interfaces](../summary.html)

Questions and Exercises

[Home Page](../../../index.html)
>
[Collections](../../index.html)
>
[Interfaces](../index.html)

[« Previous](../summary.html) • [Trail](../../TOC.html) • [Next »](../../implementations/index.html)

# Questions and Exercises: Interfaces

### Questions

> 1. This lesson mentions three ways to traverse a
>    `List`. Describe them, and note the limitations of
>    each.- Consider the four core interfaces, `Set`,
>      `List`, `Queue`, and `Map`.
>      For each of the following four assignments, specify which of the
>      four core interfaces is best suited, and explain how to use it
>      to implement the assignment.
>      * Whimsical Toys Inc (WTI) needs to record the names of
>        all its employees. Every month, an employee will be chosen
>        at random from these records to receive a free toy.* WTI has decided that each new product will be
>          named after an employee — but only first names
>          will be used, and each name will be used only once.
>          Prepare a list of unique first names.* WTI decides that it only wants to use the most
>            popular names for its toys. Count the number of
>            employees who have each first name.* WTI acquires season tickets for the local lacrosse
>              team, to be shared by employees. Create a waiting list
>              for this popular sport.- The following program is supposed to print the string "Blue". Instead,
>        it throws an error. Why?
>
>        ```
>
>        import java.util.*;
>
>        public class SortMe {
>            public static void main(String args[]) {
>                SortedSet<StringBuffer> s = new TreeSet<StringBuffer>();
>                s.add(new StringBuffer("Red"));
>                s.add(new StringBuffer("White"));
>                s.add(new StringBuffer("Blue"));
>                System.out.println(s.first());
>            }
>        }
>
>        ```

### Exercises

> 1. Write a program that prints its arguments in random order. Do not
>    make a copy of the argument array.
> 2. Take the
>    [`FindDups example`](../examples/FindDups.java)
>    and modify it to use a `SortedSet` instead of a
>    `Set`. Specify a `Comparator` so that case is
>    ignored when sorting and identifying set elements.- Write a method that takes a `List<String>` and
>      applies
>      [`String.trim`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#trim())
>      to each element. To do this, you'll need to pick one of the three
>      iteration idioms that you described in Question 1. Two of these will
>      not give the result you want, so be sure to write a program that
>      demonstrates that the method actually works!

[Check your answers.](answers.html)

[« Previous](../summary.html)
•
[Trail](../../TOC.html)
•
[Next »](../../implementations/index.html)

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

**Previous page:** Summary of Interfaces
  
**Next page:** Implementations




A browser with JavaScript enabled is required for this page to operate properly.