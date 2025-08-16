[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Java Management Extensions (JMX)
  
**Lesson:** Remote Management

[Remote Management](index.html)

[Exposing a Resource for Remote Management By JConsole](jconsole.html)

Creating a Custom JMX Client

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)
>
[Remote Management](index.html)

[« Previous](jconsole.html) • [Trail](../TOC.html) • [Next »](../end.html)

# Creating a Custom JMX Client

The previous lessons in this trail have shown you how to create JMX technology MBeans and MXBeans, and register them with a JMX agent. However, all the previous examples have used an existing JMX client, JConsole. This lesson will demonstrate how to create your own custom JMX client.

An example of a custom JMX client,
[`Client`](../examples/Client.java)
is included in
[`jmx_examples.zip`](../examples/jmx_examples.zip). This JMX client interacts with the same MBean, MXBean and JMX agent as were seen in the previous lessons. Due to the size of the `Client` class, it will be examined in chunks, in the following sections.

## Importing the JMX Remote API Classes

To be able to create connections to JMX agents that are running remotely from the JMX client, you need to use the classes from the
[`javax.management.remote`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/package-summary.html).

```


package com.example;

[...]

import javax.management.remote.JMXConnector;
import javax.management.remote.JMXConnectorFactory;
import javax.management.remote.JMXServiceURL;

public class Client {

    [...]


```

The `Client` class will be creating
[`JMXConnector`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXConnector.html)
instances, for which it will need a
[`JMXConnectorFactory`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXConnectorFactory.html)
and a
[`JMXServiceURL`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXServiceURL.html).

## Creating a Notification Listener

The JMX client needs a notification handler, to listen for and to process any notifications that might be sent by the MBeans that are registered in the JMX agent's MBean server. The JMX client's notification handler is an instance of the
[`NotificationListener`](http://download.oracle.com/javase/7/docs/api/javax/management/NotificationListener.html)
interface, as shown below.

```


    [...]
    
    
    public static class ClientListener implements NotificationListener {
        public void handleNotification(Notification notification,
                                       Object handback) {
            echo("\nReceived notification:");
            echo("\tClassName: " + notification.getClass().getName());
            echo("\tSource: " + notification.getSource());
            echo("\tType: " + notification.getType());
            echo("\tMessage: " + notification.getMessage());
            if (notification instanceof AttributeChangeNotification) {
                AttributeChangeNotification acn =
                    (AttributeChangeNotification) notification;
                echo("\tAttributeName: " + acn.getAttributeName());
                echo("\tAttributeType: " + acn.getAttributeType());
                echo("\tNewValue: " + acn.getNewValue());
                echo("\tOldValue: " + acn.getOldValue());
            }
        }
    }
    
    [...]
        


```

This notification listener determines the origin of any notifications it receives, and retrieves the information stored in the notification. It then performs different actions with the notification information according to the type of notification received. In this case, when the listener receives notifications of the type
[`AttributeChangeNotification`](http://download.oracle.com/javase/7/docs/api/javax/management/AttributeChangeNotification.html) it will obtain the name and type of the MBean attribute that has changed, as well as its old and new values, by calling the `AttributeChangeNotification` methods `getAttributeName`, `getAttributeType`, `getNewValue` and `getOldValue`.

A new `ClientListener` instance is created by later in the code.

```

 
 ClientListener listener = new ClientListener();


```

## Creating an RMI Connector Client

The `Client` class creates an RMI connector client that is configured to connect to an RMI connector server that you will launch when you start the JMX agent, `Main`. This will allow the JMX client to interact with the JMX agent as if they were running on the same machine.

```


    [...]
    
    public static void main(String[] args) throws Exception {

        echo("\nCreate an RMI connector client and " +
             "connect it to the RMI connector server");
        JMXServiceURL url =
            new JMXServiceURL("service:jmx:rmi:///jndi/rmi://:9999/jmxrmi");
        JMXConnector jmxc = JMXConnectorFactory.connect(url, null);

	[...]
	
	

```

As you can see, the `Client` defines a
[`JMXServiceURL`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXServiceURL.html)
named `url`, that represents the location at which the connector client expects to find the connector server. This URL allows the connector client to retrieve the RMI connector server stub `jmxrmi` from the RMI registry running on port 9999 of the local host, and to connect to the RMI connector server.

With the RMI registry thus identified, the connector client can be created. The connector client, `jmxc`, is an instance of the interface
[`JMXConnector`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXConnector.html), created by the `connect()` method of
[`JMXConnectorFactory`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXConnectorFactory.html). The `connect()` method is passed the parameters `url` and a null environment map when it is called.

## Connecting to the Remote MBean Server

With the RMI connection in place, the JMX client must connect to the remote MBean server, so that it can interact with the various MBeans registered in it by the remote JMX agent.

```


        [...]
	
        MBeanServerConnection mbsc = jmxc.getMBeanServerConnection();
		
        [...]
	



```

An instance of
[`MBeanServerConnection`](http://download.oracle.com/javase/7/docs/api/javax/management/MBeanServerConnection.html), named mbsc, is then created by calling the `getMBeanServerConnection()` method of the `JMXConnector` instance `jmxc`.

The connector client is now connected to the MBean server created by the JMX agent, and can register MBeans and perform operations on them with the connection remaining completely transparent to both ends.

To start with, the client defines some simple operations to discover information about the MBeans found in the agent's MBean server.

```


        [...]
	
        echo("\nDomains:");
        String domains[] = mbsc.getDomains();
        Arrays.sort(domains);
        for (String domain : domains) {
            echo("\tDomain = " + domain);
        }
	
        [...]
	
        echo("\nMBeanServer default domain = " + mbsc.getDefaultDomain());

        echo("\nMBean count = " + mbsc.getMBeanCount());
        echo("\nQuery MBeanServer MBeans:");
        Set names =
            new TreeSet(mbsc.queryNames(null, null));
        for (ObjectName name : names) {
            echo("\tObjectName = " + name);
        }
	
	[...]
	

```

The client calls various methods of `MBeanServerConnection` in order to obtain the domains in which the different MBeans are operating, the number of MBeans registered in the MBean server, and the object names for each of the MBeans it discovers.

## Performing Operations on Remote MBeans via Proxies

The client accesses the `Hello` MBean in the MBean server through the MBean server connection by creating an MBean **proxy**. This MBean proxy is local to the client, and emulates the remote MBean.

```


        [...]

        ObjectName mbeanName = new ObjectName("com.example:type=Hello");

        HelloMBean mbeanProxy =
            JMX.newMBeanProxy(mbsc, mbeanName, HelloMBean.class, true);

        echo("\nAdd notification listener...");
	mbsc.addNotificationListener(mbeanName, listener, null, null);

        echo("\nCacheSize = " + mbeanProxy.getCacheSize());

        mbeanProxy.setCacheSize(150);

        echo("\nWaiting for notification...");
        sleep(2000);

        echo("\nCacheSize = " + mbeanProxy.getCacheSize());
        echo("\nInvoke sayHello() in Hello MBean...");
        mbeanProxy.sayHello();

        echo("\nInvoke add(2, 3) in Hello MBean...");
        echo("\nadd(2, 3) = " + mbeanProxy.add(2, 3));

        waitForEnterPressed();
	
	[...]
	

```

MBean proxies allow you to access an MBean through a Java interface, allowing you to make calls on the proxy rather than having to write lengthy code to access a remote MBean. An MBean proxy for `Hello` is created here by calling the method `newMBeanProxy()` in the
[`javax.management.JMX`](http://download.oracle.com/javase/7/docs/api/javax/management/JMX.html) class, passing it the MBean's `MBeanServerConnection`, object name, the class name of the MBean interface and `true`, to signify that the proxy must behave as a
[`NotificationBroadcaster`](http://download.oracle.com/javase/7/docs/api/javax/management/NotificationBroadcaster.html). The JMX client can now perform the operations defined by `Hello` as if they were the operations of a locally registered MBean. The JMX client also adds a notification listener and changes the MBean's `CacheSize` attribute, to make it send a notification.

## Performing Operations on Remote MXBeans via Proxies

You can create proxies for MXBeans in exactly the same way as you create MBean proxies.

```

	[...]
	
        ObjectName mxbeanName =
            new ObjectName("com.example:type=QueueSampler");
        QueueSamplerMXBean mxbeanProxy =
            JMX.newMXBeanProxy(mbsc, mxbeanName, QueueSamplerMXBean.class);
        QueueSample queue1 = mxbeanProxy.getQueueSample();
        echo("\nQueueSample.Date = " + queue1.getDate());
        echo("QueueSample.Head = " + queue1.getHead());
        echo("QueueSample.Size = " + queue1.getSize());
        echo("\nInvoke clearQueue() in QueueSampler MXBean...");
        mxbeanProxy.clearQueue();

        QueueSample queue2 = mxbeanProxy.getQueueSample();
        echo("\nQueueSample.Date = " + queue2.getDate());
        echo("QueueSample.Head = " + queue2.getHead());
        echo("QueueSample.Size = " + queue2.getSize());

	[...]


```

As shown above, to create a proxy for an MXBean, all you have to do is call
[`JMX.newMXBeanProxy`](http://download.oracle.com/javase/7/docs/api/javax/management/JMX.html#newMXBeanProxy(javax.management.MBeanServerConnection,%20javax.management.ObjectName,%20java.lang.Class)) instead of `newMBeanProxy`. The MXBean proxy `mxbeanProxy` allows the client to invoke the `QueueSample` MXBean's operations as if they were the operations of a locally registered MXBean.

## Closing the Connection

Once the JMX client has obtained all the information it needs and performed all the required operations on the MBeans in the remote JMX agent's MBean server, the connection must be closed down.

```


        jmxc.close();


```

The connection is closed with a call to the
[`JMXConnector.close`](http://download.oracle.com/javase/7/docs/api/javax/management/remote/JMXConnector.html#close())
method.

### To Run the Custom JMX Client Example

This example requires version 6 of the Java SE platform. To monitor the `Main` JMX agent remotely using a the custom JMX client
[`Client`](../examples/Client.java), follow these steps:

1. If you have not done so already, save
   [`jmx_examples.zip`](../examples/jmx_examples.zip) into your `work_dir` directory.
2. Unzip the bundle of sample classes by using the following command in a terminal window.

   ```

   unzip jmx_examples.zip

   ```
3. Compile the example Java classes from within the `work_dir` directory.

   ```

   javac com/example/*.java

   ```
4. Start the `Main` application, specifying the properties that expose `Main` for remote management:

   ```

   java -Dcom.sun.management.jmxremote.port=9999
        -Dcom.sun.management.jmxremote.authenticate=false
        -Dcom.sun.management.jmxremote.ssl=false 
        com.example.Main

   ```

   A confirmation that `Main` is waiting for something to happen is generated.
5. Start the `Client` application in a different terminal window:

   ```

   java com.example.Client

   ```

   A confirmation that an `MBeanServerConnection` has been obtained is displayed.
6. Press Enter.

   The domains in which all the MBeans that are registered in the MBean server started by `Main` are displayed.
7. Press Enter again.

   The number of MBeans that are registered in the MBean server is displayed, as well as the object names of all these MBeans. The MBeans displayed include all the standard platform MXBeans running in the Java VM, as well as the `Hello` MBean and the `QueueSampler` MXBean that were registered in the MBean server by `Main`.
8. Press Enter again.

   The `Hello` MBean's operations are invoked by `Client`, with the following results:
   * A notification listener is added to `Client` to listen for notifications from `Main`.
   * The value of the `CacheSize` attribute is changed from 200 to 150.
   * In the terminal window in which you started `Main`, confirmation of the `CacheSize` attribute change is displayed.
   * In the terminal window in which you started `Client`, a notification from `Main` is displayed, informing `Client` of the `CacheSize` attribute change.
   * The `Hello` MBean's `sayHello` operation is invoked.
   * In the terminal window in which you started `Main`, the message "Hello world" is displayed.
   * The `Hello` MBean's `add` operation is invoked, with the values 2 and 3 as parameters. The result is displayed by `Client`.
9. Press Enter again.

   The `QueueSampler` MXBean's operations are invoked by `Client`, with the following results:
   * The `QueueSample` values `date`, `head`, and `size` are displayed.
   * The `clearQueue` operation is invoked.
10. Press Enter again.

    The `Client` closes the connection to the MBean server and a confirmation is displayed.

[« Previous](jconsole.html)
•
[Trail](../TOC.html)
•
[Next »](../end.html)

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

**Previous page:** Exposing a Resource for Remote Management By JConsole
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.