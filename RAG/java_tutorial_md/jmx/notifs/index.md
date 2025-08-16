[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)

**Trail:** Java Management Extensions (JMX)

[Home Page](../../index.html)
>
[Java Management Extensions (JMX)](../index.html)

[« Previous](../mbeans/index.html) • [Trail](../TOC.html) • [Next »](../remote/index.html)

# Lesson: Notifications

The JMX API defines a mechanism to enable MBeans to generate notifications, for example, to signal a state change, a detected event, or a problem.

To generate notifications, an MBean must implement the interface
[`NotificationEmitter`](http://download.oracle.com/javase/7/docs/api/javax/management/NotificationEmitter.html) or extend
[`NotificationBroadcasterSupport`](http://download.oracle.com/javase/7/docs/api/javax/management/NotificationBroadcasterSupport.html). To send a notification, you need to construct an instance of the class
[`javax.management.Notification`](http://download.oracle.com/javase/7/docs/api/javax/management/Notification.html) or a subclass (such as
[`AttributeChangedNotification`](http://download.oracle.com/javase/7/docs/api/javax/management/AttributeChangeNotification.html)), and pass the instance to
[`NotificationBroadcasterSupport.sendNotification`](http://download.oracle.com/javase/7/docs/api/javax/management/NotificationBroadcasterSupport.html#sendNotification(javax.management.Notification).

Every notification has a source. The source is the object name of the MBean that generated the notification.

Every notification has a sequence number. This number can be used to order notifications coming from the same source when order matters and there is a risk of the notifications being handled in the wrong order. The sequence number can be zero, but preferably the number increments for each notification from a given MBean.

The
[`Hello`](../examples/Hello.java)
MBean implementation in
[Standard MBeans](../../jmx/mbeans/standard.html)
actually implements the notification mechanism. However, this code was omitted in that lesson for the sake of simplicity. The complete code for `Hello` follows:

```


package com.example; 
 
import javax.management.*; 
 
public class Hello 
        extends NotificationBroadcasterSupport implements HelloMBean { 
 
    public void sayHello() { 
        System.out.println("hello, world"); 
    } 
 
    public int add(int x, int y) { 
        return x + y; 
    } 
 
    public String getName() { 
        return this.name; 
    } 
 
    public int getCacheSize() { 
        return this.cacheSize; 
    } 
 
    public synchronized void setCacheSize(int size) { 
        int oldSize = this.cacheSize; 
        this.cacheSize = size; 
 
        System.out.println("Cache size now " + this.cacheSize); 
 
        Notification n = 
            new AttributeChangeNotification(this, 
					    sequenceNumber++, 
					    System.currentTimeMillis(), 
					    "CacheSize changed", 
					    "CacheSize", 
					    "int", 
					    oldSize, 
					    this.cacheSize); 
 
	sendNotification(n); 
    } 
 
    @Override 
    public MBeanNotificationInfo[] getNotificationInfo() { 
        String[] types = new String[] { 
            AttributeChangeNotification.ATTRIBUTE_CHANGE 
        }; 
        String name = AttributeChangeNotification.class.getName(); 
        String description = "An attribute of this MBean has changed"; 
        MBeanNotificationInfo info = 
            new MBeanNotificationInfo(types, name, description); 
        return new MBeanNotificationInfo[] {info}; 
    } 
 
    private final String name = "Reginald"; 
    private int cacheSize = DEFAULT_CACHE_SIZE; 
    private static final int DEFAULT_CACHE_SIZE = 200; 
 
    private long sequenceNumber = 1; 
} 



```

This `Hello` MBean implementation extends the `NotificationBroadcasterSupport` class. `NotificationBroadcasterSupport` implements the `NotificationEmitter` interface.

The operations and attributes are set in the same way as in the standard MBean example, with the exception that the `CacheSize` attribute's setter method now defines a value of `oldSize`. This value records the `CacheSize` attribute's value prior to the set operation.

The notification is constructed from an instance, `n`, of the JMX class `AttributeChangeNotification`, which extends `javax.management.Notification`. The notification is constructed within the definition of the `setCacheSize()` method from the following information. This information is passed to `AttributeChangeNotification` as parameters.

* The object name of the source of the notification, namely the `Hello` MBean, represented by `this`
* A sequence number, namely `sequenceNumber`, that is set to 1 and that increases incrementally
* A timestamp
* The content of the notification message
* The name of the attribute that has changed, in this case, `CacheSize`
* The type of attribute that has changed
* The old attribute value, in this case, `oldSize`
* The new attribute value, in this case, `this.cacheSize`

The notification `n` is then passed to the `NotificationBroadcasterSupport.sendNotification()` method.

Finally, the
[`MBeanNotificationInfo`](http://download.oracle.com/javase/7/docs/api/javax/management/MBeanNotificationInfo.html) instance is defined to describe the characteristics of the different notification instances generated by the MBean for a given type of notification. In this case the type of notifications sent is `AttributeChangeNotification` notifications.

## Running the MBean Notification Example

Once again, you will use JConsole to interact with the `Hello` MBean, this time to send and receive
notifications. This example requires version 6 of the Java SE platform.

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
4. Start the `Main` application.

   ```

   java com.example.Main

   ```

   A confirmation that `Main` is waiting for something to happen is generated.
5. Start JConsole in a different terminal window on the same machine.

   ```

   jconsole

   ```

   The New Connection dialog box is displayed, presenting a list of running JMX agents that you can connect to.
6. In the New Connection dialog box, select `com.example.Main` from the list and click Connect.

   A summary of your platform's current activity is displayed.
7. Click the MBeans tab.

   This panel shows all the MBeans that are currently registered in the MBean server.
8. In the left frame, expand the `com.example` node in the MBean tree.

   You see the example MBean `Hello` that was created and registered by `Hello`. If you click `Hello`, you see its Notifications node in the MBean tree.
9. Expand the Notifications node of the `Hello` MBean in the MBean tree.

   Note that the panel is blank.
10. Click the Subscribe button.

    The current number of notifications received (0) is displayed in the Notifications node label.
11. Expand the Attributes node of the `Hello` MBean in the MBean tree, and change the value of the `CacheSize` attribute to 150.

    In the terminal window in which you started `Main`, a confirmation of this attribute change is displayed. Note that the number of received notifications displayed in the Notifications node has changed to 1.
12. Expand again the Notifications node of the `Hello` MBean in the MBean tree.

    The details of the notification are displayed.
13. To close JConsole, select Connection -> Exit.

[« Previous](../mbeans/index.html)
•
[Trail](../TOC.html)
•
[Next »](../remote/index.html)

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
  
**Next page:** Remote Management




A browser with JavaScript enabled is required for this page to operate properly.