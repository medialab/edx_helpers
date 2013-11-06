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
import os
import yaml
from colifrapy import Model
from colifrapy.tools.utilities import normalize_path
from course_folder import CourseFolder
from templates.course import CourseXMLTemplate

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

        # Creating output folder
        self.opts.output = normalize_path(self.opts.output, True)
        if not os.path.exists(self.opts.output):
            os.mkdir(self.opts.output)

        # Creating XML
        course = CourseXMLTemplate(folder)

    # Testing
    def test(self):
        self.log.write('main:test')
