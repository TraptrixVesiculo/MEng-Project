[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Implementing Your Own Permission

[Implementing Your Own Permission](index.html)

[TerrysGame](game.html)

[The HighScore Class](highscore.html)

The HighScorePermission Class

[A Sample Policy File](policy.html)

[Putting It All Together](together.html)

[Steps for the HighScore Developer (Chris)](chris.html)

[Steps for the TerrysGame Developer (Terry)](terry.html)

[Steps for a User Running TerrysGame (Kim)](kim.html)

[Home Page](../../index.html)
>
[Security Features in Java SE](../index.html)
>
[Implementing Your Own Permission](index.html)

[« Previous](highscore.html) • [Trail](../TOC.html) • [Next »](policy.html)

# The HighScorePermission Class

The `HighScorePermission` class defines the permission
that `TerrysGame`
needs to update the user's high score.

All permission classes
should subclass from either `java.security.Permission` or
`java.security.BasicPermission`.
The basic difference between the two is that
`java.security.Permission` defines more complex
permissions that require names and actions. For example,
a `java.io.FilePermission`
extends from `java.security.Permission`, and requires a name
(a filename), and actions allowed for that file
(read/write/delete).

In contrast, `java.security.BasicPermission`
defines simpler permissions that only require a name.
For example, `java.lang.RuntimePermission`
extends from `java.security.BasicPermission` and
simply needs a name
(like "exitVM"), which allows programs to exit the Java Virtual
Machine.

Our `HighScorePermission` is a simple
permission, and hence can be
extended from `java.security.BasicPermission`.

Often, the method implementations in the
`BasicPermission` class itself do not need to be overridden by its
subclasses. That is the case with our `HighScorePermission`,
so all we need to implement are the constructors,
which just invoke the superclass constructors,
as shown in the
[`following`](examples/com/scoredev/scores/HighScorePermission.java):

```


package com.scoredev.scores;

import java.security.*;

public final class HighScorePermission extends BasicPermission {

    public HighScorePermission(String name)
    {
	super(name);
    }

    // note that actions is ignored and not used,
    // but this constructor is still needed
    public HighScorePermission(String name, String actions) 
    {
	super(name, actions);
    }
}

```

[« Previous](highscore.html)
•
[Trail](../TOC.html)
•
[Next »](policy.html)

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

**Previous page:** The HighScore Class
  
**Next page:** A Sample Policy File




A browser with JavaScript enabled is required for this page to operate properly.