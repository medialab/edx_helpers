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
import markdown
from lxml import etree
from template import XMLTemplate
from model.mdx.scribd import ScribdExtension
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
    directory = 'html'

    def process(self):
        self.root = etree.Element('html')
        self.root.set('filename', self.id)

    def parse(self):
        
        # Retrieving name of component
        try:
            name = yaml.load(self.data.splitlines()[0])['name'].strip()
            self.root.set('display_name', name)
        except:
            pass

        # Compiling markdown
        self.html = markdown.markdown(
            '\n'.join(self.data.splitlines()[1:]),
            [ScribdExtension()]
        )


class VideoXMLTemplate(Component):

    # Properties
    directory = 'video'

    def process(self):
        self.root = etree.Element('video')

    def parse(self):

        # Retrieving given metadatas
        metas = yaml.load(self.data)

        # Allocating meta datas
        self.root.set('youtube_id_1_0', metas['id'].strip())
        self.root.set('youtube', '1.00:%s' % metas['id'].strip())
        self.root.set('display_name', metas['name'].strip())
