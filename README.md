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


Other project templates
==================================================

- Markdown for printing: <https://github.com/sleepymurph/template_markdown_for_printing>
- LaTeX article: <https://github.com/sleepymurph/template_latex_article>
