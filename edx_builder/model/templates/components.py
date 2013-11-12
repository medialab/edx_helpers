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
import yaml
from lxml import etree
from template import XMLTemplate
from model.tools.hasher import hashid


class Component(XMLTemplate):

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.process()
        self.parse()

        print self


class HtmlXMLTemplate(Component):

    # Properties
    html = None

    def process(self):
        self.root = etree.Element('html')
        self.root.set('filename', self.id)

    def parse(self):
        pass


class VideoXMLTemplate(Component):

    def process(self):
        self.root = etree.Element('video')

    def parse(self):

        # Retrieving given metadatas
        metas = yaml.load(self.data)

        # Allocating meta datas
        self.root.set('youtube_id_1_0', metas['id'])
        self.root.set('youtube', '1.00:%s' % metas['id'])
        self.root.set('display_name', metas['name'])
