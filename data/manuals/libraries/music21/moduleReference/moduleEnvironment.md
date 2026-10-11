Source: https://music21.org/music21docs/moduleReference/moduleEnvironment.html

# music21.environment

The environment module describes an object for accessing and setting
variables related to the user’s music21 environment. Such variables include
the location of external applications such as MusicXML readers (e.g. MuseScore),
whether music21 is allowed to download files directly (via the virtual corpus),
and other settings.

Additional documentation for and examples of using this module are found in
[User’s Guide, Chapter 24, Environment](../usersGuide/usersGuide_24_environment.html#usersguide-24-environment).

# TODO: Update to user’s guide – showing each function

## UserSettings

class music21.environment.UserSettings[[source]](../_modules/music21/environment.html#UserSettings)
:   The UserSettings object provides a simple interface for configuring the
    user preferences in the [`Environment`](#music21.environment.Environment "music21.environment.Environment") object.

    It automatically writes all changes to disk.

    First, create an instance of UserSettings:

    ```python
    >>> us = environment.UserSettings()
    ```

    Second, view the available settings keys.

    ```python
    >>> for key in sorted(us.keys()):
    ...     key
    'autoDownload'
    'braillePath'
    'debug'
    'directoryScratch'
    'graphicsPath'
    'ipythonShowFormat'
    'lilypondBackend'
    'lilypondFormat'
    'lilypondPath'
    'lilypondVersion'
    'localCorporaSettings'
    'localCorpusPath'
    'localCorpusSettings'
    'manualCoreCorpusPath'
    'midiPath'
    'musescoreDirectPNGPath'
    'musicxmlPath'
    'pdfPath'
    'showFormat'
    'vectorPath'
    'warnings'
    'writeFormat'
    ```

    Third, after finding the desired setting, supply the new value as a Python
    dictionary key value pair. Setting this value updates the user’s settings
    file. For example, to set the file path to the Application that will be
    used to open MusicXML files, use the ‘musicxmlPath’ key.

    ```python
    >>> us['musicxmlPath'] = '/Applications/Finale Reader.app'
    >>> us['musicxmlPath']
    '/Applications/Finale Reader.app'
    ```

    Note that the ‘localCorpusPath’ setting operates in a slightly different
    manner than other settings. Each time the ‘localCorpusPath’ setting is set,
    an additional local corpus file path is added to the list of local corpus
    paths (unless that path is already defined in the list of local corpus
    paths). To view all local corpus paths, access the ‘localCorpusSettings’
    settings. This setting can also be used to set a complete list of file
    paths.

    ```python
    >>> us['localCorpusPath'] = '~/Documents'
    >>> list(us['localCorpusSettings'])
    ['~/Documents']
    ```

    Alternatively, the environment.py module provides convenience functions for
    setting these settings: [`keys()`](#music21.environment.keys "music21.environment.keys"),
    [`get()`](#music21.environment.get "music21.environment.get"), and [`set()`](#music21.environment.set "music21.environment.set").

[`UserSettings`](#music21.environment.UserSettings "music21.environment.UserSettings") methods

UserSettings.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/environment.html#UserSettings.__getitem__)

UserSettings.create()[[source]](../_modules/music21/environment.html#UserSettings.create)
:   If an environment configuration file does not exist, create one based on
    the default settings.

UserSettings.delete()[[source]](../_modules/music21/environment.html#UserSettings.delete)
:   Permanently remove the user configuration file.

UserSettings.getSettingsPath()[[source]](../_modules/music21/environment.html#UserSettings.getSettingsPath)
:   Return the path to the platform specific settings file.

UserSettings.items()[[source]](../_modules/music21/environment.html#UserSettings.items)
:   dict-like interface to allow iterating over items of the UserSettings.

UserSettings.keys()[[source]](../_modules/music21/environment.html#UserSettings.keys)
:   Return the keys found in the user’s
    [`Environment`](#music21.environment.Environment "music21.environment.Environment") object.

    Changed in v9.3 – yields a generator, like Python 3 dict – rather than
    :   returning a list

UserSettings.restoreDefaults()[[source]](../_modules/music21/environment.html#UserSettings.restoreDefaults)
:   Restore platform specific defaults.

UserSettings.values()[[source]](../_modules/music21/environment.html#UserSettings.values)
:   dict-like interface to allow iterating over values of the UserSettings.

## Environment

class music21.environment.Environment(*modName=None*, *forcePlatform=None*)[[source]](../_modules/music21/environment.html#Environment)
:   The environment.Environment object stores user preferences as a
    dictionary-like object. Additionally, the Environment object provides
    convenience methods to music21 modules for getting temporary files,
    launching files with external applications, and printing debug and warning
    messages.

    Generally, each module creates a single, module-level instance of
    Environment, passing the module’s name during creation. (This is an
    efficient operation since the Environment module caches most information
    from module to module)

    For a more user-friendly interface for creating and editing settings, see
    the [`UserSettings`](#music21.environment.UserSettings "music21.environment.UserSettings") object.

    ```python
    >>> env = environment.Environment(forcePlatform='darwin')
    >>> env['musicxmlPath'] = '/Applications/Finale Reader.app'
    >>> env['musicxmlPath']
    PosixPath('/Applications/Finale Reader.app')
    ```

[`Environment`](#music21.environment.Environment "music21.environment.Environment") methods

Environment.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/environment.html#Environment.__getitem__)

Environment.formatToApp(*m21Format*)[[source]](../_modules/music21/environment.html#Environment.formatToApp)

Environment.formatToKey(*m21Format*)[[source]](../_modules/music21/environment.html#Environment.formatToKey)

Environment.getDefaultRootTempDir()[[source]](../_modules/music21/environment.html#Environment.getDefaultRootTempDir)
:   Use the Python tempfile.gettempdir() to get the system specified
    temporary directory, and try to add a new ‘music21’ directory, and then
    return this directory.

    This method is only called if the no scratch directory preference has
    been set.

    If not able to create a ‘music21’ directory, the standard default is
    returned.

    Returns a pathlib.Path

Environment.getKeysToPaths()[[source]](../_modules/music21/environment.html#Environment.getKeysToPaths)
:   Get the keys that refer to file paths.

    ```python
    >>> a = environment.Environment()
    >>> for x in sorted(a.getKeysToPaths()):
    ...     x
    ...
    'braillePath'
    'graphicsPath'
    'lilypondPath'
    'localCorpusPath'
    'manualCoreCorpusPath'
    'midiPath'
    'musescoreDirectPNGPath'
    'musicxmlPath'
    'pdfPath'
    'vectorPath'
    ```

Environment.getRefKeys()[[source]](../_modules/music21/environment.html#Environment.getRefKeys)
:   Get the raw keys stored in the internal reference dictionary.

    These are different from the keys() method in that the
    ‘localCorpusPath’ entry is not included.

    ```python
    >>> a = environment.Environment()
    >>> for x in sorted(a.getRefKeys()):
    ...     x
    ...
    'autoDownload'
    'braillePath'
    'debug'
    'directoryScratch'
    'graphicsPath'
    'ipythonShowFormat'
    'lilypondBackend'
    'lilypondFormat'
    'lilypondPath'
    'lilypondVersion'
    'localCorporaSettings'
    'localCorpusSettings'
    'manualCoreCorpusPath'
    'midiPath'
    'musescoreDirectPNGPath'
    'musicxmlPath'
    'pdfPath'
    'showFormat'
    'vectorPath'
    'warnings'
    'writeFormat'
    ```

Environment.getRootTempDir()[[source]](../_modules/music21/environment.html#Environment.getRootTempDir)
:   Return a directory for writing temporary files. This does not create a
    new directory for each use, but either uses the user-set preference or
    gets the system-provided directory (with a music21 subdirectory, if
    possible).

Environment.getSettingsPath()[[source]](../_modules/music21/environment.html#Environment.getSettingsPath)
:   Return the path to the platform specific settings file.

Environment.getTempFile(*suffix: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *returnPathlib: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/environment.html#Environment.getTempFile)

Environment.getTempFile(*suffix: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *returnPathlib: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True] = True*) → [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)")
:   Return a file path to a temporary file with the specified suffix (file
    extension).

    v5 – added returnPathlib.
    v6 – returnPathlib defaults to True.

Environment.keys()[[source]](../_modules/music21/environment.html#Environment.keys)
:   Return valid keys to get and set values for the Environment instance.

    ```python
    >>> e = environment.Environment()
    >>> for x in sorted(list(e.keys())):
    ...     x
    ...
    'autoDownload'
    'braillePath'
    'debug'
    'directoryScratch'
    'graphicsPath'
    'ipythonShowFormat'
    'lilypondBackend'
    'lilypondFormat'
    'lilypondPath'
    'lilypondVersion'
    'localCorporaSettings'
    'localCorpusPath'
    'localCorpusSettings'
    'manualCoreCorpusPath'
    'midiPath'
    'musescoreDirectPNGPath'
    'musicxmlPath'
    'pdfPath'
    'showFormat'
    'vectorPath'
    'warnings'
    'writeFormat'
    ```

Environment.printDebug(*msg*, *statusLevel=1*)[[source]](../_modules/music21/environment.html#Environment.printDebug)
:   Format one or more data elements into string, and print it to stderr.
    The first arg can be a list of strings or a string; lists are
    concatenated with common.formatStr().

Environment.read(*filePath=None*)[[source]](../_modules/music21/environment.html#Environment.read)
:   Load an XML preference file if and only if the file is available
    and has been written in the past. This means that no preference file
    will ever be written unless manually done so. If no preference file
    exists, the method returns None.

Environment.restoreDefaults()[[source]](../_modules/music21/environment.html#Environment.restoreDefaults)
:   Restore only defaults for all parameters. Useful for testing.

    ```python
    >>> a = environment.Environment()
    >>> a['debug'] = 1
    >>> a.restoreDefaults()
    >>> a['debug']
    0
    ```

    And we can `read()` the environment settings back from our
    configuration file to restore our normal working environment.

    ```python
    >>> a = environment.Environment().read()
    ```

Environment.warn(*msg*, *header=None*)[[source]](../_modules/music21/environment.html#Environment.warn)
:   To print a warning to the user, send a list of strings to this method.
    Similar to printDebug but even if debug is off.

Environment.write(*filePath=None*)[[source]](../_modules/music21/environment.html#Environment.write)
:   Write an XML preference file. This must be manually called to store
    any changes made to the object and access preferences later.
    If filePath is None, the default storage location will be used.

Environment.xmlReaderType()[[source]](../_modules/music21/environment.html#Environment.xmlReaderType)
:   Returns an xmlReaderType depending on the ‘musicxmlPath’

    ```python
    >>> a = environment.Environment()
    >>> a['musicxmlPath'] = '/Applications/Musescore.app'
    >>> a.xmlReaderType()
    'Musescore'
    >>> a['musicxmlPath'] = '/Applications/Sibelius 7.app'
    >>> a.xmlReaderType()
    'Sibelius'
    >>> a['musicxmlPath'] = r'C:\Program Files\Finale\Finale 2014.exe'
    >>> a.xmlReaderType()
    'Finale'
    ```

    Nostalgia is unknown…

    ```python
    >>> a['musicxmlPath'] = r'C:\Program Files\Deluxe Music Construction Set.exe'
    >>> a.xmlReaderType()
    'unknown'
    ```

    ```python
    >>> a['musicxmlPath'] = None
    >>> a.xmlReaderType() is None
    True
    ```

[`Environment`](#music21.environment.Environment "music21.environment.Environment") instance variables

Environment.modNameParent
:   A string representation of the module that contains this
    Environment instance.

## LocalCorpusSettings

class music21.environment.LocalCorpusSettings(*paths=None*, *name=None*, *cacheFilePath=None*)[[source]](../_modules/music21/environment.html#LocalCorpusSettings)
:   A lightweight object for storing the ‘LocalCorpusSettings’ tag in the
    .music21rc

    It is a subclass of list and has two additional attributes, name (which
    should be None for the unnamed localCorpus) and cacheFilePath
    for a full filepath (ending in .json) as a location
    to store the .metadataBundle (.json) cache for the
    LocalCorpus. This can be None, in which case the (volatile) temp
    directory is used.

    ```python
    >>> lcs = environment.LocalCorpusSettings(['/tmp', '/home'])
    >>> lcs
    LocalCorpusSettings(['/tmp', '/home'])
    ```

    ```python
    >>> lcs.name = 'theWholeEnchilada'
    >>> lcs
    LocalCorpusSettings(['/tmp', '/home'], name='theWholeEnchilada')
    ```

    ```python
    >>> lcs.cacheFilePath = '/home/enchilada.json'
    >>> lcs
    LocalCorpusSettings(['/tmp', '/home'],
                        name='theWholeEnchilada',
                        cacheFilePath='/home/enchilada.json')
    ```

    ```python
    >>> list(lcs)
    ['/tmp', '/home']
    >>> lcs.name
    'theWholeEnchilada'
    >>> lcs.cacheFilePath
    '/home/enchilada.json'
    >>> '/home' in lcs
    True
    >>> '/root' in lcs
    False
    ```

## Functions

music21.environment.envSingleton()[[source]](../_modules/music21/environment.html#envSingleton)
:   returns the \_environStorage[‘instance’], \_EnvironmentCore singleton
    object

music21.environment.etIndent(*elem*, *level=0*, *spaces=2*)[[source]](../_modules/music21/environment.html#etIndent)
:   indent an elementTree element for printing

music21.environment.get(*key*)[[source]](../_modules/music21/environment.html#get)
:   Return the current setting of a UserSettings key.

    This will create a user settings file if necessary:

    ```python
    >>> environment.get('musicxmlPath')
    '/Applications/Finale Reader.app'
    ```

music21.environment.keys()[[source]](../_modules/music21/environment.html#keys)
:   Return all valid UserSettings keys.

music21.environment.set(*key*, *value*)[[source]](../_modules/music21/environment.html#set)
:   Directly set a single UserSettings key, by providing a key and the
    appropriate value. This will create a user settings file if necessary.

    ```python
    >>> environment.set('wer', 'asdf')
    Traceback (most recent call last):
    music21.environment.EnvironmentException: no preference: wer
    ```

    ```python
    >>> environment.set('musicxmlPath', '/Applications/Finale Reader.app')
    ```
