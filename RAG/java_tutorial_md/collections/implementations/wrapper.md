[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Collections
  
**Lesson:** Implementations

[Implementations](index.html)

[Set Implementations](set.html)

[List Implementations](list.html)

[Map Implementations](map.html)

[Queue Implementations](queue.html)

Wrapper Implementations

[Convenience Implementations](convenience.html)

[Summary of Implementations](summary.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Collections](../index.html)
>
[Implementations](index.html)

[« Previous](queue.html) • [Trail](../TOC.html) • [Next »](convenience.html)

# Wrapper Implementations

Wrapper implementations delegate all their real work to a specified
collection but add extra functionality on top of what this collection
offers. For design pattern fans, this is an example of the
*decorator* pattern. Although it may seem a bit exotic,
it's really pretty straightforward.

These implementations are anonymous; rather than providing a public class,
the library provides a static factory method. All these implementations
are found in the
[`Collections`](http://download.oracle.com/javase/7/docs/api/java/util/Collections.html) class, which consists solely of static methods.

### Synchronization Wrappers

> The synchronization wrappers add automatic synchronization (thread-safety)
> to an arbitrary collection. Each of the six core collection interfaces —
> [`Collection`](http://download.oracle.com/javase/7/docs/api/java/util/Collection.html),
> [`Set`](http://download.oracle.com/javase/7/docs/api/java/util/Set.html),
> [`List`](http://download.oracle.com/javase/7/docs/api/java/util/List.html),
> [`Map`](http://download.oracle.com/javase/7/docs/api/java/util/Map.html),
> [`SortedSet`](http://download.oracle.com/javase/7/docs/api/java/util/SortedSet.html), and
> [`SortedMap`](http://download.oracle.com/javase/7/docs/api/java/util/SortedMap.html) — has one static factory method.
>
> ```
>
> public static <T> Collection<T>
>     synchronizedCollection(Collection<T> c);
> public static <T> Set<T>
>     synchronizedSet(Set<T> s);
> public static <T> List<T>
>     synchronizedList(List<T> list);
> public static <K,V> Map<K,V>
>     synchronizedMap(Map<K,V> m);
> public static <T> SortedSet<T>
>     synchronizedSortedSet(SortedSet<T> s);
> public static <K,V> SortedMap<K,V>
>     synchronizedSortedMap(SortedMap<K,V> m);
>
> ```
>
> Each of these methods returns a synchronized (thread-safe)
> `Collection` backed up by the specified collection.
> To guarantee serial access, *all* access to
> the backing collection must be accomplished through the returned
> collection. The easy way to guarantee this is not to keep a reference
> to the backing collection. Create the synchronized collection with the following trick.
>
> ```
>
> List<Type> list =
>     Collections.synchronizedList(new ArrayList<Type>());
>
> ```
>
> A collection created in this fashion is every bit as thread-safe
> as a normally synchronized collection, such as a
> [`Vector`](http://download.oracle.com/javase/7/docs/api/java/util/Vector.html).
>
> In the face of concurrent access, it is imperative that the user
> manually synchronize on the returned collection when iterating over it.
> The reason is that iteration is accomplished via multiple calls into the
> collection, which must be composed into a single atomic operation.
> The following is the idiom to iterate over a wrapper-synchronized collection.
>
> ```
>
> Collection<Type> c =
>     Collections.synchronizedCollection(myCollection);
> synchronized(c) {
>     for (Type e : c)
>         foo(e);
> }
>
> ```
>
> If an explicit iterator is used, the `iterator` method must be called
> from within the `synchronized` block. Failure to follow
> this advice may result in nondeterministic behavior.
> The idiom for iterating over a `Collection` view of a synchronized
> `Map` is similar. It is imperative that the user synchronize
> on the synchronized `Map` when iterating over any of its
> `Collection` views rather than synchronizing on the
> `Collection` view itself, as shown in the following example.
>
> ```
>
> Map<KeyType, ValType> m =
>     Collections.synchronizedMap(new HashMap<KeyType, ValType>());
>     ...
> Set<KeyType> s = m.keySet();
>     ...
> synchronized(m) {  // Synchronizing on m, not s!
>     while (KeyType k : s)
>         foo(k);
> }
>
> ```
>
> One minor downside of using wrapper implementations is that you
> do not have the ability to execute any *noninterface*
> operations of a wrapped implementation. So, for instance,
> in the preceding `List` example, you cannot call
> `ArrayList`'s
> [`ensureCapacity`](http://download.oracle.com/javase/7/docs/api/java/util/ArrayList.html#ensureCapacity(int)) operation on the wrapped `ArrayList`.

### Unmodifiable Wrappers

> Unlike synchronization wrappers, which add functionality to the wrapped
> collection, the unmodifiable wrappers take functionality away.
> In particular, they take away the ability to modify the collection
> by intercepting all the operations that would modify the collection
> and throwing an `UnsupportedOperationException`.
> Unmodifiable wrappers have two main uses, as follows:
>
> * To make a collection immutable once it has been built. In this case,
>   it's good practice not to maintain a reference to the backing collection.
>   This absolutely guarantees immutability.* To allow certain clients read-only access to your data structures.
>     You keep a reference to the backing collection but hand out a reference
>     to the wrapper. In this way, clients can look but not modify,
>     while you maintain full access.
>
> Like synchronization wrappers, each of the six core `Collection`
> interfaces has one static factory method.
>
> ```
>
> public static <T> Collection<T>
>     unmodifiableCollection(Collection<? extends T> c);
> public static <T> Set<T>
>     unmodifiableSet(Set<? extends T> s);
> public static <T> List<T>
>     unmodifiableList(List<? extends T> list);
> public static <K,V> Map<K, V>
>     unmodifiableMap(Map<? extends K, ? extends V> m);
> public static <T> SortedSet<T>
>     unmodifiableSortedSet(SortedSet<? extends T> s);
> public static <K,V> SortedMap<K, V>
>     unmodifiableSortedMap(SortedMap<K, ? extends V> m);
>
> ```

### Checked Interface Wrappers

> The `Collections.checked` *interface* wrappers
> are provided for use with generic collections. These implementations
> return a *dynamically* type-safe view of the specified collection,
> which throws a `ClassCastException` if a client attempts to
> add an element of the wrong type. The generics mechanism in the
> language provides compile-time (static) type-checking, but it is
> possible to defeat this mechanism. Dynamically type-safe views
> eliminate this possibility entirely.

[« Previous](queue.html)
•
[Trail](../TOC.html)
•
[Next »](convenience.html)

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

**Previous page:** Queue Implementations
  
**Next page:** Convenience Implementations




A browser with JavaScript enabled is required for this page to operate properly.