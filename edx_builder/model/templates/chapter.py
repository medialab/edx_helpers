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
from template import XMLTemplate
from sequential import SequentialXMLTemplate


# AKA Section
class ChapterXMLTemplate(XMLTemplate):

    # Properties
    subsections = []

    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.configure(
            'chapter',
            {
                'display_name': self.data['name'],
                'start': self.data['start']
            }
        )

        self.computeSubsections()

    # Computing Sequences
    def computeSubsections(self):
        for sub in self.data['subsections']:

            # Adding to root element
            h = self.addChild('sequential', sub['name'])
            
            # Initialize sequential templates
            self.subsections.append(SequentialXMLTemplate(h, sub))
