[![build-test](https://github.com/darkwizard242/ansible-role-awscli/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-awscli/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-awscli/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-awscli/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/d/darkwizard242/awscli) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awscli&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-awscli) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awscli&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-awscli) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awscli&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-awscli) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-awscli?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-awscli?color=orange&style=flat-square)

# Ansible Role: awscli

Role to install [awscli](https://github.com/aws/aws-cli) pip package on **Debian/Ubuntu** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
awscli_debian_pre_reqs:
  - python3
  - python3-pip
awscli_debian_pre_reqs_desired_state: present
pip_executable: pip3
awscli_app_debian_package: awscli
awscli_desired_state: present
```

### Variables table:

Variable                             | Description
------------------------------------ | ---------------------------------------------------------------------------------------------------------------
awscli_debian_pre_reqs               | Packages required to install AWS CLI on Debian based systems. Using python3 as python2.x is EOL by end of 2020.
awscli_debian_pre_reqs_desired_state | Desired state for AWS CLI pre-requisite apps on Debian systems.
pip_executable                       | The executable to utilize for installing **pip** package of `awscli`.
awscli_app_debian_package            | Name of awscli application package require to be installed i.e. `awscli` on Debian based systems.
awscli_desired_state                 | Desired state for AWS CLI.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **awscli** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awscli
```

For customizing behavior of role (i.e. installation of latest **awscli** package instead of ensure it is installed ) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awscli
  vars:
    awscli_desired_state: latest
```

For customizing behavior of role (i.e. removal of **awscli** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awscli
  vars:
    awscli_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-awscli/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://alimuhammad.dev/), a DevOps/CloudOps Engineer who loves to learn and contribute to Open Source community.
