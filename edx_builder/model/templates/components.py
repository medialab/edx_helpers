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
from model.mdx import ScribdExtension, ImageExtension, LinkExtension


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
            name = yaml.load(self.data.splitlines()[0])['name']
            self.root.set('display_name', name)
        except:
            pass

        # Compiling markdown
        self.html = markdown.markdown(
            '\n'.join(self.data.splitlines()[1:]),
            [
                ScribdExtension(),
                ImageExtension(),
                LinkExtension()
            ]
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
        self.root.set('youtube_id_1_0', metas['id'])
        self.root.set('youtube', '1.00:%s' % metas['id'])
        self.root.set('display_name', metas['name'])


class DiscussionXMLTemplate(Component):

    # Properties
    directory = 'discussion'

    def process(self):
        self.root = etree.Element('discussion')

    def parse(self):

        # Retrieving given metadatas
        metas = yaml.load(self.data) 

        # Allocating meta datas
        if metas.get('name') is not None:
            self.root.set('display_name', metas['name'])

        if metas.get('category') is not None:
            self.root.set('discussion_category', metas['category'])

        if metas.get('subcategory') is not None:
            self.root.set('discussion_target', metas['subcategory'])
