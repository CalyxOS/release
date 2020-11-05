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
| sunfish | Pixel 4a |
| jasmine_sprout | Xiaomi Mi A2 |

## Files

### $device-$channel (build_number timestamp build_id)
e.g. walleye-stable (2020.05.06.14 1588775806 QQ2A.200501.001.B3)

This indicates a stable build for the device walleye (Pixel 2)

On the server, this is available as:
walleye-ota_update-2020.05.06.14.zip
walleye-factory-2020.05.06.14.zip

Additionally, incremental updates are also generated against the previous stable build.

### $device-$channel-changelog.html
e.g. walleye-stable-changelog.html

This contains the changelog for the particular build.

Most of the time it's the same for all devices, but it may differ on certain occassions.
