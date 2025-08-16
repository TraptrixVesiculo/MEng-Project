[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Deployment
  
**Lesson:** Applets
  
**Section:** Doing More With Applets
  
**Subsection:** Working With a Server-Side Application

[Applets](index.html)

[Getting Started With Applets](getStarted.html)

[Defining an Applet Subclass](subclass.html)

[Methods for Milestones](appletMethods.html)

[Life Cycle of an Applet](lifeCycle.html)

[Applet's Execution Environment](appletExecutionEnv.html)

[Developing an Applet](developingApplet.html)

[Deploying an Applet](deployingApplet.html)

[Deploying With the Applet Tag](html.html)

[Doing More With Applets](doingMoreWithApplets.html)

[Finding and Loading Data Files](data.html)

[Defining and Using Applet Parameters](param.html)

[Displaying Short Status Strings](showStatus.html)

[Displaying Documents in the Browser](browser.html)

[Invoking JavaScript Code From an Applet](invokingJavaScriptFromApplet.html)

[Invoking Applet Methods From JavaScript Code](invokingAppletMethodsFromJavaScript.html)

[Manipulating DOM of Applet's Web Page](manipulatingDOMFromApplet.html)

[Displaying a Customized Loading Progress Indicator](customProgressIndicatorForApplet.html)

[Writing Diagnostics to Standard Output and Error Streams](stdout.html)

[Developing Draggable Applets](draggableApplet.html)

[Communicating With Other Applets](iac.html)

[Working With a Server-Side Application](server.html)

Network Client Applet Example

[What Applets Can and Cannot Do](security.html)

[Solving Common Applet Problems](problemsindex.html)

[Questions and Exercises](QandE/questions.html)

[Home Page](../../index.html)
>
[Deployment](../index.html)
>
[Applets](index.html)

[« Previous](server.html) • [Trail](../TOC.html) • [Next »](security.html)

# Network Client Applet Example

The
[`QuoteClientApplet`](examples/QuoteClientApplet.java) class allows you to fetch quotations from a server-side application that runs on the same host as
this applet. This class also displays the quotation received from the server.

The
[`QuoteServer.java`](examples/QuoteServer.java) and
[`QuoteServerThread.java`](examples/QuoteServerThread.java) classes make up the server-side application that returns quotations.
Here's a text file (
[`one-liners.txt`](examples/one-liners.txt)) that contains a number of quotations.

Perform the following steps to test `QuoteClientApplet`.

1. Download and save the following files to your local machine.
   * [`QuoteClientApplet`](examples/QuoteClientApplet.java)
   * [`QuoteServer.java`](examples/QuoteServer.java)
   * [`QuoteServerThread.java`](examples/QuoteServerThread.java)
   * [`one-liners.txt`](examples/one-liners.txt)
   * [`quoteApplet.html`](examples/quoteApplet.html)
2. Include the following HTML code in a web page to deploy `QuoteClientApplet`.

   ```

   <script src="http://www.java.com/js/deployJava.js"></script>
   <script> 
       var attributes = { code:'QuoteClientApplet.class',  width:500, height:100} ; 
       var parameters = {codebase_lookup:'true'};
       deployJava.runApplet(attributes, parameters, '1.6'); 
   </script>


   ```

   Alternatively, you can use the
   [`quoteApplet.html`](examples/quoteApplet.html) page that already contains this HTML code.
3. Compile the `QuoteClientApplet.java` class. Copy the
   generated class files to the
   same directory where you saved your web page.
4. Compile the classes for the server-side application,
   `QuoteServer.java` and `QuoteServerThread.java`.
5. Copy the file `one-liners.txt` to the directory that has the
   class files for the server-side application (generated in the previous step).
6. Start the server-side application.

   ```

   java QuoteServer

   ```

   You should see a message with the port number, as shown in the following example.
   Note the port number.

   ```

   QuoteServer listening on port:3862

   ```
7. Open the web page containing your applet in a browser by entering the URL
   of the web page. The host name in the URL should be the same as the name of the host on which
   the server-side application is running.

   For example, if the server-side application is running on a machine
   named `JohnDoeMachine`,
   you should enter a similar URL. The exact port number and path will vary
   depending on your web server setup.

   ```

   http://JohnDoeMachine:8080/quoteApplet/quoteApplet.html

   ```

   The `QuoteClientApplet` will be displayed on the web page.
8. Enter the port number of your server-side application in the applet's
   text field and click OK. A quotation is displayed.

Here is a screen capture of the applet in action.

![QuoteServer Sample Output](../../figures/deployment/applet/19quote.png)

**`QuoteServer` Sample Output**

[« Previous](server.html)
•
[Trail](../TOC.html)
•
[Next »](security.html)

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

**Previous page:** Working With a Server-Side Application
  
**Next page:** What Applets Can and Cannot Do




A browser with JavaScript enabled is required for this page to operate properly.