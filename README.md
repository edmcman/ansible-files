# Ed's Ansible Configs

This is how I configure my computer.  Some of it is probably reusable.  Maybe some of it is easy helpful!  Who knows.

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
* Why doesn't session/exit work?  Also notion saved layout.
* dorothy?
* rear
* sedutil better version than linux_stable
* pyenv
* wine office? https://ruados.github.io/articles/2021-05/office365-wine
* Why doesn't screenshot key register?
* Is it possible to get personal & work Chrome profiles to go to the right frame
  automatically?  Probably, using `--user-data-dir` and `--class`.
* Auto prompt for Kerberos password?  It appears to do this with pam I'd have to rename my account.

# Thoughts

There are two steps:
1. Provisioning
2. Configuration
 
