import docker


client = docker.from_env()

containers_list = client.containers.list(all=True)

images_list = client.images.list()

print("Showing all containers...")
for container in containers_list:
    print(container.name)

print()

print("Showing all images...")
for image in images_list:
    tags = image.tags
    first_tag = tags[0] if tags else "no-tag"
    print(first_tag)
