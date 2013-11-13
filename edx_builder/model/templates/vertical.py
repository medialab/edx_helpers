# -------------------------------------------------------------------
# EdxBuilder Vertical XML Template
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
from template import XMLTemplate
from components import HtmlXMLTemplate, VideoXMLTemplate
from model.tools.unit_parser import parse_unit


# AKA Unit
class VerticalXMLTemplate(XMLTemplate):

    # Properties
    components = []
    components_types = {
        'html': HtmlXMLTemplate,
        'video': VideoXMLTemplate
    }
    
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.configure(
            'vertical',
            {
                'display_name': self.data['name']
            }
        )

        self.computeComponents()

    # Computing Components
    def computeComponents(self):

        # Parsing unit file
        for component in parse_unit(self.data['file']):

            # Adding component to xml
            h = self.addChild(component['type'], component['data'])

            # Adding components to data
            self.components.append(
                self.components_types[component['type']](h, component['data'])
            )
