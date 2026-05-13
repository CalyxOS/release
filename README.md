# Release

Holds the metadata used by the [OTA update client](https://gitlab.com/CalyxOS/platform_packages_apps_Updater)
OTA Server: https://release.calyxos.org/

### Channels
* stable - The default, stable channel.
* security-express - The security express channel, first to get security updates.
* beta - The beta channel, first to get updates.

These can be set via the Updater app. These builds are known working.

Additionally,
* testing - For internal testing. Every build starts here.
* otatest - For testing OTAs of updates. See https://gitlab.com/CalyxOS/calyxos/-/work_items/13

## Files

### ota/$device/$device-$channel (build_number timestamp version)
e.g. ota/tegu/tegu-stable (260720100 1777254985 16)

This indicates a stable build for the device tegu (Pixel 9a)

On the server, this is available as:
ota/tegu/16/tegu-ota_update-260720100.zip
factory/tegu/16/tegu-factory-260720100.zip

Additionally, incremental updates are also generated against the previous stable build.

### ota/$device/$device-$channel-changelog.html
e.g. ota/tegu/tegu-stable-changelog.html

This contains the changelog for the particular build.

Most of the time it's the same for all devices, but it may differ on certain occassions.
