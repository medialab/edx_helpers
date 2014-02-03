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
import md5
import uuid
from lxml import etree
from colifrapy import Commander


class XMLTemplate(object):

    def configure(self, element, metas):
        self.root = etree.Element(element)
        self.__setMetas(metas)

    def addChild(self, tag, hashid=None, seed=None):

        # NASTY OVERRIDE - CHANGE WHEN DECISIONS ARE MADE
        platform = Commander().opts.platform
        if platform == 'edx' and tag == 'video':
            tag = 'html'

        if seed is not None:
            h = md5.new(seed.encode('utf-8')).hexdigest()
        else:
            h = hashid or uuid.uuid4().hex
        se = etree.Element(tag)
        se.set('url_name', h)
        self.root.append(se)

        return h

    def compile(self):
        return etree.tostring(self.root, pretty_print=True)

    def __setMetas(self, metas):
        for m in metas:
            self.root.set(m, metas[m])

    def __repr__(self):
        return self.compile()
