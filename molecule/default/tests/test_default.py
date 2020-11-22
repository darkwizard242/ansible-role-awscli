import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/awscli'


def test_awscli_binary_exists(host):
    """
    Tests if awscli binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_awscli_binary_file(host):
    """
    Tests if awscli binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_awscli_binary_which(host):
    """
    Tests the output to confirm awscli's binary location.
    """
    assert host.check_output('which aws') == PACKAGE_BINARY
