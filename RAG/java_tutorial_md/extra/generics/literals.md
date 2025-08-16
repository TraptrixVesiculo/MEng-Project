[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Bonus
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](intro.html)

[Defining Simple Generics](simple.html)

[Generics and Subtyping](subtype.html)

[Wildcards](wildcards.html)

[Generic Methods](methods.html)

[Interoperating with Legacy Code](legacy.html)

[The Fine Print](fineprint.html)

Class Literals as Runtime-Type Tokens

[More Fun with Wildcards](morefun.html)

[Converting Legacy Code to Use Generics](convert.html)

[Acknowledgements](acknowledgements.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Generics](index.html)

[« Previous](fineprint.html) • [Trail](../TOC.html) • [Next »](morefun.html)

# Class Literals as Runtime-Type Tokens

One of the changes in JDK 5.0 is that the class `java.lang.Class` is
generic. It's an interesting example of using genericity for something
other than a container class.

Now that `Class` has a type parameter `T`, you might well ask,
what does `T` stand for? It stands for the type that the `Class`
object is representing.

For example, the type of `String.class` is
`Class<String>`, and the type of `Serializable.class` is
`Class<Serializable>`. This can be used to improve the type safety
of your reflection code.

In particular, since the `newInstance()` method in `Class` now
returns a `T`, you can get more precise types when creating objects
reflectively.

For example, suppose you need to write a utility method that
performs a database query, given as a string of SQL, and returns a
collection of objects in the database that match that query.

One way is to pass in a factory object explicitly, writing code
like:

```

interface Factory<T> { T make();} 

public <T> Collection<T> select(Factory<T> factory, String statement) { 
    Collection<T> result = new ArrayList<T>(); 
    /* Run sql query using jdbc */  
    for (/* Iterate over jdbc results. */) { 
        T item = factory.make();
        /* Use reflection and set all of item's fields from sql results. */ 
        result.add(item); 
    } 
    return result; 
}

```

You can call this either as

```

select(new Factory<EmpInfo>(){ public EmpInfo make() {
                               return new EmpInfo();
                               }}
      , "selection string");

```

or you can declare a class `EmpInfoFactory` to
support the `Factory` interface

```

class EmpInfoFactory implements Factory<EmpInfo> {
    ...
    public EmpInfo make() { return new EmpInfo();}
}

```

and call it

```

select(getMyEmpInfoFactory(), "selection string");

```

The downside of this solution is that it requires either:

* the use of verbose anonymous factory classes at the call site, or* declaring a factory class for every type used and passing
    a factory instance at the call site, which is somewhat unnatural.

It is natural to use the class literal as a factory
object, which can then be used by reflection. Today (without generics) the
code might be written:

```

Collection emps = sqlUtility.select(EmpInfo.class, "select * from emps");
...
public static Collection select(Class c, String sqlStatement) { 
    Collection result = new ArrayList();
    /* Run sql query using jdbc. */
    for (/* Iterate over jdbc results. */ ) { 
        Object item = c.newInstance(); 
        /* Use reflection and set all of item's fields from sql results. */  
        result.add(item); 
    } 
    return result; 
}

```

However, this would not give us a collection of the precise type we desire.
Now that `Class` is generic, we can instead write
the following:

```

Collection<EmpInfo> emps = 
                      sqlUtility.select(EmpInfo.class, "select * from emps");
...
public static <T> Collection<T> select(Class<T> c, String sqlStatement) { 
    Collection<T> result = new ArrayList<T>();
    /* Run sql query using jdbc. */
    for (/* Iterate over jdbc results. */ ) { 
        T item = c.newInstance(); 
        /* Use reflection and set all of item's fields from sql results. */  
        result.add(item);
    } 
    return result; 
} 

```

The above code gives us the precise type of collection in a type safe way.

This technique of using class literals as run time type tokens is a very
useful trick to know. It's an idiom that's used extensively in the new
APIs for manipulating annotations, for example.

[« Previous](fineprint.html)
•
[Trail](../TOC.html)
•
[Next »](morefun.html)

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

**Previous page:** The Fine Print
  
**Next page:** More Fun with Wildcards




A browser with JavaScript enabled is required for this page to operate properly.