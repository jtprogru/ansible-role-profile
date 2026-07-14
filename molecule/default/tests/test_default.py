"""Testinfra checks for the jtprogru.profile role.

Values here mirror the role defaults and the test vars in converge.yml.
"""

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

PROFILE_NAME = "jtprogru"
PROFILE_GROUP = "admins"
PROFILE_SHELL = "/bin/bash"
SUDOERS_FILE = "/etc/sudoers.d/10-admins.conf"
# The static test key configured in converge.yml.
TEST_KEY_MARKER = "moleculeTestKey"


def test_group_exists(host):
    assert host.group(PROFILE_GROUP).exists


def test_user_exists(host):
    user = host.user(PROFILE_NAME)
    assert user.exists
    assert user.shell == PROFILE_SHELL
    assert PROFILE_GROUP in host.check_output("id -nG %s", PROFILE_NAME).split()


def test_sudoers_dropin(host):
    f = host.file(SUDOERS_FILE)
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o440
    assert "%%%s ALL=(ALL) NOPASSWD: ALL" % PROFILE_GROUP in f.content_string


def test_sudoers_is_valid(host):
    # visudo -c validates the whole /etc/sudoers tree, including drop-ins.
    assert host.run("visudo -c").rc == 0


def test_authorized_key(host):
    authorized_keys = host.file(
        "/home/%s/.ssh/authorized_keys" % PROFILE_NAME
    )
    assert authorized_keys.exists
    assert TEST_KEY_MARKER in authorized_keys.content_string


def test_vim_installed(host):
    # Assert the binary rather than a package name: on RHEL family the rpm is
    # vim-enhanced, on Debian/Ubuntu it is vim.
    assert host.exists("vim")
