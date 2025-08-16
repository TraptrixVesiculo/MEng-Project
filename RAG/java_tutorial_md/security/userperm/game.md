[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Security Features in Java SE
  
**Lesson:** Implementing Your Own Permission

[Implementing Your Own Permission](index.html)

TerrysGame

[The HighScore Class](highscore.html)

[The HighScorePermission Class](perm.html)

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

[« Previous](index.html) • [Trail](../TOC.html) • [Next »](highscore.html)

# TerrysGame

Below is the source code for `TerrysGame`.
For simplicity, `TerrysGame` does not actually contain code to play
a game. It simply retrieves or updates a user's high score.

To see what the user's current high score value is, you could run:

```

java TerrysGame get

```

To set a new high score value for the user, you could run:

```

java TerrysGame set score 

```

To retrieve the user's current high score, `TerrysGame` simply
instantiates a `HighScore` object and makes a call to its
`getHighScore` method. To set a new
high score for the user,
`TerrysGame` instantiates a `HighScore` object and calls
`setHighScore`, passing it the user's new high score.

Here is the source code for `TerrysGame`,
[`TerrysGame.java`](examples/com/gamedev/games/TerrysGame.java):

```


package com.gamedev.games;

import java.io.*;
import java.security.*;
import java.util.Hashtable;
import com.scoredev.scores.*;

public class TerrysGame
{
    public static void main(String args[])
	throws Exception 
    {
	HighScore hs = new HighScore("TerrysGame");

	if (args.length == 0)
	    usage();

	if (args[0].equals("set")) {
	    hs.setHighScore(Integer.parseInt(args[1]));
	} else if (args[0].equals("get")) {
	    System.out.println("score = "+ hs.getHighScore());
	} else {
	    usage();
	}
    }

    public static void usage()
    {
	System.out.println("TerrysGame get");
	System.out.println("TerrysGame set <score>");
	System.exit(1);
    }
}

```

[« Previous](index.html)
•
[Trail](../TOC.html)
•
[Next »](highscore.html)

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

**Previous page:** Implementing Your Own Permission
  
**Next page:** The HighScore Class




A browser with JavaScript enabled is required for this page to operate properly.