Source: https://music21.org/music21docs/moduleReference/moduleVexflowToMusic21j.html

# music21.vexflow.toMusic21j

Convert a music21 object into JSON and send it to the browser for music21j to use.

## VexflowPickler

class music21.vexflow.toMusic21j.VexflowPickler[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler)

[`VexflowPickler`](#music21.vexflow.toMusic21j.VexflowPickler "music21.vexflow.toMusic21j.VexflowPickler") methods

VexflowPickler.fromObject(*thisObject*, *mode=None*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.fromObject)

VexflowPickler.fromStream(*thisStream*, *mode=None*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.fromStream)

VexflowPickler.getHTML(*dataSplit*, *title=None*, *defaults=None*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.getHTML)
:   Get the complete HTML page to pass to the browser:

    ```python
    >>> vfp = vexflow.toMusic21j.VexflowPickler()
    >>> print(vfp.getHTML('{"hi": "hello"}', 'myPiece'))
       <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
                "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <!-- for MSIE 10 on Windows 8 -->
        <meta http-equiv="X-UA-Compatible" content="requiresActiveX=true"/>
        <title>myPiece</title>
        <script data-main='https://www.music21.org/music21j/src/music21'
                src='https://www.music21.org/music21j/ext/require/require.js'></script>
        <script>
        require(['music21'], function() {
                        var pickleIn = {"hi": "hello"};
                        var jpc = new music21.fromPython.Converter();
                        streamObj = jpc.run(pickleIn);
                        streamObj.renderOptions.events.resize = "reflow";
                    streamObj.appendNewCanvas();
                    });
        </script>
        </head>
        <body>
        </body>
        </html>
    ```

VexflowPickler.getJSBody(*dataSplit*, *defaults=None*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.getJSBody)
:   Get the javascript code without the <script> tags to render the JSON

    ```python
    >>> vfp = vexflow.toMusic21j.VexflowPickler()
    >>> print(vfp.getJSBody('{"hi": "hello"}'))
            require(['music21'], function() {
                var pickleIn = {"hi": "hello"};
                var jpc = new music21.fromPython.Converter();
                streamObj = jpc.run(pickleIn);
                streamObj.renderOptions.events.resize = "reflow";
            streamObj.appendNewCanvas();
            });
    ```

VexflowPickler.getJSBodyScript(*dataSplit*, *defaults=None*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.getJSBodyScript)
:   Get the <script>…</script> tag to render the JSON

    ```python
    >>> vfp = vexflow.toMusic21j.VexflowPickler()
    >>> print(vfp.getJSBodyScript('{"hi": "hello"}'))
       <script>
            require(['music21'], function() {
                var pickleIn = {"hi": "hello"};
                var jpc = new music21.fromPython.Converter();
                streamObj = jpc.run(pickleIn);
                streamObj.renderOptions.events.resize = "reflow";
            streamObj.appendNewCanvas();
            });
        </script>
    ```

VexflowPickler.getLoadTemplate(*urls=None*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.getLoadTemplate)
:   Gets the <script> tag for loading music21 from require.js

    ```python
    >>> vfp = vexflow.toMusic21j.VexflowPickler()
    >>> vfp.getLoadTemplate()
    "<script data-main='https://www.music21.org/music21j/src/music21'
        src='https://www.music21.org/music21j/ext/require/require.js'></script>"
    ```

    ```python
    >>> d = {'m21URI': 'file:///tmp/music21', 'requireURI': 'http://requirejs.com/require.js'}
    >>> vfp.getLoadTemplate(d)
    "<script data-main='file:///tmp/music21' src='http://requirejs.com/require.js'></script>"
    ```

VexflowPickler.splitLongJSON(*jsonString*, *chunkSize=110*)[[source]](../_modules/music21/vexflow/toMusic21j.html#VexflowPickler.splitLongJSON)

## Functions

music21.vexflow.toMusic21j.fromObject(*thisObject*, *\**, *mode='html'*, *local=False*)[[source]](../_modules/music21/vexflow/toMusic21j.html#fromObject)
:   returns a string of data for a given Music21Object such as a Score, Note, etc. that
    can be displayed in a browser using the music21j package. Called by .show(‘vexflow’).

    ```python
    >>> n = note.Note('C#4')
    >>> print(vexflow.toMusic21j.fromObject(n))
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
            "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <!-- for MSIE 10 on Windows 8 -->
        <meta http-equiv="X-UA-Compatible" content="requiresActiveX=true"/>
        <title>Music21 Fragment</title>
        <script data-main='https://www.music21.org/music21j/src/music21'
                src='https://www.music21.org/music21j/ext/require/require.js'></script>
        <script>
            require(['music21'], function() {
                var pickleIn = '{"m21Version": {"py/tuple": [1, 9, 2]}, "stream":
    {"_mutable": true, "_activeSite": null, "' +
    '_priority": 0, "_elements": [], "_cache": {}, "definesExplicitPageBreaks":
    false, "_unlinkedDuration": null, "' +
    'id": ..., "_duration": null, "py/object": "music21.stream.Stream",
    "streamStatus": {"py/object": "music' +
    '21.stream.streamStatus.StreamStatus", "_enharmonics": null,
    "_dirty": null, "_concertPitch": null, "_accidentals"' +
    ': null, "_ties": null, "_rests": null, "_ornaments": null,
    "_client": null, "_beams": null, "_measures": nu' +
    ...
    'd": null}, "definesExplicitSystemBreaks": false, ...}}';
                var jpc = new music21.fromPython.Converter();
                streamObj = jpc.run(pickleIn);
                streamObj.renderOptions.events.resize = "reflow";
                streamObj.appendNewCanvas();
            });
        </script>

    </head>
    <body>
    </body>
    </html>
    ```

    * Changed in v8: mode and useLocal are keyword only.
