# Release

Holds the metadata used by the [OTA update client](https://gitlab.com/calyxos/platform_packages_apps_updater)
OTA Server: https://release.calyxinstitute.org/

### Channels
* stable - The default, stable channel.
* beta - The beta channel, first to get updates.

These can be set via the Updater app. These builds are known working, 

Additionally,
* testing - For internal testing. Every build starts here.
* otatest - For testing OTAs of updates. See https://gitlab.com/calyxos/calyxos/-/issues/13

### Devices
| Codename | Name |
| -------- | ---- |
| walleye | Pixel 2 |
| taimen | Pixel 2 XL |
| blueline | Pixel 3 |
| crosshatch | Pixel 3 XL |
| sargo | Pixel 3a |
| bonito | Pixel 3a XL |
| flame | Pixel 4 |
| coral | Pixel 4 XL |
| jasmine_sprout | Xiaomi Mi A2 |

## Files

### $device-$channel
e.g. walleye-stable

This indicates a stable build for the device walleye (Pixel 2)

### $device-$channel-changelog.html
e.g. walleye-stable-changelog.html

This contains the changelog for the particular build.

Most of the time it's the same for all devices, but it may differ on certain occassions.
