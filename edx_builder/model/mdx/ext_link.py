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
from model.tools.unit_index import UnitIndex


# Pattern
#========
class LinkOverridenPattern(LinkPattern):

    # Building the embed
    def handleMatch(self, m):

        # Basics
        text = m.group(2)
        href = m.group(9)
        jump = '/jump_to_id/' in href
        index = UnitIndex()

        # Creating the url
        el = etree.Element('a')
        el.text = text

        if jump:
            unit_path  = href.split('/jump_to_id/')[-1]

            hashid = index.get(unit_path)
            if hashid is None:
                raise Exception('Bad internal link : %s' % (unit_path,))
            el.set('href', '/jump_to_id/' + hashid)
        else:
            el.set('href', href)
            el.set('target', '_blank')

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
