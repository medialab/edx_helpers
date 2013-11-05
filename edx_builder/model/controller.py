# -------------------------------------------------------------------
# EdxBuilder Main Controller
# -------------------------------------------------------------------
#
#
#   Author : Guillaume Plique
#   Organization : Sciences-Po Medialab
#   Version : 0.1.0

# Dependencies
#=============
import yaml
from colifrapy import Model
from course_folder import CourseFolder
from templates.chapter import ChapterXMLTemplate

# Main Class
#===========
class Controller(Model):

    # Announcement
    def __init__(self):
        self.log.header('main:title')

    # Building Package
    def build(self):

        # Parsing folder
        folder = CourseFolder(self.opts.target)

        # Creating XML
        course = ChapterXMLTemplate(folder)

    # Testing
    def test(self):
        self.log.write('main:test')
