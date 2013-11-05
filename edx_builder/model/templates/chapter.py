# -------------------------------------------------------------------
# EdxBuilder Chapter XML Template
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from lxml import etree
from template import XMLTemplate
from model.tools.hasher import hashid


class ChapterXMLTemplate(XMLTemplate):

    # Properties
    sequences = []

    def __init__(self, folder):
        self.folder = folder
        self.configure(
            'chapter',
            {
                'display_name': self.folder.layout['display_name'],
                'start': self.folder.layout['start']
            }
        )

        self.computeSequences()

    # Computing Sequences
    def computeSequences(self):
        for s in self.folder.sequences():

            # Adding to root element
            se = etree.Element('sequential')
            se.set('url_name', hashid(s['display_name']))
            self.root.append(se)
            
            # Adding to sequences objects

        print self

        # Init new templates passing them the hash value
