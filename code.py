#!/usr/bin/env python


import os
import web
import tempfile
import hashlib
import subprocess


URLS = (
        '/', 'MainView',
        )
TEX = (
        '/usr/bin/texexec',
        '--purgeall',
        )
HASH = hashlib.sha256
RENDER = web.template.render('templates/')
TEMPLATE = '\starttext\n\nHello world!\n\n\stoptext'


class MainView(object):
    def GET(self, template=None):
        if template is None:
            template = TEMPLATE
        return RENDER.main(template)

    def POST(self):
        inputs = web.input(
                template=TEMPLATE,
                )

        try:
            with tempfile.NamedTemporaryFile(suffix='.tex', delete=False) as temp:
                temp.write(inputs['template'].strip())
                temp.flush()

            outname = os.path.splitext(temp.name)[0] + '.pdf'
            dirname = os.path.dirname(temp.name)
            subprocess.check_call(TEX + (temp.name,), cwd=dirname)
            with open(outname, 'rb') as out:
                data = out.read()

            os.remove(temp.name)
            os.remove(outname)

            digest = HASH(data).hexdigest()
            disposition = 'inline; filename={}.pdf'.format(digest)
            web.header('Content-Type', 'application/pdf')
            web.header('Content-Disposition', disposition)
            return data
        except:
            return web.internalerror('Sorry, something went wrong with your request.')


if __name__ == '__main__':
    app = web.application(URLS, globals())
    app.run()
