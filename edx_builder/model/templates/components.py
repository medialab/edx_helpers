# -------------------------------------------------------------------
# EdxBuilder Vertical XML Template
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from lxml import etree
from template import XMLTemplate
from model.tools.hasher import hashid

class Component(XMLTemplate):

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.process()
        self.parse()

class HtmlXMLTemplate(Component):

    # Properties
    html = None
    
    def process(self):
        self.root = etree.Element('html')
        self.root.set('filename', self.id)

        print self

    def parse(self):
        pass

class VideoXMLTemplate(Component):
    
    def process(self):
        self.root = etree.Element('video')

        print self

    def parse(self):
        pass
