Source: https://ableset.com/docs/custom-styles

# Custom Styles

If you're familiar with [CSS](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/What_is_CSS), AbleSet allows you to easily add Custom Styles to
the web app. You can find the custom CSS file by clicking on "Show Global Custom
Styles" in AbleSet's settings menu.

You can also add project-specific Custom Styles using the *Custom Styles* folder
in your Ableton Live project's [AbleSet Folder](https://ableset.com/docs/ableset-folder).

AbleSet will automatically apply your styles when you save changes to this file.

I've tried to give most elements and states in the web app meaningful class
names, but if you find yourself trying to add a style to an element that doesn't
have a good class name, feel free to reach out to me!

This is an experimental feature and your styles could break the layout of the
web app, so basic CSS knowledge is recommended. If you want to reset your
custom styles, just delete all lines from the file and save it.

## User Styles

Check out the [User Styles](https://forum.ableset.app/c/user-styles/11) category
on the AbleSet forum for a collection of styles you can use to customize
AbleSet.

## Examples

### Custom Fonts

This simple example changes the font of all elements on the performance page:

```
.performance {
  font-family: Georgia, "Times New Roman", Times, serif;
}
```

Your browser will use the first font in the list that is available. The snippet
above would look like this on macOS:

![Performance Page with Custom Fonts](https://ableset.com/images/docs/27-custom-styles/custom-font.png)

### Custom Backgrounds

All files in the global "custom-styles" folder are served under the "/custom-styles"
path, so you could add a background image called `bg.jpg` to the that folder
and reference it like this to show it behind the lyrics, for example:

```
.lyrics-page {
  background-image: url("/custom-styles/bg.jpg");
  background-size: cover;
}
```

This results in the lyrics page look like this:

![Lyrics Page with Background Image](https://ableset.com/images/docs/27-custom-styles/lyrics-bg.png)

Files stored in your project's "Custom Styles" folder are served under the
"/custom-styles/project" path, so an image file called `bg.jpg` that is stored
there could be used as a background like this:

```
.lyrics-page {
  background-image: url("/custom-styles/project/bg.jpg");
  background-size: cover;
}
```

## Custom Scripts

AbleSet lets you add custom JavaScript using the `scripts.js` file in the styles
folder. This file is loaded after all other scripts on the web app have been
loaded.

AbleSet also exposes an `ableset` object on the window that you can access.
This gives you access to the current state, sockets, and more.

For example, to get the current setlist state, you can call:

```
ableset.queryClient.getQueryData(["setlist"]);

// Use this to get a list of all queries:
console.log(ableset.queryClient.queryCache.queriesMap);
```

To observe changes in the state, you can use the `QueryObserver` object:

```
const observer = new ableset.QueryObserver(ableset.queryClient, {
  queryKey: ["setlist"],
});

observer.subscribe((result) => console.log(result.data));
```

To get access to sockets, e.g. to listen to changes in real-time, you can call:

```
// Listen to all events
ableset.getSocket("setlist").onAny((event, data) => console.log(event, data));

// Listen to specific event
ableset.getSocket("global").on("songTime", (time) => console.log(time));
```

The following sockets are available:

* `global`
* `setlist`
* `lyrics`
* `canvas`
* `mixer`
* `ablenet`
* `audioInterfaces`
* `timecode`
* `settings`
* `midiMapping`

Feel free to experiment with the events each of these sockets receives.
