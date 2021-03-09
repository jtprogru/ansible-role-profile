# jtprogru.profile

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/ansible-role-profile/CI?label=CI) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/ansible-role-profile/Release?label=Release) ![GitHub](https://img.shields.io/github/license/jtprogru/ansible-role-profile) ![Ansible Role](https://img.shields.io/ansible/role/53231)

This is my personal role for configure my account on remote servers


## Role Variables

See `defaults/main.yml`

Before running playbook you need to change password with this command:
```bash
❯ ansible-vault encrypt_string 'P@s$W0Rd' --name 'profile_password'
profile_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66303239653430313165373362383164373333303638646664616664356330373865333539323566
          6563636536343531326166343664643432613234363837380a623536346136323837623466643364
          38333865323366373164616335323962363630313735366362363033613166616164626239313762
          3933623264356335380a636361373561373430626563363761626130366134353633633739336361
          3834
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
