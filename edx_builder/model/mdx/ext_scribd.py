# -------------------------------------------------------------------
# Scribd Markdown Extension
# -------------------------------------------------------------------
#
#
#   Author : Guillaume PLIQUE
#   Organization : Medialab Sciences-po Paris
#   Version : 0.1.0

# Dependencies
#=============
from markdown.util import etree
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern


# Pattern
#========
class PDFPattern(Pattern):

    # Building the embed
    def handleMatch(self, m):

        # Creating the basis of the iframe
        el = etree.Element('iframe')
        el.set('class', 'scribd_iframe_embed')
        el.set('scrolling', 'no')
        el.set('data-auto-height', 'false')
        el.set('width', '820')
        el.set('height', '546')
        el.set('frameborder', '0')
        el.set('src', '//www.scribd.com/embeds/185064084/content?start_page=1&view_mode=scroll&access_key=key-2oshwm8ft80hr8f9r6gq&show_recommendations=false')

        # Returning
        return el


# Extension
#==========
class ScribdExtension(Extension):
    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'scribd', PDFPattern,
            r'\[\[\pdf:(.*?)]\]')
