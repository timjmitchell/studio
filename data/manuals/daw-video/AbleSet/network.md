Source: https://ableset.com/docs/network

# Connecting to AbleSet From Other Devices

AbleSet hosts its own server which you can access from any other device's
browser as long as it is on the same network as your computer. This doesn't
require an internet connection, so you can set up your own local network on
stage.

There are a few different ways to create a network, and some might suit your
setup more than others.

## Connect an iPhone or iPad to your Mac

If you don't use [AbleNet](https://ableset.com/docs/ablenet) and just want to connect to AbleSet
from an iPhone or iPad with a wired connection and without any extra dongles,
this is the easiest way.

First, connect your iPhone or iPad to your Mac via USB. If you're using macOS Monterey
or older, open your Sharing preferences and go to "Internet Sharing" in the sidebar:

![Sharing Preferences](https://ableset.com/images/docs/07-network/sharing.jpg)

1. Make sure that "Share your connection from" is set to Wi-Fi. Your WiFi
   doesn't need to be connected to any network for this to work, but for some
   reason choosing Wi-Fi here works best.
2. In the list of "To computers using", check your iPhone's or iPad's connection
   – it should be called "iPhone USB" or "iPad USB".
3. Then check the checkbox next to "Internet Sharing" to turn sharing on.

You can now connect to AbleSet using the .local domain or the remote IP address
that is shown in AbleSet's menu bar window.

If you're using macOS Ventura or newer, you'll find these settings by clicking on
"General" in the sidebar, then clicking on "Sharing" and then clicking on the
little info icon next to "Internet Sharing". You should see a dialog that looks
like this:

![Sharing Preferences on macOS Ventura or newer](https://ableset.com/images/docs/07-network/sharing-ventura.jpeg)

1. Click on the toggle at the top to enable the sharing settings, confirm the
   warning message if necessary.
2. Set "Share your connection from" to "Wi-Fi". Your WiFi
   doesn't need to be connected to any network for this to work, but for some
   reason choosing Wi-Fi here works best.
3. In the list of "To devices using", check your iPhone's or iPad's connection
   – it should be called "iPhone USB" or "iPad USB".
4. Click "Done" to close the dialog.

## Create a Network Using a Router

If you want to connect to AbleSet from multiple devices, you can use a router.
This is one of the most common setups for on-stage networks and any simple
router with or without Wi-Fi can be used for this.

Follow your router's instruction manual to set it up and then connect both your
computer and the devices you want to use to connect to AbleSet to it. Most
routers will automatically assign IP addresses so you don't need to worry about
that.

Once all devices are connected, you can access AbleSet using either the .local
domain or the remote IP address shown in the app's menu bar window.

Although it is possible to connect to AbleSet using Wi-Fi, I'd recommend using a
wired Ethernet connection on stage since there will likely be lots of wireless
interference from microphones, IEM systems, and other devices.

There are Lightning/USB-C to Ethernet dongles available if you want to connect a
phone or tablet to your network with a wired connection.

## Create a Network Using a Switch

This is similar to setting up a network using a router, except that switches
often don't assign IP addresses to your devices automatically. You can manually
assign IP addresses to your devices by going to the device's network settings
and setting the "Configure IPv4" option to "Manually", or similar depending the
device you use.

When choosing an IP address, make sure that the first three parts match on all
devices. For example, you could use the IP address `192.168.1.100` for your
first device, `192.168.1.101` for the second, and so on.

Make sure that the subnet mask is set to `255.255.255.0` on all devices.

## Connect Two Devices Directly Using Ethernet

Instead of using a switch, you can also connect two devices directly using
Ethernet. This is useful if you only have two devices and don't want to use a
router or switch.

If you connect two Apple devices – iPhone/iPad/Mac – directly using Ethernet,
they should automatically assign IP addresses. If this doesn't happen or you're
not using Apple devices, you can set your devices' IP addresses manually using
the steps described in the previous section.
