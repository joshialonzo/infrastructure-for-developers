# Docker

Docker containers are composed of namespaces and control groups.

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

* Definition: What processes can see on a system

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

* Definition: Limit resources that containers can use, like memory and processor time.

* Monitor and restrict CPU usage
* Monitor and restrict network and disk bandwidth
* Monitor and restrict memory consumption
* Assign disk quotas (Not supported by Docker)

## Docker limitations

* Natively only runs on Linux
* Container images are bound to their parent operating systems

## Docker advantages

* Dockerfiles make configuring and packaging apps and their environments really easy
* The Docker Hub makes sharing images with anyone in the world easy
* The Docker CLI makes it really easy to start your apps in containers

## Test Docker is working properly

```bash
docker run --rm hello-world
```

## Install Docker on Linux Ubuntu

```bash
# install curl
sudo apt install curl
# download docker to the tmp folder
curl -o /tmp/get-docker.sh https://get.docker.com
# install docker
sh /tmp/get-docker.sh
# avoid to write sudo before the docker command
sudo usermod -aG docker $USER
```

## Best practices

* Use verified images
* Scan images
    1. Clair
    2. Trivy
    3. Dagda
* Avoid latest
    * You don't know the version you are downloading
    * The app's version can change when you pull later
    * latest can be overriden, making rollback difficult
* Use non-root users
    * It makes your containers more secure
