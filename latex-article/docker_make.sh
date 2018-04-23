#!/bin/bash

# Helper script to compile the document in a Docker container

set -x

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}" | xargs readlink -f)"
SCRIPT_DIR_NAME="$(basename "$SCRIPT_DIR")"
PARENT_DIR="$(echo "$SCRIPT_DIR/.." | xargs readlink -f)"

IMAGE_NAME="$SCRIPT_DIR_NAME"

docker build --tag "$IMAGE_NAME" "$SCRIPT_DIR"

docker run \
    --rm \
    --volume "$PARENT_DIR":/home/compile/repo \
    --workdir "/home/compile/repo/$SCRIPT_DIR_NAME" \
    --env UID=$(id -u) \
    "$IMAGE_NAME" \
    make $*
