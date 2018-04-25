LaTeX source code for article
==================================================

## Building the article PDFs

This build process is controlled by Make,
and there is a Docker file to create a container with all needed dependencies.

To render the draft and final PDFs in this directory via Docker:

    ./docker_make.sh render

This will build a Docker container, run the Make process, and copy both the draft and final PDFs out to the parent directory.

Be warned: A LaTeX installation (TeX Live) makes for a very large container (~3 GB).
We have tried to separate container layers so that the container with just the base OS and TeX Live can be reused, but it is still going to take up a decent amount of space on your `/var/` partition.


### To actively work on the document

First, check the Docker file for dependencies to install on your machine, then use any of the following make targets:

- `make` (default):
    Builds `doc.tex` in this subdirectory, in draft mode

- `make final`:
    Builds `doc-final.tex` in this subdirectory, in final mode

- `make clean`:
    Remove temporary files

- `make render`:
    Build both draft and final documents and copy them out into the parent directory

You can run any of these targets in a Docker container by giving it as an argument to the `docker_make.sh` script:

    ./docker_make.sh TARGET

If committing the rendered PDFs to version control it is recommended to commit source changes first, then `make render` and then commit the new PDFs in a separate commit.
This will make it easier to merge, cherry-pick, and rearrange commits if needed without hitting conflicts from the changing binary PDF files that Git does not know how to merge.
