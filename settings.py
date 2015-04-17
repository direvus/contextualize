#
# Base for relative URLs
BASE = 'http://localhost:8080/'

#
# Provided to 'subprocess' to render the context source to PDF.
TEX = (
        '/usr/bin/texexec',
        '--purgeall',
        )

#
# The initial value of the context source text area.
TEMPLATE = '\starttext\n\nHello world!\n\n\stoptext'

#
# Hash digest function to use in generating output filenames.
from hashlib import sha256
HASH = sha256
