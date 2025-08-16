[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JavaBeans(TM)
  
**Lesson:** Using the BeanContext API

[Using the BeanContext API](index.html)

[Overview of the BeanContext API](overview.html)

Bean Context #1: Containment Only

[Bean Context #2: Containment and Services](services.html)

[AWT Containers and the BeanContextProxy Interface](gui.html)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Using the BeanContext API](index.html)

[« Previous](overview.html) • [Trail](../TOC.html) • [Next »](services.html)

# Bean Context #1: Containment Only

The "containment" portion of the Extensible Runtime Containment and Services Protocol is defined by
the `BeanContext` interface. In its most basic form, a `BeanContext` is used to
logically
group a set of related java beans, bean contexts, or arbitrary objects.
JavaBeans nested into a `BeanContext` are known as "child" beans.
Once nested, a child bean can query its `BeanContext`
for various membership information, as illustrated in the following
examples.

Here are some possible `BeanContext` containment
scenarios:

![A rectangle with nothing in it.](../../figures/javabeans/emptyBeanContext.gif)

![A rectangle with a single coffee bean labeled JavaBean.](../../figures/javabeans/single.gif)

![A rectangle with three coffee beans, each below the previous, indented, and labeled JavaBean.](../../figures/javabeans/3beans.gif)

![A rectangle (BeanContext #2) inside another rectangle (BeanContext #1)](../../figures/javabeans/2contexts.gif)

The sample code presented in this chapter uses instances of the
`BeanContextSupport` helper class to provide the basic `BeanContext`
functionality. A `BeanContextSupport` object is simply a concrete
implementation of the `BeanContext` interface.

With a `BeanContextSupport` instance, it is possible to:

* Add an object, bean, or `BeanContext`:
  [`boolean add(Object o)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#add(java.lang.Object))* Remove an object, bean, or `BeanContext`:
    [`boolean remove(Object o)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#remove(java.lang.Object))* Add a `BeanContextMembershipListener`:
      [`void addBeanContextMembershipListener(BeanContextMembershipListener bcml)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#addBeanContextMembershipListener(java.beans.beancontext.BeanContextMembershipListener))* Remove a `BeanContextMembershipListener`:
        [`void removeBeanContextMembershipListener(BeanContextMembershipListener bcml)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#removeBeanContextMembershipListener(java.beans.beancontext.BeanContextMembershipListener))* Get all JavaBean or `BeanContext` instances currently
          nested in this `BeanContext` as an array or as an Iterator:
          [`Object[] toArray()`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#toArray()),
          [`Object[] toArray(Object[] a)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#toArray(java.lang.Object[])), and
          [`Iterator iterator()`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#iterator())* Determine whether or not a specified object
            is currently a child of the `BeanContext`:
            [`boolean contains(Object o)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#contains(java.lang.Object))* Get the number of children currently nested in this `BeanContext`:
              [`int size()`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#size())* Determine whether or not the `BeanContext` currently has zero children:
                [`boolean isEmpty()`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#isEmpty())* Instantiate a new JavaBean instance as a child of the target `BeanContext`:
                  [`Object instantiateChild(String beanName)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextSupport.html#instantiateChild(java.lang.String))

The following test programs, which are run from the command line, illustrate the use of these methods.

The comments in the source code explain the purpose of each.

**File:
[`Example1.java`](examples/Example1.java)**

```


import java.beans.beancontext.*;

public class Example1 {
    private static BeanContextSupport context = new BeanContextSupport(); // The BeanContext
    private static BeanContextChildSupport bean = new BeanContextChildSupport(); // The JavaBean
  
    public static void main(String[] args) {
        report();  

        // Add the bean to the context
        System.out.println("Adding bean to context...");
        context.add(bean);

        report();
    }

    private static void report() {
        // Print out a report of the context's membership state.
        System.out.println("=============================================");

        // Is the context empty?
        System.out.println("Is the context empty? " + context.isEmpty());

        // Has the context been set for the child bean?
        boolean result = (bean.getBeanContext()!=null);
        System.out.println("Does the bean have a context yet? " + result);

        // Number of children in the context
        System.out.println("Number of children in the context: " + context.size());

        // Is the specific bean a member of the context?
        System.out.println("Is the bean a member of the context? " + context.contains(bean));

        // Equality test
        if (bean.getBeanContext() != null) {
            boolean isEqual = (bean.getBeanContext()==context); // true means both references point to the same object
            System.out.println("Contexts are the same? " + isEqual);
        }
        System.out.println("=============================================");   
    }
}

```

**Output**:

```

=============================================
Is the context empty? true
Does the bean have a context yet? false
Number of children in the context: 0
Is the bean a member of the context? false
=============================================
Adding bean to context...
=============================================
Is the context empty? false
Does the bean have a context yet? true
Number of children in the context: 1
Is the bean a member of the context? true
Contexts are the same? true
=============================================

```

**File:
[`Example2.java`](examples/Example2.java)**

```


import java.beans.beancontext.*;

public class Example2 {
    public static void main(String[] args) {

        // A BeanContext 
        BeanContextSupport context = new BeanContextSupport(); 

        // Many JavaBeans
        BeanContextChildSupport[] beans = new BeanContextChildSupport[100];

        System.out.println("Number of children in the context: " + context.size());

        // Create the beans and add them to the context
        for (int i = 0; i < beans.length; i++) {
            beans[i] = new BeanContextSupport();
            context.add(beans[i]);
        }
        System.out.println("Number of children in the context: " + context.size());

        // Context now has 100 beans in it, get references to them all
        Object[] children = context.toArray();
        System.out.println("Number of objects retrieved from the context: " + children.length);
    }
}

```

**Output:**

```

Number of children in the context: 0
Number of children in the context: 100
Number of objects retrieved from the context: 100

```

**File:
[`Example3.java`](examples/Example3.java)**

```


import java.beans.beancontext.*;
import java.io.*;

public class Example3 {
    public static void main(String[] args) {
        BeanContextSupport context = new BeanContextSupport();
        System.out.println("Number of children nested into the context: " + context.size());

        BeanContextChildSupport child = null;
        try {
            child = (BeanContextChildSupport)context.instantiateChild("java.beans.beancontext.BeanContextChildSupport");
        }
        catch(IOException e){
            System.out.println("IOException occurred: " + e.getMessage());
        }
        catch(ClassNotFoundException e){
            System.out.println("Class not found: " + e.getMessage());
        }
        System.out.println("Number of children nested into the context: " + context.size());
    }
}

```

**Output**:

```

Number of children nested into the context: 0
Number of children nested into the context: 1

```

## BeanContextMembershipEvent Notification

The `BeanContext` API uses the standard Java event
model to register listeners and deliver events.
For an overview of this standard event model,
refer to
[Writing Event Listeners](../../uiswing/events/index.html).
For details about handling specific events, see
[Writing Event Listeners](../../uiswing/events/index.html).

In a basic `BeanContext`, the event classes and interfaces involved are:

* [`java.beans.beancontext.BeanContextMembershipEvent`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextMembershipEvent.html): Encapsulates the list of children added to, or removed from, the membership of
  a particular `BeanContext`.
  An instance of this event is fired whenever a successful add(), remove(), retainAll(),
  removeAll(), or clear() is invoked on a given `BeanContext` instance.* [`java.beans.BeanContextMembershipListener`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextMembershipListener.html): Objects
    wishing to receive BeanContextMembershipEvents implement this interface.
    It defines methods
    [`void childrenAdded(BeanContextMembershipEvent bcme)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextMembershipListener.html#childrenAdded(java.beans.beancontext.BeanContextMembershipEvent)) and
    [`void childrenRemoved(BeanContextMembershipEvent bcme)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextMembershipListener.html#childrenRemoved(java.beans.beancontext.BeanContextMembershipEvent)), which are called when a child is added to or removed
    from a given `BeanContext` instance.

## BeanContextMembershipEvent Notification: Sample Code

**File:
[`MembershipTest.java`](examples/MembershipTest.java)**

```


import java.beans.beancontext.*;

public class MembershipTest {
    public static void main(String[] args) {
        BeanContextSupport context = new BeanContextSupport(); // the context
        MyMembershipListener listener = new MyMembershipListener(); 
        BeanContextChildSupport bean = new BeanContextChildSupport(); // a JavaBean
        context.addBeanContextMembershipListener(listener); // now listening!
        context.add(bean);
        context.remove(bean);
    }
}

class MyMembershipListener implements BeanContextMembershipListener {
    public void childrenAdded(BeanContextMembershipEvent bcme) {
        System.out.println("Another bean has been added to the context.");
    }

    public void childrenRemoved(BeanContextMembershipEvent bcme) {
        System.out.println("A bean has been removed from the context.");
    }
}

```

**Output:**

```

Another bean has been added to the context.
A bean has been removed from the context.

```

## The same example, implemented using an anonymous inner class

```

import java.beans.beancontext.*;

public class MembershipTest {
    public static void main(String[] args) {
        BeanContextSupport context = new BeanContextSupport();
        context.addBeanContextMembershipListener(new BeanContextMembershipListener() {
            public void childrenAdded(BeanContextMembershipEvent bcme) {
                System.out.println("Another bean has been added to the context.");
            }

            public void childrenRemoved(BeanContextMembershipEvent bcme) {
                System.out.println("A bean has been removed from the context.");
            }
        });
        BeanContextChildSupport bean = new BeanContextChildSupport();
        context.add(bean);
        context.remove(bean);
    }
}

```

**Output:**

```

Another bean has been added to the context.
A bean has been removed from the context.

```

[« Previous](overview.html)
•
[Trail](../TOC.html)
•
[Next »](services.html)

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

**Previous page:** Overview of the BeanContext API
  
**Next page:** Bean Context #2: Containment and Services




A browser with JavaScript enabled is required for this page to operate properly.