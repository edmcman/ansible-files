# Canon printer driver

Installs the US UFR II driver for Ubuntu AMD64, including the imageCLASS MF4890dw. The role installs or upgrades to the pinned Debian package and leaves newer installed versions alone.

To update the pin, select a US UFR II Linux release that supports the printer from Canon's support site. Download its archive from Canon, calculate `sha256sum` on it, and inspect its `x64/Debian` directory for the `cnrdrvcups-ufr2-us` package version. Update `canon_driver_url`, `canon_driver_version`, and `canon_driver_checksum` together in `defaults/main.yml`. The version must include the Debian revision (for example, `6.40-1.01`).

The current release is [UFR II/UFRII LT V6.40](https://support.canon.ca/article/0100923702); Canon's [supported model list](https://sg.canon/en/support/0100924010) includes the MF4890dw.
