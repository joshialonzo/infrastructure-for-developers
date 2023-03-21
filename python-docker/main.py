import docker


client = docker.from_env()

containers_list = client.containers.list(all=True)

images_list = client.images.list()

print("Showing all containers...")
for container in containers_list:
    print(container.name)
