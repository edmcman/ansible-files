# Setup

1. `./scripts/install_ansible.bash`
2. `ansible-galaxy install -r requirements.yml`
3. `ansible-playbook --connection=local -i localhost, local.yml --tags all,initial -K`

The `initial` tag includes some roles that probably shouldn't be run a lot,
because they download large files each time.  So remove `initial` after you've
run it once.

It is important to use the `-K` flag with `ansible-playbook` instead of running
as root, or the dconf configuration changes will not be applied to the correct
user's profile.

# TODO

* AppImageLauncher? https://github.com/TheAssassin/AppImageLauncher/wiki/Install-on-Ubuntu-or-Debian
* SEI CA certificates (for firefox)
* beeper autostart
* volume keys
* Why doesn't session/exit work?
* git credential helper
* aws cli
* vmware
* nvidia cuda
* Kerberos
* dorothy?
* Use glib overrides
* gnome-keyring integration

# Thoughts

There are two steps:
1. Provisioning
2. Configuration
 