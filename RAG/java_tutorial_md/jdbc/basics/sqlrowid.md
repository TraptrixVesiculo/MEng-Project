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

[Using DISTINCT Data Type](distinct.html)

[Using Structured Objects](sqlstructured.html)

[Using Customized Type Mappings](sqlcustommapping.html)

[Using Datalink Objects](sqldatalink.html)

Using RowId Objects

[Using Stored Procedures](storedprocedures.html)

[Using JDBC with GUI API](jdbcswing.html)

[Home Page](../../index.html)
>
[JDBC(TM) Database Access](../index.html)
>
[JDBC Basics](index.html)

[« Previous](sqldatalink.html) • [Trail](../TOC.html) • [Next »](storedprocedures.html)

# Using RowId Objects

**Note**: MySQL and Java DB currently do not support the `RowId` JDBC interface. Consequently, no JDBC tutorial example is available to demonstrate the features described in this section.

A `RowId` object represents an address to a row in a database table. Note, however, that the `ROWID` type is not a standard SQL type. `ROWID` values can be useful because they are typically the fastest way to access a single row and are unique identifies for rows in a table. However, you should not use a `ROWID` value as the primary key of a table. For example, if you delete a particular row from a table, a database might reassign its `ROWID` value to a row inserted later.

The following topics are covered:

* [Retrieving RowId Objects](#retrieving_rowid_objects)
* [Using RowId Objects](#using_rowid_objects)
* [Lifetime of RowId Validity](#lifetime_rowid_validity)

## Retrieving RowId Objects

Retrieve a `java.sql.RowId` object by calling the getter methods defined in the interfaces `ResultSet` and
`CallableStatement`. The `RowId` object that is returned is an
immutable object that you can use for subsequent referrals as a unique identifier to a row. The following is an example of calling the `ResultSet.getRorId` method:

```

java.sql.RowId rowId_1 = rs.getRowId(1);

```

## Using RowId Objects

You can set a `RowId` object as a parameter in a parameterized `PreparedStatement` object:

```

Connection conn = ds.getConnection(user, passwd);
PreparedStatement ps = conn.prepareStatement("INSERT INTO BOOKLIST" + "(ID, AUTHOR, TITLE, ISBN) VALUES (?, ?, ?, ?)");
ps.setRowId(1, rowId_1);

```

You can also update a column with a specific `RowId` object in an updatable `ResultSet` object:

```

ResultSet rs = ...
rs.next();
rs.updateRowId(1, rowId_1);

```

A `RowId` object value is typically not portable between data sources and should be
considered as specific to the data source when using the set or update method in
`PreparedStatement` and `ResultSet` objects, respectively. It is therefore
inadvisable to get a `RowId` object from a `ResultSet` object with a connection to one data source and
then attempt to use the same `RowId` object in a unrelated `ResultSet` object with a connection to a different data source.

## Lifetime of RowId Validity

A `RowId` object is valid as long as the identified row is not deleted and the lifetime of the `RowId` object
is within the bounds of the lifetime specified by that the data source for the `RowId`.

To determine the lifetime of `RowId` objects of your database or data source, call the method `DatabaseMetaData.getRowIdLifetime`. It returns a value of a `RowIdLifetime` enumerated data type. The following method [`JDBCTutorialUtilities.rowIdLifeTime`](gettingstarted.html) returns the lifetime of `RowId` objects:

```

  public static void rowIdLifetime(Connection conn) throws SQLException {
    DatabaseMetaData dbMetaData = conn.getMetaData();
    RowIdLifetime lifetime = dbMetaData.getRowIdLifetime();
    switch (lifetime) {
    case ROWID_UNSUPPORTED:
      System.out.println("ROWID type not supported");
      break;
    case ROWID_VALID_FOREVER:
      System.out.println("ROWID has unlimited lifetime");
      break;
    case ROWID_VALID_OTHER:
      System.out.println("ROWID has indeterminate lifetime");
      break;
    case ROWID_VALID_SESSION:
      System.out.println("ROWID type has lifetime that is valid for at least the containing session");
    break;
    case ROWID_VALID_TRANSACTION:
      System.out.println("ROWID type has lifetime that is valid for at least the containing transaction");
    }
  }

```

[« Previous](sqldatalink.html)
•
[Trail](../TOC.html)
•
[Next »](storedprocedures.html)

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

**Previous page:** Using Datalink Objects
  
**Next page:** Using Stored Procedures




A browser with JavaScript enabled is required for this page to operate properly.