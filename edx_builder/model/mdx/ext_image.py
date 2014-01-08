# -------------------------------------------------------------------
# Image Markdown Extension
# -------------------------------------------------------------------
#
#
#   Author : Guillaume PLIQUE
#   Organization : Medialab Sciences-po Paris
#   Version : 0.1.0

# Dependencies
#=============
import re
from markdown.util import etree
from markdown.extensions import Extension
from markdown.inlinepatterns import ImagePattern, IMAGE_LINK_RE


# Pattern
#========
class ImageOverridenPattern(ImagePattern):

    # Building the embed
    def handleMatch(self, m):

        # Creating the image
        el = etree.Element('img')
        el.set('src', m.group(9))

        # Description
        meta = m.group(2).split(':')
        alt = meta[0]
        el.set('alt', alt)

        # Attributes
        floating = False
        for attribute in meta[1:]:

            # Left & right
            if attribute == 'left' or attribute == 'rigth':
                margin_side = 'left' if attribute == 'right' else 'right'
                el.set(
                    'style',
                    'float: %s; margin-%s: 10px;' % \
                      (attribute, margin_side)
                )
                floating = True

            # Height
            if 'height' in attribute:
                hm = re.match(r'.*\((\w+)\)', attribute)
                height = '400' if hm is None else hm.group(1)
                el.set('height', height)
                el.set('width', 'auto')

        # Center the image
        if not floating:
            el.set('style', str('display: block; '
                                'margin-right: auto; '
                                'margin-left: auto;'))

        # Returning
        return el


# Extension
#==========
class ImageExtension(Extension):
    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'image', ImageOverridenPattern, IMAGE_LINK_RE)
