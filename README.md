To PDF: A Plugin for Pelican
====================================================

[![Build Status](https://img.shields.io/github/actions/workflow/status/MattMarcha/pelican-to-pdf/main.yml?branch=main)](https://github.com/MattMarcha/pelican-to-pdf/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-to-pdf)](https://pypi.org/project/pelican-to-pdf/)
[![Downloads](https://img.shields.io/pypi/dm/pelican-to-pdf)](https://pypi.org/project/pelican-to-pdf/)
![License](https://img.shields.io/pypi/l/pelican-to-pdf?color=blue)

To PDF is a Pelican plugin for generating custom PDFs from articles and pages.
Works on top of `wkhtmltopdf` and `pdfkit`.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-to-pdf

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `to_pdf` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

### Prerequises

- wkhtmltopdf (system)
- pdfkit (Python)


Usage
-----

Simply add the metadata `To_pdf` to your page to trigger a PDF generation for the page/article.
The value can be empty, or a python dictionnary to set the file name and/or add a stylesheet :

```markdown
To_pdf: {'name': 'mysuperfile', 'css': 'content/static/print.css'}
```

> Note :
> - PDF files will be generated at the same path as the HTML file.
> - Identical names at same path will result in overwriting.

#### Emojis

For emojis support in wkhtmltopdf, the font has to be set to one with emoji support which will depend of the system or has to be fetched online (ex: `Noto Color Emoji` on my system).
For emojis added through css `content`, use the unicode.

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/MattMarcha/pelican-to-pdf/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the AGPL-3.0 license.
