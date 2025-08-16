[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects
  
**Section:** Nested Classes

[Classes and Objects](index.html)

[Classes](classes.html)

[Declaring Classes](classdecl.html)

[Declaring Member Variables](variables.html)

[Defining Methods](methods.html)

[Providing Constructors for Your Classes](constructors.html)

[Passing Information to a Method or a Constructor](arguments.html)

[Objects](objects.html)

[Creating Objects](objectcreation.html)

[Using Objects](usingobject.html)

[More on Classes](more.html)

[Returning a Value from a Method](returnvalue.html)

[Using the this Keyword](thiskey.html)

[Controlling Access to Members of a Class](accesscontrol.html)

[Understanding Instance and Class Members](classvars.html)

[Initializing Fields](initial.html)

[Summary of Creating and Using Classes and Objects](summaryclasses.html)

[Questions and Exercises](QandE/creating-questions.html)

[Questions and Exercises](QandE/objects-questions.html)

[Nested Classes](nested.html)

Inner Class Example

[Summary of Nested Classes](summarynested.html)

[Questions and Exercises](QandE/nested-questions.html)

[Enum Types](enum.html)

[Questions and Exercises](QandE/enum-questions.html)

[Annotations](annotations.html)

[Questions and Exercises](QandE/annotations-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Classes and Objects](index.html)

[« Previous](nested.html) • [Trail](../TOC.html) • [Next »](summarynested.html)

# Inner Class Example

To see an inner class in use, let's first consider an array. In the following example, we
will create an array, fill it with integer values and then output only values of even
indices of the array in ascending order.

The `DataStructure` class below consists of:

* The `DataStructure` outer class, which includes methods to add an integer onto
  the array and print out values of even indices of the array.
* The `InnerEvenIterator` inner class, which is similar to a standard Java *iterator*. Iterators are
  used to step through a data structure and typically have methods to test for the last element, retrieve the
  current element, and move to the next element.
* A `main` method that instantiates a `DataStructure` object (`ds`) and uses it
  to fill the `arrayOfInts` array with integer values (0, 1, 2, 3, etc.), then calls
  a `printEven` method to print out values of even indices of `arrayOfInts`.

```


public class DataStructure {
    //create an array
    private final static int SIZE = 15;
    private int[] arrayOfInts = new int[SIZE];
    
    public DataStructure() {
        //fill the array with ascending integer values
        for (int i = 0; i < SIZE; i++) {
            arrayOfInts[i] = i;
        }
    }
    
    public void printEven() {
        //print out values of even indices of the array
        InnerEvenIterator iterator = this.new InnerEvenIterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.getNext() + " ");
        }
    }
    
//inner class implements the Iterator pattern
    private class InnerEvenIterator {
        //start stepping through the array from the beginning
        private int next = 0;
        
        public boolean hasNext() {
            //check if a current element is the last in the array
            return (next <= SIZE - 1);
        }
        
        public int getNext() {
            //record a value of an even index of the array
            int retValue = arrayOfInts[next];
            //get the next even element
            next += 2;
            return retValue;
        }
    }
    
    public static void main(String s[]) {
        //fill the array with integer values and print out only values of even indices
        DataStructure ds = new DataStructure();
        ds.printEven();
    }
}

```

The output is:

```

0 2 4 6 8 10 12 14 

```

Note that the `InnerEvenIterator` class refers directly
to the `arrayOfInts` instance variable of the `DataStructure` object.

Inner classes can be used to implement helper classes
like the one shown in the example above. If you plan on handling
user-interface events, you will need to know how to use inner
classes because the event-handling mechanism makes extensive
use of them.

### Local and Anonymous Inner Classes

There are two additional types of inner classes. You can declare an inner class within the body of a method. Such a class is known as a
*local inner class*. You can also declare an inner class within the body of a method without naming it.
These classes are known as *anonymous inner classes*. You will encounter such classes in advanced Java
programming.

### Modifiers

You can use the same modifiers for inner classes that you use for other members of
the outer class. For example, you can use the access
specifiers — `private`, `public`, and
`protected` — to restrict access to inner classes,
just as you do to other class members.

[« Previous](nested.html)
•
[Trail](../TOC.html)
•
[Next »](summarynested.html)

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

**Previous page:** Nested Classes
  
**Next page:** Summary of Nested Classes




A browser with JavaScript enabled is required for this page to operate properly.