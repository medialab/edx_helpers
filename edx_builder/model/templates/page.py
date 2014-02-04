# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# EdxBuilder Static Page Template
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import markdown
from model.mdx import ScribdExtension, ImageExtension, LinkExtension

class StaticPage(object):

    def __init__(self, id, mstring):
        self.id = id
        self.html = markdown.markdown(
            mstring,
            extensions=[
                LinkExtension(),
                ImageExtension(),
                ScribdExtension()
            ]
        )
