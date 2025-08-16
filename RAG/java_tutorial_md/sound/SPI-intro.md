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

Introduction to the Service Provider Interfaces

[Providing Sampled-Audio Services](SPI-providing-sampled.html)

[Providing MIDI Services](SPI-providing-MIDI.html)

[Home Page](../index.html)
>
[Sound](./index.html)

[« Previous](MIDI-synth.html) • [Trail](./TOC.html) • [Next »](SPI-providing-sampled.html)

# Introduction to the Service Provider Interfaces

### What Are Services?

Services are units of sound-handling functionality that are automatically
available when an application program makes use of an implementation of the
Java Sound API. They consist of objects
that do the work of reading, writing, mixing, processing, and converting audio
and MIDI data. An implementation of the Java Sound API generally supplies a
basic set of services, but mechanisms are also included in the API to support
the development of new sound services by third-party developers (or by the vendor
of the implementation itself). These new services can be "plugged into" an existing
installed implementation to expand its functionality without requiring a new
release. In the Java Sound API architecture, third-party services are integrated
into the system in such a way that an application program's interface to them
is the same as the interface to the "built-in" services. In some cases, application
developers who use the `javax.sound.sampled` and `javax.sound.midi`
packages might not even be aware that they are employing third-party services.

Examples of potential third-party, sampled-audio services include:

* Sound file readers and writers* Converters that translate between different audio data formats* New audio mixers and input/output devices, whether implemented purely in
      software, or in hardware with a software interface

Third-party MIDI services might consist of:

* MIDI file readers and writers* Readers for various types of soundbank files (which are often specific to
    particular synthesizers)* MIDI-controlled sound synthesizers, sequencers, and I/O ports, whether implemented purely in software, or in hardware with a software interface

### How Services Work

The `javax.sound.sampled` and `javax.sound.midi` packages
provide functionality to application developers who wish to include sound services
in their application programs. These packages are for *consumers* of
sound services, providing interfaces to get information about, control, and
access audio and MIDI services. In addition, the Java Sound API also supplies
two packages that define abstract classes to be used by *providers* of
sound services: the `javax.sound.sampled.spi` and `javax.sound.midi.spi`
packages.

Developers of new sound services implement concrete subclasses of the appropriate
classes in the SPI packages. These subclasses, along with any additional classes
required to support the new service, are placed in a Java
Archive (JAR) archive file with a description of the included service or services.
When this JAR file is installed in the user's `CLASSPATH`, the runtime
system automatically makes the new service available, extending the functionality
of the Java platform's runtime system.

Once the new service is installed, it can be accessed just like any previously
installed service. Consumers of services can get information about the new service,
or obtain instances of the new service class itself, by invoking methods of
the `AudioSystem` and `MidiSystem` classes (in the `javax.sound.sampled`
and `javax.sound.midi` packages, respectively) to return information
about the new services, or to return instances of new or existing service classes
themselves. Application programs need not—and should not—reference
the classes in the SPI packages (and their subclasses) directly to make use
of the installed services.

For example, suppose a hypothetical service provider called Acme Software,
Inc. is interested in supplying a package that allows application programs to
read a new format of sound file (but one whose audio data is in a standard data
format). The SPI class `AudioFileReader` can be subclassed into a
class called, say, `AcmeAudioFileReader`. In the new subclass, Acme
would supply implementations of all the methods defined in `AudioFileReader`;
in this case there are only two methods (with argument variants), `getAudioFileFormat`
and `getAudioInputStream`. Then when an application program attempted
to read a sound file that happened to be in Acme's file format, it would invoke
methods of the `AudioSystem` class in `javax.sound.sampled`
to access the file and information about it. The methods `AudioSystem.getAudioInputStream`
and `AudioSystem.getAudioFileFormat` provide a standard API to read
audio streams; with the `AcmeAudioFileReader` class installed, this
interface is extended to support the new file type transparently. Application
developers don't need direct access to the newly registered SPI classes: the
`AudioSystem` object methods pass the query on to the installed `AcmeAudioFileReader`
class.

What's the point of having these "factory" classes? Why not permit the application
developer to get access directly to newly provided services? That is a possible
approach, but having all management and instantiation of services pass through
gatekeeper system objects shields the application developer from having to know
anything about the identity of installed services. Application developers just
use services of value to them, perhaps without even realizing it. At the same
time this architecture permits service providers to effectively manage the available
resources in their packages.

Often the use of new sound services is transparent to the application program.
For example, imagine a situation where an application developer wants to read
in a stream of audio from a file. Assuming that `thePathName` identifies
an audio input file, the program does this:

```
    File theInFile = new File(thePathName);
    AudioInputStream theInStream = AudioSystem.getAudioInputStream(theInFile); 

```

Behind the scenes, the `AudioSystem` determines what installed service
can read the file and asks it to supply the audio data as an `AudioInputStream`
object. The developer might not know or even care that the input audio file is
in some new file format (such as Acme's), supported by installed third-party services.
The program's first contact with the stream is through the `AudioSystem`
object, and all its subsequent access to the stream and its properties are through
the methods of `AudioInputStream`. Both of these are standard objects
in the `javax.sound.sampled` API; the special handling that the new
file format may require is completely hidden.

### How Providers Prepare New Services

Service providers supply their new services in specially formatted JAR files,
which are to be installed in a directory on the user's system where the Java
runtime will find them. JAR files are archive files, each containing sets of
files that might be organized in hierarchical directory structures within the
archive. Details about the preparation of the class files that go into these
archives are discussed in the next few pages, which describe the specifics of
the audio and MIDI SPI packages; here we'll just give an overview of the process
of JAR file creation.

The JAR file for a new service or services should contain a class file for
each service supported in the JAR file. Following the Java platform's convention,
each class file has the name of the newly defined class, which is a concrete
subclass of one of the abstract service provider classes. The JAR file also
must include any supporting classes required by the new service implementation.
So that the new service or services can be located by the runtime system's service
provider mechanism, the JAR file must also contain special files (described
below) that map the SPI class names to the new subclasses being defined.

To continue from our example above, say Acme Software, Inc. is distributing
a package of new sampled-audio services. Let's suppose this package consists
of two new services:

* The `AcmeAudioFileReader` class, which was mentioned above, and
  which is a subclass of `AudioFileReader`* A subclass of `AudioFileWriter` called `AcmeAudioFileWriter`,
    which will write sound files in Acme's new format

Starting from an arbitrary directory—let's call it `/devel`—where
we want to do the build, we create subdirectories and put the new class files
in them, organized in such a manner as to give the desired pathname by which the
new classes will be referenced:

```
    com/acme/AcmeAudioFileReader.class
    com/acme/AcmeAudioFileWriter.class

```

In addition, for each new SPI class being subclassed, we create a mapping file
in a specially named directory `META-INF/services`. The name of the
file is the name of the SPI class being subclassed, and the file contains the
names of the new subclasses of that SPI abstract class.

We create the file
> `META-INF/services/javax.sound.sampled.spi.AudioFileReader`, which
> consists of
>
> > ```
> >
> >     # Providers of sound file-reading services 
> >     # (a comment line begins with a pound sign)
> >     com.acme.AcmeAudioFileReader
> >
> > ```

and also the file

> `META-INF/services/javax.sound.sampled.spi.AudioFileWriter,` which
> consists of
>
> > ```
> >    # Providers of sound file-writing services 
> >     com.acme.AcmeAudioFileWriter
> >
> > ```

Now we run `jar` from any directory with the command line:

> ```
> jar cvf acme.jar -C /devel .
>
> ```

The `-C` option causes `jar` to switch to the `/devel` directory, instead of using the directory in which the command is executed. The final period argument instructs `jar` to archive all the contents of that directory (namely, `/devel`), but not thedirectory itself.

This run will create the file `acme.jar` with the contents:
> ```
> com/acme/AcmeAudioFileReader.class
> com/acme/AcmeAudioFileWriter.class
> META-INF/services/javax.sound.sampled.spi.AudioFileReader
> META-INF/services/javax.sound.sampled.spi.AudioFileWriter
> META-INF/Manifest.mf
>
> ```

The file `Manifest.mf,` which is generated by the `jar` utility itself, is a list of all the files contained in the archive.

### How Users Install New Services

For end users (or system administrators) who wish to get access to a new service
through their application programs, installation is simple. They place the provided
JAR file in a directory in their `CLASSPATH.` Upon execution, the
Java runtime will find the referenced classes when needed.

It's not an error to install more than one provider for the same service.
For example, two different service providers might supply support for reading
the same type of sound file. In such a case, the system arbitrarily chooses
one of the providers. Users who care which provider is chosen should install
only the desired one.

[« Previous](MIDI-synth.html)
•
[Trail](./TOC.html)
•
[Next »](SPI-providing-sampled.html)

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

**Previous page:** Synthesizing Sound
  
**Next page:** Providing Sampled-Audio Services




A browser with JavaScript enabled is required for this page to operate properly.