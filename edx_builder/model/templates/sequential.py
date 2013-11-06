# -------------------------------------------------------------------
# EdxBuilder Sequential XML Template
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from template import XMLTemplate
from vertical import VerticalXMLTemplate

# AKA Subsection
class SequentialXMLTemplate(XMLTemplate):

    # Properties
    units = []
    
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.configure(
            'sequential',
            {
                'display_name': self.data['name'],
                'start': self.data['start']
            }
        )

        self.computeUnits()
        print self

    # Computing Units
    def computeUnits(self):
        for unit in self.data['units']:

            # Adding to root element
            h = self.addChild('vertical', unit['name'])

            # Initialize vertical templates
            self.units.append(VerticalXMLTemplate(h, unit))
