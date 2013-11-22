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
from markdown.util import etree
from template import XMLTemplate
from chapter import ChapterXMLTemplate


# AKA Whole Course
class CourseXMLTemplate(XMLTemplate):

    # Properties
    sections = []
    overview = ''
    effort = ''
    xml = ''

    def __init__(self, folder):
        self.folder = folder
        ly = folder.layout

        self.static = folder.static
        self.identifier = ly.get('identifier') or '2014_Spring'
        
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
        self.overview = etree.tostring(overview_root)

        # Effort
        self.effort = self.folder.layout.get('effort') or '3:00'

        # Course XML
        course_root = etree.Element('course')
        course_root.set('url_name', self.identifier)
        course_root.set('org', self.folder.layout['organization'])
        course_root.set('course', self.folder.layout['number'])

        self.xml = etree.tostring(course_root)
