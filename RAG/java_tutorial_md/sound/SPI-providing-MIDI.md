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

[Accessing MIDI System Resources](accessing-MIDI.html)

[Transmitting and Receiving MIDI Messages](MIDI-messages.html)

[Introduction to Sequencers](MIDI-seq-intro.html)

[Using Sequencer Methods](MIDI-seq-methods.html)

[Using Advanced Sequencer Features](MIDI-seq-adv.html)

[Synthesizing Sound](MIDI-synth.html)

[Introduction to the Service Provider Interfaces](SPI-intro.html)

[Providing Sampled-Audio Services](SPI-providing-sampled.html)

Providing MIDI Services

[Home Page](../index.html)
>
[Sound](./index.html)

[« Previous](SPI-providing-sampled.html) • [Trail](./TOC.html) • [Next »](./end.html)

# Providing MIDI Services

[Introduction to the Service Provider Interfaces](SPI-intro.html)
explained that the `javax.sound.sampled.spi`
and `javax.sound.midi.spi` packages define abstract classes to be
used by developers of sound services. By implementing a subclass of one of these
abstract classes, a service provider can create a new service that extends the
functionality of the runtime system. The previous section covered the use of the `javax.sound.sampled.spi`
package. This section discusses how to use the `javax.sound.midi.spi`
package to provide new services for handling MIDI devices and files.

There are four abstract classes in the `javax.sound.midi.spi` package, which represent four different types of services that you can provide for the MIDI system:

* [`MidiFileWriter`](http://download.oracle.com/javase/7/docs/api/javax/sound/midi/spi/MidiFileWriter.html) provides MIDI file-writing services. These services
  make it possible for an application program to save, to a MIDI file, a MIDI
  `Sequence` that it has generated or processed. 

  * [`MidiFileReader`](http://download.oracle.com/javase/7/docs/api/javax/sound/midi/spi/MidiFileReader.html) provides file-reading services that return a
    MIDI `Sequence` from a MIDI file for use in an application program.

    * [`MidiDeviceProvider`](http://download.oracle.com/javase/7/docs/api/javax/sound/midi/spi/MidiDeviceProvider.html) supplies instances of one or more specific
      types of MIDI device, possibly including hardware devices. 

      * [`SoundbankReader`](http://download.oracle.com/javase/7/docs/api/javax/sound/midi/spi/SoundbankReader.html) supplies soundbank file-reading services. Concrete
        subclasses of `SoundbankReader` parse a given soundbank file, producing
        a `Soundbank` object that can be loaded into a `Synthesizer`.

An application program will not directly create an instance of a service object—whether
a provider object, such as a `MidiDeviceProvider`, or an object,
such as a `Synthesizer`, that is supplied by the provider object.
Nor will the program directly refer to the SPI classes. Instead, the application
program makes requests to the `MidiSystem` object in the `javax.sound.midi`
package, and `MidiSystem` in turn uses concrete subclasses of the
`javax.sound.midi.spi` classes to process these requests.

### Providing MIDI File-Writing Services

There are three standard MIDI file formats, all of which an implementation of the Java Sound API can support: Type 0, Type 1, and Type 2. These file formats differ in their internal representation of the MIDI sequence data in the file, and are appropriate for different kinds of sequences. If an implementation doesn't itself support all three types, a service provider can supply the support for the unimplemented ones. There are also variants of the standard MIDI file formats, some of them proprietary, which similarly could be supported by a third-party vendor.

The ability to write MIDI files is provided by concrete subclasses of `MidiFileWriter`. This abstract class is directly analogous to `javax.sampled.spi.AudioFileWriter`. Again, the methods are grouped into query methods for learning what types of files can be written, and methods for actually writing a file. As with `AudioFileWriter`, two of the query methods are concrete:

> ```
> boolean isFileTypeSupported(int fileType)
> boolean isFileTypeSupported(int fileType, Sequence sequence) 
>
> ```

The first of these provides general information about whether the file writer can ever write the specified type of MIDI file type. The second method is more specific: it asks whether a particular Sequence can be written to the specified type of MIDI file. Generally, you don't need to override either of these two concrete methods. In the default implementation, each invokes one of two other corresponding query methods and iterates over the results returned. Being abstract, these other two query methods need to be implemented in the subclass:
> ```
> abstract int[] getMidiFileTypes() 
> abstract int[] getMidiFileTypes(Sequence sequence) 
>
> ```

The first of these returns an array of all the file types that are supported in general. A typical implementation might initialize the array in the file writer's constructor and return the array from this method. From that set of file types, the second method finds the subset to which the file writer can write the given Sequence. In accordance with the MIDI specification, not all types of sequences can be written to all types of MIDI files.

The `write` methods of a `MidiFileWriter` subclass perform the encoding of the data in a given `Sequence` into the correct data format for the requested type of MIDI file, writing the coded stream to either a file or an output stream:
> ```
> abstract int write(Sequence in, int fileType, 
>                    java.io.File out) 
> abstract int write(Sequence in, int fileType, 
>                    java.io.OutputStream out) 
>
> ```

To do this, the `write` method must parse the `Sequence` by iterating over its tracks, construct an appropriate file header, and write the header and tracks to the output.The MIDI file's header format is, of course, defined by the MIDI specification. It includes such information as a "magic number" identifying this as a MIDI file, the header's length, the number of tracks, and the sequence's timing information (division type and resolution). The rest of the MIDI file consists of the track data, in the format defined by the MIDI specification.

Let's briefly look at how the application program, MIDI
system, and service provider cooperate in writing a MIDI file. In a typical
situation, an application program has a particular MIDI `Sequence`
to save to a file. The program queries the `MidiSystem` object to
see what MIDI file formats, if any, are supported for the particular `Sequence`
at hand, before attempting to write the file. The `MidiSystem.getMidiFileTypes(Sequence)`
method returns an array of all the MIDI file types to which the system can write
a particular sequence. It does this by invoking the corresponding `getMidiFileTypes`
method for each of the installed `MidiFileWriter` services, and collecting
and returning the results in an array of integers that can be thought of as
a master list of all file types compatible with the given `Sequence`.
When it comes to writing the `Sequence` to a file, the call to `MidiSystem.write`
is passed an integer representing a file type, along with the `Sequence`
to be written and the output file; `MidiSystem` uses the supplied
type to decide which installed `MidiFileWriter` should handle the
write request, and dispatches a corresponding `write` to the appropriate
`MidiFileWriter`.

### Providing MIDI File-Reading Services

The `MidiFileReader` abstract class is directly analogous to `javax.sampled.spi.AudioFileReader` class. Both consist of two overloaded methods, each of which can take a `File`, `URL`, or `InputStream` argument. The first of the overloaded methods returns the file format of a specified file. In the case of `MidiFileReader`, the API is:

> ```
> abstract MidiFileFormat getMidiFileFormat(java.io.File file) 
> abstract MidiFileFormat getMidiFileFormat(
>     java.io.InputStream stream) 
> abstract MidiFileFormat getMidiFileFormat(java.net.URL url) 
>
> ```

Concrete subclasses must implement these methods to return a filled-out `MidiFileFormat` object describing the format of the specified MIDI file (or stream or URL), assuming that the file is of a type supported by the file reader and that it contains valid header information. Otherwise, an `InvalidMidiDataException` should be thrown.

The other overloaded method returns a MIDI `Sequence` from a given file, stream, or URL :
> ```
>
> abstract Sequence getSequence(java.io.File file) 
> abstract Sequence getSequence(java.io.InputStream stream) 
> abstract Sequence getSequence(java.net.URL url) 
>
> ```

The `getSequence` method performs the actual work of parsing the bytes in the MIDI input file and constructing a corresponding `Sequence` object. This is essentially the inverse of the process used by `MidiFileWriter.write`. Because there is a one-to-one correspondence between the contents of a MIDI file as defined by the MIDI specification and a `Sequence` object as defined by the Java Sound API, the details of the parsing are straightforward. If the file passed to `getSequence` contains data that the file reader can't parse (for example, because the file has been corrupted or doesn't conform to the MIDI specification), an `InvalidMidiDataException` should be thrown.

### Providing Particular MIDI Devices

A `MidiDeviceProvider` can be considered a factory that supplies one or more particular types of MIDI device. The class consists of a method that returns an instance of a MIDI device, as well as query methods to learn what kinds of devices this provider can supply.

As with the other `javax.sound.midi.spi`
services, application developers get indirect access to a `MidiDeviceProvider`
service through a call to `MidiSystem` methods, in this case `MidiSystem.getMidiDevice`
and `MidiSystem.getMidiDeviceInfo`. The purpose of subclassing `MidiDeviceProvider`
is to supply a new kind of device, so the service developer must also create
an accompanying class for the device being returned—just as we saw with
`MixerProvider` in the `javax.sound.sampled.spi` package.
There, the returned device's class implemented the `javax.sound.sampled.Mixer`
interface; here it implements the `javax.sound.midi.MidiDevice` interface.
It might also implement a subinterface of `MidiDevice`, such as `Synthesizer`
or `Sequencer`.

Because a single subclass of `MidiDeviceProvider` can provide more than one type of `MidiDevice`, the `getDeviceInfo` method of the class returns an array of `MidiDevice.Info` objects enumerating the different `MidiDevices` available:

> ```
> abstract MidiDevice.Info[] getDeviceInfo() 
>
>
> ```

The returned array can contain a single element, of course. A typical implementation
of the provider might initialize an array in its constructor and return it here.
This allows `MidiSystem` to iterate over all installed `MidiDeviceProviders`to construct a list of all installed devices. `MidiSystem`
can then return this list (`MidiDevice.Info[]` array) to an application
program.

`MidiDeviceProvider` also includes a concrete query method:
> ```
> boolean isDeviceSupported(MidiDevice.Info info) 
>
> ```

This method permits the system to query the provider about a specific kind of device. Generally, you don't need to override this convenience method. The default implementation iterates over the array returned by getDeviceInfo and compares the argument to each element.

The third and final `MidiDeviceProvider` method returns the requested device:
> ```
> abstract MidiDevice getDevice(MidiDevice.Info info) 
>
> ```

This method should first test the argument to make sure it describes a device that this provider can supply. If it doesn't, it should throw an `IllegalArgumentException`. Otherwise, it returns the device.

### Providing Soundbank File-Reading Services

A `SoundBank` is a set of `Instruments`
that can be loaded into a `Synthesizer`. An `Instrument`
is an implementation of a sound-synthesis algorithm that produces a particular
sort of sound, and includes accompanying name and information strings. A `SoundBank`
roughly corresponds to a bank in the MIDI specification, but it's a more extensive
and addressable collection; it can perhaps better be thought of as a collection
of MIDI banks.

`SoundbankReader` consists of a single overloaded method, which the system invokes to read a `Soundbank` object from a soundbank file:

> ```
> abstract Soundbank getSoundbank(java.io.File file) 
> abstract Soundbank getSoundbank(java.io.InputStream stream) 
> abstract Soundbank getSoundbank(java.net.URL url) 
>
> ```

Concrete subclasses of `SoundbankReader` will work in tandem with
particular provider-defined implementations of `SoundBank`, `Instrument`,
and `Synthesizer` to allow the system to load a `SoundBank`
from a file into an instance of a particular `Synthesizer` class.
Synthesis techniques may differ wildly from one `Synthesizer` to
another, and, as a consequence, the data stored in an `Instrument`
or `SoundBank` providing control or specification data for the synthesis
process of a `Synthesizer` can take a variety of forms. One synthesis
technique may require only a few bytes of parameter data; another may be based
on extensive sound samples. The resources present in a `SoundBank`
will depend upon the nature of the `Synthesizer` into which they
get loaded, and therefore the implementation of the `getSoundbank`
method of a `SoundbankReader` subclass has access to knowledge of
a particular kind of `SoundBank`. In addition, a particular subclass
of `SoundbankReader` understands a particular file format for storing
the `SoundBank` data. That file format may be vendor-specific and
proprietary.

`SoundBank` is just an interface, with only weak constraints on the contents of a `SoundBank` object. The methods an object must support to implement this interface (`getResources`, `getInstruments`, `getVendor`, `getName`, etc.) impose loose requirements on the data that the object contains. For example, `getResources` and `getInstruments` can return empty arrays. The actual contents of a subclassed `SoundBank` object, in particular its instruments and its non-instrument resources, are defined by the service provider. Thus, the mechanism of parsing a soundbank file depends entirely on the specification of that particular kind of soundbank file.

Soundbank files are created outside the Java Sound API, typically by the vendor of the synthesizer that can load that kind of soundbank. Some vendors might supply end-user tools for creating such files.

[« Previous](SPI-providing-sampled.html)
•
[Trail](./TOC.html)
•
[Next »](./end.html)

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

**Previous page:** Providing Sampled-Audio Services
  
**Next page:** End of Trail




A browser with JavaScript enabled is required for this page to operate properly.