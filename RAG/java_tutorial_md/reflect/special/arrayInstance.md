[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** The Reflection API
  
**Lesson:** Arrays and Enumerated Types
  
**Section:** Arrays

[Arrays and Enumerated Types](index.html)

[Arrays](array.html)

[Identifying Array Types](arrayComponents.html)

Creating New Arrays

[Getting and Setting Arrays and Their Components](arraySetGet.html)

[Troubleshooting](arrayTrouble.html)

[Enumerated Types](enum.html)

[Examining Enums](enumMembers.html)

[Getting and Setting Fields with Enum Types](enumSetGet.html)

[Troubleshooting](enumTrouble.html)

[Home Page](../../index.html)
>
[The Reflection API](../index.html)
>
[Arrays and Enumerated Types](index.html)

[« Previous](arrayComponents.html) • [Trail](../TOC.html) • [Next »](arraySetGet.html)

# Creating New Arrays

Just as in non-reflective code, reflection supports the ability to
dynamically create arrays of arbitrary type and dimensions via
[`java.lang.reflect.Array.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Array.html#newInstance(java.lang.Class, int)). Consider
[`ArrayCreator`](example/ArrayCreator.java), a basic interpreter capable of dynamically creating arrays. The syntax that
will be parsed is as follows:

```

fully_qualified_class_name variable_name[] = { val1, val2, val3, ... }

```

Assume that the `fully_qualified_class_name` represents a class that
has a constructor with a single
[`String`](http://download.oracle.com/javase/7/docs/api/java/lang/String.html)
argument. The dimensions of the array are determined by the number of values
provided. The following example will construct an instance of an array of
`fully_qualified_class_name` and populate its values with instances
given by `val1`, `val2`, etc. (This example assumes
familiarity with
[`Class.getConstructor()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#getConstructor(java.lang.Class...))
and
[`java.lang.reflect.Constructor.newInstance()`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html#newInstance(java.lang.Object...)). For a discussion of the reflection APIs for
[`Constructor`](http://download.oracle.com/javase/7/docs/api/java/lang/reflect/Constructor.html)
see the  [Creating New Class
Instances](../member/ctorInstance.html) section of this trail.)

```


import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Arrays;
import static java.lang.System.out;

public class ArrayCreator {
    private static String s = "java.math.BigInteger bi[] = { 123, 234, 345 }";
    private static Pattern p = Pattern.compile("^\\s*(\\S+)\\s*\\w+\\[\\].*\\{\\s*([^}]+)\\s*\\}");

    public static void main(String... args) {
        Matcher m = p.matcher(s);

        if (m.find()) {
            String cName = m.group(1);
            String[] cVals = m.group(2).split("[\\s,]+");
            int n = cVals.length;

            try {
                Class<?> c = Class.forName(cName);
                Object o = Array.newInstance(c, n);
                for (int i = 0; i < n; i++) {
                    String v = cVals[i];
                    Constructor ctor = c.getConstructor(String.class);
                    Object val = ctor.newInstance(v);
                    Array.set(o, i, val);
                }

                Object[] oo = (Object[])o;
                out.format("%s[] = %s%n", cName, Arrays.toString(oo));

            // production code should handle these exceptions more gracefully
            } catch (ClassNotFoundException x) {
                x.printStackTrace();
            } catch (NoSuchMethodException x) {
                x.printStackTrace();
            } catch (IllegalAccessException x) {
                x.printStackTrace();
            } catch (InstantiationException x) {
                x.printStackTrace();
            } catch (InvocationTargetException x) {
                x.printStackTrace();
            }
        }
    }
}

```

```

$ java ArrayCreator
java.math.BigInteger [] = [123, 234, 345]

```

The above example shows one case where it may be desirable to create an
array via reflection; namely if the component type is not known until runtime.
In this case, the code uses
[`Class.forName()`](http://download.oracle.com/javase/7/docs/api/java/lang/Class.html#forName())
to get a class for the desired component type and then calls a specific
constructor to initialize each component of the array before setting the
corresponding array value.

[« Previous](arrayComponents.html)
•
[Trail](../TOC.html)
•
[Next »](arraySetGet.html)

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

**Previous page:** Identifying Array Types
  
**Next page:** Getting and Setting Arrays and Their Components




A browser with JavaScript enabled is required for this page to operate properly.