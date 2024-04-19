# Setup

1. `./scripts/install_ansible.bash`
2. `ansible-galaxy install -r requirements.yml`
3. `sudo -E ansible-playbook --connection=local -i localhost, local.yml --tags all,initial`

The `initial` tag includes some roles that probably shouldn't be run a lot,
because they download large files each time.  So remove `initial` after you've
run it once.

# TODO

* AppImageLauncher? https://github.com/TheAssassin/AppImageLauncher/wiki/Install-on-Ubuntu-or-Debian
* SEI CA certificates (for firefox)
* beeper autostart
* volume keys
* Why doesn't session/exit work?
* git credential helper
* github gh command
* aws cli
* vmware
* nvidia cuda
* Kerberos
* dorothy?

# Thoughts

There are two steps:
1. Provisioning
2. Configuration
 