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

Sort Control

[Manage Referral Control](mdsaIT.html)

[Manipulating LdapName (Distinguished Name)](ldapname.html)

[Manipulating Relative Distringuished Name (RDN)](rdn.html)

[Setting Timeout for Ldap Operations](readtimeout.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[New features in JDK 5.0 and JDK 6](index.html)

[« Previous](paged-results.html) • [Trail](../TOC.html) • [Next »](mdsaIT.html)

# Sort Control

The sort control is used when a client wants the server
to send the sorted search results. The server-side sorting
is useful in a situation where the client needs to sort the results
according to some criteria but is not equipped to perform
the sort process on its own.
The sort control is specified in [RFC 2891](http://ietf.org/rfc/rfc2891.txt).
The classes below provide the functionality required to support
sort control.

* [javax.naming.ldap.SortControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/SortControl.html)* [javax.naming.ldap.SortKey](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/SortKey.html)* [javax.naming.ldap.SortResponseControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/SortResponseControl.html)

The SortKey is an odered list of keys based upon which the server
sorts the result.

##### How to use Sort Control?

The example below illustrates the client-server interaction
between a client performing a search requesting a server-side sorting based
on the attribute "cn".

1. Client sends a search request asking for

   ```

      
       // Activate sorting
        String sortKey = "cn";
        ctx.setRequestControls(new Control[] { 
            new SortControl(sortKey, Control.CRITICAL) });

        // Perform a search
        NamingEnumeration results =
            ctx.search("", "(objectclass=*)", new SearchControls());

      
   ```

   - The server responds with entries that are sorted
     based on the "cn" attribute and its corresponding matching rule.

     ```

        
         // Iterate over sorted search results
          while (results != null && results.hasMore()) {
              // Display an entry
              SearchResult entry = (SearchResult)results.next();
              System.out.println(entry.getName());

              // Handle the entry's response controls (if any)
              if (entry instanceof HasControls) {
                  // ((HasControls)entry).getControls();
              }
          }
          // Examine the sort control response 
          Control[] controls = ctx.getResponseControls();
          if (controls != null) {
              for (int i = 0; i < controls.length; i++) {
                  if (controls[i] instanceof SortResponseControl) {
                      SortResponseControl src = (SortResponseControl)controls[i];
                      if (! src.isSorted()) {
                          throw src.getException();
                      }
                  } else {
                      // Handle other response controls (if any)
                  }
              }
          }	
         
         
     ```

     The complete JNDI example can be found [here](examples/SortedResults.java)

     ---

     **Note:**
     The sort control is supported by both Sun Java Directory Server and the
     Windows Active Directory server.

     ---

[« Previous](paged-results.html)
•
[Trail](../TOC.html)
•
[Next »](mdsaIT.html)

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

**Previous page:** Paged Results Control
  
**Next page:** Manage Referral Control




A browser with JavaScript enabled is required for this page to operate properly.