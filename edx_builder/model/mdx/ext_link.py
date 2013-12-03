# -------------------------------------------------------------------
# Link Markdown Extension
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
from markdown.inlinepatterns import LinkPattern, LINK_RE


# Pattern
#========
class LinkOverridenPattern(LinkPattern):

    # Building the embed
    def handleMatch(self, m):

        # Creating the url
        el = etree.Element('a')
        el.text = m.group(2)
        el.set('href', m.group(9))
        el.set('target', '_blank')

        # Safeguard against static ?
        pass

        # Returning
        return el


# Extension
#==========
class LinkExtension(Extension):
    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        self.add_inline(md, 'link', LinkOverridenPattern, LINK_RE)
