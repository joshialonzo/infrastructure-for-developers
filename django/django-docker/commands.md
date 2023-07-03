# build the docker image
`docker build --tag python-django .`

# create the container
`docker run -d --publish 8000:8000 --name python_django_app python-django`

# get into the container
`docker exec -it python_django_app bash`

# delete the container
`docker rm -f python_django_app`