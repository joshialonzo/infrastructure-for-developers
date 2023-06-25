docker build --file server.Dockerfile --tag our-first-server .
docker run our-first-server
# dettach from the container
# docker run -d our-first-server