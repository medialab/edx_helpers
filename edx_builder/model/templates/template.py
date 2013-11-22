# -------------------------------------------------------------------
# EdxBuilder XML Template
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from markdown.util import etree
from model.tools.hasher import hashid


class XMLTemplate(object):

    def configure(self, element, metas):
        self.root = etree.Element(element)
        self.__setMetas(metas)

    def addChild(self, tag, feed):
        h = hashid(feed)
        se = etree.Element(tag)
        se.set('url_name', h)
        self.root.append(se)

        return h

    def compile(self):
        return etree.tostring(self.root)

    def __setMetas(self, metas):
        for m in metas:
            self.root.set(m, metas[m])

    def __repr__(self):
        return self.compile()
