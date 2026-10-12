Source: https://ableset.com/docs/count-in

# Count-In

AbleSet has a Count-In feature which allows you to start playback of sections a
few bars before the section starts. This is helpful for practice situations
where you want to work on a specific section.

![Count-In Settings](https://ableset.com/images/docs/18-count-in/count-in-settings.png)

The menu allows you to choose between a 1-bar, 2-bar, or 4-bar count-in. You can
also choose to solo the click track during the count-in. AbleSet will look for
the first track or group that contains "click" as the click track.

Tracks named "Lifesine" will always be soloed as well so if you're using a
[redundant audio interface](https://ableset.com/docs/audio-interfaces), it won't failover to your
backup computer.

You can mark additional tracks as click tracks by adding the `+CLICK` flag to
their name. These tracks will also be soloed during count-ins.

For count-in to work reliably in versions of Live older than 11.1.5, make sure
that you set Live's grid size to a fixed "1 bar" or lower. Otherwise, AbleSet
will not be able to correctly position the playhead, and you'll get a warning
message.
