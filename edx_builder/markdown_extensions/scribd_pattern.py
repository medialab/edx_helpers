# -------------------------------------------------------------------
# Scribd Inline Pattern
# -------------------------------------------------------------------
#
#
#   Author : Guillaume PLIQUE
#   Organization : Medialab Sciences-po Paris
#   Version : 0.1.0

# Dependencies
#=============
from markdown.inlinepatterns import Pattern
from markdown.util import etree


class ScribdPattern(Pattern):

    # Building the embed
    def handleMatch(self, m):

        # Creating the iframe
        el = etree.Element('iframe')
        el.set('class', 'scribd_iframe_embed')
        el.set('frameborder', '0')
        el.set('url', m.group(1))

        # Returning
        return el
