Welcome to Acrylamid
====================

Acrylamid is yet another static blog compiler written in python that aims to
be lightweight, fast and producing high quality output. It is licensed under
BSD Style, 2 clauses.

.. toctree::
   :maxdepth: 1

   installation
   tutorial
   conf.py
   commands
   filters
   views
   templating
   extending
   howtos
   internals
   about

Why?
----

Why another static blog compiler, that's a valid question. So, why would you
use Acrylamid: It's fast when you start blogging and it stays fast when you
have hundreds of articles due incremental compilation. It ships with all
builtin Markdown extensions, custom ones and additional reStructuredText
directives to embed YouTube or Code. With all complexity of Acrylamid itself,
it is super easy to use.

Why not Acrylamid? It's not well tested by different people with different
requirements. It may has some serious issues I didn't noticed yet. It also
lacks some internal documentation. The default layout is indeed not the most
beautiful and Acrylamid has no asset handling yet.

Features
--------

Acrylamid is a mixture of `nanoc <http://nanoc.stoneship.org/>`_, `Pyblosxom
<http://pyblosxom.bluesock.org/>`_ and `Pelican <http://pelican.notmyidea.org/>`_. It
features mainly:

- blog articles, static pages, tags, RSS/Atom feeds and an article overview
- theming support (using jinja2_ or mako_) and support for jinja2 directly in postings
- Markdown_, reStructuredText_, textile_ and pandoc_
- Markdown extensions and custom reStructuredText directives
- MathML, modern web-typography and hyphenation using soft-hyphens
- RSS/Atom/WordPress import, deployment and a handy CLI
- it's very flexible/configurable and fast due *incremental rendering*

.. _jinja2: http://jinja.pocoo.org/
.. _mako: http://www.makotemplates.org/
.. _Markdown: http://daringfireball.net/projects/markdown/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _textile: https://en.wikipedia.org/wiki/Textile_%28markup_language%29
.. _pandoc: http://johnmacfarlane.net/pandoc/
.. _AsciiMathML: http://www1.chapman.edu/~jipsen/mathml/asciimath.html

Quickstart
----------

::

    easy_install -U acrylamid

It has actually only one dependency, ``jinja2`` but for convenience it also
installs ``markdown`` and ``translitcodec``. In addition it has support for
PyYAML, reStructuredText, syntax highlighting using pygments, asciimathml
to render MathML and finally smartypants for nicer typography.

::

    easy_install -U docutils pygments asciimathml smartypants

Get acrylamid, edit *conf.py* and *layouts/* and compile with:

.. raw:: html

    <pre>
    $ acrylamid init myblog
      <span style="font-weight: bold; color: #00aa00">   create</span>  tutorial/output/conf.py
        ...
    $ cd myblog/
    $ acrylamid compile && acrylamid view
       <span class="ansi1 ansi32">   create</span>  [0.06s] output/articles/index.html
       <span class="ansi1 ansi32">   create</span>  [0.44s] output/2012/die-verwandlung/index.html
       <span class="ansi1 ansi32">   create</span>  [0.00s] output/index.html
       <span class="ansi1 ansi32">   create</span>  [0.00s] output/tag/die-verwandlung/index.html
       <span class="ansi1 ansi32">   create</span>  [0.00s] output/tag/franz-kafka/index.html
       <span class="ansi1 ansi32">   create</span>  [0.03s] output/atom/index.html
       <span class="ansi1 ansi32">   create</span>  [0.03s] output/rss/index.html
       <span class="ansi1 ansi32">   create</span>  [0.00s] output/sitemap.xml
    Blog compiled in 0.61s
     * Running on http://127.0.0.1:8000/
    </pre>


Real World Examples?
********************

- sources from my `personal blog <http://blog.posativ.org/>`_:
  `/posativ/blog.posativ.org <https://github.com/posativ/blog.posativ.org/>`_.
- sebix' (contributer) `blog <http://sebix.github.com/>`_ sources:
  `/sebix/sebix.github.com-sources <https://github.com/sebix/sebix.github.com-sources>`_.


Filters
-------

You can apply various filter to a single entry, to a specific view or globally
and Acrylamid resolves it automatically (some filters conflict with others so
you can for example apply *Markdown* as global filter but render some entries
with reStructuredText). Currently supported by acrylamid, see :doc:`filters`
for detailed information:

- **Markdown**: rendering Markdown (+asciimathml, pygments, built-in extensions)
- **reST**: reStructuredText (+pygments)
- **pandoc**: Pandoc (+Markdown, textitle, rst, ...)
- **textile**: using Textile as markup language
- **HTML**: don't render with filters mentioned above (it's a conflicting filter)

- **typography**: https://code.google.com/p/typogrify/ (and custom modifications)
- **hyphenation**: hyphenate words (len > 10) based on language
- **summarize**: summarizes posts to 200 words

- **head_offset**: decrease headings by offset
- **jinja2**: write jinja2 in your entries (you can also execute system calls therewith)
- **acronyms**: automatically replace acronyms and abbreviations to help unexperienced users


Commands
--------

See :doc:`commands` for a detailed overview.

::

    $ acrylamid --help
    usage: acrylamid [-h] [-v] [-q] [-C] [--version]  ...

    positional arguments:

        init          initializes base structure in DIR
        compile       compile blog
        view          fire up built-in webserver
        autocompile   automatic compilation and serving
        import        import content from URL or FILE
        new           create a new entry
        check         run W3C or validate links
        clean         remove abandoned files
        deploy        run task
        info          short summary
        ping          notify ressources

    optional arguments:
      -h, --help      show this help message and exit
      -v, --verbose   more verbose
      -q, --quiet     less verbose
      -C, --no-color  disable color
      --version       show program's version number and exit

    All subcommands except `init` require a conf.py file.

Need Help?
----------

Join ``#acrylamid`` on Freenode_!

.. _Freenode: http://freenode.net/

API Reference
-------------

.. toctree::
   :maxdepth: 2

   api/core
   api/readers
   api/helpers
   api/lib
