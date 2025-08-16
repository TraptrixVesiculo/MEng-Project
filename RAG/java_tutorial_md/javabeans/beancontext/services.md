[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** JavaBeans(TM)
  
**Lesson:** Using the BeanContext API

[Using the BeanContext API](index.html)

[Overview of the BeanContext API](overview.html)

[Bean Context #1: Containment Only](containment.html)

Bean Context #2: Containment and Services

[AWT Containers and the BeanContextProxy Interface](gui.html)

[Home Page](../../index.html)
>
[JavaBeans(TM)](../index.html)
>
[Using the BeanContext API](index.html)

[« Previous](containment.html) • [Trail](../TOC.html) • [Next »](gui.html)

# Bean Context #2: Containment and Services

As mentioned in the introduction, the `BeanContext` API also provides a
standard mechanism through which JavaBeans can discover and utilize the
services offered by their enclosing `BeanContext`.
Service capability is defined by the
`BeanContextServices`
interface. Because this interface is a `BeanContext` extension, it inherits all
`BeanContext` membership capabilities.
The discovery and
requesting of services can be summarized in the following steps:

1. A JavaBean that implements the
   [`java.beans.beancontext.BeanContextServicesListener`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesListener.html) interface joins the bean context (the context itself
   is a `BeanContextServices` implementation),
   and registers its intent to be notified of new services via the context's
   [`addBeanContextServicesListener(BeanContextServicesListener bcsl)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServices.html#addBeanContextServicesListener(java.beans.beancontext.BeanContextServicesListener)) method.- A
     [`java.beans.beancontext.BeanContextServiceProvider`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceProvider.html) registers
     a new service with the context via the
     context's `addService()` method. The context notifies
     all currently registered listeners that this new service has been added.- After being notified of the newly available service,
       the listening JavaBean requests an instance of the service
       from the context.- The context tells the service provider to deliver the service to the requesting JavaBean.

**BeanContextServices: Service Related Methods**

Using a
[`java.beans.beancontext.BeanContextServicesSupport`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html) object as the bean context, it is possible to:

* Add a service to this `BeanContext`:
  [`boolean addService(java.lang.Class serviceClass, BeanContextServiceProvider serviceProvider)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#addService(java.lang.Class, java.beans.beancontext.BeanContextServiceProvider))* Add a service to this `BeanContext`:
    [`boolean addService(Class serviceClass, BeanContextServiceProvider bcsp, boolean fireEvent)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#addService(java.lang.Class, java.beans.beancontext.BeanContextServiceProvider, boolean))* Revoke a service:
      [`void revokeService(java.lang.Class serviceClass, BeanContextServiceProvider serviceProvider, boolean revokeCurrentServicesNow)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#revokeService(java.lang.Class, java.beans.beancontext.BeanContextServiceProvider, boolean))* Release a `BeanContextChild`'s (or any arbitrary object associated with a `BeanContextChild`) reference to the specified service:
        [`void releaseService(BeanContextChild child, java.lang.Object requestor, java.lang.Object service)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#releaseService(java.beans.beancontext.BeanContextChild, java.lang.Object, java.lang.Object))* Add a `BeanContextServicesListener`
          [`void addBeanContextServicesListener(BeanContextServicesListener bcsl)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#addBeanContextServicesListener(java.beans.beancontext.BeanContextServicesListener))* Remove a `BeanContextServicesListener`:
            [`void removeBeanContextServicesListener(BeanContextServicesListener bcsl)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#removeBeanContextServicesListener(java.beans.beancontext.BeanContextServicesListener))* Get the currently available services for this context:
              [`Iterator getCurrentServiceClasses()`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#getCurrentServiceClasses())* Determine whether or not a given service is currently available from this context:
                [`boolean hasService(java.lang.Class serviceClass)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#hasService(java.lang.Class))* Get a service from the context:
                  [`Object getService(BeanContextChild child, java.lang.Object requestor, java.lang.Class serviceClass, java.lang.Object serviceSelector, BeanContextServiceRevokedListener bcsrl)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#getService(java.beans.beancontext.BeanContextChild, java.lang.Object, java.lang.Class, java.lang.Object, java.beans.beancontext.BeanContextServiceRevokedListener))* Get the list of service dependent service parameters (Service Selectors) for the specified service:
                    [`Iterator getCurrentServiceSelectors(java.lang.Class serviceClass)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServicesSupport.html#getCurrentServiceSelectors(java.lang.Class))

**Service Event Notification**

JavaBeans nested into a `BeanContextServices` implement `BeanContextServicesListener`
to listen for new services
being added, and/or `BeanContextServiceRevokedListener` to listen for services being revoked.

There are two event types that may be intercepted by such listeners:

* [`BeanContextServiceAvailableEvent`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceAvailableEvent.html): received by the `BeanContextServicesListener` in
  order to identify the service being registered.* [`BeanContextServiceRevokedEvent`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceRevokedEvent.html): received by the
    `BeanContextServiceRevokedListener` in order to identify the
    service being revoked.

**The Service Provider**

JavaBeans can query their enclosing bean context for a list of available services, or ask for a specific service
by name. The service itself, however, is actually delivered by a `BeanContextServiceProvider`.
The provider can be any object that implements the
[`java.beans.beancontext.BeanContextServiceProvider`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceProvider.html) interface. Services
become available in a context via the bean context's addService() registration method.

BeanContextServiceProvider offers the following three methods, which will be automatically called when a bean requests (or releases) a service from its context:

* [`Object getService(BeanContextServices bcs, java.lang.Object requestor, java.lang.Class serviceClass, java.lang.Object serviceSelector)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceProvider.html#getService(java.beans.beancontext.BeanContextServices, java.lang.Object, java.lang.Class, java.lang.Object))* [`Iterator getCurrentServiceSelectors(BeanContextServices bcs, java.lang.Class serviceClass)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceProvider.html#getCurrentServiceSelectors(java.beans.beancontext.BeanContextServices, java.lang.Class))* [`public void releaseService(BeanContextServices bcs, java.lang.Object requestor, java.lang.Object service)`](http://download.oracle.com/javase/7/docs/api/java/beans/beancontext/BeanContextServiceProvider.html#releaseService(java.beans.beancontext.BeanContextServices, java.lang.Object, java.lang.Object)) Release a service from any object that currently has a reference to it

**The Service**

The service itself is best described by this paragraph from the specification:

*A service, represented by a Class object,
is typically a reference to either an interface,
or to an implementation
that is not publicly instantiable.
This Class defines an interface protocol or contract
between a BeanContextServiceProvider,
the factory of the service,
and an arbitrary object associated with a BeanContextChild
that is currently
nested within the BeanContext the service is registered with.*

The following section presents a sample application that uses a word
counting service to count the number of words in a given text file.

## A Word Counting Service Example

The classes defined in this sample application are:

* [`DocumentBean.java`](examples/DocumentBean.java): A JavaBean that encapsulates a `File` object. Create an instance of this bean by passing it
  a `String` indicating the name of the text file to represent. This bean extends `BeanContextChildSupport`, which allows
  it to listen for addition/revocation of services in its context. When the bean detects that a
  `WordCount` service
  has been added to the context, it requests the service to count the number of words it contains.* [`WordCountServiceProvider.java`](examples/WordCountServiceProvider.java): A class that acts as the
    factory for delivering the `WordCount` service. This
    class implements the `BeanContextServiceProvider` interface.* [`WordCount.java`](examples/WordCount.java): This interface defines the service itself.* [`DocumentTester.java`](examples/DocumentTester.java): The main test program.

**File:
[`DocumentBean.java`](examples/DocumentBean.java)**

```


import java.beans.beancontext.*;
import java.io.*;
import java.util.*;

public final class DocumentBean extends BeanContextChildSupport {

    private File document; 
    private BeanContextServices context;

    public DocumentBean(String fileName) {
        document = new File(fileName);
    }

    public void serviceAvailable(BeanContextServiceAvailableEvent bcsae) {
        System.out.println("[Detected a service being added to the context]");

        // Get a reference to the context
        BeanContextServices context = bcsae.getSourceAsBeanContextServices();
        System.out.println("Is the context offering a WordCount service? "
                           + context.hasService(WordCount.class)); 

        // Use the service, if it's available
        if (context.hasService(WordCount.class)) {        
            System.out.println("Attempting to use the service...");
            try {
                WordCount service = (WordCount)context.getService(this, this,
		                                           WordCount.class, document, this);
                System.out.println("Got the service!");
                service.countWords();
            } catch(Exception e) { }
        }        
    }

    public void serviceRevoked(BeanContextServiceRevokedEvent bcsre) {
        System.out.println("[Detected a service being revoked from the context]");
    }
}

```

**File:
[`WordCountServiceProvider.java`](examples/WordCountServiceProvider.java)**

```


import java.beans.beancontext.*;
import java.util.*;
import java.io.*;

public final class WordCountServiceProvider implements BeanContextServiceProvider {

    public Object getService(BeanContextServices bcs, 
                             Object requestor,
                             Class serviceClass,
                             Object serviceSelector) {

        // For this demo, we know that the cast from serviceSelector
        // to File will always work.
        final File document = (File)serviceSelector;

        return new WordCount() {
            public void countWords() {
                try {
                    // Create a Reader to the DocumentBean's File
                    BufferedReader br = new BufferedReader(new FileReader(document));
                    String line = null;
                    int wordCount = 0;
                    while ((line = br.readLine()) != null) {
                        StringTokenizer st = new StringTokenizer(line);
                        while (st.hasMoreTokens()) {
                            System.out.println("Word " + (++wordCount)
                                               + " is: " + st.nextToken());
                        }
                    }
                    System.out.println("Total number of words in the document: "
                                       + wordCount);
                    System.out.println("[WordCount service brought to you by WordCountServiceProvider]");                
                    br.close();
                 } catch(Exception e) { }
            }
        };
    }

    public void releaseService(BeanContextServices bcs,
                               Object requestor,
                               Object service) {
        // do nothing
    }

    public Iterator getCurrentServiceSelectors(BeanContextServices bcs, Class serviceClass) {
        return null; // do nothing
    }
}

```

**File:
[`WordCount.java`](examples/WordCount.java)**

```


public interface WordCount {

     public abstract void countWords();

}

```

**File:
[`DocumentTester.java`](examples/DocumentTester.java)**

```


import java.beans.beancontext.*;
import java.util.*;

public class DocumentTester {

     public static void main(String[] args) {       
          BeanContextServicesSupport context = new BeanContextServicesSupport(); // a bean context
          DocumentBean doc1 = new DocumentBean("Test.txt"); 
          context.add(doc1);
          context.addBeanContextServicesListener(doc1); // listen for new services
          WordCountServiceProvider provider = new WordCountServiceProvider();
          context.addService(WordCount.class, provider); // add the service to the context
     }
}

```

**File:
[`Test.txt`](examples/Test.txt)**

```

This   text will  be analyzed  
 
 by the WordCount 

service.

```

**Output:**

```

[Detected a service being added to the context]
Is the context offering a WordCount service? true
Attempting to use the service...
Got the service!
Word 1 is: This
Word 2 is: text
Word 3 is: will
Word 4 is: be
Word 5 is: analyzed
Word 6 is: by
Word 7 is: the
Word 8 is: WordCount
Word 9 is: service.
Total number of words in the document: 9
[WordCount service brought to you by WordCountServiceProvider]

```

[« Previous](containment.html)
•
[Trail](../TOC.html)
•
[Next »](gui.html)

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

**Previous page:** Bean Context #1: Containment Only
  
**Next page:** AWT Containers and the BeanContextProxy Interface




A browser with JavaScript enabled is required for this page to operate properly.