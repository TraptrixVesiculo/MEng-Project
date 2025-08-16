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

Paged Results Control

[Sort Control](sort.html)

[Manage Referral Control](mdsaIT.html)

[Manipulating LdapName (Distinguished Name)](ldapname.html)

[Manipulating Relative Distringuished Name (RDN)](rdn.html)

[Setting Timeout for Ldap Operations](readtimeout.html)

[Home Page](../../index.html)
>
[Java Naming and Directory Interface(TM).](../index.html)
>
[New features in JDK 5.0 and JDK 6](index.html)

[« Previous](controls-std.html) • [Trail](../TOC.html) • [Next »](sort.html)

# Paged Results Control

#### BasicControl

The
[javax.naming.ldap.BasicControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/BasicControl.html) which implements the javax.naming.ldap.Control
serves as a base implementation for extending other controls.

#### Paged Results Control

The paged results control is useful for LDAP clients which
want to receive search results in a controlled manner limited
by the page size.
The page size can be configured by the client as per the availability
of its resources, like bandwidth and the processing capability.

The server uses a cookie (similar to the HTTP session cookie mechanism)
to maintain the state of the search requests in order to track the
results being sent to the client.
The paged results control is specified in
[RFC 2696](http://ietf.org/rfc/rfc2696.txt).
The classes below provide the functionality required to support
paged results control.

* [javax.naming.ldap.PagedResultsControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/PagedResultsControl.html)* [javax.naming.ldap.PagedResultsResponseControl](http://download.oracle.com/javase/7/docs/api/javax/naming/ldap/PagedResultsResponseControl.html)

##### How to use Paged Results Control?

The example below illustrates the client-server interaction
between a client doing a search requesting a page size limit of 5.
The entire result set returned by the server contains 21 entries.

1. Client sends a search request asking for paged results with a page size of 5.

   ```

      
       // Activate paged results
        int pageSize = 5; // 5 entries per page
        byte[] cookie = null;
        int total;
        ctx.setRequestControls(new Control[]{ 
            new PagedResultsControl(pageSize, Control.CRITICAL) });
        // Perform the search
        NamingEnumeration results =
            ctx.search("", "(objectclass=*)", new SearchControls());
       
       
   ```

   - The server responds with entries plus an indication
     of 21 total entries in the search result and an opaque
     cookie to be used by the client when retrieving subsequent
     pages.

     ```

        
        // Iterate over a batch of search results sent by the server
              while (results != null && results.hasMore()) {
                  // Display an entry
                  SearchResult entry = (SearchResult)results.next();
                  System.out.println(entry.getName());

                  // Handle the entry's response controls (if any)
                  if (entry instanceof HasControls) {
                      // ((HasControls)entry).getControls();
                  }
              }
        // Examine the paged results control response 
              Control[] controls = ctx.getResponseControls();
              if (controls != null) {
                  for (int i = 0; i < controls.length; i++) {
                      if (controls[i] instanceof PagedResultsResponseControl) {
                          PagedResultsResponseControl prrc =
                              (PagedResultsResponseControl)controls[i];
                          total = prrc.getResultSize();
                          cookie = prrc.getCookie();
                      } else {
                          // Handle other response controls (if any)
                      }
                  }
              }   
         
         
     ```

     - Client sends an identical search request, returning the opaque cookie, asking for
       the next page.

       ```

          
         // Re-activate paged results
                ctx.setRequestControls(new Control[]{
                    new PagedResultsControl(pageSize, cookie, Control.CRITICAL) });
          
          
       ```

       - Server responds with five entries plus an indication
         that there are more entries
         The client repeats the search performed in step 4 until a null cookie is returned
         by the server, which indicates no more entries to be sent by the server.

The complete JNDI example can be found [here](examples/PagedSearch.java).

---

**Note:**
The Paged Search Control is supported by the Windows Active Directory Server.
It's not supported by the Sun Java Directory Server version 5.2

---

[« Previous](controls-std.html)
•
[Trail](../TOC.html)
•
[Next »](sort.html)

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

**Previous page:** Standard LDAP Controls
  
**Next page:** Sort Control




A browser with JavaScript enabled is required for this page to operate properly.