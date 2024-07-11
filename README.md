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
* Why doesn't session/exit work?  Also notion saved layout.
* Install dorothy?
* pyenv
* wine office? https://ruados.github.io/articles/2021-05/office365-wine
* Add directories to "bookmarks" in open dialogs

# Development notes

To test versions of `sei_ansible` locally, use the following command:

```bash
ansible-galaxy collection install /path/to/sei-ansible/eschwartz/ --force
```