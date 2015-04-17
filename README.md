# Contextualize
A small [web.py](http://webpy.org) webapp to
generate [ConTeXt](http://wiki.contextgarden.net) documents

## Introduction

ConTeXt is a document typesetting system and markup language, sort of in the
same vein as LaTeX but rather more pleasant to use, especially if you are
familiar with markup languages like HTML.

Contextualize is a simple web interface for generating ConTeXt documents.  You
type in your ConTeXt source, hit the button, and (if you haven't made any
syntax errors) out comes the PDF.

It is primarily designed with authors of ConTeXt documents in mind, to offer an
easy way to experiment with layout and markup, but it could just as well be
implemented as a generation service for a production system.

## Deployment

You will require:
* Python 2.7
* ConTeXt
* web.py
* a web server capable of serving web.py

For example, on Debian/Ubuntu:

    apt-get install context python-webpy

Or, on Gentoo:

    emerge -av dev-texlive/texlive-context dev-python/webpy

To run the built-in web.py test server locally, just execute code.py.

For deployment on to a proper web server, see http://webpy.org/cookbook/

## Usage

To generate a ConTeXt document in a web browser, just point your browser at a
running instance of Contextualize, enter a valid ConTeXt source document into
the text box, and hit the button.  If all goes to plan, you'll get a nicely
typeset PDF document.

To generate a document from software, craft a HTTP POST request using
multipart/form-data, and the ConTeXt source populated in the form field
"template".  If all goes to plan, you will receive a HTTP 200 OK response, with
a Content-Type header of application/pdf, and a response body containing the
PDF document itself.

## License

Contextualize is released under the MIT License, which can be found in the file
LICENSE at the root of this repository.

## Credits

Contextualize was written by Brendan Jurd.
