FROM ubuntu
LABEL maintainer="Josue Alonzo <joshi.alonzo@gmail.com>"

USER root
COPY ./web-server.bash /

RUN chmod 755 /web-server.bash
RUN apt -y update
RUN apt -y install bash netcat

USER nobody

ENTRYPOINT [ "/web-server.bash" ]
