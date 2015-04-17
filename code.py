#!/usr/bin/env python


import os
import web
import tempfile
import subprocess

import settings


URLS = (
        '', 'MainView',
        '/', 'MainView',
        '/contextualize', 'MainView',
        '/contextualize/', 'MainView',
        )
RENDER = web.template.render('templates/')


class MainView(object):
    def GET(self, template=None):
        if template is None:
            template = settings.TEMPLATE
        return RENDER.main(settings.BASE, template)

    def POST(self):
        inputs = web.input(
                template=settings.TEMPLATE,
                )

        try:
            with tempfile.NamedTemporaryFile(suffix='.tex', delete=False) as temp:
                temp.write(inputs['template'].strip())
                temp.flush()

            outname = os.path.splitext(temp.name)[0] + '.pdf'
            dirname = os.path.dirname(temp.name)
            subprocess.check_call(settings.TEX + (temp.name,), cwd=dirname)
            with open(outname, 'rb') as out:
                data = out.read()

            os.remove(temp.name)
            os.remove(outname)

            digest = settings.HASH(data).hexdigest()
            disposition = 'inline; filename={}.pdf'.format(digest)
            web.header('Content-Type', 'application/pdf')
            web.header('Content-Disposition', disposition)
            return data
        except:
            return web.internalerror('Sorry, something went wrong with your request.')


app = web.application(URLS, globals())
application = app.wsgifunc()


if __name__ == '__main__':
    app.run()
