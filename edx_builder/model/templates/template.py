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
from lxml import etree


class XMLTemplate(object):

    def configure(self, element, metas):
        self.root = etree.Element(element)
        self.__setMetas(metas)

    def __setMetas(self, metas):
        for m in metas:
            self.root.set(m, metas[m])

    def __repr__(self):
        return etree.tostring(self.root, pretty_print=True)
