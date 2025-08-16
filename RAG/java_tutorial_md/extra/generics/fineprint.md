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

The Fine Print

[Class Literals as Runtime-Type Tokens](literals.html)

[More Fun with Wildcards](morefun.html)

[Converting Legacy Code to Use Generics](convert.html)

[Acknowledgements](acknowledgements.html)

[Home Page](../../index.html)
>
[Bonus](../index.html)
>
[Generics](index.html)

[« Previous](legacy.html) • [Trail](../TOC.html) • [Next »](literals.html)

# The Fine Print

#### A Generic Class is Shared by All Its Invocations

What does the following code fragment print?

```

List <String> l1 = new ArrayList<String>();
List<Integer> l2 = new ArrayList<Integer>();
System.out.println(l1.getClass() == l2.getClass());

```

You might be tempted to say `false`, but you'd be wrong. It prints
`true`, because all instances of a generic class have the same
run-time class, regardless of their actual type parameters.

Indeed, what makes a class generic is the fact that it has the same behavior
for all of its possible type parameters; the same class can be viewed as
having many different types.

As consequence, the static variables and methods of a class are also
shared among all the instances. That is why it is illegal to refer to
the type parameters of a type declaration in a static method or initializer,
or in the declaration or initializer of a static variable.

#### Casts and InstanceOf

Another implication of the fact that a generic class is shared among all its
instances, is that it usually makes no sense to ask an instance if it is
an instance of a particular invocation of a generic type:

```

Collection cs = new ArrayList<String>();
if (cs instanceof Collection<String>) { ...} // Illegal.

```

similarly, a cast such as

```

Collection<String> cstr = (Collection<String>) cs; // Unchecked warning,

```

gives an unchecked warning, since this isn't something the runtime system is
going to check for you.

The same is true of type variables

```

<T> T badCast(T t, Object o) {return (T) o; // Unchecked warning. 
    }

```

Type variables don't exist at run time. This means that they entail no
performance overhead in either time nor space, which is nice. Unfortunately,
it also means that you can't reliably use them in casts.

#### Arrays

The component type of an array object may not be a type variable or a parameterized type, unless
it is an (unbounded) wildcard type.You can declare array *types* whose
element type is a type variable or a parameterized type, but not array *objects*.

This is annoying, to be sure. This restriction is necessary to avoid
situations like:

```

List<String>[] lsa = new List<String>[10]; // Not really allowed.
Object o = lsa;
Object[] oa = (Object[]) o;
List<Integer> li = new ArrayList<Integer>();
li.add(new Integer(3));
oa[1] = li; // Unsound, but passes run time store check 
String s = lsa[1].get(0); // Run-time error: ClassCastException.

```

If arrays of parameterized type were allowed, the previous example would compile
without any unchecked warnings, and yet fail at run-time. We've had type-safety
as a primary design goal of generics. In particular, the language is
designed to guarantee
that **if your entire application
has been compiled without unchecked warnings using javac -source 1.5,
it is type safe**.

However, you can still use wildcard arrays. The following
variation on the previous code forgoes the use of both array objects
and array types whose element type is parameterized. As a result,
we have to cast explicitly to get a `String` out of the array.

```

List<?>[] lsa = new List<?>[10]; // OK, array of unbounded wildcard type.
Object o = lsa;
Object[] oa = (Object[]) o;
List<Integer> li = new ArrayList<Integer>();
li.add(new Integer(3));
oa[1] = li; // Correct.
String s = (String) lsa[1].get(0); // Run time error, but cast is explicit.

```

In the next variation, which causes a compile-time error,
we refrain from creating an array object
whose element type is parameterized, but still use an array type
with a parameterized element type.

```

List<String>[] lsa = new List<?>[10]; // Error.

```

Similarly, attempting to create an array object whose element
type is a type variable causes a compile-time error:

```

<T> T[] makeArray(T t) {
    return new T[100]; // Error.
}

```

Since type variables
don't exist at run time, there is no way to determine what the actual
array type would be.

The way to work around these kinds of limitations is to use class literals
as run time type tokens, as described in the next section,
[Class Literals as Runtime-Type Tokens](literals.html).

[« Previous](legacy.html)
•
[Trail](../TOC.html)
•
[Next »](literals.html)

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

**Previous page:** Interoperating with Legacy Code
  
**Next page:** Class Literals as Runtime-Type Tokens




A browser with JavaScript enabled is required for this page to operate properly.