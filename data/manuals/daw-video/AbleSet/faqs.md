Source: https://ableset.com/docs/faqs

# Frequently Asked Questions

## Compatibility

### What version of Live is AbleSet compatible with?

AbleSet works with all editions of Live 10, 11, and 12, though some features like
section clips and lyrics tracks require Live 11 or 12. If you want to use the Max
for Live controller, you either need Live Suite or the Max upgrade for Live
Standard.

### What version of macOS can AbleSet run on?

I've tested and officially support AbleSet on macOS Monterey (12) and higher.

### What version of Windows can AbleSet run on?

AbleSet can run on Windows 10 and 11.

### What version of iOS or iPadOS is AbleSet compatible with?

AbleSet is officially compatible with iOS 15 and newer, but you might be able to
use it on versions as old as iOS 12. If your iPhone or iPad supports iOS 13, it
can also be updated to iOS 15. You can find a list of all supported [iPads](https://en.wikipedia.org/wiki/IPadOS_15#Supported_devices) and
[iPhones](https://en.wikipedia.org/wiki/IOS_15#Supported_devices) on Wikipedia.

Some features, like the Canvas, will likely not work on versions below iOS 15.

### What version of Android is AbleSet compatible with?

I've tested AbleSet on Android 7 and higher, but you might be able to run it on
older versions of Android as well.

## License

### How many computers can a license be activated on?

AbleSet licenses can be activated on a different number of computers depending
on their edition:

* AbleSet Intro: 1 activation
* AbleSet Standard: 2 activations
* AbleSet Pro: 3 activations

If you've upgraded from AbleSet 1, your license can still be activated on up to
four computers.

To see the status of your licenses and how many computers they can be activated
on, go to your [account](https://ableset.com/account) page.

### How can I deactivate my license on a computer?

If you still have access to your computer, open AbleSet, then click the settings
icon in AbleSet's status window and select "Deactivate Machine". This will reset
AbleSet into the demo mode on that computer and open up a slot for activating
your license on another computer.

### Can I activate my license without an internet connection?

Yes, to activate AbleSet offline, click the "Offline Activation" button in the
activation window. Scan the displayed QR code or copy the link to a device that
has an internet connection and enter your license key there.

You'll receive an activation code that you can either download as a file or copy
to your clipboard to transfer it to your offline computer. Drag or paste the key
into the activation key field to activate your license.

### How long is a license valid?

AbleSet licenses don't expire and come with one year of free updates. If you
want to update to a version that was released more than a year after you bought
your license, you can renew it from your [account](https://ableset.com/account) page.

### How much does it cost to renew my license?

This depends on which version and edition of AbleSet you bought. If you bought
AbleSet 1 or 2, renewing your license costs $75. If you bought AbleSet 3, these
are the renewal costs:

* AbleSet 3 Intro: $65
* AbleSet 3 Standard: $89
* AbleSet 3 Pro: $129

### How much does it cost to upgrade to another edition?

Upgrades cost the difference between the price of your current edition and the
edition you want to upgrade to. So, if you bought AbleSet Standard and want to
upgrade to AbleSet Pro, the total cost would be the same as if you bought
AbleSet Pro in the first place.

Here's a list of upgrade prices:

* Intro to Standard: $50
* Intro to Pro: $140
* Standard to Pro: $90

### Will my license get renewed when I upgrade it?

Yes, your license will be renewed for another year of free updates when you
upgrade it.

### Why does a license only come with one year of free updates?

I've thought about the licensing scheme for AbleSet for a long time. I don't
like subscription models where you lose access to the software you're paying for
as soon as you stop paying, but working on new features takes a lot of work, so
I decided to use this hybrid model instead.

If you're not interested in the new updates that get released more than one year
after you bought your license, you don't have to renew it and can continue using
the version you own for as long as you like. If you like the new features, you
can renew your license at any point in time to receive another year of updates.

### What are the limitations of AbleSet's free trial?

The free trial of AbleSet lets you test all features for as long as you want,
with the only limitation being that you have to restart the app every 15 minutes
for it to continue working.

### Where can I get an invoice or a receipt for my license?

The payment confirmation email you received when purchasing AbleSet contains a
link to your receipt. The linked page also allows you to generate an invoice.

## Network

### Does AbleSet have to be connected to the internet to work?

No, since AbleSet runs its own web server on your computer, you can use it
without an internet connection. Just make sure all your devices are on the same
network and you're good to go.

### How can I create a network on stage?

There are multiple ways to create a network on stage. Check out
[this guide](https://ableset.com/docs/network) for more information on this topic.

### What port does AbleSet run on?

AbleSet runs on port 80 by default. Since this is the default port for websites,
you don't have to enter it in your browser to access the web app. If AbleSet can't
start on port 80, e.g. when it's already in use by another program, it will look
for a free port starting with port 3000 and display that port in the status window.

## Redundant Setup / AbleNet

### Does AbleNet have the same 1024 bar limitation Live's sync has?

AbleNet doesn't have any limitation regarding the length of the set.

## Troubleshooting

### AbleSet is stuck on "Connecting to Ableton..."

This is a sign that AbleSet can't establish a connection to its Ableton and can
have multiple causes. Try those steps to fix it:

* Is Live running and is the AbleSet plugin selected in the MIDI preferences?
  + If you don't see the AbleSet plugin, it might not be installed. Go to
    AbleSet's settings menu, click on "Add AbleSet Plugin to Ableton", and then
    follow the assistant to install and configure the plugin.
* Do you see any error messages in the status bar of Live?

### I see "Cannot bind to ('127.0.0.1', 39041), port in use. Trying again..." in Live's status bar

This can happen if another program is already using the port Live uses to
communicate with AbleSet, or if the port wasn't closed properly by the operating
system before.

To fix this, please try restarting your computer. This resets all open ports and
should allow Live to connect to AbleSet again.

### Ableton Live doesn't jump to the next song or section in time

While Live is playing, AbleSet jumps to a song or section by activating its
locator a short time before the jump is supposed to happen which respects Live's
global quantization. You can simulate this by clicking on that locator in the
arrangement view yourself while Live is playing.

If clicking on the same locator yourself also shows the same behavior, that's a
good sign that the locator isn't placed on the quantization grid. You can fix
this either by moving the locator onto the quantization grid or by decreasing
the global quantization – 1/2 and 1/4 should work well.

### I'm getting a "Playhead is Lagging" error notification

AbleSet's plugin runs on the same thread as Live's user interface. If you're
working in a large project and it's zoomed out all the way, the plugin isn't
able to send the playhead position to AbleSet at a regular interval which can
cause all kinds of issues, like jumps to other songs not happening in time,
loop brackets not being enabled, etc.

The easiest workaround is to zoom in your timeline so only one or two songs
are visible at a time. This means Live doesn't have to render as many elements
which frees up resources for AbleSet's plugin.

Alternatively, if you have access to Max for Live, you can add the
[AbleSet Controller](https://ableset.com/docs/midi-mapping/#max-for-live-device) to your project.
This device runs independently of Live's user interface and can send the
playhead position to AbleSet at a higher frequency.

### I can't connect to AbleSet from my Android device

To connect to AbleSet from your Android phone, please make sure that it's on the
same network as your computer and then enter the Remote or Host address shown in
AbleSet's status window into your browser on Android.

If this doesn't help, sometimes disabling mobile data might do the trick as that
forces Android to look for the IP address on your local network instead of
trying to access it over the internet.

### How can I report a bug?

You can send bug reports to [support@ableset.app](mailto:support@ableset.app). To help me understand and
reproduce the bug on my end, you can include the following information:

* A description of the bug and steps that led to it
* AbleSet's log package (Settings -> Create Log Package) including the project
  file
* Pictures or videos of the bug
