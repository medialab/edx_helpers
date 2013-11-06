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
from template import XMLTemplate
from chapter import ChapterXMLTemplate

# AKA Whole Course
class CourseXMLTemplate(XMLTemplate):

    # Properties
    sections = []

    def __init__(self, folder):
        self.folder = folder
        layout = self.folder.layout
        self.configure(
            'course',
            {
                'display_name': layout['name'],
                'start': layout['start'],
                'advanced_modules': layout['advanced_modules'].__repr__() or [],
                'course_image': layout['course_image'] or 'cover.png'
            }
        )

        self.computeSections()
        print self

    # Computing Sections
    def computeSections(self):
        for sec in self.folder.sections():

            # Adding to root element
            h = self.addChild('chapter', sec['name'])

            # Initialize sequential templates
            self.sections.append(ChapterXMLTemplate(h, sec))
