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
from markdown.extensions import Extension
from scribd_pattern import ScribdPattern


class ScribdExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('scribd', ScribdPattern(md), '<references')