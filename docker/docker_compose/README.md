# Docker Compose

Docker tutorials, including this one, typically walk through a simple example of starting one or two Docker containers. However, software systems out in the wild are rarely that simple. A mature software system will usually have at least a few Dockerized services, each with specific, individual configurations. There may be some shared third-party dependencies, or some services may depend on each other, which means that they need to be initialized in a specific order. In a microservice architecture, there may be hundreds of services to contend with. The simple steps to follow for starting one or two containers become extremely tedious or even impossible for starting hundreds of containers. That's where Docker Compose comes in.

## Configuration Management Tools: Procedural

* Series of ordered steps
* Based on assumptions about previous step
* Easy to introduce errors

## Configuration Management Tools: Declarative

* Specify end results
* Systems will determine which steps to execute
* Produces the same result each time

## Configuration as code

* Version control
* Self-documenting
* Easy management