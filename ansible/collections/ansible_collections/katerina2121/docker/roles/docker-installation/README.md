# katerina2121.docker docker-installation Role

Installs Docker on Ubuntu. Configures Docker repository, installs required dependencies, and optionally adds users to the docker group for non-root access.

## Requirements

- Ansible 2.14+
- Supported OS: Ubuntu

## Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `docker_installation_users` | List of system users to be added to the `docker` group for non-root access to Docker daemon | `["{{ ansible_user }}"]` |

## Dependencies

No

## Example Playbook

```yaml
- name: Execute tasks on servers
  hosts: servers
  roles:
    - role: katerina2121.docker.docker-installation
      docker_installation_users:
        - "{{ ansible_user }}"
        - admin
```

Another way to consume this role would be:

```yaml
- name: Initialize the docker-installation role from katerina2121.docker
  hosts: servers
  gather_facts: false
  tasks:
    - name: Trigger invocation of docker-installation role
      ansible.builtin.include_role:
        name: katerina2121.docker.docker-installation
      vars:
        docker_installation_users:
          - "{{ ansible_user }}"
          - admin
```

## Role Idempotency

True

## Role Atomicity

True

## Roll-back capabilities

No built-in rollback.

## Author Information

Ekaterina Lobova katya.lobova2005@gmail.com
