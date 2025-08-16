[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

JDBC Basics

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

[Using DISTINCT Data Type](distinct.html)

[Using Structured Objects](sqlstructured.html)

[Using Customized Type Mappings](sqlcustommapping.html)

[Using Datalink Objects](sqldatalink.html)

[Using RowId Objects](sqlrowid.html)

[Using Stored Procedures](storedprocedures.html)

[Using JDBC with GUI API](jdbcswing.html)

**Trail:** JDBC(TM) Database Access

[Home Page](../../index.html)
>
[JDBC(TM) Database Access](../index.html)

[« Previous](../overview/index.html) • [Trail](../TOC.html) • [Next »](gettingstarted.html)

# Lesson: JDBC Basics

In this lesson you will learn the basics of the JDBC API.

* [Getting Started](gettingstarted.html) sets up a basic database development environment and shows you how to compile and run the JDBC tutorial samples.
* [Processing SQL Statements with JDBC](processingsqlstatements.html) outlines the steps required to process any SQL statement. The pages that follow describe these steps in more detail:

  + [Establishing a Connection](connecting.html) connects you to your database.
  + [Connecting with DataSource Objects](sqldatasources.html) shows you how to connect to your database with `DataSource` objects, the preferred way of getting a connection to a data source.
  + [Handling SQLExceptions](sqlexception.html) shows you how to handle exceptions caused by database errors.
  + [Setting Up Tables](tables.html) describes all the database tables used in the JDBC tutorial samples and how to create and populate tables with JDBC API and SQL scripts.
  + [Retrieving and Modifying Values from Result Sets](retrieving.html) develop the process of configuring your database, sending queries, and retrieving data from your database.
  + [Using Prepared Statements](prepared.html) describes a more flexible way to create database queries.
  + [Using Transactions](transactions.html) shows you how to control when a database query is actually executed.
* [Using RowSet Objects](rowset.html) introduces you to `RowSet` objects; these are objects that hold tabular data in a way that make it more flexible and easier to use than result sets. The pages that follow describe the different kinds of `RowSet` objects available:

  + [Using JdbcRowSet Objects](jdbcrowset.html)
  + [Using CachedRowSetObjets](cachedrowset.html)
  + [Using JoinRowSet Objects](joinrowset.html)
  + [Using FilteredRowSet Objects](filteredrowset.html)
  + [Using WebRowSet Objects](webrowset.html)
* [Using Advanced Data Types](sqltypes.html) introduces you to other data types; the pages that follow describe these data types in further detail:

  + [Using Large Objects](blob.html)
  + [Using SQLXML Objects](sqlxml.html)
  + [Using Array Objects](array.html)
  + [Using DISTINCT Data Type](distinct.html)
  + [Using Structured Objects](sqlstructured.html)
  + [Using Customized Type Mappings](sqlcustommapping.html)
  + [Using Datalink Objects](sqldatalink.html)
  + [Using RowId Objects](sqlrowid.html)
* [Using Stored Proceduresshows you how to create and use a stored procedure, which is a group of SQL statements that can be called like a Java method with variable input and output parameters.](storedprocedures.html)
* [Using JDBC with GUI API](jdbcswing.html) demonstrates how to integrate JDBC with the Swing API.

[« Previous](../overview/index.html)
•
[Trail](../TOC.html)
•
[Next »](gettingstarted.html)

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

**Previous page:** Previous Lesson
  
**Next page:** Getting Started




A browser with JavaScript enabled is required for this page to operate properly.