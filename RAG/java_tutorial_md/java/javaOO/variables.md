[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Learning the Java Language
  
**Lesson:** Classes and Objects
  
**Section:** Classes

[Classes and Objects](index.html)

[Classes](classes.html)

[Declaring Classes](classdecl.html)

Declaring Member Variables

[Defining Methods](methods.html)

[Providing Constructors for Your Classes](constructors.html)

[Passing Information to a Method or a Constructor](arguments.html)

[Objects](objects.html)

[Creating Objects](objectcreation.html)

[Using Objects](usingobject.html)

[More on Classes](more.html)

[Returning a Value from a Method](returnvalue.html)

[Using the this Keyword](thiskey.html)

[Controlling Access to Members of a Class](accesscontrol.html)

[Understanding Instance and Class Members](classvars.html)

[Initializing Fields](initial.html)

[Summary of Creating and Using Classes and Objects](summaryclasses.html)

[Questions and Exercises](QandE/creating-questions.html)

[Questions and Exercises](QandE/objects-questions.html)

[Nested Classes](nested.html)

[Inner Class Example](innerclasses.html)

[Summary of Nested Classes](summarynested.html)

[Questions and Exercises](QandE/nested-questions.html)

[Enum Types](enum.html)

[Questions and Exercises](QandE/enum-questions.html)

[Annotations](annotations.html)

[Questions and Exercises](QandE/annotations-questions.html)

[Home Page](../../index.html)
>
[Learning the Java Language](../index.html)
>
[Classes and Objects](index.html)

[« Previous](classdecl.html) • [Trail](../TOC.html) • [Next »](methods.html)

# Declaring Member Variables

There are several kinds of variables:

* Member variables in a class—these are called *fields*.
* Variables in a method or block of code—these are called *local variables*.
* Variables in method declarations—these are called *parameters*.

The `Bicycle` class uses the following lines of code to define its fields:

```

public int cadence;
public int gear;
public int speed;

```

Field declarations are composed of three components, in order:

1. Zero or more modifiers, such as `public` or `private`.
2. The field's type.
3. The field's name.

The fields of `Bicycle` are named `cadence`, `gear`, and `speed` and
are all of data type integer (`int`). The `public` keyword identifies these fields as public members, accessible by
any object that can access the class.

### Access Modifiers

The first (left-most) modifier used lets you control what other classes have access to a member field. For the moment,
consider only `public` and `private`. Other access modifiers will be discussed later.

* `public` modifier—the field is accessible from all classes.
* `private` modifier—the field is accessible only within its own class.

In the spirit of encapsulation, it is common to make fields private. This means that they can only be *directly*
accessed from the Bicycle class. We still need access to these values, however. This can be done *indirectly* by adding public methods that obtain the field values for us:

```

public class Bicycle {
	
	private int cadence;
	private int gear;
	private int speed;
	
	public Bicycle(int startCadence, int startSpeed, int startGear) {
		gear = startGear;
		cadence = startCadence;
		speed = startSpeed;
	}
	
	public int getCadence() {
		return cadence;
	}
	
	public void setCadence(int newValue) {
		cadence = newValue;
	}
	
	public int getGear() {
		return gear;
	}
	
	public void setGear(int newValue) {
		gear = newValue;
	}
	
	public int getSpeed() {
		return speed;
	}
	
	public void applyBrake(int decrement) {
		speed -= decrement;
	}
	
	public void speedUp(int increment) {
		speed += increment;
	}
	
}

```

### Types

All variables must have a type. You can use primitive types such as `int`,
`float`, `boolean`, etc. Or you can use
reference types, such as strings, arrays, or objects.

### Variable Names

All variables, whether they are fields, local variables, or parameters, follow the same naming
rules and conventions that were covered in the Language Basics
lesson,
[Variables—Naming](../../java/nutsandbolts/variables.html#naming) .

In this
lesson,
be aware that the same naming rules and conventions are used for method and class names, except that

* the first letter of a class name should be capitalized, and
* the first (or only) word in a method name should be a verb.

[« Previous](classdecl.html)
•
[Trail](../TOC.html)
•
[Next »](methods.html)

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

**Previous page:** Declaring Classes
  
**Next page:** Defining Methods




A browser with JavaScript enabled is required for this page to operate properly.