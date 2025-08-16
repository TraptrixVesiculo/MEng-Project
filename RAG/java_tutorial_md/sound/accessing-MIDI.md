[Download
the JDK](http://java.sun.com/javase/6/download.jsp)
  
[Search the
Tutorials](../search.html)
  
[Hide the TOC](javascript:toggleLeft())

**Trail:** Sound

[Overview of the Sampled Package](sampled-overview.html)

[Accessing Audio System Resources](accessing.html)

[Playing Back Audio](playing.html)

[Capturing Audio](capturing.html)

[Processing Audio with Controls](controls.html)

[Using Files and Format Converters](converters.html)

[Overview of the MIDI Package](overview-MIDI.html)

Accessing MIDI System Resources

[Transmitting and Receiving MIDI Messages](MIDI-messages.html)

[Introduction to Sequencers](MIDI-seq-intro.html)

[Using Sequencer Methods](MIDI-seq-methods.html)

[Using Advanced Sequencer Features](MIDI-seq-adv.html)

[Synthesizing Sound](MIDI-synth.html)

[Introduction to the Service Provider Interfaces](SPI-intro.html)

[Providing Sampled-Audio Services](SPI-providing-sampled.html)

[Providing MIDI Services](SPI-providing-MIDI.html)

[Home Page](../index.html)
>
[Sound](./index.html)

[« Previous](overview-MIDI.html) • [Trail](./TOC.html) • [Next »](MIDI-messages.html)

# Accessing MIDI System Resources

The Java Sound API offers a flexible model for MIDI system configuration, just as it does for configuration of the sampled-audio system. An implementation of the Java Sound API can itself provide different sorts of MIDI devices, and additional ones can be supplied by service providers and installed by users. You can write your program in such a way that it makes few assumptions about which specific MIDI devices are installed on the computer. Instead, the program can take advantage of the MIDI system's defaults, or it can allow the user to select from whatever devices happen to be available.

This section shows how your program can learn what MIDI
resources have been installed, and how to get access to the desired ones. After
you've accessed and opened the devices, you can connect them to each other,
as discussed later in
[Transmitting and Receiving MIDI Messages](MIDI-messages.html).

### The MidiSystem Class

The role of the
[`MidiSystem`](http://download.oracle.com/javase/7/docs/api/javax/sound/midi/MidiSystem.html)
class in the Java Sound API's MIDI package is directly analogous to the role of
[`AudioSystem`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/AudioSystem.html)
in the sampled-audio package. `MidiSystem` acts as a clearinghouse for accessing the installed MIDI resources.

You can query the `MidiSystem` to learn what sorts of devices are installed, and then you can iterate over the available devices and obtain access to the desired ones. For example, an application program might start out by asking the `MidiSystem` what synthesizers are available, and then display a list of them, from which the user can select one. A simpler application program might just use the system's default synthesizer.

The `MidiSystem` class also provides methods for translating between MIDI files and `Sequences`. It can report the file format of a MIDI file and can write files of different types.

An application program can obtain the following resources from the `MidiSystem`:

* Sequencers
  * Synthesizers
    * Transmitters (such as those associated with MIDI input ports)
      * Receivers (such as those associated with MIDI output ports)
        * Data from standard MIDI files
          * Data from soundbank files

This page focuses on the first four of these types of resource. The
others are discussed later in this tutorial.

### Obtaining Default Devices

A typical MIDI application program that uses the Java Sound API begins by obtaining the devices it needs, which can consist of one or more sequencers, synthesizers, input ports, or output ports.

There is a default synthesizer device, a default sequencer device, a default transmitting device, and a default receiving device. The latter two devices normally represent the MIDI input and output ports, respectively, if there are any available on the system. (It's easy to get confused about the directionality here. Think of the ports' transmission or reception in relation to the software, not in relation to any external physical devices connected to the physical ports. A MIDI input port *transmits* data from an external device to a Java Sound API `Receiver`, and likewise a MIDI output port *receives* data from a software object and relays the data to an external device.)

A simple application program might just use the default instead of exploring all the installed devices. The `MidiSystem` class includes the following methods for retrieving default resources:

> ```
>     static Sequencer getSequencer()
>     static Synthesizer getSynthesizer()
>     static Receiver getReceiver()
>     static Transmitter getTransmitter()
> 	
> ```

The first two of these methods obtain the system's default sequencing and synthesis resources, which either represent physical devices or are implemented wholly in software. The `getReceiver` method obtains a `Receiver` object that takes MIDI messages sent to it and relays them to the default receiving device. Similarly, the getTransmitter method obtains a Transmitter object that can send MIDI messages to some receiver on behalf of the default transmitting device.

### Learning What Devices Are Installed

Instead of using the default devices, a more thorough approach is to select the desired devices from the full set of devices that are installed on the system. An application program can select the desired devices programmatically, or it can display a list of available devices and let the user select which ones to use. The `MidiSystem` class provides a method for learning which devices are installed, and a corresponding method to obtain a device of a given type.

Here is the method for learning about the installed devices:

> ```
>     static MidiDevice.Info[] getMidiDeviceInfo()
>
> ```

As you can see, it returns an array of information objects. Each of these returned `MidiDevice.Info` objects identifies one type of sequencer, synthesizer, port, or other device that is installed. (Usually a system has at most one instance of a given type. For example, a given model of synthesizer from a certain vendor will be installed only once. ) The `MidiDevice.Info` includes the following strings to describe the device:

* Name
  * Version number
    * Vendor (the company that created the device)
      * A description of the device

You can display these strings in your user interface to let the user select from the list of devices.

However, to use the strings programmatically to select a device (as opposed to displaying the strings to the user), you need to know in advance what they might be. The company that provides each device should include this information in its documentation. An application program that requires or prefers a particular device can use this information to locate that device. This approach has the drawback of limiting the program to device implementations that it knows about in advance.

Another, more general, approach is to go ahead and iterate over the `MidiDevice.Info` objects, obtaining each corresponding device, and determining programmatically whether it's suitable to use (or at least suitable to include in a list from which the user can choose). The next section describes how to do this.

### Obtaining a Desired Device

Once an appropriate device's info object is found, the application program invokes the following `MidiSystem` method to obtain the corresponding device itself:

> ```
>     static MidiDevice getMidiDevice(MidiDevice.Info info)
>
> ```

You can use this method if you've already found the info object describing the device you need. However, if you can't interpret the info objects returned by `getMidiDeviceInfo` to determine which device you need, and if you don't want to display information about all the devices to the user, you might be able to do the following instead: Iterate over all the `MidiDevice.Info` objects returned by `getMidiDeviceInfo`, get the corresponding devices using the method above, and test each device to see whether it's suitable. In other words, you can query each device for its class and its capabilities before including it in the list that you display to the user, or as a way to decide upon a device programmatically without involving the user. For example, if your program needs a synthesizer, you can obtain each of the installed devices, see which are instances of classes that implement the `Synthesizer` interface, and then display them in a list from which the user can choose one, as follows:
> ```
>
> // Obtain information about all the installed synthesizers.
> Vector synthInfos;
> MidiDevice device;
> MidiDevice.Info[] infos = MidiSystem.getMidiDeviceInfo();
> for (int i = 0; i < infos.length; i++) {
>     try {
>         device = MidiSystem.getMidiDevice(infos[i]);
>     } catch (MidiUnavailableException e) {
>           // Handle or throw exception...
>     }
>     if (device instanceof Synthesizer) {
>         synthInfos.add(infos[i]);
>     }
> }
> // Now, display strings from synthInfos list in GUI.	
>
> ```

As another example, you might choose a device programmatically, without involving the user. Let's suppose you want to obtain the synthesizer that can play the most notes simultaneously.  You iterate over all the MidiDevice.Info objects, as above, but after determining that a device is a synthesizer, you query its capabilities by invoking the `getMaxPolyphony` method of `Synthesizer`. You reserve the synthesizer that has the greatest polyphony, as described in the next section. Even though you're not asking the user to choose a synthesizer, you might still display strings from the chosen `MidiDevice.Info` object, just for the user's information.

### Opening Devices

The previous section showed how to get an installed device. However, a device might be installed but unavailable. For example, another application program might have exclusive use of it. To actually reserve a device for your program, you need to use the `MidiDevice` method `open`:

> ```
> if (!(device.isOpen())) {
>     try {
>       device.open();
>   } catch (MidiUnavailableException e) {
>           // Handle or throw exception...
>   }
> }
>
> ```

Once you've accessed a device and reserved it by opening
it, you'll probably want to connect it to one or more other devices to let MIDI
data flow between them. This procedure is described in later in
[Transmitting and Receiving MIDI Messages](MIDI-messages.html).

When done with a device, you release it for other programs' use by invoking the `close` method of `MidiDevice`.

[« Previous](overview-MIDI.html)
•
[Trail](./TOC.html)
•
[Next »](MIDI-messages.html)

---

Problems with the examples? Try [Compiling and Running
the Examples: FAQs](../information/run-examples.html).
  
Complaints? Compliments? Suggestions? [Give
us your feedback](http://download.oracle.com/javase/feedback.html).

Your use of this page and all the material on pages under "The Java Tutorials" banner,
and all the material on pages under "The Java Tutorials" banner is subject to the [Java SE Tutorial Copyright
and License](../information/license.html).
Additionally, any example code contained in any of these Java
Tutorials pages is licensed under the
[Code
Sample License](http://developers.sun.com/license/berkeley_license.html).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | duke image | Oracle logo | | [About Oracle](http://www.oracle.com/us/corporate/index.html) | [Oracle Technology Network](http://www.oracle.com/technology/index.html) | [Terms of Service](https://www.samplecode.oracle.com/servlets/CompulsoryClickThrough?type=TermsOfService) | Copyright © 1995, 2011 Oracle and/or its affiliates. All rights reserved. |

**Previous page:** Overview of the MIDI Package
  
**Next page:** Transmitting and Receiving MIDI Messages




A browser with JavaScript enabled is required for this page to operate properly.