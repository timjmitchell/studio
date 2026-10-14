# Logic Pro 12: OS upgrade compatibility check (2026-10-14)

Does the macOS upgrade that Logic Pro 12 needs break anything in the studio, especially
Universal Audio? Machine facts come from the 2026-10-11 probe in
[inventory-first-pass.md](../studio/inventory-first-pass.md). Vendor facts come from web
search on 2026-10-14. Apple and UA pages were not readable directly from the research
session, so **confirm the two key requirements (Logic 12's minimum macOS, and UA's Tahoe
article) before upgrading.**

Confidence: ✅ documented · 🔶 inferred · 🧪 tested · ❓ to test.

## Verdict

Logic 12 needs **macOS 15.6 or later**, and the Mac is on **14.5 Sonoma**. Upgrading is safe for
the UA system as long as the UAD software is updated in the same session. The bigger risks are
free disk space, Roland/BOSS drivers, and SoftRAID on 26.4+. **Recommended route:** go to
Sequoia 15.6+ now and move to Tahoe once the Roland/BOSS drivers are confirmed.

## Logic Pro 12 requirements vs. this Mac

| | Logic Pro 12 | Mac Studio (probe 2026-10-11) |
|---|---|---|
| macOS | **15.6 or later** (Sequoia 15.6+ or Tahoe 26) 🔶 forums + Production Expert | **14.5 (23F79)** ❌ |
| Chip | Apple silicon (Production Expert says Intel was dropped; one blog disagrees) | M1 Max, Mac13,1 ✅ |
| Logic installed | — | 11.2.2 |

Both target OSes are supported on the M1 Max.

## Universal Audio

| Item | Installed | Status on Sequoia / Tahoe |
|---|---|---|
| Apollo x8, UAD-2 Satellite TB3, Twin X | Thunderbolt chain | ✅ UA lists Thunderbolt Apollos and Satellites as supported on both. Only FireWire units are excluded, and there are none here |
| UAD DSP plugins | 11.8.0 | 🔶 Supported. The current release is 11.8.3 (2026-03-03), so update to it |
| UAD Console | 1.3.1 | 🔶 Newer than the last version with release notes found (1.2.9). Tahoe support not confirmed from release notes |
| UA Connect 1.11.0, UA Midi Control 5.11.1, LUNA 3.0.0 | | ❓ No specific statements found. Update through UA Connect |

Known UA problems after an OS upgrade:

1. **The driver gets blocked.** Approve the UA software in System Settings › Privacy & Security
   (within about 30 minutes of installing), then restart. If this step is skipped, Console
   can't see the Apollos ✅ (UA).
2. **Reinstall may be needed** after moving to Tahoe. UA's advice is a full uninstall and
   reinstall with the Apollo Interface Software option checked ✅ (UA).
3. **UA doesn't support macOS betas.** Only install public releases ✅ (UA).
4. **The agent tooling depends on the UA Mixer Engine** (TCP 4710). After the upgrade, read back
   `/devices/0` and `/devices/1` once, on a single connection (R15), and compare them with the
   2026-10-11 snapshot ❓.

## Other risks

- ⚠️ **Disk space.** The internal SSD is 460 GB and was 86% full (about 64 GB free). A major
  macOS upgrade needs about 25–35 GB, and Logic 12's content needs more.
- ⚠️ **Roland/BOSS drivers** (UM-ONE driver, TD-17 driver 1.0.2, VE-500 driver 1.0.3). Roland's
  Tahoe list includes the **UM-ONE mk2**; which UM-ONE model this is remains ❓. Nothing was found
  for the TD-17 or VE-500. Roland advises staying on the current macOS until a product is
  verified.
- 🔶 **SoftRAID 8.6.1** (the ThunderBay RAID). It has been Tahoe-ready since 8.6, and staff say
  there are no issues on 26.3. One user saw **read-only volumes on a 26.4 beta**, so check before
  going to 26.4+.
- ✅ **SoundID Reference 5.13.5.** Officially supported on Tahoe from build 5.13.5.1210, so check
  the exact build. It runs inside Console as Apollo Monitor Correction. Microphone and Local
  Network permissions may need to be granted again.
- ❓ **Not checked:** MIDI Guitar 3, Antares, Toontrack, Arturia, IK, Soundtoys, NI, iLok, Stream
  Deck, Melodyne.
- **Logic projects.** Once a project is saved in Logic 12, Logic 11 can't open it. Back up
  `/Volumes/Samsung_X5/Hot Fog/` first.

## Upgrade order

1. Make a backup (Time Machine or the RAID) and free space on the internal SSD.
2. While still on 14.5, update the UAD software (11.8.3+), UA Connect and Console. Save the
   current Console session.
3. Upgrade to **Sequoia 15.6+**.
4. Approve UA in Privacy & Security and restart. Check that all three UA units show up, and read
   back the Mixer Engine.
5. Install Logic 12 and keep Logic 11 alongside it.
6. Move to Tahoe later, once the Roland/BOSS drivers are confirmed.

## Open questions

- Which UM-ONE is this: the original or the mk2?
- Is Tahoe specifically needed, or only Logic 12?

## Sources

- [Production Expert: Logic Pro 12, Intel Macs dropped](https://www.production-expert.com/production-expert-1/apple-announce-logic-pro-12-pushes-deeper-into-ai-and-appears-to-leaves-intel-macs-behind)
- [Logic Users Group: Logic Pro 12 released](https://logic-users-group.com/threads/logic-pro-12-released.12433/)
- [Just a Phase: Apple releases Logic Pro 12](https://www.justaphase.blog/home/2026/1/29/apple-releases-logic-pro-12)
- [Apple: Logic Pro release notes](https://support.apple.com/109503)
- [UA: UAD DSP Software Compatibility with macOS Tahoe 26](https://help.uaudio.com/hc/en-us/articles/41351505627028-UAD-DSP-Software-Compatibility-with-macOS-Tahoe-26)
- [UA: macOS UAD Software Compatibility](https://help.uaudio.com/hc/en-us/sections/40455914220564-macOS-UAD-Software-Compatibility)
- [UA: Important UAD Software Notes](https://help.uaudio.com/hc/en-us/articles/215270403)
- [UA: UAD-2 PCIe System Requirements](https://help.uaudio.com/hc/en-us/articles/206439113-UAD-2-PCIe-Card-System-Requirements)
- [UAD Forum: issues upgrading to Tahoe](https://uadforum.com/community/index.php?threads%2Fany-issues-with-upgrading-mac-os-to-tahoe.81127%2F=)
- [MOTUnation: DP11, Apollo x6 and Tahoe 26.4](https://www.motunation.com/forum/viewtopic.php?t=75517)
- [OWC: SoftRAID 8.6 for Tahoe](https://www.owc.com/blog/softraid-8-6-now-available-for-macos-26-tahoe-with-smart-over-usb-and-day-one-compatibility)
- [SoftRAID forum: 8.6.1 and macOS 26.3](https://forums.softraid.com/sequoia-issues/any-issues-with-softraid-version-8-6-1-and-macos-26-3/)
- [Roland: Compatibility with macOS](https://www.roland.com/us/support/support_news/25090811m1/)
- [Sonarworks: SoundID Reference and macOS 26 Tahoe](https://support.sonarworks.com/hc/en-us/articles/8255822380818)
