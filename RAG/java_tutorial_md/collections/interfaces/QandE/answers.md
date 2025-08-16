[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../../search.html)

**Trail:** Collections
  
**Lesson:** Interfaces

[Home Page](../../../index.html)
>
[Collections](../../index.html)
>
[Interfaces](../index.html)

[« Previous](../QandE/questions.html) • [TOC](../../TOC.html)

# Answers to Questions and Exercises:

### Questions

> 1. Question:
>    This lesson mentions three ways to traverse a
>    `List`. Describe them, and note the limitations of
>    each.Answer:
>    * Use the enhanced `for` statement:
>
>      ```
>
>      List<Thing> list;
>      ...
>      for (Thing thing : list) {
>          ...
>      }
>
>      ```
>
>      Limitations: cannot be used to add, remove, or modify elements.* Use the traditional `for` statement together with an
>        `Iterator`:
>
>        ```
>
>        List<Thing> list;
>        ...
>        for (Iterator<Thing> it = list.iterator(); it.hasNext(); ) {
>            Thing thing = it.next();
>            ...
>        }
>
>        ```
>
>        Limitations: cannot be used to modify elements.* Use the traditional `for` statement together with an
>          `ListIterator`:
>
>          ```
>
>          List<Thing> list;
>          ...
>          for (ListIterator<Thing> it = list.iterator(); it.hasNext(); ) {
>              Thing thing = it.next();
>              ...
>          }
>
>          ```
>
>          Limitations: none.- Question:
>      Consider the four core interfaces, `Set`,
>      `List`, `Queue`, and `Map`.
>      For each of the following four assignments, specify which of the
>      four core interfaces is best-suited, and explain how to use it
>      to implement the assignment.Answer:
>      * *Whimsical Toys Inc (WTI) needs to record the names of
>        all its employees. Every month, an employee will be chosen
>        at random from these records to receive a free
>        toy.*
>          
>        Use a `List`. Choose a random employee by
>        picking a number between `0` and
>        `size()-1`.* *WTI has decided that each new product will be
>          named after an employee — but only first names
>          will be used, and each name will be used only once.
>          Prepare a list of unique first names.*
>            
>          Use a `Set`. Collections that
>          implement this interface don't allow the same element
>          to be entered more than once.* *WTI decides that it only wants to use the most
>            popular names for its toys. Count up the number of
>            employees who have each first name.*
>              
>            Use a `Map`, where the keys are first
>            names, and each value is a count of the number of
>            employees with that first name.* *WTI acquires season tickets for the local lacrosse
>              team, to be shared by employees. Create a waiting list
>              for this popular sport.*
>                
>              Use a `Queue`. Invoke
>              `add()` to add employees to the waiting
>              list, and `remove()` to remove them.- Question:
>        The following program is supposed to print the string "Blue". Instead,
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
>
>        Answer:
>        `TreeSort` elements must be instances of a class that
>        implements
>        [`Comparable`](http://download.oracle.com/javase/7/docs/api/java/lang/Comparable.html). `StringBuffer` does not.

### Exercises

> 1. Exercise:
>    Write a program that prints its arguments in random order. Do not
>    make a copy of the argument array.Answer:
>
>    ```
>
>
>    import java.util.*;
>
>    public class Ran {
>        public static void main(String[] args) {
>            List<String> argList = Arrays.asList(args);
>            Collections.shuffle(argList);
>            for (String arg: argList) {
>                System.out.format("%s ", arg);
>            }
>            System.out.println();
>        }
>    }
>
>    ```
>
>    - Exercise:
>      Take the
>      [`FindDups example`](../examples/FindDups.java)
>      and modify it to use a `SortedSet` instead of a
>      `Set`. Specify a `Comparator` so that case is
>      ignored when sorting and identifying set elements.Answer:
>
>      ```
>
>
>      import java.util.*;
>
>      public class FindDups {
>
>          public static void main(String[] args) {
>              Comparator<String> comparator = new Comparator<String>() {
>                  public int compare (String s1, String s2) {
>                      return s1.compareToIgnoreCase(s2);
>                  }
>              };
>
>              SortedSet<String> s = new TreeSet<String>(comparator);
>              for (String a : args)
>                  if (!s.add(a))
>                      System.out.println("Duplicate detected: " + a);
>
>              System.out.println(s.size() + " distinct words: " + s);
>          }
>      }
>
>      ```
>
>      - Exercise:
>        Write a method that takes a `List<String>` and
>        applies
>        [`String.trim`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html#trim())
>        to each element. To do this, you'll need to pick one of the three
>        iteration idioms that you described in Question 1. Two of these will
>        not give the result you want, so be sure to write a program that
>        demonstrates that the method actually works!Answer:
>        The enhanced `for` statement does not allow you to modify
>        the `List`. Using an `Iterator` allows you to
>        delete elements, but not replace an existing element or add a new one.
>        That leaves `ListIterator`:
>
>        ```
>
>
>        import java.util.*;
>
>        public class ListTrim {
>            static void listTrim(List<String> strings) {
>                for (ListIterator<String> lit = strings.listIterator();
>                        lit.hasNext(); ) {
>                    lit.set(lit.next().trim());
>                }
>            }
>
>            public static void main(String[] args) {
>                List<String> l = Arrays.asList(" red ", " white ", " blue ");
>                listTrim(l);
>                for (String s : l) {
>                    System.out.format("\"%s\"%n", s);
>                }
>            }
>        }
>
>        ```

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

**Previous page:** Questions and Exercises: Interfaces




A browser with JavaScript enabled is required for this page to operate properly.