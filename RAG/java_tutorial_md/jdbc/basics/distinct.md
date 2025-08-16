[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JDBC(TM) Database Access
  
**Lesson:** JDBC Basics

[JDBC Basics](index.html)

[Getting Started](gettingstarted.html)

[Processing SQL Statements with JDBC](processingsqlstatements.html)

[Establishing a Connection](connecting.html)

[Connecting with DataSource Objects](sqldatasources.html)

[Handling SQLExceptions](sqlexception.html)

[Setting Up Tables](tables.html)

[Retrieving and Modifying Values from Result Sets](retrieving.html)

[Using Prepared Statements](prepared.html)

[Using Transactions](transactions.html)

[Using RowSet Objects](rowset.html)

[Using JdbcRowSet Objects](jdbcrowset.html)

[Using CachedRowSetObjects](cachedrowset.html)

[Using JoinRowSet Objects](joinrowset.html)

[Using FilteredRowSet Objects](filteredrowset.html)

[Using WebRowSet Objects](webrowset.html)

[Using Advanced Data Types](sqltypes.html)

[Using Large Objects](blob.html)

[Using SQLXML Objects](sqlxml.html)

[Using Array Objects](array.html)

Using DISTINCT Data Type

[Using Structured Objects](sqlstructured.html)

[Using Customized Type Mappings](sqlcustommapping.html)

[Using Datalink Objects](sqldatalink.html)

[Using RowId Objects](sqlrowid.html)

[Using Stored Procedures](storedprocedures.html)

[Using JDBC with GUI API](jdbcswing.html)

[Home Page](../../index.html)
>
[JDBC(TM) Database Access](../index.html)
>
[JDBC Basics](index.html)

[« Previous](array.html) • [Trail](../TOC.html) • [Next »](sqlstructured.html)

# Using DISTINCT Data Type

**Note**: MySQL and Java DB currently do not support the `DISTINCT` SQL data type. Consequently, no JDBC tutorial example is available to demonstrate the features described in this section.

The `DISTINCT` data type behaves differently from the other advanced SQL data types.
Being a user-defined type that is based on one of the already existing built-in
types, it has no interface as its mapping in the Java programming language.
Instead, the standard mapping for a `DISTINCT` data type is the Java
type to which its underlying SQL data type maps.

To illustrate, create a `DISTINCT` data type and then see how to
retrieve, set, or update it. Suppose you always use a two-letter abbreviation
for a state and want to create a `DISTINCT` data type to be used for
these abbreviations. You could define your new `DISTINCT` data type with
the following SQL statement:

```

CREATE TYPE STATE AS CHAR(2);

```

Some databases use an alternate syntax for creating a `DISTINCT` data type,
which is shown in the following line of code:

```

CREATE DISTINCT TYPE STATE AS CHAR(2);

```

If one syntax does not work, you can try the other. Alternatively, you can check the
documentation for your driver to see the exact syntax it expects.

These statements create a new data type, `STATE`, which can be
used as a column value or as the value for an attribute of a SQL structured
type. Because a value of type `STATE` is in reality a value that
is two `CHAR` types, you use the same method to retrieve it that you
would use to retrieve a `CHAR` value, that is, `getString`.
For example, assuming that the fourth column of `ResultSet rs` stores values of type `STATE`, the following
line of code retrieves its value:

```

String state = rs.getString(4);

```

Similarly, you would use the method `setString` to store a `STATE` value in the database and the method `updateString` to modify its value.

[« Previous](array.html)
•
[Trail](../TOC.html)
•
[Next »](sqlstructured.html)

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

**Previous page:** Using Array Objects
  
**Next page:** Using Structured Objects




A browser with JavaScript enabled is required for this page to operate properly.