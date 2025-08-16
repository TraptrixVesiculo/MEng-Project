[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Generics

[Generics](index.html)

[Introduction](generics.html)

[Generic Types](gentypes.html)

[Generic Methods and Constructors](genmethods.html)

Type Inference

[Bounded Type Parameters](bounded.html)

[Subtyping](subtyping.html)

[Wildcards](wildcards.html)

[Type Erasure](erasure.html)

[Using Non-Reifiable Parameters with Varargs Methods](non-reifiable-varargs-type.html)

[Summary of Generics](summarygenerics.html)

[Questions and Exercises](QandE/generics-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Generics](index.html)

[« Previous](genmethods.html) • [Trail](../TOC.html) • [Next »](bounded.html)

# Type Inference

The following topics are covered:

* [Type Inference and Generic Methods](#type-inference-methods)
* [Type Inference and Instantiation of Generic Classes](#type-inference-instantiation)
* [Type Inference and Generic Constructors of Generic and Non-Generic Classes](#type-inference-constructors)

## Type Inference and Generic Methods

The section,
[Generic Methods and Constructors](genmethods.html), introduced you to type inference, which enables you to invoke a generic method as you would an ordinary method, without specifying a type between angle brackets. Consider the following example,
[`BoxDemo4`](examples/BoxDemo4.java), which requires the
[`Box`](examples/Box.java) example and Java SE 7 or later:

```

public class BoxDemo4 {

  public static <U> void addBox(U u, java.util.List<Box<U>> boxes) {
    Box<U> box = new Box<>();
    box.add(u);
    boxes.add(box);
  }

  public static <U> void outputBoxes(java.util.List<Box<U>> boxes) {
    int counter = 0;
    for (Box<U> box: boxes) {
      U boxContents = box.get();
      System.out.println(
        "Box #" + counter + " contains [" +
        boxContents.toString() + "]");
      counter++;
    }
  }

  public static void main(String[] args) {
    java.util.ArrayList<Box<Integer>> listOfIntegerBoxes =
      new java.util.ArrayList<>();
    BoxDemo4.<Integer>addBox(new Integer(10), listOfIntegerBoxes);
    BoxDemo4.addBox(new Integer(20), listOfIntegerBoxes);
    BoxDemo4.addBox(new Integer(30), listOfIntegerBoxes);
    BoxDemo4.outputBoxes(listOfIntegerBoxes);
  }
}

```

The following is the output from this example:

```

Box #0 contains [10]
Box #1 contains [20]
Box #2 contains [30]

```

The generic method `addBox` defines one type parameter named `U`. Generally, the Java compiler can infer the type parameters of a generic method call. Consequently, in most cases, you do not have to specify them. For example, to call the generic method `addBox`, you can specify the type parameter as follows:

```

BoxDemo4.<Integer>addBox(new Integer(10), listOfIntegerBoxes);

```

Alternatively, if you omit the type parameters, the Java compiler automatically infers (from the method's arguments) that the type parameter is `Integer`:

```

BoxDemo4.addBox(new Integer(20), listOfIntegerBoxes);

```

## Type Inference and Instantiation of Generic Classes

You can replace the type arguments required to invoke the constructor of a generic class with an empty set of type parameters (`<>`) as long as the compiler can infer the type arguments from the context. This pair of angle brackets is informally called the *diamond operator*.

For example, consider the following variable declaration:

```
Map<String, List<String>> myMap = new HashMap<String, List<String>>();
```

In Java SE 7, you can substitute the parameterized type of the constructor with an empty set of type parameters (`<>`):

```
Map<String, List<String>> myMap = new HashMap<>();
```

Note that to take advantage of automatic type inference during generic class instantiation, you must specify the diamond operator. In the following example, the compiler generates an unchecked conversion warning because the `HashMap()` constructor refers to the `HashMap` raw type, not the `Map<String, List<String>>` type:

```
Map<String, List<String>> myMap = new HashMap(); // unchecked conversion warning
```

Java SE 7 supports limited type inference for generic instance creation; you can only use type inference if the parameterized type of the constructor is obvious from the context. For example, the following example does not compile:

```
List<String> list = new ArrayList<>();
list.add("A");

  // The following statement should fail since addAll expects
  // Collection<? extends String>

list.addAll(new ArrayList<>());
```

Note that the diamond operator often works in method calls; however, it is suggested that you use this operator primarily for variable declarations.

In comparison, the following example compiles:

```
// The following statements compile:

List<? extends String> list2 = new ArrayList<>();
list.addAll(list2);
```

## Type Inference and Generic Constructors of Generic and Non-Generic Classes

Note that constructors can be generic (in other words, declare their own formal type parameters) in both generic and non-generic classes. Consider the following example:

```
class MyClass<X> {
  <T> MyClass(T t) {
    // ...
  }
}
```

Consider the following instantiation of the class `MyClass`, which is valid in Java SE 7 and prior releases:

```
new MyClass<Integer>("")
```

This statement creates an instance of the parameterized type `MyClass<Integer>`; the statement explicitly specifies the type `Integer` for the formal type parameter, `X`, of the generic class `MyClass<X>`. Note that the constructor for this generic class contains a formal type parameter, `T`. The compiler infers the type `String` for the formal type parameter, `T`, of the constructor of this generic class (because the actual parameter of this constructor is a `String` object).

Compilers from releases prior to Java SE 7 are able to infer the actual type parameters of generic constructors, similar to generic methods. However, the compiler in Java SE 7 can infer the actual type parameters *of the generic class being instantiated* if you use the diamond operator (`<>`). Consider the following examples, which are valid for Java SE 7 and later:

* ```
  MyClass<Integer> myObject = new MyClass<>("");
  ```

  In this example, the compiler infers the type `Integer` for the formal type parameter, `X`, of the generic class `MyClass<X>`. It infers the type `String` for the formal type parameter, `T`, of the constructor of this generic class.
* ```
  MyClass<Integer> myObject = new <String`> MyClass<>("");
  ```

  In this example, the compiler infers the type `Integer` for the formal type parameter, `X`, of the generic class `MyClass<X>`. The statement explicitly specifies the type `String` for the formal type parameter, `T`, of the constructor of this generic class.

[« Previous](genmethods.html)
•
[Trail](../TOC.html)
•
[Next »](bounded.html)

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

**Previous page:** Generic Methods and Constructors
  
**Next page:** Bounded Type Parameters




A browser with JavaScript enabled is required for this page to operate properly.