#!/usr/bin/env bash

container_name="public_service"
container_port=7777

## build images
docker build -t "$container_name" .

# remove container
docker rm --force "$container_name"

## start container
docker run -itd --name="$container_name" --env FLASK_ENV="production" -p "${container_port}":5000 --restart=always "$container_name"
