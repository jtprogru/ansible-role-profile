# jtprogru.profile

![CI](https://img.shields.io/github/actions/workflow/status/jtprogru/ansible-role-profile/ci.yml?branch=master&label=CI)
![Release](https://img.shields.io/github/actions/workflow/status/jtprogru/ansible-role-profile/release.yml?label=Release)
![License](https://img.shields.io/github/license/jtprogru/ansible-role-profile)
![Ansible Role](https://img.shields.io/ansible/role/52416)

My personal role for configuring a user account on remote Linux servers: it creates a group and a personal user, grants that group passwordless sudo, installs the user's SSH key, and installs vim.

## Role Variables

See `defaults/main.yml`. All variables are validated via `meta/argument_specs.yml`.

| Variable | Default | Description |
| --- | --- | --- |
| `profile_name` | `jtprogru` | Login name of the personal user to create. |
| `profile_group` | `admins` | Group granted passwordless sudo via a sudoers drop-in. |
| `profile_key` | `https://github.com/jtprogru.keys` | SSH public key(s) for `authorized_keys`. Accepts a raw key string or an HTTP(S) URL. |
| `profile_user_shell` | `/bin/bash` | Login shell for the personal user. |
| `profile_password` | _(unset)_ | Optional user password. When unset, the password is left untouched. |

If you want to manage the user's password, set `profile_password` — ideally encrypted with `ansible-vault`:

```bash
❯ ansible-vault encrypt_string 'P@s$W0Rd' --name 'profile_password'
profile_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          63623031323635356166633164353137353665376130383636653336653131386663333537353833
          ...
Encryption successful
```

## Example Playbook

```yaml
- hosts: all
  become: true
  gather_facts: true

  roles:
    - jtprogru.profile
```

This role uses `ansible.posix.authorized_key`; install the collection with:

```bash
ansible-galaxy collection install -r requirements.yml
```

## Local development

Tooling is kept in a local `.venv` managed by [uv](https://docs.astral.sh/uv/), so your system Ansible is never touched. Testing uses [Molecule](https://ansible.readthedocs.io/projects/molecule/) with the Docker driver and [testinfra](https://testinfra.readthedocs.io/) assertions (Docker must be running).

```bash
make setup    # create .venv, install the toolchain + collections
make lint     # yamllint + ansible-lint
make test     # full molecule cycle (create → converge → idempotence → verify → destroy)
```

Pick a target distro with `MOLECULE_DISTRO` (default `ubuntu2604`):

```bash
make test MOLECULE_DISTRO=debian13
make test-all   # runs ubuntu2604, debian13, rockylinux9
```

Handy sub-commands during development: `make converge`, `make verify`, `make login`, `make destroy`.

## License

[WTFPL](LICENSE)
