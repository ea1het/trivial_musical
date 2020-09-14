#
# How-To build this container image
#
#
#
# GitHub Container Repo usage
# ---------------------------
# Step 1: Authenticate
#    $ cat ~/GH_TOKEN.txt | docker login docker.pkg.github.com -u your_username --password-stdin
#
# Step 2: Tag
#    $ docker tag IMAGE_ID docker.pkg.github.com/your_username/repository-name/IMAGE_NAME:VERSION
#
# Step 3: Publish
#    $ docker push docker.pkg.github.com/your_username/repository-name/IMAGE_NAME:VERSION
#
#
#
#
# Platform specific images (when you build for your own platform)
# ---------------------------------------------------------------
# docker build \
#       --build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
#       --build-arg VCS_REF=`git rev-parse --short HEAD` \
#       --build-arg VERSION=v1.0 \
#    -t ea1het/trivial_musical:v1.0 .
#
#
#
# Cross-compile platform independent images (when you use a build facility
# in your platform to cross-compile for another platform)
# ------------------------------------------------------------------------
# docker buildx ls
# docker buildx create --name testbuilder
# docker buildx use testbuilder
# docker buildx inspect --bootstrap
# docker buildx build \
#       --platform linux/arm/v6 \
#       --build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
#       --build-arg VCS_REF=`git rev-parse --short HEAD` \
#       --build-arg VERSION=v1.0 \
#   -t ea1het/trivial_musical:1.0 --push .
#
#


FROM python:3.8-alpine3.10

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL maintainer="Jonathan Gonzalez <j@0x30.io>"\
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Trivial Musical" \
      org.label-schema.description="This project builds a trivial game about music and musicians." \
      org.label-schema.url="docker.pkg.github.com/ea1het/trivial_musical" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="docker.pkg.github.com/ea1het/trivial_musical/trivial_musical:$VERSION" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install --no-cache-dir uvicorn gunicorn \
    && apk del .build-deps gcc libc-dev make \
    && rm -rf /root/.cache \
    && rm -rf /var/cache/apk/* \
    && find / \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && mkdir /app

EXPOSE 5000

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT /app/start.sh

