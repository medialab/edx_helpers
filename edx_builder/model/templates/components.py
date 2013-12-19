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
from colifrapy import Settings
from cloudkey from CloudKey

CLOUDKEY = None

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

        # Setting name of component
        self.root.set('display_name', self.data['name'])

        # Compiling markdown
        self.html = markdown.markdown(
            self.data['text'],
            extensions=[
                LinkExtension(),
                ImageExtension(),
                ScribdExtension()
            ]
        )


class VideoXMLTemplate(Component):

    # Properties
    directory = 'video'

    def process(self):
        self.root = etree.Element('video')

    def parse(self):

        # Allocating meta datas
        self.root.set('youtube_id_1_0', self.data['id'])
        self.root.set('youtube', '1.00:%s' % self.data['id'])
        self.root.set('display_name', self.data['name'])

        # Start and End time
        start_time = self.data.get('start')
        end_time = self.data.get('end')

        if start_time is not None:
            self.root.set('start_time', start_time)

        if end_time is not None:
            self.root.set('end_time', end_time)


class OverridenVideoXMLTemplate(Component):

    # Properties
    html = None
    directory = 'html'

    def process(self):

        # Setting up cloudkey once
        if CLOUDKEY is None:
            s = Settings()
            CLOUDKEY = CloudKey(
                self.settings.dailymotion['user_id'],
                self.settings.dailymotion['api_key']
            )

        self.root = etree.Element('html')
        self.root.set('filename', self.id)

    def parse(self):

        # Setting name of component
        self.root.set('display_name', self.data['name'])

        # Compiling html
        video = etree.Element('iframe')
        video.set('frameborder', '0')
        video.set('width', '820')
        video.set('height', '461')

        src = CLOUDKEY.media.get_embed_url(self.data['id'])
        video.set('src', src)

        self.html = etree.tostring(video, pretty_print=True)


class DiscussionXMLTemplate(Component):

    # Properties
    directory = 'discussion'

    def process(self):
        self.root = etree.Element('discussion')

    def parse(self):

        # Allocating meta datas
        if self.data.get('name') is not None:
            self.root.set('display_name', self.data['name'])

        if self.data.get('category') is not None:
            self.root.set('discussion_category', self.data['category'])

        if self.data.get('subcategory') is not None:
            self.root.set('discussion_target', self.data['subcategory'])
