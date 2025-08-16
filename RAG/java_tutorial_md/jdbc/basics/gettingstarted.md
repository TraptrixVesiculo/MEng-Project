[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JDBC(TM) Database Access
  
**Lesson:** JDBC Basics

[JDBC Basics](index.html)

Getting Started

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

[Home Page](../../index.html)
>
[JDBC(TM) Database Access](../index.html)
>
[JDBC Basics](index.html)

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](processingsqlstatements.html)

# Getting Started

The sample code that comes with this tutorial creates a database that is used by a proprietor of a small coffee house called The Coffee Break, where coffee beans are sold by the pound and brewed coffee is sold by the cup.

The following steps configure a JDBC development environment with which you can compile and run the tutorial samples:

1. Install the latest version of the Java SE SDK on your computer.

   Ensure that the full directory path of the Java SE SDK `bin` directory is in your `PATH` environment variable so that you can run the Java compiler and the Java application launcher from any directory.
2. Install your database management system (DBMS) if needed.

   You may use Java DB, which comes with the latest version of Java SE SDK. This tutorial has been tested for the following DBMS:

   * [Java DB](http://developers.sun.com/javadb/)
   * [MySQL](http://www.mysql.com/)

   Note that if you are using another DBMS, you might have to alter the code of the tutorial samples.
3. Install a JDBC driver from the vendor of your database.

   If you are using Java DB, it already comes with a JDBC driver. If you are using MySQL, install the latest version of [Connector/J](http://www.mysql.com/products/connector/).

   To obtain a JDBC driver for a particular DBMS, refer to [JDBC Data Access API](http://developers.sun.com/product/jdbc/drivers).

   There are many possible implementations of JDBC drivers. These implementations are categorized as follows:

   * **Type 1**: Drivers that implement the JDBC API as a mapping to another data access API, such as ODBC (Open Database Connectivity). Drivers of this type are generally dependent on a native library, which limits their portability. The JDBC-ODBC Bridge is an example of a Type 1 driver.

     **Note**: The JDBC-ODBC Bridge should be considered a transitional solution. It is not supported by Oracle. Consider using this only if your DBMS does not offer a Java-only JDBC driver.
   * **Type 2**: Drivers that are written partly in the Java programming language and partly in native code. These drivers use a native client library specific to the data source to which they connect. Again, because of the native code, their portability is limited. Oracle's OCI (Oracle Call Interface) client-side driver is an example of a Type 2 driver.
   * **Type 3**: Drivers that use a pure Java client and communicate with a middleware server using a database-independent protocol. The middleware server then communicates the client's requests to the data source.
   * **Type 4**: Drivers that are pure Java and implement the network protocol for a specific data source. The client connects directly to the data source.

   Check which driver type comes with your DBMS. Java DB comes with two Type 4 drivers, an Embedded driver and a Network Client Driver. MySQL Connector/J is a Type 4 driver.

   Installing a JDBC driver generally consists of copying the driver to your computer, then adding the location of it to your class path. In addition, many JDBC drivers other than Type 4 drivers require you to install a client-side API. No other special configuration is usually needed.
4. Install Apache Ant.

   These steps use Apache Ant, a Java-based tool, to build, compile, and run the JDBC tutorial samples. Go to the following link to download Apache Ant:

   `http://ant.apache.org/`

   Ensure that the Apache Ant executable file is in your `PATH` environment variable so that you can run it from any directory.
5. Install Apache Xalan.

   The sample `RSSFeedsTable.java`, which is described in [Using SQLXML Objects](sqlxml.html), requires Apache Xalan if your DBMS is Java DB. The sample uses Apache Xalan-Java. Go to the following link to download it:

   `http://xml.apache.org/xalan-j/`
6. Download the sample code.

   The sample code, `JDBCTutorial.zip`, consists of the following files:

   * `properties`
     + `javadb-build-properties.xml`
     + `javadb-sample-properties.xml`
     + `mysql-build-properties.xml`
     + `mysql-sample-properties.xml`
   * `sql`
     + `javadb`
       - `create-procedures.sql`
       - `create-tables.sql`
       - `drop-tables.sql`
       - `populate-tables.sql`
     + `mysql`
       - `create-procedures.sql`
       - `create-tables.sql`
       - `drop-tables.sql`
       - `populate-tables.sql`
   * `src/com/oracle/tutorial/jdbc`
     + `CachedRowSetSample.java`
     + `CityFilter.java`
     + `ClobSample.java`
     + `CoffeesFrame.java`
     + `CoffeesTable.java`
     + `CoffeesTableModel.java`
     + `DatalinkSample.java`
     + `ExampleRowSetListener.java`
     + `FilteredRowSetSample.java`
     + `JdbcRowSetSample.java`
     + `JDBCTutorialUtilities.java`
     + `JoinSample.java`
     + `ProductInformationTable.java`
     + `RSSFeedsTable.java`
     + `StateFilter.java`
     + `StoredProcedureJavaDBSample.java`
     + `StoredProcedureMySQLSample.java`
     + `SuppliersTable.java`
     + `WebRowSetSample.java`
   * `txt`
     + `colombian-description.txt`
   * `xml`
     + `rss-coffee-industry-news.xml`
     + `rss-the-coffee-break-blog.xml`
   * `build.xml`

   Create a directory to contain all the files of the sample. These steps refer to this directory as `<JDBC tutorial directory>`. Unzip the contents of `JDBCTutorial.zip` into `<JDBC tutorial directory>`.

   - Modify the `build.xml` file.

     The `build.xml` file is the build file that Apache Ant uses to compile and execute the JDBC samples. The files `properties/javadb-build-properties.xml` and `properties/mysql-build-properties.xml` contain additional Apache Ant properties required for Java DB and MySQL, respectively. The files `properties/javadb-sample-properties.xml` and `properties/mysql-sample-properties.xml` contain properties required by the sample.

     Modify these XML files as follows:

     1. In the `build.xml` file, modify the property `ANTPROPERTIES` to refer to either `properties/javadb-build-properties.xml` or `properties/mysql-build-properties.xml`, depending on your DBMS. For example, if you are using Java DB, your `build.xml` file would contain this:

        ```

        <property name="ANTPROPERTIES" value="properties/javadb-build-properties.xml"/>

          <import file="${ANTPROPERTIES}"/>

        ```

        Similarly, if you are using MySQL, your `build.xml` file would contain this:

        ```

        <property name="ANTPROPERTIES" value="properties/mysql-build-properties.xml"/>

          <import file="${ANTPROPERTIES}"/>

        ```
     2. In the `properties/javadb-build-properties.xml` or `properties/mysql-build-properties.xml` file (depending on your DBMS), modify the following properties, as described in the following table:

        | Property | Description |
        | --- | --- |
        | `JAVAC` | The full path name of your Java compiler, `javac` |
        | `JAVA` | The full path name of your Java runtime executable, `java` |
        | `PROPERTIESFILE` | The name of the properties file, either `properties/javadb-sample-properties.xml` or `properties/mysql-sample-properties.xml` |
        | `MYSQLDRIVER` | The full path name of your MySQL driver. For Connector/J, this is typically `<Connector/J installation directory>/mysql-connector-java-version-number.jar`. |
        | `JAVADBDRIVER` | The full path name of your Java DB driver. This is typically `<Java DB installation directory>/lib/derby.jar`. |
        | `XALANDIRECTORY` | The full path name of the directory that contains Apache Xalan. |
        | `CLASSPATH` | The class path that the JDBC tutorial uses. *You do not need to change this value.* |
        | `XALAN` | The full path name of the file `xalan.jar`. |
        | `DB.VENDOR` | A value of either `derby` or `mysql` depending on whether you are using Java DB or MySQL, respectively. The tutorial uses this value to construct the URL required to connect to the DBMS and identify DBMS-specific code and SQL statements. |
        | `DB.DRIVER` | The fully qualified class name of the JDBC driver. For Java DB, this is `org.apache.derby.jdbc.EmbeddedDriver`. For MySQL, this is `com.mysql.jdbc.Driver`. |
        | `DB.HOST` | The host name of the computer hosting your DBMS. |
        | `DB.PORT` | The port number of the computer hosting your DBMS. |
        | `DB.SID` | The name of the database the tutorial creates and uses. |
        | `DB.URL.NEWDATABASE` | The connection URL used to connect to your DBMS when creating a new database. *You do not need to change this value.* |
        | `DB.URL` | The connection URL used to connect to your DBMS. *You do not need to change this value.* |
        | `DB.USER` | The name of the user that has access to create databases in the DBMS. |
        | `DB.PASSWORD` | The password of the user specified in `DB.USER`. |
        | `DB.DELIMITER` | The character used to separate SQL statements. *Do not change this value.* It should be the semicolon character (`;`). |- Modify the tutorial properties file.

       The tutorial samples use the values in either the `properties/javadb-sample-properties.xml` file or `properties/mysql-sample-properties.xml` file (depending on your DBMS) to connect to the DBMS and initialize databases and tables, as described in the following table:

       | Property | Description |
       | --- | --- |
       | `dbms` | A value of either `derby` or `mysql` depending on whether you are using Java DB or MySQL, respectively. The tutorial uses this value to construct the URL required to connect to the DBMS and identify DBMS-specific code and SQL statements. |
       | `jar_file` | The full path name of the JAR file that contains all the class files of this tutorial. |
       | `driver` | The fully qualified class name of the JDBC driver. For Java DB, this is `org.apache.derby.jdbc.EmbeddedDriver`. For MySQL, this is `com.mysql.jdbc.Driver`. |
       | `database_name` | The name of the database the tutorial creates and uses. |
       | `user_name` | The name of the user that has access to create databases in the DBMS. |
       | `password` | The password of the user specified in `user_name`. |
       | `server_name` | The host name of the computer hosting your DBMS. |
       | `port_number` | The port number of the computer hosting your DBMS. |
     - Compile and package the samples.

       At a command prompt, change the current directory to `<JDBC tutorial directory>`. From this directory, run the following command to compile the samples and package them in a jar file:

       ```
       ant jar
       ```
     - Create databases, tables, and populate tables.

       If you are using MySQL, then run the following command to create a database:

       ```
       ant create-mysql-database
       ```

       If you are using either Java DB or MySQL, then from the same directory, run the following command to delete existing sample database tables, recreate the tables, and populate them:

       ```
       ant setup
       ```

       **Note**: You should run the command `ant setup` every time before you run one of the Java classes in the sample. Many of these samples expect specific data in the contents of the sample's database tables.
     - Run the samples.

       Each target in the `build.xml` file corresponds to a Java class or SQL script in the JDBC samples. The following table lists the targets in the `build.xml` file, which class or script each target executes, and other classes or files each target requires:

       | Ant Target | Class or SQL Script | Other Required Classes or Files |
       | --- | --- | --- |
       | `javadb-create-procedure` | `javadb/create-procedures.sql`; see the `build.xml` file to view other SQL statements that are run | No other required files |
       | `mysql-create-procedure` | `mysql/create-procedures.sql`. | No other required files |
       | `run` | `JDBCTutorialUtilities` | No other required classes |
       | `runct` | `CoffeesTable` | `JDBCTutorialUtilities` |
       | `runst` | `SuppliersTable` | `JDBCTutorialUtilities` |
       | `runjrs` | `JdbcRowSetSample` | `JDBCTutorialUtilities` |
       | `runcrs` | `CachedRowSetSample`, `ExampleRowSetListener` | `JDBCTutorialUtilities` |
       | `runjoin` | `JoinSample` | `JDBCTutorialUtilities` |
       | `runfrs` | `FilteredRowSetSample` | `JDBCTutorialUtilities`, `CityFilter`, `StateFilter` |
       | `runwrs` | `WebRowSetSample` | `JDBCTutorialUtilities` |
       | `runclob` | `ClobSample` | `JDBCTutorialUtilities`, `txt/colombian-description.txt` |
       | `runrss` | `RSSFeedsTable` | `JDBCTutorialUtilities`, the XML files contained in the `xml` directory |
       | `rundl` | `DatalinkSample` | `JDBCTutorialUtilities` |
       | `runspjavadb` | `StoredProcedureJavaDBSample` | `JDBCTutorialUtilities`, `SuppliersTable`, `CoffeesTable` |
       | `runspmysql` | `StoredProcedureMySQLSample` | `JDBCTutorialUtilities`, `SuppliersTable`, `CoffeesTable` |
       | `runframe` | `CoffeesFrame` | `JDBCTutorialUtilities`, `CoffeesTableMode` |

       For example, to run the class `CoffeesTable`, change the current directory to `<JDBC tutorial directory>`, and from this directory, run the following command:

       ```

       ant runct

       ```

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](processingsqlstatements.html)

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

**Previous page:** JDBC Basics
  
**Next page:** Processing SQL Statements with JDBC




A browser with JavaScript enabled is required for this page to operate properly.