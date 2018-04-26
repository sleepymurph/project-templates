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

I also have an extensive LaTeX article template, available at:
<https://github.com/sleepymurph/template_latex_article>
