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

Providing Sampled-Audio Services

[Providing MIDI Services](SPI-providing-MIDI.html)

[Home Page](../index.html)
>
[Sound](./index.html)

[« Previous](SPI-intro.html) • [Trail](./TOC.html) • [Next »](SPI-providing-MIDI.html)

# Providing Sampled-Audio Services

As you know,
the Java
Sound API includes two packages,
`javax.sound.sampled.spi` and`javax.sound.midi.spi`, that define abstract classes to be used by developers
of sound services. By implementing and installing a subclass of one of these
abstract classes, a service provider registers the new service, extending the
functionality of the runtime system. This page tells you how to go
about using the `javax.sound.sampled.spi` package to provide new
services for handling sampled audio.



There are four abstract classes in the `javax.sound.sampled.spi` package, representing four different types of services that you can provide for the sampled-audio system:

* [`AudioFileWriter`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/spi/AudioFileWriter.html) provides sound file-writing services. These services make it possible for an application program to write a stream of audio data to a file of a particular type.

  * [`AudioFileReader`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/spi/AudioFileReader.html) provides file-reading services. These services enable an application program to ascertain a sound file's characteristics, and to obtain a stream from which the file's audio data can be read.

    * [`FormatConversionProvider`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/spi/FormatConversionProvider.html) provides services for converting audio data formats. These services allow an application program to translate audio streams from one data format to another.

      * [`MixerProvider`](http://download.oracle.com/javase/7/docs/api/javax/sound/sampled/spi/MixerProvider.html) provides management of a particular kind of mixer. This mechanism allows an application program to obtain information about, and access instances of, a given kind of mixer.

To recapitulate earlier discussions, service providers can extend the functionality of the runtime system. A typical SPI class has two types of methods: ones that respond to queries about the types of services available from a particular provider, and ones that either perform the new service directly, or return instances of objects that actually provide the service. The runtime environment's service-provider mechanism provides *registration* of installed services with the audio system, and *management* of the new service provider classes.

In essence there is a double isolation of the service instances from the application developer. An application program never directly creates instances of the service objects, such as mixers or format converters, that it needs for its audio processing tasks. Nor does the program even directly request these objects from the SPI classes that administer them. The application program makes requests to the `AudioSystem` object in the `javax.sound.sampled` package, and `AudioSystem` in turn uses the SPI objects to process these queries and service requests.

The existence of new audio services might be completely transparent to both the user and the application programmer. All application references are through standard objects of the `javax.sound.sampled` package, primarily `AudioSystem`, and the special handling that new services might be providing is often completely hidden.

In this discussion, we'll continue the previous convention of referring to new SPI subclasses by names like `AcmeMixer` and `AcmeMixerProvider`.

### Providing Audio File-Writing Services

Let's start with `AudioFileWriter`, one of the simpler SPI classes.

A subclass that implements the methods of `AudioFileWriter` must provide implementations of a set of methods to handle queries about the file formats and file types supported by the class, as well as provide methods that actually write out a supplied audio data stream to a `File` or `OutputStream`.

`AudioFileWriter` includes two methods that have concrete implementations in the base class:

```

boolean isFileTypeSupported(AudioFileFormat.Type fileType) 
boolean isFileTypeSupported(AudioFileFormat.Type fileType, AudioInputStream stream) 

```

The first of these methods informs the caller whether this file writer can write sound files of the specified type. This method is a general inquiry, it will return `true` if the file writer can write that kind of file, assuming the file writer is handed appropriate audio data. However, the ability to write a file can depend on the format of the specific audio data that's handed to the file writer. A file writer might not support every audio data format, or the constraint might be imposed by the file format itself. (Not all kinds of audio data can be written to all kinds of sound files.) The second method is more specific, then, asking whether a particular `AudioInputStream` can be written to a particular type of file.

Generally, you won't need to override these two concrete methods. Each is simply a wrapper that invokes one of two other query methods and iterates over the results returned. These other two query methods are abstract and therefore need to be implemented in the subclass:

```

abstract AudioFileFormat.Type[] getAudioFileTypes() 
abstract AudioFileFormat.Type[] getAudioFileTypes(AudioInputStream stream) 

```

These methods correspond directly to the previous two. Each returns an array of all the supported file types-all that are supported in general, in the case of the first method, and all that are supported for a specific audio stream, in the case of the second method. A typical implementation of the first method might simply return an array that the file writer's constructor initializes. An implementation of the second method might test the stream's `AudioFormat` object to see whether it's a data format that the requested type of file supports.

The final two methods of `AudioFileWriter` do the actual file-writing work:

```

abstract int write(AudioInputStream stream, 
     AudioFileFormat.Type fileType, java.io.File out) 
abstract int write(AudioInputStream stream, 
     AudioFileFormat.Type fileType, java.io.OutputStream out) 

```

These methods write a stream of bytes representing the audio data to the stream or file specified by the third argument. The details of how this is done depend on the structure of the specified type of file. The `write` method must write the file's header and the audio data in the manner prescribed for sound files of this format (whether it's a standard type of sound file or a new, possibly proprietary one).

### Providing Audio File-Reading Services

The `AudioFileReader` class consists of six abstract methods that your subclass needs to implement-actually, two different overloaded methods, each of which can take a `File`, `URL`, or `InputStream` argument. The first of these overloaded methods accepts queries about the file format of a specified file:

```

abstract AudioFileFormat getAudioFileFormat(java.io.File file) 
abstract AudioFileFormat getAudioFileFormat(java.io.InputStream stream) 
abstract AudioFileFormat getAudioFileFormat(java.net.URL url) 

```

A typical implementation of `getAudioFileFormat` method reads and parses the sound file's header to ascertain its file format. See the description of the AudioFileFormat class to see what fields need to be read from the header, and refer to the specification for the particular file type to figure out how to parse the header.

Because the caller providing a stream as an argument to this method expects the stream to be unaltered by the method, the file reader should generally start by marking the stream. After reading to the end of the header, it should reset the stream to its original position.

The other overloaded `AudioFileReader` method provides file-reading services, by returning an AudioInputStream from which the file's audio data can be read:

```

abstract AudioInputStream getAudioInputStream(java.io.File file) 
abstract AudioInputStream getAudioInputStream(java.io.InputStream stream) 
abstract AudioInputStream getAudioInputStream(java.net.URL url) 

```

Typically, an implementation of `getAudioInputStream` returns an `AudioInputStream` wound to the beginning of the file's data chunk (after the header), ready for reading. It would be conceivable, though, for a file reader to return an `AudioInputStream` whose audio format represents a stream of data that is in some way decoded from what is contained in the file. The important thing is that the method return a formatted stream from which the audio data contained in the file can be read. The `AudioFormat` encapsulated in the returned `AudioInputStream` object will inform the caller about the stream's data format, which is usually, but not necessarily, the same as the data format in the file itself.

Generally, the returned stream is an instance of `AudioInputStream`; it's unlikely you would ever need to subclass `AudioInputStream`.

### Providing Format-Conversion Services

A `FormatConversionProvider` subclass transforms an `AudioInputStream` that has one audio data format into one that has another format. The former (input) stream is referred to as the *source* stream, and the latter (output) stream is referred to as the *target* stream. Recall
that an `AudioInputStream` contains an `AudioFormat`, and the `AudioFormat` in turn contains a particular type of data encoding, represented by an `AudioFormat.Encoding` object. The format and encoding in the source stream are called the source format and source encoding, and those in the target stream are likewise called the target format and target encoding.

The work of conversion is performed in the overloaded abstract method of `FormatConversionProvider` called `getAudioInputStream`. The class also has abstract query methods for learning about all the supported target and source formats and encodings. There are concrete wrapper methods for querying about a specific conversion.

The two variants of `getAudioInputStream` are:

```

abstract AudioInputStream getAudioInputStream(AudioFormat.Encoding targetEncoding, 
     AudioInputStream sourceStream) 

```

and

```

abstract AudioInputStream getAudioInputStream(AudioFormat targetFormat, 
     AudioInputStream sourceStream) 

```

These differ in the first argument, according to whether the caller is specifying a complete target format or just the format's encoding.

A typical implementation of `getAudioInputStream` works by returning a new subclass of `AudioInputStream` that wraps around the original (source) `AudioInputStream` and applies a data format conversion to its data whenever a `read` method is invoked. For example, consider the case of a new `FormatConversionProvider` subclass called `AcmeCodec`, which works with a new `AudioInputStream` subclass called `AcmeCodecStream`.

The implementation of `AcmeCodec's` second `getAudioInputStream` method might be:
> ```
> public AudioInputStream getAudioInputStream
>       (AudioFormat outputFormat, AudioInputStream stream) {
>         AudioInputStream cs = null;
>         AudioFormat inputFormat = stream.getFormat();
>         if (inputFormat.matches(outputFormat) ) {
>             cs = stream;
>         } else {
>             cs = (AudioInputStream)
>                 (new AcmeCodecStream(stream, outputFormat));
>             tempBuffer = new byte[tempBufferSize];
>         }
>         return cs;
>     }
>
> ```

The actual format conversion takes place in new `read` methods of the returned `AcmeCodecStream`, a subclass of `AudioInputStream`. Again, application programs that access this returned `AcmeCodecStream` simply operate on it as an `AudioInputStream`, and don't need to know the details of its implementation.

The other methods of a `FormatConversionProvider` all permit queries about the input and output encodings and formats that the object supports. The following four methods, being abstract, need to be implemented:
> ```
>
> abstract AudioFormat.Encoding[] getSourceEncodings() 
> abstract AudioFormat.Encoding[] getTargetEncodings() 
> abstract AudioFormat.Encoding[] getTargetEncodings(
>     AudioFormat sourceFormat) 
> abstract  AudioFormat[] getTargetFormats(
>     AudioFormat.Encoding targetEncoding, 
>     AudioFormat sourceFormat) 
>
> ```

As in the query methods of the `AudioFileReader` class discussed
above, these queries are typically handled by checking private data of the object
and, for the latter two methods, comparing them against the argument(s).

The remaining four `FormatConversionProvider` methods are concrete and generally don't need to be overridden:
> ```
>
> boolean isConversionSupported(
>     AudioFormat.Encoding targetEncoding,
>     AudioFormat sourceFormat) 
> boolean isConversionSupported(AudioFormat targetFormat, 
>     AudioFormat sourceFormat) 
> boolean isSourceEncodingSupported(
>     AudioFormat.Encoding sourceEncoding) 
> boolean isTargetEncodingSupported(
>     AudioFormat.Encoding targetEncoding) 
>
> ```

As with `AudioFileWriter.isFileTypeSupported()`, the default implementation
of each of these methods is essentially a wrapper that invokes one of the other
query methods and iterates over the results returned.

### Providing New Types of Mixers

As its name implies, a `MixerProvider` supplies instances of mixers. Each concrete `MixerProvider` subclass acts as a factory for the `Mixer` objects used by an application program. Of course, defining a new `MixerProvider` only makes sense if one or more new implementations of the `Mixer` interface are also defined. As in the `FormatConversionProvider` example above, where our `getAudioInputStream` method returned a subclass of `AudioInputStream` that performed the conversion, our new class `AcmeMixerProvider` has a method `getMixer` that returns an instance of another new class that implements the `Mixer` interface. We'll call the latter class `AcmeMixer`. Particularly if the mixer is implemented in hardware, the provider might support only one static instance of the requested device. If so, it should return this static instance in response to each invocation of `getMixer`.

Since `AcmeMixer` supports the `Mixer` interface, application programs don't require any additional information to access its basic functionality. However, if `AcmeMixer` supports functionality not defined in the `Mixer` interface, and the vendor wants to make this extended functionality accessible to application programs, the mixer should of course be defined as a public class with additional, well-documented public methods, so that a program that wishes to make use of this extended functionality can import `AcmeMixer` and cast the object returned by `getMixer` to this type.

The other two methods of `MixerProvider` are:

```

abstract Mixer.Info[] getMixerInfo() 

```

and

```

boolean isMixerSupported(Mixer.Info info) 

```

These methods allow the audio system to determine whether this particular provider
class can produce a device that an application program needs. In other words,
the `AudioSystem` object can iterate over all the installed `MixerProviders`
to see which ones, if any, can supply the device that the application program
has requested of the `AudioSystem`.
The `getMixerInfo` method returns an array of objects containing information
about the kinds of mixer available from this provider object. The system can pass
these information objects, along with those from other providers, to an application
program.

A single `MixerProvider` can provide more than one kind of mixer. When the system invokes the `MixerProvider's getMixerInfo` method, it gets a list of information objects identifying the different kinds of mixer that this provider supports. The system can then invoke `MixerProvider.getMixer(Mixer.Info)` to obtain each mixer of interest.

Your subclass needs to implement `getMixerInfo`, as it's abstract. The `isMixerSupported` method is concrete and doesn't generally need to be overridden. The default implementation simply compares the provided `Mixer.Info` to each one in the array returned by `getMixerInfo`.