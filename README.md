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



LaTeX Report Template
==================================================

Subdirectory: `latex_report`

This is a starter LaTeX report with a ton of customizations that I use
consistently.

This is for more serious documents where Markdown+Pandoc won't cut it.

## Basic Usage

The build process is controlled by `make`. To build:

1. `cd` into subdirectory
2. run `make`

This will create a `report_latex.pdf` document in the parent directory
(root of the repository).

To base a new document off of this skeleton:

1. Copy the `report_latex` directory into your project and rename it
2. Don't forget the hidden `.gitignore` file
3. Edit the Makefile to change the name of the final document
4. Change the title, author, and git URL in `doc.tex`
5. Write the document contents in `doc-content.tex`
6. Edit any other files as needed


## Files

```
Document skeleton:

    doc.tex             Main document skeleton
    packages.tex        LaTeX Package includes
    macros-general.tex  Macros that are part of this template

Document content:

    doc-content.tex     Place for document contents
    macros-doc.tex      Place for document-specific macros
    glossary.tex        Place for glossary entries
    sources.bib         Bibliography database
    scratchpad.tex      Place for scratch text that might get reused

Build process and helpers:

    Makefile            Build process
    gen_meta_tex.sh     Script that extracts Git information
    .gitignore          Generated files for Git to ignore (TeX generates a lot of them)
```


## Important Notes

### Structure: sources in subdirectory, rendered PDF committed in top level of repository

I keep my LaTeX sources in Git, naturally.
I keep the document source in a subdirectory of the repository,
and then I commit a rendered copy of the PDF in the top level of the repository.

This comes from collaboration.
I want my collaborators to be able to look at the latest version of the
document directly from the repository without having to set up the LaTeX build
environment.

### The "final" option

This template is set up to obey the `final` option in the `\documentclass`.
There are many draft-only notes, annotations, and even sections that will
disappear when `final` is added.

I even define a few custom macros for draft-only (non-`final`) content:

- `\draftonlysection`: a whole section that will only appear in non-final mode.
    Examples are the Git version information and the scratchpad.

- `\draftonlynote`: a snippet of text that will only appear in non-final mode.

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
