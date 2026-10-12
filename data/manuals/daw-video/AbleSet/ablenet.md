Source: https://ableset.com/docs/ablenet

# AbleNet: Redundant Playback Setups

AbleNet allows you to control two or more computers in a redundant playback
setup. AbleNet is decentralized, so any computer in the setup can crash or lose
connection – as long as one computer is still online, AbleSet will continue
working.

I've created a short video that explains the basic steps:

[Open YouTube Video](https://youtu.be/HgQyiJ-t7jg?t=0)

In short, to setup AbleNet, open the same Ableton session and enable AbleNet in
the settings menu of AbleSet on all computers. The computers will automatically
connect to each other and can now be controlled simultaneously with AbleSet.

You can open AbleSet in the browser or on your mobile device using either
computer's IP address. When the computer you're currently connected to goes
offline, AbleSet will automatically redirect you to the next available computer.

To connect two computers to the same output channels, you could use any of the
[compatible redundant audio interfaces](https://ableset.com/docs/audio-interfaces). These allow you to connect two or more
computers and automatically switch to the backup computer when it detects that
the main one isn't working anymore.

## Automatic Drift Correction

Sometimes, your instances of Live might not start playback exactly at the same
time, either because of network or disk latency. AbleNet offers an Automatic
Drift Correction that takes care of nudging your computers back into sync.

To do this, AbleSet uses Live's Phase Nudge buttons to slightly slow down or
speed up playback until all computers are in sync. You'll see the buttons flash
while this happens:

[](/images/docs/09-ablenet/drift-correction.webm)

In most cases, you don't need this, and if you do, you only want to enable this
setting on your backup computer so that it can sync to your main computer and
your main computer doesn't speed up or slow down playback, even if just
slightly, to get in sync with the backup one.

For Automatic Drift Correction to work correctly, all audio clips have to be
warped so they can follow the slight tempo changes caused by the Phase Nudge
adjustments. Unwarped audio clips will continue playing at normal speed and
get out of sync with Live's metronome.

I'd recommend using the *Texture* or *Beats* warp mode for audio clips as they
both don't alter the audio output at all while playing at normal speed.

## Custom IP Addresses

AbleNet uses Apple's [Bonjour protocol](https://en.wikipedia.org/wiki/Bonjour_(software)) to automatically detect other instances
of AbleSet on the network. This will work in most cases, but if it doesn't, you
can manually specify a list of IP addresses that AbleSet should connect to.

To do that, go to AbleSet's Settings page and scroll down to the AbleNet section.
In a setup with two computers, you can enter the IP address of the other computer
respectively in the "Connect to Custom IPs" field:

![Custom IP Addresses Settings Window](https://ableset.com/images/docs/09-ablenet/custom-ips.png)

Giving your computers static IP addresses simplifies this setup since you don't
have to update this setting every time your computers get automatically assigned
a new one. You can read more about this on the [Network documentation](https://ableset.com/docs/network/#create-a-network-using-a-switch).

If AbleSet is running on a custom port, you can add it to the IP address, e.g.
192.168.198.20:3005.

## Sync Playback Now

In case one of your computers or Ableton crashes, you can use the "Sync Playback
Now" option to synchronize its playhead position with the one of your other
computer and start playback so that both sessions are playing in sync again.
This usually takes just a few seconds.

## Tips for Using AbleNet

* Ideally, you should connect all computers via Ethernet. That way, they're not
  susceptible to wireless interference which could cause latency issues.
* Make sure that you're loading the exact same set on all computers. Otherwise,
  the computers might behave differently when jumping between songs.
