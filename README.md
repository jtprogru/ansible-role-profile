# jtprogru.profile

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/ansible-role-profile/CI?label=CI) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/ansible-role-profile/Release?label=Release) ![GitHub](https://img.shields.io/github/license/jtprogru/ansible-role-profile) [![Ansible Role](https://img.shields.io/ansible/role/53231)](https://galaxy.ansible.com/jtprogru/profile/)

This is my personal role for configure my account on local machine (macOS) and remote servers (Linux)


## Role Variables

See `defaults/main.yml`

Before running playbook you need to change password with this command:
```bash
❯ ansible-vault encrypt_string 'P@s$W0Rd' --name 'profile_password'
profile_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          63623031323635356166633164353137353665376130383636653336653131386663333537353833
          6561633239396437373933623439643938663036323034340a633761653638646461346636306231
          32623466653336643930383332386134363264326364313933626265393537633930393161323863
          3564303863336539330a316233316236613732396237613238656239376233653665366338633164
          6564
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

## License

[WTFPL](LICENSE.md)
