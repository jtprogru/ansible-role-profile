# jtprogru.profile

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/ansible-role-profile/CI?label=CI) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprogru/ansible-role-profile/Release?label=Release) ![GitHub](https://img.shields.io/github/license/jtprogru/ansible-role-profile) ![Ansible Role](https://img.shields.io/ansible/role/53231) 

This is my personal role for configure my account on remote servers


## Role Variables

See `defaults/main.yml`:
```yaml
---
profile_name: "savin"
profile_password: "!vault |
  $ANSIBLE_VAULT;1.1;AES256
  66303239653430313165373362383164373333303638646664616664356330373865333539323566
  6563636536343531326166343664643432613234363837380a623536346136323837623466643364
  38333865323366373164616335323962363630313735366362363033613166616164626239313762
  3933623264356335380a636361373561373430626563363761626130366134353633633739336361
  3834"

profile_key: "https://github.com/jtprog.keys"
profile_group: "admins"

profile_dotconf_files:
  - local: ".bashrc"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/bashrc"
  - local: ".aliases"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/aliases"
  - local: "flake8"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/flake8"
  - local: ".gitconfig"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/gitconfig"
  - local: ".gitignore"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/gitignore_global"
  - local: ".profile"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/profile"
  - local: ".tmux.conf"
    remote: "https://raw.githubusercontent.com/gpakosz/.tmux/master/.tmux.conf"
  - local: ".tmux.local.conf"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/tmux.local.conf"
  - local: ".vimrc"
    remote: "https://raw.githubusercontent.com/jtprog/dotconf/master/remote/vimrc"

profile_vim_plug_remote: "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
profile_vim_plug_local: "~/.vim/autoload/plug.vim"

```

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

  vars:
    my_configuration_sysops_employer:
      name: "savin"
      password: "!vault |
        $ANSIBLE_VAULT;1.1;AES256
        37343065363965316362393936303137393863356330653065363731393133663261343061373639
        3631396164386466313630346530356630383336343063330a663666353564666438383536373433
        31373131633438653531366466323033356139343834326262353662323233356264636133396163
        6365386435313938310a663634363131313636353963333731343134386632316139333038613433
        3238"

      key: "https://github.com/jtprog.keys"
      group: "admins"


  roles:
     - jtprogru.profile
```

## License

[WTFPL](LICENSE.md)
