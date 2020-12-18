# jtprog.my_configuration

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprog/ansible-role-my-configuration/CI?label=CI) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jtprog/ansible-role-my-configuration/Release?label=Release) ![GitHub](https://img.shields.io/github/license/jtprog/ansible-role-my-configuration)

This is my personal role for configure my account on remote servers


## Role Variables

See `defaults/main.yml`:
```yaml
my_configuration_sysops_employer:
  name: "savin"
  password: "!vault |
    $ANSIBLE_VAULT;1.1;AES256
    34633830663234313535353864316632363133383038626132336630303735376231363138313766
    3039376133396562383865666462346433326335306463620a653639643432623237633962663634
    37366164643865306461386435306466313733656666303532323361376533616237663834303764
    3436376337353633310a373062636134306133333263363135653236376163643330643736623735
    3566"

  key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDSu21GQc321540NSlt9vM7y8HfFj4xrmCLOaQgOphzekO3D49l7IZ1fOl6B7sAFozHiPlrwr+2/2LiaQqMPFH3WuQjiHtSdI2kk5lvCJJt0EE/AeEQF08OpQI9/HcHALPasdoiNFDBPPVl5oIVdCJQvLUVEx1n5mVC9yXVZNCAIu8nwizqUC+/mZAVrxOyC/QuLi99IZJnbFwlbfOB2JS8iRICUCwYumVEC4JNyZxyksRDHPXsvvUHF+y0+CN5+3FajNjWxRmPeBBY6Rnb8ONdJq/mIgIJ3QoVsrGWl1yuKR9rQx/x53QuPX6ayTT1FP3mDcbeGfwtD/aYqvS1hxVKpMaahzuHoq+qsYc73l3Y5JL7e8QWwGFgMXxgyt9Luy82yN1JdTMjoGYdXQmgwK8YajEOBH55L45K+AyHOEHdY7f+Nc5tTGW9vsZ5cBI22NLv04RohubqldM94C/Nfta7MShKwo19ZLGwuy+PCd6KSMPfwqsZ7/VHbdIGRRXhwPFwy/ANxDJQuUJwOWhiwDQIv92HMrOkwc+gq7ZXrF3wNLrLiLW5rb7Qlu8joNx1Vyz4GSaHdogR60/N/5E3YJgX924vKlPlozJb/tVrwwBWzC+6/IlaifjA0+iwfdHzJqREJoCZpvSXGctz1Yo6iYmL2dmvXuZxh+r47eLQoVWzLw== savin@jtprog.ru"
  group: "admins"

my_configuration_bash_history_time_format: "%d/%m/%y %T "

my_configuration_vimrc_colorscheme: "industry"
```

Before running playbook you need to change password with this command:
```bash
ansible-vault encrypt_string 'P@s$W0Rd' --name 'sysops_employer.password'
sysops_employer.password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          34633830663234313535353864316632363133383038626132336630303735376231363138313766
          3039376133396562383865666462346433326335306463620a653639643432623237633962663634
          37366164643865306461386435306466313733656666303532323361376533616237663834303764
          3436376337353633310a373062636134306133333263363135653236376163643330643736623735
          3566
```

## Example Playbook

```yaml
- hosts: all
  roles:
     - jtprog.my_configuration
```

## License

[WTFPL](LICENSE.md)
