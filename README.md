Project Templates/Skeletons
==================================================

This is a collection of skeletons for various projects that I seem to keep
recreating over and over again.


Multithreaded Python HTTP Server
==================================================

Subdirectory: `python_http_server/`

I am a teacher's assistant in a distributed-systems class.
I often want to give my students example code with a simple HTTP server that:

- is multithreaded
- responds nicely to term signals
- does not depend on any non-standard libraries
- dies after a given amount of time (in case they're using a shared computer and forget to shut down their homework)

It took me a long time to put all of that together.
So I wanted to save it somewhere where I could find it and reuse it when needed.


Why Not a Module?
--------------------------------------------------

Confession: I haven't bothered to learn about Python's packaging tools or ecosystem.
Python's "batteries-included" standard library usually gets me where I need to go.

I could probably package this up into a little microframework,
or better yet just use an existing REST framework like Bottle or Flask.
But since I often adapt this code into something to hand out to students,
I would rather be able to hand out one file that just runs.


Markdown Document For Printing
==================================================

Subdirectory: `markdown_doc_for_printing/`

For quick printed documents like letters, I like to write in Markdown
and convert to PDF with [Pandoc](https://pandoc.org/).

Pandoc lets you put a YAML block at the beginning of the document with
variables that affect the paper size, margins, PDF metadata, etc.
I always forget what those options are, so I wanted to have a starter document
that I could copy and edit at will.

To use:

1. Copy the document `doc.markdown`
2. Edit it
3. Convert to PDF with Pandoc: `pandoc doc.markdown -o doc.pdf`

Give yourself a Vim macro:

    :nmap <Buffer> <Leader>p :w \| :!pandoc -o %.pdf %<CR>


Notes
--------------------------------------------------

### A4 paper

Note that this template insists on A4 paper because I live in Europe.
This is set by the `papersize: a4` in the YAML header.
Delete or change that as needed.

If you do change it, note that the Pandoc LaTeX template concatenates `paper` to the `papersize` setting.
So `papersize: a4` becomes `\documentclass[a4paper]{article}` in the LaTeX.
So whatever paper size you use, you need to leave the `paper` part off of the
`papersize` option.

Remembering exactly how to set this is probably the biggest reason I
need this template.

### Dependency: Open Sans

[Open Sans](https://fonts.google.com/specimen/Open+Sans)
is the official font at the university where I work.
Therefore it is the default font for my templates.

This means that this template requires the
[`opensans` package for LaTeX](https://ctan.org/pkg/opensans).
On Ubuntu this package is part of the
[`texlive-fonts-extra` package](https://packages.ubuntu.com/xenial/texlive-fonts-extra).

    apt install texlive-fonts-extra

Or you can use a different font by editing the file.
Edit or remove the `fontfamily` and `fontfamilyoptions`
values in the YAML block.

#### Trade-off: Open Sans vs full UTF-8 support

This method of switching to Open Sans only works with the default `pdflatex` engine.
And the `pdflatex` engine has impartial UTF-8 support.
The Pandoc LaTeX template (and my LaTeX template) use the `inputenc` package for partial support.
This works for most of my purposes, but it can still give errors like the following:

```
! Package inputenc Error: Unicode char А (U+410)
(inputenc)                not set up for use with LaTeX.

See the inputenc package documentation for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.66 ...YZŽabcčćdđefghijklmnopqrsštuvwxyzžА

Try running pandoc with --latex-engine=xelatex.
pandoc: Error producing PDF

shell returned 43
```

If you switch to `xelatex` for better UTF-8 support,
the document will no longer be in Open Sans:

    pandoc doc.markdown -o doc.markdown.pdf --latex-engine=xelatex

Apparently fonts work completely differently in XeLaTeX,
and I have not had a chance to figure that out.

TODO: Figure out how to get Open Sans with `xelatex` too.


LaTeX Article Template
==================================================

Subdirectory: `latex-article`

This is a starter LaTeX article with a ton of customizations that I use
consistently.

This is for more serious documents where Markdown+Pandoc won't cut it.

Basic Usage
--------------------------------------------------

The build process is controlled by `make`. To build:

1. `cd` into subdirectory.
2. Run `make` to compile `doc.pdf` in LaTeX's `draft` mode
3. Run `make final` to compile `doc-final.pdf` in LaTeX's `final` mode
4. Run `make render` to compile both draft and final versions, then copy them to the parent directory as `latex-article-draft.pdf` and `latex-article-final.pdf`, respectively.

The idea here is to be able
to rapidly generate and view the document as you work on it
(`latex-article/doc.pdf` and `latex-article/doc-final.pdf`),
then at stopping points,
to commit rendered versions of the document for easier sharing with collaborators
(`latex-article-draft.pdf` and `latex-article-final.pdf`).

See the [README file in the subdirectory](latex-article/) for details.

To base a new document off of this skeleton:

1. Copy the `latex-article` directory into your project and rename it.
    The rendered PDF names `latex-article-draft.pdf` and `latex-article-final.pdf` are taken from the subdirectory name, so they will change when you rename the subdirectory.
2. Don't forget to copy the hidden `.gitignore` file.
3. Change the title, author, and git URL in `doc.tex`
4. Write the document contents in `doc-content.tex`
5. Edit any other files as needed



Running in a Docker container
--------------------------------------------------

This directory also includes a Dockerfile to set up a build environment.
To build the document inside a Docker container, run

    ./docker_make.sh [MAKE TARGETS]

See `Dockerfile` for dependencies and `docker_make` for Docker invocations.

This will create a docker image named after the document subdirectory,
in this case `latex-article`.

To remove the image (change the name to match the subdirectory name):

    docker rmi latex-article

Then you can remove dangling resources with a command like `docker system prune`.
See the [How to Remove Docker Images, Containers, and Volumes](https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes) tutorial from Digital Ocean for more cleanup commands.

See the [README file in the subdirectory](latex-article/) for details about the build process.


Why Not a Package?
--------------------------------------------------

Because I have barely scratched the surface of TeX/LaTeX and I definitely
don't know enough about how packaging works.

I've also had experience with a custom LaTeX document class that did too much.
It brought in so many packages that it clashed with many of the packages I tried to use,
which added another layer of difficulty to working with the document.

This is the nice and lazy way for now:
copy my usual customizations,
but then tweak them as needed for each individual document.


Files
--------------------------------------------------

```
Document skeleton:

    doc.tex             Main document skeleton
    packages.tex        LaTeX Package includes
    macros-general.tex  Macros that are part of this template

Document content:

    doc-content.tex     Place for document contents
    abstract.txt        Abstract (plain text)
    macros-doc.tex      Place for document-specific macros
    sources.bib         Bibliography database
    glossary.tex        Place for glossary entries

Build process and helpers:

    Makefile            Build process
    gen_meta_tex.sh     Script that extracts Git information
    .gitignore          Generated files for Git to ignore (TeX generates a lot of them)
    tmux-session-doc.sh Script to launch a tmux session for this document
```


Notes
--------------------------------------------------

### Structure: sources in subdirectory, rendered PDF committed in top level of repository

I keep my LaTeX sources in Git, naturally.
I keep the document source in a subdirectory of the repository,
and then I commit a rendered copy of the PDF in the top level of the repository
(see
[`latex-article-draft.pdf`](latex-article-draft.pdf) and
[`latex-article-final.pdf`](latex-article-final.pdf)
in this repo).

This comes from collaboration.
I want my collaborators to be able to look at the latest version of the
document directly from the repository without having to set up the LaTeX build
environment.


### Abstract in plain text

The abstract for the document comes from `abstract.txt`.
This file is deliberately in plain text so that it will be easier to copy-and-paste the abstract text elsewhere, without having to worry about TeX escapes for common characters like `%` and `&`.
If you do not need an abstract at all, simply delete the file, and the template will skip the abstract section entirely.


### Dependency: Open Sans

[Open Sans](https://fonts.google.com/specimen/Open+Sans)
is the official font at the university where I work.
Therefore it is the default font for my templates.

This means that this template requires the
[`opensans` package for LaTeX](https://ctan.org/pkg/opensans).
On Ubuntu this package is part of the
[`texlive-fonts-extra` package](https://packages.ubuntu.com/xenial/texlive-fonts-extra).

    apt install texlive-fonts-extra

Or you can use a different font by editing the `packages.tex` file.
The font packages are near the top.


### The "final" option

This template is set up to obey the `final` option in the `\documentclass`.
There are many draft-only notes, annotations, and even sections that will
disappear when `final` is added.

I even define a several custom macros for draft-only (non-`final`) content.
See `macros-general.tex` for their definitions and `doc-content-example.tex` for examples of their use.


### US English, A4 paper

I am an American living in Norway.
I write in US English, but I want the European paper size.
In theory I should be able to set up my locales for all of that to happen
automatically, but I haven't managed to figure it out yet.
For now, I just use the `a4paper` option in the main `\documentclass` macro.
If you need to change that, find it at the top of `doc.tex`.

There may be a few more Europe-friendly tweaks to my styles.
For example, I set the `biblatex` package to print dates like "Apr. 7, 2017"
instead of the "04/07/2017" to avoid any possible confusion over MDY vs DMY.


### Graphviz Diagrams

I love Graphviz.
I use it for all kinds of diagrams and visualizations.
So I have it built into the document build process here.

To use Graphviz:

1. Add dot files in this directory

2. Add the dot file name to the `DOT_DIAGRAMS` variable in the Makefile,
    with a PDF extension

        # To include a diagram generated from diagram_example.dot
        DOT_DIAGRAMS=diagram_example.pdf

3. Create a figure in the document


### M4 preprocessing for Graphviz diagrams

The build process runs the diagrams through the `m4` preprocessor first,
then through `dot`.
This lets you use macros in your Graphviz files to define common styles
and other shortcuts.

For example, this macro defines `TENTATIVE` as a shortcut for `style="dashed'`
to create a reusable link style:


    define(TENTATIVE, `style="dashed"')

    digraph{
        hello -> world [TENTATIVE]
        world -> "!" [TENTATIVE]
    }

This layer of indirection can make debugging tricky.
So the intermediate build step is explicit.
The result of M4 expansion will be written to a file with a
`.preprocessed.dot` extension.
This file can be checked for syntax errors and unexpected macro trouble.


### Git Info

I give draft after draft to collaborators for feedback.
To make it easier to keep track of revisions, I have macros that include Git
information directly into the document.

There are a few important things to note about this Git information:

- It only lists changes inside the document source subdirectory.
    This is another advantage of keeping document source in subdirectories.
    More subdirectories can be included by editing the `DOC_SOURCE_DIRS` variable in the Makefile.

- The repository URL can be changed by editing the `\GitUrl` macro in `doc.tex`.
    Or just delete it if you don't have a repository URL.

- The history will not be included when the document is marked `final`.

To get a clean history in the document: commit the source directory, run `make`
again, and then commit the rendered PDF in the parent directory.

How it works is a little tricky:

1. The make process runs a script called `gen_meta_tex.sh` which extracts Git
   information and writes out a TeX file full of macros.

2. The document includes the generated TeX file and uses the macros.

3. The make process also generates the Git log as a plain text (`.txt`) file,
   and the document includes that as well. The history is a separate file
   because the `verbatim` package is tricky.
