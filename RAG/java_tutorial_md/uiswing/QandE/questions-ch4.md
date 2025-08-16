[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Creating a GUI With JFC/Swing

[Home Page](../../index.html)
>
[Creating a GUI With JFC/Swing](../index.html)

[« Previous](../TOC.html) • [Trail](../TOC.html) • [Next »](../lookandfeel/index.html)

# Questions and Exercises: Laying Out Components within a Container

### Questions

In each of the following questions, choose the layout manager(s)
most naturally suited for the described layout. Assume that the
container controlled by the layout manager is a `JPanel`.
[*Hint:* Two sections that might help are [A
Visual Index to Swing Components](../../ui/features/components.html) and [Tips
on Choosing a Layout Manager](../layout/using.html#choosing).]

> 1. The container has one component that should take up as
> much space as possible  
> > |  |  |
> > | --- | --- |
> > | Layout1-1.png | Layout1-2.png |
> >
> > a. `BorderLayout`  
> > b. `GridLayout`  
> > c. `GridBagLayout`  
> > d. a and b  
> > e. b and c
>
> 2. The container has a row of components that should all be
> displayed at the same size, filling the container’s entire
> area.
>
> > ![Layout2-1.png](../../figures/uiswing/QandE/Layout2-1.png)
>
> > ![Layout2-2.png](../../figures/uiswing/QandE/Layout2-2.png)
>
> > a. `FlowLayout`  
> > b. `GridLayout`  
> > c. `BoxLayout`  
> > d. a and b
>
> 3. The container displays a number of components in a column,
> with any extra space going between the first two components.  
> > |  |  |
> > | --- | --- |
> > | Layout3-1.png | Layout3-2.png |
> >
> > a. `FlowLayout`  
> > b. `BoxLayout`  
> > c. `GridLayout`  
> > d. `BorderLayout`
>
> 4. The container can display three completely different components
> at different times, depending perhaps on user input or program
> state. Even if the components’ sizes differ, switching
> from one component to the next shouldn’t change the amount
> of space devoted to the component.
>
> > ![Layout4-1.png](../../figures/uiswing/QandE/Layout4-1.png)
>
> > ![Layout4-2.png](../../figures/uiswing/QandE/Layout4-2.png)
> >
> > a. `SpringLayout`  
> > b. `BoxLayout`  
> > c. `CardLayout`  
> > d. `GridBagLayout`

### Exercises

> 1. Implement the layout described and shown in question 1.
>
> 2. Implement the layout described and shown in question 2.
>
> 3. Implement the layout described and shown in question 3.
>
> 4. Implement the layout described and shown in question 4.
>
> 5. By adding a single line of code, make the program you wrote for Exercise
> 2 display the components from right-to-left, instead of from left-to-right.
>
> > ![Layout2-3.png](../../figures/uiswing/QandE/Layout2-3.png)

[Check your answers.](answers-ch4.html)

[« Previous](../TOC.html)
•
[Trail](../TOC.html)
•
[Next »](../lookandfeel/index.html)

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

**Previous page:** Solving Common Layout Problems
  
**Next page:** Modifying the Look and Feel




A browser with JavaScript enabled is required for this page to operate properly.