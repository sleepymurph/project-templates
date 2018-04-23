#!/bin/bash

# Helper script to compile the document in a Docker container

set -x

SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}" | xargs readlink -f)"
GIT_ROOT_DIR="$(cd $SCRIPT_DIR && git rev-parse --show-toplevel)"

SCRIPT_PATH_FROM_GIT_ROOT="${SCRIPT_DIR##$GIT_ROOT_DIR}"
IMAGE_NAME="$(basename "$SCRIPT_DIR")"

docker build --tag "$IMAGE_NAME" "$SCRIPT_DIR"

docker run \
    --rm \
    --volume "$GIT_ROOT_DIR":/home/compile/repo \
    --workdir "/home/compile/repo/$SCRIPT_PATH_FROM_GIT_ROOT" \
    --env UID=$(id -u) \
    "$IMAGE_NAME" \
    make $*
