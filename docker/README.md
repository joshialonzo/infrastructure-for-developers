# Docker

## Virtual Machines

* Use the hypervisor to emulate real hardware
* Can take up a lot of space
* Require you to install/configure operating system
* Can run multiple apps at the same time
* Cannot interact with their hosts

### Architecture

App A, App B, ...
OS 1, OS 3, ...
VM 1, VM 2, ...
Hypervisor
Infrastructure

## Containers

* Do not emulate any hardware and do not need to "boot up"
* Do not require operating system installation
* Take up much less space
* Can run only one app at a time (by design)
* Can interact with their hosts

### Architecture

App A, App B, ...
Docker
Host Operating System
Infrastructure

## Docker Anatomy

* A container is composed of:
    * container namespace
    * container controller

## Namespaces

* Name | Description
* USERNS | User lists
* MOUNT | Access to file systems
* NET | Network communication
* IPC | Interprocess communication
* TIME | Ability to change time (Not supported by Docker)
* PID | Process ID Management
* CGROUP | Create control groups
* UTC | Create host/domain names

## Control group uses

* Monitor and restrict CPU usage
* Monitor and restrict network and disk bandwidth
* Monitor and restrict memory consumption
* Assign disk quotas (Not supported by Docker)

## Docker limitations

* Natively only runs on Linux
* Container images are bound to their parent operating systems