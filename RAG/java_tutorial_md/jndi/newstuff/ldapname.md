[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Naming and Directory Interface(TM).
  
**Lesson:** New features in JDK 5.0 and JDK 6

[New features in JDK 5.0 and JDK 6](index.html)

[Retrieving Distinguished Name](dn.html)

[Standard LDAP Controls](controls-std.html)

[Paged Results Control](paged-results.html)

[Sort Control](sort.html)

[Manage Referral Control](mdsaIT.html)

Manipulating LdapName (Distinguished Name)

[Manipulating Relative Distringuished Name (RDN)](rdn.html)

[Setting Timeout for Ldap Operations](readtimeout.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[New features in JDK 5.0 and JDK 6](index.html)

[« Previous](mdsaIT.html) • [Trail](../TOC.html) • [Next »](rdn.html)

# Manipulating LdapName (Distinguished Name)

The Distinguished Name (DN) is used by LDAP in its string
representation.
The string format used to represent a DN is specified in
 [RFC2253](http://ietf.org/rfc/rfc2253.txt).
The DN is made up of components called the Relative Distinguished Names
(RDN).
Below is an example of a DN:

"CN=Steve Kille, O=Isode Limited, C=GB"

It consist of the following RDNs:

* CN=Steve Kille* O=Isode Limited* C=GB

The classes below that are available in JDK 5.0 represent the DN and
RDN respectively.

* [javax.naming.ldap.LdapName](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html)* [javax.naming.ldap.Rdn](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/Rdn.html)

The LdapName class implements the
[javax.naming.Name](http://download.oracle.com/javase/7/docs/api/javax/naming/Name.html) interface similar to the
[javax.naming.CompoundName](http://download.oracle.com/javase/7/docs/api/javax/naming/Name.html) and
[javax.naming.CompositeName](http://download.oracle.com/javase/7/docs/api/javax/naming/CompositeName.html) classes.

LdapName and Rdn classes allow easy manipulation of DNs and RDNs. Using these APIs
it's easy to construct an RDN by pairing up names and values. A DN can be
constructed with a list of RDNs. Similarly the individual components
of DN and RDN can be retrieved from their string representation.

### LdapName

An LdapName can be created with its string representation as defined in
 [RFC2253](http://ietf.org/rfc/rfc2253.txt) or with a list of Rdns.
When the former way is used, the specified string is parsed as per the
rules defined in RFC2253. An
[InvalidNameException](http://download.oracle.com/javase/7/docs/api/javax/naming/InvalidNameException.html)
is thrown if the string is not a valid DN.
Here's an example that uses the constructor to parse an LDAP name and
print its components.

```

    
    String name = "cn=Mango,ou=Fruits,o=Food";
    try {
        LdapName dn = new LdapName(name);
        System.out.println(dn + " has " + dn.size() + " RDNs: ");
        for (int i = 0; i < dn.size(); i++) {
    	    System.out.println(dn.get(i));
        }
    } catch (InvalidNameException e) {
        System.out.println("Cannot parse name: " + name);
    }
    
```

Running this example with an input of "cn=Mango,ou=Fruits,o=Food" produces the following results:

```

    
    cn=Mango,ou=Fruits,o=Food has 3 RDNs: 
    o=Food
    ou=Fruits
    cn=Mango
    
```

The LdapName class contains methods to access its components as RDNs and strings,
to modify an LdapName, to compare two LdapNames for equality,
and to get a string representation of the name.

#### Accessing the name components of an LDAP name:

Here are the methods that you can use to access the name components as RDNs and strings:

[getRdn(int posn)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getRdn(int))  
[get(int posn)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#get(int))  
[getRdns()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getRdns())  
[getAll()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getAll())  
[getPrefix(int posn)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getPrefix(int posn))  
[getSuffix(int posn)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getSuffix(int posn))  
[clone()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#clone())

To retrieve the component at a particular position within an LdapName, you use getRdn() or get().
The previous constructor example shows an example of its use.
[getRdns()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getRdns())
returns a list of all the RDNs and
[getAll()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getAll())
returns all of the components of an LdapName
as an enumeration.

The right most RDN is at index 0, and the left most RDN is at
index n-1. For example, the distinguished name:
"cn=Mango, ou=Fruits, o=Food" is numbered in the following
sequence ranging from 0 to 2: {o=Food, ou=Fruits, cn=Mango} 

You can also get a LdapNames's suffix or prefix as a LdapName instance.
Here's an [example](examples/LdapNameSuffixPrefix.java)
that gets the suffix and prefix of an LDAP name.

```

    
    LdapName dn = new LdapName("cn=Mango, ou=Fruits, o=Food");
    Name suffix = dn.getSuffix(1);  // 1 <= index < cn.size()
    Name prefix = dn.getPrefix(1);  // 0 <= index < 1
    
```

When you run this program, it generates the following output:

```

    
        cn=Mango ou=Fruits
        o=Food 
    
```

To make a copy of an LdapName, you use clone().

#### Modifying an LDAP name

Following are the methods that you can use to modify an LDAP name:

[add(Rdn rdn)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#add(Rdn))  
[add(String comp)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#add(String))  
[add(int posn, String comp)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#add(int, String))  
[addAll(List suffixRdns)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#addAll(List))  
[addAll(Name suffix)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#addAll(Name suffix))  
[addAll(int posn, List suffixRdns)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#addAll(int, List))  
[addAll(int posn, Name suffix)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#addAll(int, Name))  
[remove(int posn)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#remove(int))

After creating an LdapName instance, you can add and remove components from it.
Here's an  [example](examples/ModifyLdapName.java) that appends an
LdapName to an existing LdapName,
adds components to the front and the end, and removes the second component.

```

    
     LdapName dn = new LdapName("ou=Fruits,o=Food");
     LdapName dn2 = new LdapName("ou=Summer");
     System.out.println(dn.addAll(dn2)); // ou=Summer,ou=Fruits,o=Food
     System.out.println(dn.add(0, "o=Resources")); // ou=Summer,ou=Fruits,o=Food,o=Resources
     System.out.println(dn.add("cn=WaterMelon")); // cn=WaterMelon,ou=Summer,ou=Fruits,o=Food,o=Resources
     System.out.println(dn.remove(1));  // o=Food
     System.out.println(dn);  // cn=WaterMelon,ou=Summer,ou=Fruits,o=Resources
    
```

#### Comparing an LDAP name

Following are the methods that you can use to compare two LDAP names:

[compareTo(Object name)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#compareTo(Object))  
[equals(Object name)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#equals(Object))  
[endsWith(List)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#endsWith(List))  
[endWith(Name name)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#endsWith(Name))  
[startsWith(List rdns)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#startsWith(iList))  
[startsWith(Name name)](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#startsWith(Name))  
[isEmpty()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#isEmpty())

You can use compareTo() to sort a list of LdapName instances.
equals() lets you determine whether two LdapNames are syntactically equal.
Two LdapNames are equal if they both have the same (case-exact matched)
components in the same order.

With startsWith() and endsWith(), you can learn whether an LdapName starts
or ends with another LdapName; that is, whether an LdapName is a suffix or
prefix of another LdapName.

The convenience method isEmpty() enables you to determine whether an
LdapName has zero components. You can also use the expression size() == 0 to perform the same check.

Here is an [example](examples/CompareLdapNames.java) that
uses some of these comparison methods.

```

    
    LdapName one = new LdapName("cn=Vincent Ryan, ou=People, o=JNDITutorial");
    LdapName two = new LdapName("cn=Vincent Ryan");
    LdapName three = new LdapName("o=JNDITutorial");
    LdapName four = new LdapName("");

    System.out.println(one.equals(two)); 	// false
    System.out.println(one.startsWith(three));  // true
    System.out.println(one.endsWith(two));      // true
    System.out.println(one.startsWith(four));   // true
    System.out.println(one.endsWith(four));     // true
    System.out.println(one.endsWith(three));    // false
    System.out.println(one.isEmpty());	        // false
    System.out.println(four.isEmpty());	        // true
    System.out.println(four.size() == 0);	// true
    
```

#### Getting the String Representation

The method below gets you the string representation of an LDAP name
formatted according to the syntax specified in RFC2253:

[toString()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#toString())

When you use the LdapName constructor, you supply the string representation of an LDAP name
and get back an LdapName instance. To do the reverse, that is, to get the string representation
of an LdapName instance, you use toString(). The result of toString() can be fed back to the
constructor to produce a LdapName instance that is equal to the original LdapName instance.
Here's an  [example](examples/LdapNametoString.java).

```

    
    LdapName dn = new LdapName(name);
    String str = dn.toString();
    System.out.println(str);
    LdapName dn2 = new LdapName(str);
    System.out.println(dn.equals(dn2));	 // true
    
```

#### LdapName as an Argument to Context Methods

The Context method require either a composite or a compound name passed as
argument to its methods.
Hence an LdapName can be directly passed to a context method as shown in the
 [example](examples/LookupLdapName.java) below:

```

    
    // Create the initial context
    Context ctx = new InitialContext(env);

    // An LDAP name
    LdapName dn = new LdapName("ou=People,o=JNDITutorial");

    // Perform the lookup using the dn
    Object obj = ctx.lookup(dn);

    
```

Similarly, when the Context methods return results from list(), listBindings(), or
search() operations, the DN can be retrieved by calling
[getNameInNamespace()](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/LdapName.html#getNameInNamepspace()). The LdapName can be constructed directly from the DN as shown in the
 [example](examples/RetrievingLdapName.java) below:

```

    
     while (answer.hasMore()) {
         SearchResult sr = (SearchResult) answer.next();
         String name = sr.getNameInNamespace();
         System.out.println(name);
         LdapName dn = new LdapName(name);

	 // do something with the dn
     }
    
```

[« Previous](mdsaIT.html)
•
[Trail](../TOC.html)
•
[Next »](rdn.html)

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

**Previous page:** Manage Referral Control
  
**Next page:** Manipulating Relative Distringuished Name (RDN)




A browser with JavaScript enabled is required for this page to operate properly.