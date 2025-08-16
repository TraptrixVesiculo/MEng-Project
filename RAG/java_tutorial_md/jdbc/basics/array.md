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

Using Array Objects

[Using DISTINCT Data Type](distinct.html)

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

[« Previous](sqlxml.html) • [Trail](../TOC.html) • [Next »](distinct.html)

# Using Array Objects

**Note**: MySQL and Java DB currently do not support the `ARRAY` SQL data type. Consequently, no JDBC tutorial example is available to demonstrate the `Array` JDBC data type.

The following topics are covered:

* [Creating Array Objects](#creating_array)
* [Retrieving and Accessing Array Values in ResultSet](#retrieving_array)
* [Storing and Updating Array Objects](#storing_array)
* [Initializing Array Objects](#initializing_array)
* [Releasing Array Resources](#releasing_array)

## Creating Array Objects

Use the method `Connection.createArrayOf` to create `Array` objects.

For example, suppose your database contains a table named `REGIONS`, which has been created and populated with the following SQL statements; note that the syntax of these statements will vary depending on your database:

```

create table REGIONS
  (REGION_NAME varchar(32) NOT NULL,
  ZIPS varchar32 ARRAY[10] NOT NULL,
  PRIMARY KEY (REGION_NAME));

insert into REGIONS values ('Northwest', '{"93101", "97201", "99210"}');
insert into REGIONS values ('Southwest', '{"94105", "90049", "92027"}');

```

```

Connection con = DriverManager.getConnection(url, props);
String [] northEastRegion = {"10022", "02110", "07399"};
Array aArray = con.createArrayOf("VARCHAR", northEastRegionnewYork);

```

The Oracle Database JDBC driver implements the `java.sql.Array` interface with the `oracle.sql.ARRAY` class.

## Retrieving and Accessing Array Values in ResultSet

As with the JDBC 4.0 large object interfaces (`Blob`, `Clob`, `NClob`), you can manipulate `Array` objects without having to bring all of their data from the database server to your client computer. An `Array` object materializes the SQL `ARRAY` it represents as either a result set or a Java array.

The following excerpt retrieves the SQL `ARRAY` value in the column `ZIPS` and assigns it to the `java.sql.Array` object `z` object. The excerpt retrieves the contents of `z` and stores it in `zips`, a Java array that contains objects of type `String`. The excerpt iterates through the `zips` array and checks that each postal (zip) code is valid. This code assumes that the class `ZipCode` has been defined previously with the method `isValid` returning `true` if the given zip code matches one of the zip codes in a master list of valid zip codes:

```


  ResultSet rs = stmt.executeQuery(
                    "SELECT region_name, zips FROM REGIONS");
  while (rs.next()) {
    Array z = rs.getArray("ZIPS");
    String[] zips = (String[])z.getArray();
    for (int i = 0; i < zips.length; i++) {
      if (!ZipCode.isValid(zips[i])) {
        // ...
        // Code to display warning
      }
    }
  }


```

In the following statement, the `ResultSet` method `getArray` returns the value stored in the column `ZIPS` of the current row as the `java.sql.Array` object `z`:

```


  Array z = rs.getArray("ZIPS");


```

The variable `z` contains a locator, which is a logical pointer to the SQL `ARRAY` on the server; it does not contain the elements of the `ARRAY` itself. Being a logical pointer, `z` can be used to manipulate the array on the server.

In the following line, `getArray` is the `Array.getArray` method, not the `ResultSet.getArray` method used in the previous line. Because the `Array.getArray` method returns an `Object` in the Java programming language and because each zip code is a `String` object, the result is cast to an array of `String` objects before being assigned to the variable `zips`.

```


  String[] zips = (String[])z.getArray();


```

The `Array.getArray` method materializes the SQL `ARRAY` elements on the client as an array of `String` objects. Because, in effect, the variable `zips` contains the elements of the array, it is possible to iterate through `zips` in a `for` loop, looking for zip codes that are not valid.

## Storing and Updating Array Objects

Use the methods `PreparedStatement.setArray` and `PreparedStatement.setObject` to pass an `Array` value as an input parameter to a `PreparedStatement` object.

The following example sets the `Array` object `northEastRegion` (created in a previous example) as the second parameter to the PreparedStatement `pstmt`:

```

PreparedStatement pstmt =
  con.prepareStatement("insert into REGIONS (region_name, zips) VALUES (?, ?)");
pstmt.setString(1, "NorthEast");
pstmt.setArray(2, northEastRegion);
pstmt.executeUpdate();

```

Similarly, use the methods `PreparedStatement.updateArray` and `PreparedStatement.updateObject` to update a column in a table with an `Array` value.

## Releasing Array Resources

`Array` objects remain valid for at least the duration of the transaction in which they are created. This could potentially result in an application running out of resources during a long running transaction. Applications may release `Array` resources by invoking their `free` method.

In the following excerpt, the method `Array.free` is called to release the resources held for a previously created `Array` object.

```

  Array aArray = con.createArrayOf("VARCHAR", northEastRegionnewYork);
  // ...
  aArray.free();

```

[« Previous](sqlxml.html)
•
[Trail](../TOC.html)
•
[Next »](distinct.html)

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

**Previous page:** Using SQLXML Objects
  
**Next page:** Using DISTINCT Data Type




A browser with JavaScript enabled is required for this page to operate properly.