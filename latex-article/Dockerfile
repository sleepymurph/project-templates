FROM ubuntu:xenial

# Start with base texlive install as one layer, because it's huge
RUN apt-get update \
    && apt-get install -y \
            texlive \
    && rm -r /var/lib/apt/lists/* /var/cache/apt/*

# Install extra texlive packages for this document
RUN apt-get update \
    && apt-get install -y \
            texlive-bibtex-extra \
            texlive-fonts-extra \
            texlive-generic-extra \
            texlive-science \
    && rm -r /var/lib/apt/lists/* /var/cache/apt/*

# Install additional packages for this document
RUN apt-get update \
    && apt-get install -y \
            build-essential \
            graphviz \
            m4 \
            git \
    && rm -r /var/lib/apt/lists/* /var/cache/apt/*

# Create a user
ENV UID 1000
RUN useradd --uid $UID --create-home --shell /bin/bash compile
USER compile

WORKDIR /home/compile/repo
