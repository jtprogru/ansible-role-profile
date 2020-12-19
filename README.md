# jtprog.my_configuration

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprog/ansible-role-my-configuration/CI?label=CI) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprog/ansible-role-my-configuration/Release?label=Release) ![GitHub](https://img.shields.io/github/license/jtprog/ansible-role-my-configuration)

This is my personal role for configure my account on remote servers


## Role Variables

See `defaults/main.yml`:
```yaml
---
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

my_configuration_bash_history_time_format: "%d/%m/%y %T "

my_configuration_vimrc_colorscheme: "industry"

```

Before running playbook you need to change password with this command:
```bash
❯ ansible-vault encrypt_string 'P@s$W0Rd' --name 'my_configuration_sysops_employer.password'
my_configuration_sysops_employer.password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          37343065363965316362393936303137393863356330653065363731393133663261343061373639
          3631396164386466313630346530356630383336343063330a663666353564666438383536373433
          31373131633438653531366466323033356139343834326262353662323233356264636133396163
          6365386435313938310a663634363131313636353963333731343134386632316139333038613433
          3238
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
     - jtprog.my_configuration
```

## License

[WTFPL](LICENSE.md)
