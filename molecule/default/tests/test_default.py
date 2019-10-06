import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_awscli_package_installed(host):
    assert host.package("awscli").is_installed


def test_awscli_binary_exists(host):
    assert host.file('/usr/local/bin/aws').exists


def test_awscli_binary_file(host):
    assert host.file('/usr/local/bin/aws').is_file


def test_awscli_binary_which(host):
    assert host.check_output('which aws') == '/usr/local/bin/aws'
