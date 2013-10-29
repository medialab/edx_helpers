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
import re
from markdown.inlinepatterns import Pattern
from markdown.utils import etree


class ScribdPattern(Pattern):

    # Pattern Regular Expression
    def getCompiledRegExp(self):
        return r'\[\[pdf:([^\]])+\]\]'

    # Building the embed
    def handleMatch(self, m):

        # Creating the iframe
        el = etree.Element('iframe')
        el.set('class', 'scribd_iframe_embed')
        el.set('frameborder', '0')

        # Returning
        return el


""" <iframe class="scribd_iframe_embed" src="//www.scribd.com/embeds/179915341/content?start_page=1&view_mode=slideshow&access_key=key-4lixibpz7pakxqqh84m&show_recommendations=false" data-auto-height="false" data-aspect-ratio="1.41222570532915" scrolling="no" id="doc_28563" width="600" height="800" frameborder="0"></iframe> """