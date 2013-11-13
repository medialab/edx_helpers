# -------------------------------------------------------------------
# EdxBuilder Course XML Template
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
from chapter import ChapterXMLTemplate


# AKA Whole Course
class CourseXMLTemplate(XMLTemplate):

    # Properties
    sections = []
    overview = ''
    effort = ''

    def __init__(self, folder):
        self.folder = folder
        self.static = folder.layout['static'] or 'static'
        self.identifier = folder.layout['identifier'] or '2014_Spring'
        
        ly = folder.layout
        self.configure(
            'course',
            {
                'display_name': ly['name'],
                'start': ly['start'],
                'advanced_modules': ly['advanced_modules'].__repr__() or [],
                'course_image': ly['course_image'] or 'cover.png'
            }
        )

        self.computeSections()
        self.computeAnnexes()

    # Computing Sections
    def computeSections(self):
        for sec in self.folder.sections():

            # Adding to root element
            h = self.addChild('chapter', sec['name'])

            # Initialize sequential templates
            self.sections.append(ChapterXMLTemplate(h, sec))

    # Compute annexes
    def computeAnnexes(self):

        # About
        overview_root = etree.Element('section')
        overview_root.set('class', 'about')
        self.overview = etree.tostring(overview_root, pretty_print=True)

        # Effort
        self.effort = self.folder.layout.get('effort') or '3:00'
