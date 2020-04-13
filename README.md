Section Handouts (Code in Place 2020)
=====================================

[Code in Place](compedu.stanford.edu/codeinplace/v1/#/) is community-service coding education in the time of Covid-19.

Looking for Section Handouts?
-----------------------------

Click on any of the following links to go directly to the handout for your section.

*ENGLISH*

- Section 1: United Nations Karel

*ESPAÑOL*

- Section 1: United Nations Karel

*FRANÇAIS*

- Section 1: United Nations Karel

*DEUTSCHE*

- Section 1: United Nations Karel

Want to help with translations?
-------------------------------
Code in Place is fortunate to have students from several countries who speak several languages.

If you have the time, energy, and capacity, we would appreciate additional translations. To add a translation, modify a `.po` file in the `locale/` directory. Ideally, use a po-editor to help with formatting. Please be careful not to break reST notation.

Eventually, if desired, we'll move the open-source translation to Transifex [3], which is a friendlier interface for crowd-sourced translations.

**If you're a Code in Place student, you can stop reading now.**

What's up with Sphinx?
----------------------
Sphinx [1] is "a tool that makes it easy to create intelligent and beautiful
documentation" commonly used for writing about and documenting Python code.
It also has nice support for internationalization [2].

Preparing Documentation for Another Language
--------------------------------------------

First, hop into your virtual environment and install `sphinx` and `sphinx-intl`:

```
(venv) $ python3 -m pip install sphinx sphinx-intl
```

Make translation files for your target languages:

```bash
$ make gettext  # Extract translatable messages into pot files.
$ sphinx-intl update -p _build/gettext -l es -l de -l fr  # Generate `po` files from those `pot` files.
```

Then, somehow, the `.po` files need to be translated.

Once the `.po` files contain translations, we'll build the documentation in your desired language. For example, to build HTML documentation in Spanish, use:

```bash
$ make -e SPHINXOPTS="-D language='es'" html
```

To build PDF handouts, use:

```bash
$ make -e SPHINXOPTS="-D language='es'" latexpdf
```

That's pretty tough to remember, and each new language overwrites the old build output, so instead, use `makedoc.sh`.

```
$ ./makedoc.sh
```

It builds all of the documentation in HTML and PDF format and brings the build output to `handouts-html` and `handouts-pdf`.

Remember, whenever you add a new handout or change the existing documents, you need to update the PO files with the new content:

```bash
$ sphinx-intl update -p _build/gettext
```

[1]: https://www.sphinx-doc.org/
[2]: http://www.sphinx-doc.org/en/master/usage/advanced/intl.html
[3]: http://www.sphinx-doc.org/en/master/usage/advanced/intl.html#using-transifex-service-for-team-translation