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