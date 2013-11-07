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
class ScribdPattern(Pattern):

    # Building the embed
    def handleMatch(self, m):

        # Creating the iframe
        el = etree.Element('iframe')
        el.set('class', 'scribd_iframe_embed')
        el.set('frameborder', '0')
        el.set('url', m.group(2))

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
        self.add_inline(md, 'scribd', ScribdPattern,
            r'\[\[\pdf:(.*?)]\]')
